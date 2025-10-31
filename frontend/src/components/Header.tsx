import { Music } from 'lucide-react'
import './Header.css'

const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <div className="logo">
          <Music className="logo-icon" />
          <h1>AI M?zik Kompozisyon Asistan?</h1>
        </div>
        <p className="tagline">?zg?n m?zikler olu?turun, yarat?c?l???n?z? serbest b?rak?n</p>
      </div>
    </header>
  )
}

export default Header