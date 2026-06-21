# Audio Prompt Template (speech / voiceover only)

`generate_audio` is text-to-speech only — it cannot make music or SFX. For ambience/score use native model audio at video time or an external tool. See `docs/HIGGSFIELD_MCP_REFERENCE.md` §5.

PURPOSE: [voiceover | character dialogue]
LANGUAGE: [e.g. en]
VOICE: [voice_id from list_voices] · VOICE TYPE: [preset | element]
MODEL: [text2speech_v2_elevenlabs (default) | _seed_speech (long narration) | _vibe_voice (clone ~3s) | _cozy_voice (low-latency multilingual)]
DELIVERY NOTES: [pace, tone — guidance only; the model speaks the literal text]

SEND VERBATIM (the exact words to be spoken — nothing else):
[Script line(s)]

MCP CALL (optional):
{ "params": { "model": "text2speech_v2_elevenlabs", "prompt": "<same as SEND VERBATIM>", "voice_type": "preset", "voice_id": "<id from list_voices>" } }
