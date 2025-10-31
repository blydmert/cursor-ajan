import React, { useState, useEffect, useRef } from 'react';
import * as Tone from 'tone';
import { Midi } from '@tonejs/midi';
import './AudioPlayer.css';

function AudioPlayer({ musicData, isPremium }) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [volume, setVolume] = useState(-10);
  const synthsRef = useRef([]);
  const intervalRef = useRef(null);
  const startTimeRef = useRef(0);

  useEffect(() => {
    if (musicData) {
      loadMusic();
    }
    return () => {
      stopMusic();
      disposeSynths();
    };
  }, [musicData]);

  const disposeSynths = () => {
    synthsRef.current.forEach(synth => {
      try {
        synth.dispose();
      } catch (e) {
        console.error('Error disposing synth:', e);
      }
    });
    synthsRef.current = [];
  };

  const loadMusic = () => {
    stopMusic();
    disposeSynths();

    // Calculate duration
    const allNotes = [
      ...musicData.midi_data.tracks.melody,
      ...musicData.midi_data.tracks.harmony,
      ...musicData.midi_data.tracks.bass,
      ...(musicData.midi_data.tracks.drums || []),
      ...(musicData.midi_data.tracks.additional || [])
    ];

    const maxTime = Math.max(...allNotes.map(note => note.time + note.duration));
    setDuration(maxTime);
  };

  const midiToFrequency = (midiNote) => {
    return Tone.Frequency(midiNote, "midi").toFrequency();
  };

  const playMusic = async () => {
    await Tone.start();
    
    // Clear existing synths
    disposeSynths();

    // Create synths for different tracks
    const melodySynth = new Tone.PolySynth(Tone.Synth, {
      oscillator: { type: "triangle" },
      envelope: {
        attack: 0.02,
        decay: 0.1,
        sustain: 0.3,
        release: 0.5
      }
    }).toDestination();
    melodySynth.volume.value = volume;

    const harmonySynth = new Tone.PolySynth(Tone.Synth, {
      oscillator: { type: "sine" },
      envelope: {
        attack: 0.05,
        decay: 0.3,
        sustain: 0.5,
        release: 1
      }
    }).toDestination();
    harmonySynth.volume.value = volume - 5;

    const bassSynth = new Tone.MonoSynth({
      oscillator: { type: "sawtooth" },
      envelope: {
        attack: 0.01,
        decay: 0.2,
        sustain: 0.2,
        release: 0.5
      }
    }).toDestination();
    bassSynth.volume.value = volume + 3;

    synthsRef.current = [melodySynth, harmonySynth, bassSynth];

    // Schedule notes
    const now = Tone.now();
    startTimeRef.current = now;

    // Melody
    musicData.midi_data.tracks.melody.forEach(note => {
      const freq = midiToFrequency(note.note);
      melodySynth.triggerAttackRelease(freq, note.duration, now + note.time, note.velocity / 127);
    });

    // Harmony
    musicData.midi_data.tracks.harmony.forEach(note => {
      const freq = midiToFrequency(note.note);
      harmonySynth.triggerAttackRelease(freq, note.duration, now + note.time, note.velocity / 127);
    });

    // Bass
    musicData.midi_data.tracks.bass.forEach(note => {
      const freq = midiToFrequency(note.note);
      bassSynth.triggerAttackRelease(freq, note.duration, now + note.time, note.velocity / 127);
    });

    // Drums (if premium)
    if (isPremium && musicData.midi_data.tracks.drums.length > 0) {
      const drumSynth = new Tone.MembraneSynth().toDestination();
      drumSynth.volume.value = volume;
      synthsRef.current.push(drumSynth);

      musicData.midi_data.tracks.drums.forEach(note => {
        const freq = midiToFrequency(note.note);
        drumSynth.triggerAttackRelease(freq, note.duration, now + note.time, note.velocity / 127);
      });
    }

    // Update current time
    intervalRef.current = setInterval(() => {
      const elapsed = Tone.now() - startTimeRef.current;
      setCurrentTime(elapsed);
      
      if (elapsed >= duration) {
        stopMusic();
      }
    }, 100);

    setIsPlaying(true);
  };

  const stopMusic = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
    
    synthsRef.current.forEach(synth => {
      try {
        synth.releaseAll();
      } catch (e) {
        console.error('Error releasing synth:', e);
      }
    });

    setIsPlaying(false);
    setCurrentTime(0);
  };

  const togglePlayPause = () => {
    if (isPlaying) {
      stopMusic();
    } else {
      playMusic();
    }
  };

  const handleVolumeChange = (e) => {
    const newVolume = parseInt(e.target.value);
    setVolume(newVolume);
    
    synthsRef.current.forEach(synth => {
      synth.volume.value = newVolume;
    });
  };

  const exportMidi = () => {
    const midi = new Midi();
    midi.header.setTempo(musicData.midi_data.tempo);

    // Add tracks
    const tracks = [
      { name: 'Melody', notes: musicData.midi_data.tracks.melody },
      { name: 'Harmony', notes: musicData.midi_data.tracks.harmony },
      { name: 'Bass', notes: musicData.midi_data.tracks.bass }
    ];

    if (isPremium) {
      tracks.push({ name: 'Drums', notes: musicData.midi_data.tracks.drums });
      tracks.push({ name: 'Additional', notes: musicData.midi_data.tracks.additional });
    }

    tracks.forEach(({ name, notes }) => {
      const track = midi.addTrack();
      track.name = name;
      
      notes.forEach(note => {
        track.addNote({
          midi: note.note,
          time: note.time,
          duration: note.duration,
          velocity: note.velocity / 127
        });
      });
    });

    // Download
    const blob = new Blob([midi.toArray()], { type: 'audio/midi' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `ai-music-${Date.now()}.mid`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  if (!musicData) return null;

  return (
    <div className="audio-player">
      <div className="player-card">
        <h3>?? M?zi?iniz Haz?r!</h3>
        
        <div className="metadata">
          <div className="metadata-item">
            <span className="label">Anahtar Kelimeler:</span>
            <span className="value">{musicData.metadata.keywords.join(', ')}</span>
          </div>
          <div className="metadata-row">
            <div className="metadata-item">
              <span className="label">Tempo:</span>
              <span className="value">{musicData.metadata.tempo} BPM</span>
            </div>
            <div className="metadata-item">
              <span className="label">Anahtar:</span>
              <span className="value">{musicData.metadata.key} {musicData.metadata.scale}</span>
            </div>
          </div>
        </div>

        <div className="player-controls">
          <button onClick={togglePlayPause} className="play-btn">
            {isPlaying ? '?? Duraklat' : '?? Oynat'}
          </button>
          
          <div className="progress-container">
            <div className="time-display">
              {formatTime(currentTime)} / {formatTime(duration)}
            </div>
            <div className="progress-bar">
              <div 
                className="progress-fill"
                style={{ width: `${(currentTime / duration) * 100}%` }}
              />
            </div>
          </div>

          <div className="volume-control">
            <span>??</span>
            <input
              type="range"
              min="-30"
              max="0"
              value={volume}
              onChange={handleVolumeChange}
              className="volume-slider"
            />
          </div>
        </div>

        <div className="export-section">
          <button onClick={exportMidi} className="export-btn">
            ?? MIDI ?ndir
          </button>
          {!isPremium && (
            <p className="export-hint">
              ?? Premium ile WAV ve MP3 formatlar?nda da indirebilirsiniz!
            </p>
          )}
        </div>
      </div>
    </div>
  );
}

export default AudioPlayer;
