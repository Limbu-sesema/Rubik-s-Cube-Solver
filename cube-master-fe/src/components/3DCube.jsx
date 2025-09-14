import React, { useRef, useEffect, useState } from "react";
import { FaStepBackward, FaStepForward, FaPause, FaPlay } from "react-icons/fa";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import { RoundedBoxGeometry } from "three/examples/jsm/geometries/RoundedBoxGeometry.js";
import {
    materials,
    Roll,
    stateMap,
    moveNotationTo3d,
    opposite_moves,
} from "../assets/utils/3Dhelpers";
import { Alert, ErrorAlert } from "./Alert";

const Cube3D = ({ cubeColors, initialFaceColors, sequence }) => {
    const mountRef = useRef(null);
    const sceneRef = useRef(null);
    const rendererRef = useRef(null);
    const cameraRef = useRef(null);
    const controlsRef = useRef(null);
    const groupRef = useRef(null);
    const cubesRef = useRef([]);
    const moveQueueRef = useRef([]);
    const isRotatingRef = useRef(false);
    const resizeObserverRef = useRef(null);
    const [alert, setAlert] = useState({ message: "", visible: false });
    const [errorAlert, setErrorAlert] = useState({ message: "", visible: false });
    const [isPlaying, setIsPlaying] = useState(false);
    const [displayMove, setDisplayMove] = useState("None");
    const [currentMoveIndex, setCurrentMoveIndex] = useState(0);
    const playbackTimeoutRef = useRef(null);

    const cleanColors = (cubeColors) => {
        const cleanedCubeColors = {};

        Object.keys(cubeColors).forEach((key) => {
            cleanedCubeColors[key] = cubeColors[key].map((color) =>
                color.replace(/^bg-/, "").replace(/\d+/g, "").replace(/-$/, "")
            );
        });

        return cleanedCubeColors;
    };

    const cleanedCubeColors = cleanColors(cubeColors);

    const rotateConditions = {
        right: { axis: "x", value: 1 },
        left: { axis: "x", value: -1 },
        top: { axis: "y", value: 1 },
        bottom: { axis: "y", value: -1 },
        front: { axis: "z", value: 1 },
        back: { axis: "z", value: -1 },
        rotateUp: { axis: "x" },
        rotateDown: { axis: "x" },
        rotateRight: { axis: "y" },
        rotateLeft: { axis: "y" },
    };

    // instruction for moves 
    const moveToInstruction = {
        F: "(Rotate the front face clockwise)",
        "F'": "(Rotate the front face anticlockwise)",
        R: "(Rotate the right face clockwise)",
        "R'": "(Rotate the right face anticlockwise)",
        U: "(Rotate the top face clockwise)",
        "U'": "(Rotate the top face anticlockwise)",
        D: "(Rotate the bottom face clockwise)",
        "D'": "(Rotate the bottom face anticlockwise)",
        L: "(Rotate the left face clockwise)",
        "L'": "(Rotate the left face anticlockwise)",
        B: "(Rotate the back face clockwise)",
        "B'": "(Rotate the back face anticlockwise)",
        RR: "(Rotate the cube right)",
        RL: "(Rotate the cube left)",
        RD: "(Rotate the cube down)",
        RU: "(Rotate the cube up)",
    };

    const cPositions = [-1, 0, 1];

    const init = () => {
        if (!mountRef.current) return;

        const container = mountRef.current;
        const { width, height } = container.getBoundingClientRect();

        // Scene setup
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x000000);
        sceneRef.current = scene;

        // Renderer setup
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(width, height);
        renderer.shadowMap.enabled = true;
        renderer.setPixelRatio(window.devicePixelRatio);
        container.appendChild(renderer.domElement);
        rendererRef.current = renderer;

        // Camera setup
        const camera = new THREE.PerspectiveCamera(35, width / height, 1, 1000);
        camera.position.set(6, 6, 6);
        cameraRef.current = camera;

        // Controls setup
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controlsRef.current = controls;

        createObjects();
    };

    const createObjects = () => {
        const geometry = new RoundedBoxGeometry(1, 1, 1, 1, 0.12);
        let index = 0;

        const createCube = (position) => {
            let mat = [];
            for (let i = 0; i < 6; i++) {
                if (stateMap[index][i]) {
                    const values = stateMap[index][i];
                    mat.push(materials[cleanedCubeColors[values.position][values.no]]); // Use cleanedCubeColors from state
                } else {
                    mat.push(materials.black);
                }
            }
            index++;

            const cube = new THREE.Mesh(geometry, mat);
            cube.position.set(position.x, position.y, position.z);
            cubesRef.current.push(cube);

            const edgesGeometry = new THREE.EdgesGeometry(geometry);
            const edgesMaterial = new THREE.LineBasicMaterial({
                color: 0x000000,
                linewidth: 1,
            });
            const edges = new THREE.LineSegments(edgesGeometry, edgesMaterial);

            cube.add(edges);
            sceneRef.current.add(cube);
        };

        cPositions.forEach((x) => {
            cPositions.forEach((y) => {
                cPositions.forEach((z) => {
                    createCube({ x, y, z });
                });
            });
        });

        const group = new THREE.Group();
        sceneRef.current.add(group);
        groupRef.current = group;
    };

    const handleResize = () => {
        if (!mountRef.current || !cameraRef.current || !rendererRef.current) return;

        const container = mountRef.current;
        const { width, height } = container.getBoundingClientRect();

        cameraRef.current.aspect = width / height;
        cameraRef.current.updateProjectionMatrix();
        rendererRef.current.setSize(width, height);
    };

    const processNextMove = async () => {
        if (moveQueueRef.current.length === 0) return;

        isRotatingRef.current = true;
        const move = moveQueueRef.current.shift();

        const rollObject = new Roll(
            rotateConditions[move.position],
            move.direction,
            sceneRef.current,
            groupRef.current,
            cubesRef.current,
            Math.PI / 50
        );

        while (rollObject.active) {
            const finished = await rollObject.rollFace();
            if (finished) {
                isRotatingRef.current = false;
                if (moveQueueRef.current.length > 0) {
                    processNextMove();
                }
                break;
            }
            await new Promise((resolve) => setTimeout(resolve, 16));
        }
    };

    const moves = (position, direction) => {
        moveQueueRef.current.push({ position, direction });
        if (!isRotatingRef.current) {
            processNextMove();
        }
    };

    const animate = () => {
        requestAnimationFrame(animate);
        if (controlsRef.current) controlsRef.current.update();
        if (rendererRef.current && sceneRef.current && cameraRef.current) {
            rendererRef.current.render(sceneRef.current, cameraRef.current);
        }
    };

    useEffect(() => {
        init();
        animate();
        window.moves = moves;

        // Set up ResizeObserver to watch container size changes
        resizeObserverRef.current = new ResizeObserver(handleResize);
        if (mountRef.current) {
            resizeObserverRef.current.observe(mountRef.current);
        }

        return () => {
            // Cleanup resize observer
            if (resizeObserverRef.current) {
                resizeObserverRef.current.disconnect();
            }

            // Cleanup Three.js
            if (mountRef.current && rendererRef.current) {
                mountRef.current.removeChild(rendererRef.current.domElement);
            }
            delete window.moves;

            rendererRef.current?.dispose();
            cubesRef.current.forEach((cube) => {
                cube.geometry.dispose();
                cube.material.forEach((material) => material.dispose());
            });
        };
    }, []);

    const togglePlayPause = () => {
        if (currentMoveIndex >= sequence.length) {
            return;
        }
        setIsPlaying((prevState) => !prevState);
    };

    useEffect(() => {
        if (!isPlaying) {
            return;
        }

        const executeMoves = () => {
            if (currentMoveIndex < sequence.length) {
                moveForward();
            } else {
                setIsPlaying(false); // Stop playing if the sequence is completed
            }
        };

        // Schedule the next move
        const timeoutId = setTimeout(executeMoves, 500);

        return () => clearTimeout(timeoutId); // Cleanup on effect re-run or unmount
    }, [isPlaying, currentMoveIndex]);

    const moveBackward = () => {
        if (currentMoveIndex > 0) {
            setCurrentMoveIndex((prev) => prev - 1);
            const previousMove = sequence[currentMoveIndex - 1];
            const opposisteMove = opposite_moves[previousMove];
            const reverseMove = moveNotationTo3d[opposisteMove];
            setDisplayMove(opposisteMove.toUpperCase());
            moves(reverseMove.position, reverseMove.direction);
        } else {
            setErrorAlert({ message: "No backmove exists!!!", visible: true });
        }
    };
    const moveForward = () => {
        if (currentMoveIndex < sequence.length) {
            const nextMove = sequence[currentMoveIndex];
            setCurrentMoveIndex((prev) => prev + 1);
            const move = moveNotationTo3d[nextMove];
            setDisplayMove(nextMove.toUpperCase());
            moves(move.position, move.direction);
        } else {
            setAlert({ message: "Cube Solved!!!", visible: true });
        }
    };

    useEffect(() => {
        return () => {
            if (playbackTimeoutRef.current) {
                clearTimeout(playbackTimeoutRef.current);
            }
        };
    }, []);

    return (
        <div className="flex flex-col items-center justify-center bg-gray-900">
            <div
                ref={mountRef}
                className="w-full h-[500px] md:w-2/3 overflow-hidden rounded-3xl bg-gray-900"
            />
            {/* Current Move Display */}
            <div className="text-lg font-semibold text-white my-4">
                {`Current Move: ${displayMove}${displayMove !== "None" ? ` ${moveToInstruction[displayMove]}` : ""
                    }`}
            </div>

            <div className="flex flex-wrap justify-center gap-4 m-4">
                <button
                    className="px-4 py-2 text-lg font-semibold text-white bg-black rounded hover:bg-gray-700"
                    onClick={moveBackward}
                    disabled={isPlaying}
                >
                    <FaStepBackward />
                </button>
                <button
                    className="px-4 py-2 text-lg font-semibold text-white bg-black rounded hover:bg-gray-700 active:bg-gray-900"
                    onClick={togglePlayPause}
                >
                    {isPlaying ? <FaPause /> : <FaPlay />}
                </button>
                <button
                    className="px-4 py-2 text-lg font-semibold text-white bg-black rounded hover:bg-gray-700"
                    onClick={moveForward}
                    disabled={isPlaying}
                >
                    <FaStepForward />
                </button>
            </div>
            {alert.visible && (
                <Alert
                    message={alert.message}
                    onClose={() => setAlert({ ...alert, visible: false })}
                />
            )}
            {errorAlert.visible && (
                <ErrorAlert
                    message={errorAlert.message}
                    onClose={() => setErrorAlert({ ...errorAlert, visible: false })}
                />
            )}
        </div>
    );
};

export default Cube3D;
