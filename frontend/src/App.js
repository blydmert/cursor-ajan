import React, { useState } from 'react';
import './App.css';
import MusicGenerator from './components/MusicGenerator';
import AudioPlayer from './components/AudioPlayer';
import PricingModal from './components/PricingModal';

function App() {
  const [generatedMusic, setGeneratedMusic] = useState(null);
  const [isPremium, setIsPremium] = useState(false);
  const [showPricing, setShowPricing] = useState(false);

  const handleGenerate = (musicData) => {
    setGeneratedMusic(musicData);
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="header-content">
          <h1>?? AI M?zik Kompozisyon Asistan?</h1>
          <p className="tagline">Yarat?c?l???n?z? yapay zeka ile g??lendirin</p>
        </div>
        <button 
          className={`premium-badge ${isPremium ? 'active' : ''}`}
          onClick={() => setShowPricing(true)}
        >
          {isPremium ? '? Premium' : '?? Y?kselt'}
        </button>
      </header>

      <main className="App-main">
        <MusicGenerator 
          onGenerate={handleGenerate} 
          isPremium={isPremium}
        />
        
        {generatedMusic && (
          <AudioPlayer 
            musicData={generatedMusic}
            isPremium={isPremium}
          />
        )}
      </main>

      <footer className="App-footer">
        <p>? 2025 AI M?zik Kompozisyon Asistan? - T?m haklar? sakl?d?r</p>
        <div className="footer-links">
          <a href="#about">Hakk?nda</a>
          <a href="#privacy">Gizlilik</a>
          <a href="#terms">Kullan?m ?artlar?</a>
        </div>
      </footer>

      {showPricing && (
        <PricingModal 
          onClose={() => setShowPricing(false)}
          onUpgrade={() => {
            setIsPremium(true);
            setShowPricing(false);
          }}
        />
      )}
    </div>
  );
}

export default App;
