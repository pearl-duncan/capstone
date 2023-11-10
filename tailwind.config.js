/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["/"],
  theme: {
    extend: {},
  },
  plugins: [],
}



module.exports = {
  //...
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
}

module.exports = {
  future: {},
  purge: [],
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}

module.exports = {

  plugins: [
      require('flowbite/plugin')
  ]

}

module.exports = {

  content: [
      "./node_modules/flowbite/**/*.js"
  ]

}