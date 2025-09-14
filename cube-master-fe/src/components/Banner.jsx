import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import homepagecubepic from "./../assets/homepage-cube-pic.jpg";


const Banner = () => {
    const navigate = useNavigate();
    const navigateToSolve = () => {
        navigate("/solve");
    }
    return (
        <div className="w-full h-screen bg-black flex flex-col md:flex-row">
            {/* Left side text */}
            <div className="md:w-1/2 p-8 md:ml-6 text-center md:text-left flex flex-col justify-center">
                <h1 className="text-5xl font-bold text-white mb-4 mt-12 md:mt-0">
                    Cube Master
                </h1>
                <p className="text-xl text-gray-300 mb-2">Rubik's Cube Solver</p>
                <p className="text-lg text-gray-400 mb-4">
                    Our solver is designed to capture images of a Rubik's cube face,
                    analyze them, and provide step-by-step instructions to solve it.
                </p>
                <button
                    onClick={navigateToSolve}
                    className="bg-blue-600 text-white py-2 px-6 rounded hover:bg-blue-700 transition duration-300"
                >
                    Solve the Cube
                </button>
            </div>

            {/* Right side image */}
            <div className="md:w-1/2 h-full">
                <img
                    src={homepagecubepic}
                    alt="Rubik's Cube Solver"
                    className="w-full h-full object-contain"
                />
            </div>
        </div>

    );
};

export default Banner;
