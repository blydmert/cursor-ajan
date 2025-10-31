import random
import uuid
from typing import List, Dict, Any
import json

class MusicGenerator:
    """
    AI-powered music generation engine using music theory and algorithmic composition
    """
    
    def __init__(self):
        self.scales = {
            "major": [0, 2, 4, 5, 7, 9, 11],
            "minor": [0, 2, 3, 5, 7, 8, 10],
            "pentatonic": [0, 2, 4, 7, 9],
            "blues": [0, 3, 5, 6, 7, 10],
            "dorian": [0, 2, 3, 5, 7, 9, 10],
            "phrygian": [0, 1, 3, 5, 7, 8, 10]
        }
        
        self.chord_progressions = {
            "pop": [[0, 4, 7], [5, 9, 12], [7, 11, 14], [0, 4, 7]],  # I-IV-V-I
            "emotional": [[0, 4, 7], [5, 9, 12], [3, 7, 10], [5, 9, 12]],  # I-IV-iii-IV
            "dark": [[0, 3, 7], [5, 8, 12], [7, 10, 14], [0, 3, 7]],  # i-iv-v-i
            "uplifting": [[0, 4, 7], [7, 11, 14], [9, 12, 16], [5, 9, 12]],  # I-V-vi-IV
            "jazzy": [[0, 4, 7, 11], [5, 9, 12, 16], [7, 11, 14, 17], [0, 4, 7, 11]]  # 7th chords
        }
        
        self.rhythm_patterns = {
            "energetic": [1, 0, 1, 0, 1, 0, 1, 1],
            "relaxed": [1, 0, 0, 1, 0, 0, 1, 0],
            "syncopated": [1, 0, 1, 1, 0, 1, 0, 1],
            "steady": [1, 0, 1, 0, 1, 0, 1, 0]
        }
        
    def _note_to_midi(self, note_name: str) -> int:
        """Convert note name to MIDI number"""
        notes = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 
                 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
        return notes.get(note_name, 0) + 60  # Middle C octave
    
    def _analyze_keywords(self, keywords: List[str]) -> Dict[str, Any]:
        """Analyze keywords to determine musical characteristics"""
        characteristics = {
            "energy": 0.5,
            "complexity": 0.5,
            "darkness": 0.5,
            "rhythm_style": "steady",
            "chord_style": "pop"
        }
        
        energy_words = ["energetic", "fast", "intense", "powerful", "dynamic"]
        calm_words = ["calm", "relaxed", "ambient", "peaceful", "soft"]
        dark_words = ["dark", "mysterious", "dramatic", "tense", "cinematic"]
        complex_words = ["complex", "jazz", "intricate", "progressive"]
        
        for keyword in keywords:
            keyword_lower = keyword.lower()
            
            if any(word in keyword_lower for word in energy_words):
                characteristics["energy"] += 0.2
                characteristics["rhythm_style"] = "energetic"
            
            if any(word in keyword_lower for word in calm_words):
                characteristics["energy"] -= 0.2
                characteristics["rhythm_style"] = "relaxed"
            
            if any(word in keyword_lower for word in dark_words):
                characteristics["darkness"] += 0.3
                characteristics["chord_style"] = "dark"
            
            if any(word in keyword_lower for word in complex_words):
                characteristics["complexity"] += 0.3
                characteristics["chord_style"] = "jazzy"
            
            if "uplifting" in keyword_lower or "happy" in keyword_lower:
                characteristics["chord_style"] = "uplifting"
        
        # Clamp values
        characteristics["energy"] = max(0, min(1, characteristics["energy"]))
        characteristics["complexity"] = max(0, min(1, characteristics["complexity"]))
        characteristics["darkness"] = max(0, min(1, characteristics["darkness"]))
        
        return characteristics
    
    def _generate_melody(self, scale_notes: List[int], num_bars: int, 
                        characteristics: Dict[str, Any], root_note: int) -> List[Dict]:
        """Generate a melody line"""
        melody = []
        notes_per_bar = 8 if characteristics["energy"] > 0.6 else 4
        
        current_time = 0
        note_duration = 0.5 if characteristics["energy"] > 0.6 else 1.0
        
        for bar in range(num_bars):
            for note_idx in range(notes_per_bar):
                # Generate note based on scale
                if random.random() > 0.1:  # 90% note, 10% rest
                    # Prefer notes closer to previous note for smooth melody
                    scale_degree = random.choice(scale_notes)
                    octave_offset = random.choice([0, 12]) if random.random() > 0.7 else 0
                    midi_note = root_note + scale_degree + octave_offset
                    
                    velocity = int(80 + characteristics["energy"] * 40)
                    
                    melody.append({
                        "note": midi_note,
                        "time": current_time,
                        "duration": note_duration,
                        "velocity": velocity
                    })
                
                current_time += note_duration
        
        return melody
    
    def _generate_harmony(self, chord_progression: List[List[int]], 
                         num_bars: int, root_note: int, tempo: int) -> List[Dict]:
        """Generate harmony/chord progression"""
        harmony = []
        beats_per_bar = 4
        bar_duration = (60 / tempo) * beats_per_bar
        
        for bar in range(num_bars):
            chord = chord_progression[bar % len(chord_progression)]
            time = bar * bar_duration
            
            for note_offset in chord:
                harmony.append({
                    "note": root_note + note_offset - 12,  # One octave lower
                    "time": time,
                    "duration": bar_duration,
                    "velocity": 60
                })
        
        return harmony
    
    def _generate_bass(self, chord_progression: List[List[int]], 
                      num_bars: int, root_note: int, tempo: int,
                      rhythm_pattern: List[int]) -> List[Dict]:
        """Generate bass line"""
        bass = []
        beats_per_bar = 4
        beat_duration = 60 / tempo
        
        for bar in range(num_bars):
            chord = chord_progression[bar % len(chord_progression)]
            root_of_chord = chord[0]
            
            for beat_idx, should_play in enumerate(rhythm_pattern):
                if should_play:
                    time = bar * beats_per_bar * beat_duration + beat_idx * beat_duration
                    bass.append({
                        "note": root_note + root_of_chord - 24,  # Two octaves lower
                        "time": time,
                        "duration": beat_duration * 0.8,
                        "velocity": 90
                    })
        
        return bass
    
    def _generate_drums(self, num_bars: int, tempo: int, 
                       rhythm_style: str) -> List[Dict]:
        """Generate drum pattern"""
        drums = []
        beats_per_bar = 4
        beat_duration = 60 / tempo
        
        # MIDI drum notes
        kick = 36
        snare = 38
        hihat = 42
        
        for bar in range(num_bars):
            for beat in range(beats_per_bar):
                time = bar * beats_per_bar * beat_duration + beat * beat_duration
                
                # Kick on beats 1 and 3
                if beat in [0, 2]:
                    drums.append({"note": kick, "time": time, "duration": 0.1, "velocity": 100})
                
                # Snare on beats 2 and 4
                if beat in [1, 3]:
                    drums.append({"note": snare, "time": time, "duration": 0.1, "velocity": 90})
                
                # Hi-hat on every beat
                if rhythm_style == "energetic":
                    for sub_beat in range(2):
                        drums.append({
                            "note": hihat,
                            "time": time + sub_beat * beat_duration / 2,
                            "duration": 0.05,
                            "velocity": 70
                        })
                else:
                    drums.append({"note": hihat, "time": time, "duration": 0.05, "velocity": 70})
        
        return drums
    
    def generate(self, keywords: List[str], duration: int, style: str,
                tempo: int, key: str, scale: str, is_premium: bool) -> Dict[str, Any]:
        """
        Main generation method
        """
        # Analyze keywords for musical characteristics
        characteristics = self._analyze_keywords(keywords)
        
        # Get scale notes
        scale_type = scale if scale in self.scales else "major"
        if characteristics["darkness"] > 0.6:
            scale_type = "minor"
        
        scale_notes = self.scales[scale_type]
        root_note = self._note_to_midi(key)
        
        # Calculate number of bars
        beats_per_bar = 4
        bar_duration = (60 / tempo) * beats_per_bar
        num_bars = int(duration / bar_duration)
        
        # Select chord progression
        chord_style = characteristics["chord_style"]
        chord_progression = self.chord_progressions.get(chord_style, self.chord_progressions["pop"])
        
        # Select rhythm pattern
        rhythm_pattern = self.rhythm_patterns.get(
            characteristics["rhythm_style"],
            self.rhythm_patterns["steady"]
        )
        
        # Generate musical elements
        melody = self._generate_melody(scale_notes, num_bars, characteristics, root_note)
        harmony = self._generate_harmony(chord_progression, num_bars, root_note, tempo)
        bass = self._generate_bass(chord_progression, num_bars, root_note, tempo, rhythm_pattern)
        
        # Premium features
        drums = []
        additional_layers = []
        if is_premium:
            drums = self._generate_drums(num_bars, tempo, characteristics["rhythm_style"])
            # Premium users get additional melodic variations
            additional_layers = self._generate_melody(
                scale_notes, num_bars, characteristics, root_note + 12
            )
        
        # Compile MIDI data
        midi_data = {
            "tempo": tempo,
            "time_signature": [4, 4],
            "key": key,
            "scale": scale_type,
            "tracks": {
                "melody": melody,
                "harmony": harmony,
                "bass": bass,
                "drums": drums,
                "additional": additional_layers
            }
        }
        
        composition_id = str(uuid.uuid4())
        
        return {
            "id": composition_id,
            "midi_data": midi_data,
            "audio_url": f"/audio/{composition_id}.wav",
            "metadata": {
                "keywords": keywords,
                "duration": duration,
                "style": style,
                "tempo": tempo,
                "key": key,
                "scale": scale_type,
                "characteristics": characteristics,
                "is_premium": is_premium
            }
        }
