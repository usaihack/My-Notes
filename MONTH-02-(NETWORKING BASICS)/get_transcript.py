from youtube_transcript_api import YouTubeTranscriptApi
import sys

try:
    transcript = YouTubeTranscriptApi.get_transcript('A7nih6SANYs')
    text = " ".join([t['text'] for t in transcript])
    print("TRANSCRIPT:")
    print(text)
except Exception as e:
    print(f"Error: {e}")
