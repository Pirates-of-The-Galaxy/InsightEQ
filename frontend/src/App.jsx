import { useState } from 'react'
import Hero from './components/Hero'
import Navbar from './components/Navbar'
import Features from './components/Features'
import Footer from './components/Footer'

function App() {
 

  return (
    <main className="bg-black">
    <Navbar />
    <Hero />
    {/* <Model /> */}
    <Features />
    {/* <HowItWorks /> */}
    <Footer />
  </main>
  )
}

export default App
