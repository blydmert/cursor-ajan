import express from 'express'
import cors from 'cors'
import dotenv from 'dotenv'
import { generateMusicRoute } from './routes/generate.js'
import { convertToMIDIRoute } from './routes/midi.js'

dotenv.config()

const app = express()
const PORT = process.env.PORT || 3001

app.use(cors())
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', message: 'AI Music Composition Assistant API' })
})

// Routes
app.post('/api/generate', generateMusicRoute)
app.post('/api/convert-to-midi', convertToMIDIRoute)

app.listen(PORT, () => {
  console.log(`?? Server running on http://localhost:${PORT}`)
  console.log(`?? API Documentation: http://localhost:${PORT}/api/health`)
})