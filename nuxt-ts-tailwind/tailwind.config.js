module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
  ],

  plugins: [require("daisyui")],

  daisyui: {
    themes: ["forest"],
  },
};
