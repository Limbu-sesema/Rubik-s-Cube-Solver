/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      animation: {
        "opacity-fade": "fade 2s infinite", // Animation name and timing
      },
      keyframes: {
        fade: {
          "0%": { opacity: "1" }, // Fully opaque
          "50%": { opacity: "0.5" }, // Fully transparent
        },
      },
    },
  },
  plugins: [],
};
