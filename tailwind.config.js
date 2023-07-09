/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors: {
        chatblack:{
          50 : '#343541',
          100 : '#343541'
        },
        okbtn : {800 : '#19C37D'}
    },
  },
  plugins: [],
}
}
