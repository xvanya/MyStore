// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import axios from 'axios'
import './App.css'
import { useEffect } from 'react'

function App() {
  // const [count, setCount] = useState(0)

  useEffect(() => {
    axios.get('http://localhost:4097/api/categories')
      .then(response => {
        console.log("Response: ", response.data)
      })
      .catch(error => {
        console.log(error)
      })
  }, [])

  return (
    <>
      <h1>Hello World</h1>
    </>
  )
}

export default App
 