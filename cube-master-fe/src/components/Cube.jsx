import React, { useState } from "react";
import { PiArrowBendRightUpBold, PiArrowBendLeftUpBold } from "react-icons/pi";
import { FaArrowUpLong } from "react-icons/fa6";

import "./cube.css";

const Cube = ({ cubeColors, currentColor, setCubeColors }) => {
    const [typeOfCube, setType] = useState("3d");
    const [rotation, setRotation] = useState({ y: -30, z: 0 });
    const [hidden, setHidden] = useState(false);

    return (
        <div
            className={`w-[650px] h-[500px] flex flex-col justify-center opacity-100 rounded-2xl`}
        >
            {/* toggle 3d and 2d */}
            <div className="w-full flex justify-center ">
                <div className="flex justify-evenly w-56 ">
                    <button
                        className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300 "
                        onClick={() => {
                            setType("3d");
                            setRotation((prev) => ({ y: -30, z: 0 }));
                            setHidden(false);
                        }}
                    >
                        3D
                    </button>
                    <button
                        className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300 active:bg-blue-700"
                        onClick={() => {
                            setType("2d");
                            setRotation((prev) => ({ y: 0, z: 0 }));
                            setHidden(true);
                        }}
                    >
                        2D
                    </button>
                </div>
            </div>

            {/* cube */}
            <div
                className={`${typeOfCube == "3d" ? "h-[381px]" : "h-[430px]"
                    } w-full flex justify-center items-center `}
            >
                {/* cube div */}
                <div
                    className={`cube${typeOfCube} h-32 w-32`}
                    style={{
                        transform: `rotateX(-30deg) rotateY(${rotation.y}deg) rotateZ(${rotation.z}deg)`,
                    }}
                >
                    <div
                        className={`${typeOfCube == "2d"
                            ? "absolute border border-black ease-in-out duration-1000 w-28 h-28 rotate-90 -translate-y-14 sm:h-[144px] sm:w-[144px] sm:rotate-0 sm:translate-x-[-80px] sm:translate-y-0"
                            : `front${typeOfCube} face${typeOfCube}`
                            } grid grid-cols-3 gap-0 border-2 select-none`}
                    >
                        {Array(9)
                            .fill(null)
                            .map((_, index) => (
                                <div
                                    key={`front-${index}`}
                                    className={`w-full h-full border border-black ${cubeColors.front[index]} text-black`}
                                    onClick={() =>
                                        setCubeColors((prevColors) => {
                                            const updatedColors = { ...prevColors };
                                            updatedColors.front[index] = currentColor;
                                            return updatedColors;
                                        })
                                    }
                                >
                                    {index + 1}F
                                </div>
                            ))}
                    </div>

                    <div
                        className={`${typeOfCube == "2d"
                            ? "absolute border border-black ease-in-out duration-1000  w-28 h-28 rotate-90 translate-y-[184px] sm:h-[144px] sm:w-[144px] sm:rotate-0 sm:translate-x-[240px] sm:translate-y-0"
                            : `back${typeOfCube} face${typeOfCube}`
                            } grid grid-cols-3 gap-0 border-2 select-none `}
                    >
                        {Array(9)
                            .fill(null)
                            .map((_, index) => (
                                <div
                                    key={`back-${index}`}
                                    className={`w-full h-full border border-black ${cubeColors.back[index]} text-black`}
                                    onClick={() =>
                                        setCubeColors((prevColors) => {
                                            const updatedColors = { ...prevColors };
                                            updatedColors.back[index] = currentColor;
                                            return updatedColors;
                                        })
                                    }
                                >
                                    {index + 1}B
                                </div>
                            ))}
                    </div>

                    <div
                        className={`${typeOfCube == "2d"
                            ? "absolute border border-black ease-in-out duration-1000  w-28 h-28 rotate-90 -translate-y-44 sm:h-[144px] sm:w-[144px] sm:rotate-0 sm:-translate-x-[240px] sm:translate-y-0"
                            : `left${typeOfCube} face${typeOfCube}`
                            } grid grid-cols-3 gap-0 border-2 select-none`}
                    >
                        {Array(9)
                            .fill(null)
                            .map((_, index) => (
                                <div
                                    key={`left-${index}`}
                                    className={`w-full h-full border border-black ${cubeColors.left[index]} text-black`}
                                    onClick={() =>
                                        setCubeColors((prevColors) => {
                                            const updatedColors = { ...prevColors };
                                            updatedColors.left[index] = currentColor;
                                            return updatedColors;
                                        })
                                    }
                                >
                                    {index + 1}L
                                </div>
                            ))}
                    </div>

                    <div
                        className={`${typeOfCube == "2d"
                            ? "absolute border border-black ease-in-out duration-1000  w-28 h-28 rotate-90 translate-y-16 sm:h-[144px] sm:w-[144px] sm:rotate-0 sm:translate-x-[80px] sm:translate-y-0 "
                            : `right${typeOfCube} face${typeOfCube} `
                            } grid grid-cols-3 gap-0 border-2 select-none`}
                    >
                        {Array(9)
                            .fill(null)
                            .map((_, index) => (
                                <div
                                    key={`right-${index}`}
                                    className={`w-full h-full border border-black ${cubeColors.right[index]} text-black`}
                                    onClick={() =>
                                        setCubeColors((prevColors) => {
                                            const updatedColors = { ...prevColors };
                                            updatedColors.right[index] = currentColor;
                                            return updatedColors;
                                        })
                                    }
                                >
                                    {index + 1}R
                                </div>
                            ))}
                    </div>

                    <div
                        className={`${typeOfCube == "2d"
                            ? "absolute border border-black ease-in-out duration-1000  w-28 h-28 rotate-90 translate-x-[120px] -translate-y-14 sm:h-[144px] sm:w-[144px] sm:rotate-0 sm:-translate-x-[80px] sm:-translate-y-[160px]"
                            : `top${typeOfCube} face${typeOfCube}`
                            } grid grid-cols-3 gap-0 border-2 select-none`}
                    >
                        {Array(9)
                            .fill(null)
                            .map((_, index) => (
                                <div
                                    key={`top-${index}`}
                                    className={`w-full h-full border border-black ${cubeColors.top[index]} text-black`}
                                    onClick={() =>
                                        setCubeColors((prevColors) => {
                                            const updatedColors = { ...prevColors };
                                            updatedColors.top[index] = currentColor;
                                            return updatedColors;
                                        })
                                    }
                                >
                                    {index + 1}U
                                </div>
                            ))}
                    </div>

                    <div
                        className={`${typeOfCube == "2d"
                            ? "absolute border border-black ease-in-out duration-1000 w-28 h-28 rotate-90 -translate-x-[120px] -translate-y-14 sm:h-[144px] sm:w-[144px] sm:rotate-0 sm:-translate-x-[80px] sm:translate-y-[160px]"
                            : `bottom${typeOfCube} face${typeOfCube}`
                            } grid grid-cols-3 gap-0 border-2 select-none`}
                    >
                        {Array(9)
                            .fill(null)
                            .map((_, index) => (
                                <div
                                    key={`bottom-${index}`}
                                    className={`w-full h-full border border-black ${cubeColors.bottom[index]} text-black`}
                                    onClick={() =>
                                        setCubeColors((prevColors) => {
                                            const updatedColors = { ...prevColors };
                                            updatedColors.bottom[index] = currentColor;
                                            return updatedColors;
                                        })
                                    }
                                >
                                    {index + 1}D
                                </div>
                            ))}
                    </div>
                </div>
            </div>

            {/* manuver 3d cube */}
            <div
                className={`${hidden ? "hidden" : ""
                    } flex justify-center align-middle `}
            >
                <div
                    className="w-16 h-12 flex items-center justify-center"
                    onClick={() => setRotation((prev) => ({ y: prev.y - 90, z: prev.z }))}
                >
                    <PiArrowBendLeftUpBold size={30} className="-rotate-12 text-white" />
                </div>
                <div
                    className="flex items-center justify-center w-16 h-12"
                    onClick={() =>
                        setRotation((prev) => ({ y: prev.y, z: prev.z - 180 }))
                    }
                >
                    <FaArrowUpLong size={25} className="text-white" />
                </div>

                <div
                    className=" w-16 h-12 flex items-center justify-center"
                    onClick={() => setRotation((prev) => ({ y: prev.y + 90, z: prev.z }))}
                >
                    <PiArrowBendRightUpBold size={30} className="rotate-12 text-white" />
                </div>
            </div>
        </div>
    );
};
export default Cube;
