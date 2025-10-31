import express from 'express'
import { generateMusicAudio } from '../services/musicGenerator.js'

const router = express.Router()

/**
 * POST /api/generate
 * Generate music based on parameters
 * 
 * Body:
 * - keywords: string (e.g., "enerjik, sinematik, elektronik")
 * - duration: number (in seconds)
 * - style: string (cinematic, electronic, acoustic, etc.)
 * - tempo: string (slow, medium, fast)
 */
export const generateMusicRoute = async (req, res) => {
  try {
    const { keywords, duration, style, tempo } = req.body

    // Validation
    if (!keywords || typeof keywords !== 'string' || keywords.trim().length === 0) {
      return res.status(400).json({ 
        error: 'Anahtar kelimeler gereklidir' 
      })
    }

    if (!duration || typeof duration !== 'number' || duration <= 0) {
      return res.status(400).json({ 
        error: 'Ge?erli bir s?re belirtilmelidir' 
      })
    }

    // Generate music
    const audioBuffer = await generateMusicAudio({
      keywords: keywords.trim(),
      duration,
      style: style || 'cinematic',
      tempo: tempo || 'medium'
    })

    // Set headers for audio file
    res.setHeader('Content-Type', 'audio/wav')
    res.setHeader('Content-Disposition', `attachment; filename="music-${Date.now()}.wav"`)
    res.setHeader('Content-Length', audioBuffer.length)

    // Send audio buffer
    res.send(Buffer.from(audioBuffer))
  } catch (error) {
    console.error('Music generation error:', error)
    res.status(500).json({ 
      error: error.message || 'M?zik olu?turulurken bir hata olu?tu' 
    })
  }
}