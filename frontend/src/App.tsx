import { useState } from 'react'
import MusicGenerator from './components/MusicGenerator'
import Header from './components/Header'
import './App.css'

function App() {
  return (
    <div className="app">
      <Header />
      <main className="main-content">
        <MusicGenerator />
      </main>
    </div>
  )
}

export default App