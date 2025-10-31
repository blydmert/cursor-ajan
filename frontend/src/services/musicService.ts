import axios from 'axios'

const API_BASE_URL = '/api'

export interface GenerationParams {
  keywords: string
  duration: number
  style: string
  tempo: string
}

export interface GenerationResult {
  audioUrl: string
  midiUrl?: string
  metadata?: {
    duration: number
    format: string
  }
}

export const generateMusic = async (params: GenerationParams): Promise<GenerationResult> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/generate`, params, {
      responseType: 'blob',
      timeout: 300000, // 5 minutes timeout for generation
      validateStatus: (status) => status === 200, // Only treat 200 as success
    })

    // Check if response is actually an error JSON
    const contentType = response.headers['content-type']
    if (contentType && contentType.includes('application/json')) {
      const text = await response.data.text()
      const errorData = JSON.parse(text)
      throw new Error(errorData.error || errorData.message || 'M?zik olu?turulurken bir hata olu?tu')
    }

    // Create blob URL from response
    const blob = new Blob([response.data], { type: 'audio/wav' })
    const audioUrl = URL.createObjectURL(blob)

    return {
      audioUrl,
      metadata: {
        duration: params.duration,
        format: 'wav'
      }
    }
  } catch (error: any) {
    if (error.response) {
      // Try to parse error response if it's a blob
      if (error.response.data instanceof Blob) {
        try {
          const text = await error.response.data.text()
          const errorData = JSON.parse(text)
          throw new Error(errorData.error || errorData.message || 'M?zik olu?turulurken bir hata olu?tu')
        } catch {
          throw new Error('M?zik olu?turulurken bir hata olu?tu')
        }
      } else {
        throw new Error(error.response.data?.error || error.response.data?.message || 'M?zik olu?turulurken bir hata olu?tu')
      }
    } else if (error.request) {
      throw new Error('Sunucuya ba?lan?lamad?. L?tfen tekrar deneyin.')
    } else {
      throw new Error(error.message || 'Beklenmeyen bir hata olu?tu')
    }
  }
}

export const downloadMIDI = async (audioUrl: string): Promise<string> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/convert-to-midi`, {
      audioUrl
    }, {
      responseType: 'blob'
    })

    const blob = new Blob([response.data], { type: 'audio/midi' })
    return URL.createObjectURL(blob)
  } catch (error: any) {
    throw new Error(error.response?.data?.message || 'MIDI d?n??t?rme ba?ar?s?z')
  }
}