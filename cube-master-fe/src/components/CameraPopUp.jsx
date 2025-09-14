import React, { useRef, useEffect, useState } from "react";

const CameraPopup = ({ onClose, setCubeColors }) => {
    const videoRef = useRef(null);
    const mediaStreamRef = useRef(null);
    const [inputFace, setFace] = useState("front");
    const topRef = useRef(null);
    const leftRef = useRef(null);
    const frontRef = useRef(null);
    const rightRef = useRef(null);
    const backRef = useRef(null);
    const bottomRef = useRef(null);

    useEffect(() => {
        switch (inputFace) {
            case "top":
                topRef.current.focus();
                break;
            case "left":
                leftRef.current.focus();
                break;
            case "front":
                frontRef.current.focus();
                break;
            case "right":
                rightRef.current.focus();
                break;
            case "back":
                backRef.current.focus();
                break;
            case "bottom":
                bottomRef.current.focus();
                break;
            default:
                break;
        }
    }, [inputFace]);

    const handleKeyDown = (event, face) => {
        event.preventDefault(); // Prevent scrolling up or down

        const faceMap = {
            front: {
                ArrowUp: "top",
                ArrowDown: "bottom",
                ArrowLeft: "left",
                ArrowRight: "right",
            },
            top: {
                ArrowDown: "front",
                ArrowLeft: "left",
                ArrowRight: "right",
                ArrowUp: "bottom",
            },
            bottom: {
                ArrowUp: "front",
                ArrowLeft: "left",
                ArrowRight: "right",
                ArrowDown: "top",
            },
            left: {
                ArrowUp: "top",
                ArrowDown: "bottom",
                ArrowRight: "front",
                ArrowLeft: "back",
            },
            right: {
                ArrowUp: "top",
                ArrowDown: "bottom",
                ArrowLeft: "front",
                ArrowRight: "back",
            },
            back: {
                ArrowLeft: "right",
                ArrowRight: "left",
                ArrowUp: "top",
                ArrowDown: "bottom",
            },
        };

        const newFace = faceMap[face]?.[event.key];
        if (newFace) {
            setFace(newFace);
        }
    };

    const squares = [
        { x: 150, y: 100, size: 30 },
        { x: 250, y: 100, size: 30 },
        { x: 350, y: 100, size: 30 },
        { x: 150, y: 200, size: 30 },
        { x: 250, y: 200, size: 30 },
        { x: 350, y: 200, size: 30 },
        { x: 150, y: 300, size: 30 },
        { x: 250, y: 300, size: 30 },
        { x: 350, y: 300, size: 30 },
    ];

    // color to bg notation to represent
    const getbg = {
        white: "bg-white",
        red: "bg-red-500",
        green: "bg-green-500",
        blue: "bg-blue-600",
        yellow: "bg-yellow-400",
        orange: "bg-orange-500",
    };

    const startCamera = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            if (videoRef.current) {
                videoRef.current.srcObject = stream;
                mediaStreamRef.current = stream;
                videoRef.current.onloadedmetadata = () => {
                    videoRef.current.play().catch((error) => {
                        console.error("Error playing video: ", error);
                    });
                };
                // videoRef.current.play();
                console.log("Camera started successfully.");
            }
        } catch (error) {
            console.error("Error accessing the camera: ", error);
        }
    };

    const stopCamera = () => {
        if (mediaStreamRef.current) {
            mediaStreamRef.current.getTracks().forEach((track) => track.stop());
            mediaStreamRef.current = null;
            if (videoRef.current) {
                videoRef.current.srcObject = null;
            }
            console.log("Camera stopped.");
        }
    };

    const analyzeFrame = async (inputFace) => {
        console.log(inputFace);
        if (videoRef.current) {
            const videoWidth = videoRef.current.videoWidth;
            const videoHeight = videoRef.current.videoHeight;

            const canvas = document.createElement("canvas");
            canvas.width = videoWidth;
            canvas.height = videoHeight;
            const context = canvas.getContext("2d", { willReadFrequently: true });

            // Draw the video frame on the canvas
            context.drawImage(videoRef.current, 0, 0, videoWidth, videoHeight);

            // Adjust squares to match video dimensions
            const adjustedSquares = squares.map(({ x, y, size }) => ({
                x: x * (videoWidth / videoRef.current.offsetWidth), // Scale to videoWidth
                y: y * (videoHeight / videoRef.current.offsetHeight), // Scale to videoHeight
                size: size * (videoWidth / videoRef.current.offsetWidth), // Scale size
            }));

            const croppedImages = adjustedSquares.map(({ x, y, size }) => {
                const imageData = context.getImageData(x, y, size, size); // Crop square
                const cropCanvas = document.createElement("canvas"); // Create a new canvas for each crop
                cropCanvas.width = size;
                cropCanvas.height = size;
                const cropContext = cropCanvas.getContext("2d");
                cropContext.putImageData(imageData, 0, 0); // Paste the cropped image onto the new canvas
                return cropCanvas.toDataURL("image/png"); // Default is "image/png"
            });

            const response = await fetch("http://127.0.0.1:8000/api/v1/scanner/scan/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ face: croppedImages }),
            });

            const data = await response.json();

            const colors = data.colors;
            console.log(colors);
            const scannedColors = [];

            if (colors) {
                colors.forEach((color) => {
                    scannedColors.push(getbg[color]);
                });
            }

            setCubeColors((prevColors) => {
                const updatedColors = { ...prevColors };
                updatedColors[inputFace] = scannedColors;
                return updatedColors;
            });
        }
    };

    useEffect(() => {
        startCamera();
        frontRef.current.focus();

        return () => {
            stopCamera();
        };
    }, []);

    // Separate useEffect for frame analysis
    useEffect(() => {
        const intervalId = setInterval(() => {
            analyzeFrame(inputFace);
        }, 1000); // Analyze every second

        return () => {
            clearInterval(intervalId);
        };
    }, [inputFace]);

    return (
        <div className="absolute flex items-center justify-center mt-5">
            <div className="bg-white p-3 rounded shadow-lg">
                {/* face to input section */}
                <div className="flex justify-center items-center">
                    <span className=" text-black text-2xl mx-4">Face:</span>
                    <div className="grid grid-cols-4 grid-rows-3 gap-1 h-16 w-24">
                        <div
                            className={`col-start-2 col-span-1 row-start-1 row-span-1 border-2 border-black ${inputFace == "top" ? "bg-black animate-opacity-fade" : ""
                                }`}
                            onClick={() => {
                                setFace("top");
                            }}
                            tabIndex={0}
                            ref={topRef}
                            onKeyDown={(event) => handleKeyDown(event, "top")}
                        ></div>
                        <div
                            className={`col-start-1 col-span-1 row-start-2 row-span-1 border-2 border-black ${inputFace == "left" ? "bg-black animate-opacity-fade" : ""
                                }`}
                            onClick={() => {
                                setFace("left");
                            }}
                            tabIndex={0}
                            ref={leftRef}
                            onKeyDown={(event) => handleKeyDown(event, "left")}
                        ></div>
                        <div
                            className={`col-start-2 col-span-1 row-start-2 row-span-1 border-2 border-black ${inputFace == "front" ? "bg-black animate-opacity-fade" : ""
                                }`}
                            onClick={() => {
                                setFace("front");
                            }}
                            tabIndex={0}
                            ref={frontRef}
                            onKeyDown={(event) => handleKeyDown(event, "front")}
                        ></div>
                        <div
                            className={`col-start-3 col-span-1 row-start-2 row-span-1 border-2 border-black ${inputFace == "right" ? "bg-black animate-opacity-fade" : ""
                                }`}
                            onClick={() => {
                                setFace("right");
                            }}
                            tabIndex={0}
                            ref={rightRef}
                            onKeyDown={(event) => handleKeyDown(event, "right")}
                        ></div>
                        <div
                            className={`col-start-4 col-span-1 row-start-2 row-span-1 border-2 border-black ${inputFace == "back" ? "bg-black animate-opacity-fade" : ""
                                }`}
                            onClick={() => {
                                setFace("back");
                            }}
                            tabIndex={0}
                            ref={backRef}
                            onKeyDown={(event) => handleKeyDown(event, "back")}
                        ></div>
                        <div
                            className={`col-start-2 col-span-1 row-start-3 row-span-1 border-2 border-black ${inputFace == "bottom" ? "bg-black animate-opacity-fade" : ""
                                }`}
                            onClick={() => {
                                setFace("bottom");
                            }}
                            tabIndex={0}
                            ref={bottomRef}
                            onKeyDown={(event) => handleKeyDown(event, "bottom")}
                        ></div>
                    </div>
                </div>

                <div className="relative w-full h-[400px] my-2">
                    <video
                        ref={videoRef}
                        className="w-full h-full object-cover transform scale-x-[-1]"
                        autoPlay
                        muted
                    ></video>

                    {/* Overlay with squares, arranged based on coordinates */}
                    <div className="absolute -left-16 md:left-0 inset-0 flex flex-col justify-center items-center pointer-events-none">
                        {squares.map((square, index) => (
                            <div
                                key={index}
                                className="absolute"
                                style={{
                                    left: `${square.x}px`,
                                    top: `${square.y}px`,
                                    width: `${square.size}px`,
                                    height: `${square.size}px`,
                                    border: "4px solid black",
                                }}
                            />
                        ))}
                    </div>
                </div>

                <div className="">
                    <button
                        onClick={() => {
                            stopCamera();
                            onClose();
                        }}
                        className="bg-red-600 text-white py-2 px-4 rounded hover:bg-red-700 transition duration-300 w-full"
                    >
                        Stop
                    </button>
                </div>
            </div>
        </div>
    );
};

export default CameraPopup;
