import React, { useState, useEffect } from 'react';
import './MusicGenerator.css';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function MusicGenerator({ onGenerate, isPremium }) {
  const [keywords, setKeywords] = useState('');
  const [duration, setDuration] = useState(30);
  const [tempo, setTempo] = useState(120);
  const [keyNote, setKeyNote] = useState('C');
  const [scale, setScale] = useState('major');
  const [style, setStyle] = useState('electronic');
  const [styles, setStyles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchStyles();
  }, []);

  const fetchStyles = async () => {
    try {
      const response = await axios.get(`${API_URL}/styles`);
      setStyles(response.data.styles);
    } catch (err) {
      console.error('Error fetching styles:', err);
    }
  };

  const handleGenerate = async () => {
    if (!keywords.trim()) {
      setError('L?tfen en az bir anahtar kelime girin');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const keywordList = keywords.split(',').map(k => k.trim()).filter(k => k);
      
      const response = await axios.post(`${API_URL}/generate`, {
        keywords: keywordList,
        duration: isPremium ? duration : Math.min(duration, 30),
        tempo,
        key: keyNote,
        scale,
        style,
        is_premium: isPremium
      });

      onGenerate(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'M?zik olu?turulurken bir hata olu?tu');
    } finally {
      setLoading(false);
    }
  };

  const presetKeywords = [
    'enerjik, elektronik, dans',
    'sakin, ambient, meditasyon',
    'sinematik, epik, orkestra',
    'karanl?k, gizemli, gerilim',
    'mutlu, ne?eli, pop',
    'duygusal, melankoli, piyano'
  ];

  return (
    <div className="music-generator">
      <div className="generator-card">
        <h2>M?zik Olu?tur</h2>
        
        <div className="form-group">
          <label>Anahtar Kelimeler (virg?lle ay?r?n)</label>
          <input
            type="text"
            value={keywords}
            onChange={(e) => setKeywords(e.target.value)}
            placeholder="?rn: enerjik, sinematik, elektronik"
            className="input-field"
          />
          
          <div className="preset-keywords">
            {presetKeywords.map((preset, idx) => (
              <button
                key={idx}
                className="preset-btn"
                onClick={() => setKeywords(preset)}
              >
                {preset}
              </button>
            ))}
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Stil</label>
            <select
              value={style}
              onChange={(e) => setStyle(e.target.value)}
              className="input-field"
            >
              {styles.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.name}
                </option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>S?re (saniye) {!isPremium && duration > 30 && <span className="premium-label">? Premium</span>}</label>
            <input
              type="number"
              value={duration}
              onChange={(e) => setDuration(parseInt(e.target.value))}
              min="10"
              max={isPremium ? "300" : "30"}
              className="input-field"
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Tempo (BPM)</label>
            <input
              type="range"
              value={tempo}
              onChange={(e) => setTempo(parseInt(e.target.value))}
              min="60"
              max="180"
              className="slider"
            />
            <span className="slider-value">{tempo} BPM</span>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>Anahtar</label>
            <select
              value={keyNote}
              onChange={(e) => setKeyNote(e.target.value)}
              className="input-field"
            >
              {['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'].map(note => (
                <option key={note} value={note}>{note}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Skala</label>
            <select
              value={scale}
              onChange={(e) => setScale(e.target.value)}
              className="input-field"
            >
              <option value="major">Major</option>
              <option value="minor">Minor</option>
              <option value="pentatonic">Pentatonic</option>
              <option value="blues">Blues</option>
              <option value="dorian">Dorian</option>
            </select>
          </div>
        </div>

        {error && <div className="error-message">{error}</div>}

        <button
          onClick={handleGenerate}
          disabled={loading}
          className="generate-btn"
        >
          {loading ? '?? Olu?turuluyor...' : '? M?zik Olu?tur'}
        </button>

        {!isPremium && (
          <div className="feature-hint">
            ?? Premium ile 5 dakikaya kadar m?zik, davul partileri ve daha fazla ?zellik!
          </div>
        )}
      </div>
    </div>
  );
}

export default MusicGenerator;
