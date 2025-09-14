import React, { useState } from "react";

const FillCube = ({ setCurrentColor, currentColor, setCubeColors, initialFaceColors }) => {
    return (
        <div className="my-2">
            <p className=" text-white font-bold text-lg select-none my-2 px-3 ">
                Fill Cube:
            </p>

            {/* colors */}
            <div
                className={`${currentColor} border-2 border-black p-3 mb-2 rounded-3xl flex align-middle justify-center flex-wrap`}
            >
                <div className="">
                    <div
                        className="bg-blue-600 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                        onClick={() => {
                            setCurrentColor("bg-blue-600");
                        }}
                    ></div>
                    <div
                        className="bg-green-500 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                        onClick={() => {
                            setCurrentColor("bg-green-500");
                        }}
                    ></div>
                    <div
                        className="bg-red-500 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                        onClick={() => {
                            setCurrentColor("bg-red-500");
                        }}
                    ></div>
                </div>
                <div className="">
                    <div
                        className="bg-orange-500 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                        onClick={() => {
                            setCurrentColor("bg-orange-500");
                        }}
                    ></div>
                    <div
                        className="bg-yellow-400 border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                        onClick={() => {
                            setCurrentColor("bg-yellow-400");
                        }}
                    ></div>
                    <div
                        className="bg-white border-2 border-black h-14 w-14 rounded-2xl mx-2 inline-block"
                        onClick={() => {
                            setCurrentColor("bg-white");
                        }}
                    ></div>
                </div>
                <div
                    className="py-4 bg-gray-500 text-white select-none h-14 w-14 rounded-2xl mx-2 text-center"
                    onClick={() => {
                        setCurrentColor("bg-white");
                        setCubeColors((prevColors) => {
                            const updatedColors = { ...prevColors };
                            const faces = ["front", "back", "left", "right", "top", "bottom"];
                            faces.forEach((face) => {
                                updatedColors[face] = [...initialFaceColors];
                            });
                            return updatedColors;
                        });
                    }}
                >
                    Clear
                </div>
            </div>
        </div>
    );
};
export default FillCube;
