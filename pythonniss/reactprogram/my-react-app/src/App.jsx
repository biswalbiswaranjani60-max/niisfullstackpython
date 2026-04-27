import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import React, { Component } from "react"
import App1 from './App1';

function Welcome() {
  return <h1>Hello User!</h1>
}


class Mycomponent extends Component {
  render() {
    return <p>This is a class component</p>;
  }
}
function App() {
  return (
    <>
      <div>
        <b>Welcome react</b><br />
        <i>hi</i><br />
        <App1/>
        <Welcome/>
        <Mycomponent/>
      </div>
    </>
  )
}

export default App
