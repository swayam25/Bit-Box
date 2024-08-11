/** @type {import("tailwindcss").Config} */
module.exports = {
  content: ["./src/**/*.{html,js,svelte,ts}"],
  darkMode: "class",
  theme: {
      extend: {
          colors: {
              "orange": {
                  "bright": "#FFAF21",
                  "rust-lite": "#52330B",
                  "rust": "#312009",
                  "dark": "#110B03"
              }
          },
          boxShadow: {
              "full": "0px 0px 15px"
          }
      }
  },
  plugins: [
      require("tailwindcss"),
      require("autoprefixer")
  ]
}