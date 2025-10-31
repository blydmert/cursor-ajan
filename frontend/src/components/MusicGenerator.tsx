import { useState } from 'react'
import { Play, Pause, Download, Loader, Sparkles } from 'lucide-react'
import AudioPlayer from './AudioPlayer'
import './MusicGenerator.css'
import { generateMusic } from '../services/musicService'

interface GenerationParams {
  keywords: string
  duration: number
  style: string
  tempo: string
}

const MusicGenerator = () => {
  const [params, setParams] = useState<GenerationParams>({
    keywords: '',
    duration: 60,
    style: 'cinematic',
    tempo: 'medium'
  })
  
  const [isGenerating, setIsGenerating] = useState(false)
  const [audioUrl, setAudioUrl] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const handleGenerate = async () => {
    if (!params.keywords.trim()) {
      setError('L?tfen en az bir anahtar kelime girin')
      return
    }

    setIsGenerating(true)
    setError(null)
    setAudioUrl(null)

    try {
      const result = await generateMusic(params)
      setAudioUrl(result.audioUrl)
    } catch (err: any) {
      setError(err.message || 'M?zik olu?turulurken bir hata olu?tu')
    } finally {
      setIsGenerating(false)
    }
  }

  const handleDownload = () => {
    if (audioUrl) {
      const link = document.createElement('a')
      link.href = audioUrl
      link.download = `muzik-${Date.now()}.wav`
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }

  return (
    <div className="music-generator">
      <div className="generator-card">
        <div className="card-header">
          <Sparkles className="header-icon" />
          <h2>Yeni M?zik Olu?tur</h2>
        </div>

        <div className="form-section">
          <label className="form-label">
            Anahtar Kelimeler
            <span className="label-hint">?rn: enerjik, sinematik, elektronik</span>
          </label>
          <input
            type="text"
            className="form-input"
            placeholder="M?zi?inizi tan?mlayan kelimeler girin..."
            value={params.keywords}
            onChange={(e) => setParams({ ...params, keywords: e.target.value })}
            disabled={isGenerating}
          />
        </div>

        <div className="form-row">
          <div className="form-section">
            <label className="form-label">S?re (saniye)</label>
            <select
              className="form-select"
              value={params.duration}
              onChange={(e) => setParams({ ...params, duration: Number(e.target.value) })}
              disabled={isGenerating}
            >
              <option value={30}>30 saniye</option>
              <option value={60}>1 dakika</option>
              <option value={120}>2 dakika</option>
              <option value={180}>3 dakika</option>
              <option value={300}>5 dakika</option>
            </select>
          </div>

          <div className="form-section">
            <label className="form-label">Stil</label>
            <select
              className="form-select"
              value={params.style}
              onChange={(e) => setParams({ ...params, style: e.target.value })}
              disabled={isGenerating}
            >
              <option value="cinematic">Sinematik</option>
              <option value="electronic">Elektronik</option>
              <option value="acoustic">Akustik</option>
              <option value="ambient">Ambient</option>
              <option value="rock">Rock</option>
              <option value="jazz">Jazz</option>
              <option value="classical">Klasik</option>
            </select>
          </div>

          <div className="form-section">
            <label className="form-label">Tempo</label>
            <select
              className="form-select"
              value={params.tempo}
              onChange={(e) => setParams({ ...params, tempo: e.target.value })}
              disabled={isGenerating}
            >
              <option value="slow">Yava?</option>
              <option value="medium">Orta</option>
              <option value="fast">H?zl?</option>
            </select>
          </div>
        </div>

        <button
          className="generate-button"
          onClick={handleGenerate}
          disabled={isGenerating || !params.keywords.trim()}
        >
          {isGenerating ? (
            <>
              <Loader className="button-icon spinning" />
              Olu?turuluyor...
            </>
          ) : (
            <>
              <Sparkles className="button-icon" />
              M?zik Olu?tur
            </>
          )}
        </button>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {audioUrl && (
          <div className="result-section">
            <AudioPlayer audioUrl={audioUrl} />
            <button
              className="download-button"
              onClick={handleDownload}
            >
              <Download className="button-icon" />
              ?ndir (WAV)
            </button>
          </div>
        )}
      </div>

      <div className="info-cards">
        <div className="info-card">
          <h3>?? ?zg?n M?zikler</h3>
          <p>AI ile tamamen ?zg?n ve telifsiz m?zikler olu?turun</p>
        </div>
        <div className="info-card">
          <h3>? H?zl? ?retim</h3>
          <p>Kompozisyon s?recinizi h?zland?r?n, yarat?c? blokaj? a??n</p>
        </div>
        <div className="info-card">
          <h3>?? ?ok Ama?l? Kullan?m</h3>
          <p>YouTube, film, oyun veya sosyal medya i?in m?zikler</p>
        </div>
      </div>
    </div>
  )
}

export default MusicGenerator