# Ensure the `assemblyai` package is installed.
# Install it via pip if you haven't already:
# pip install -U assemblyai
# (For macOS users, you might need to use `pip3` instead of `pip`.)

import assemblyai as aai

def setapi(api_key):
    """Set the AssemblyAI API key for authentication."""
    aai.settings.api_key = api_key

def transcribe(file_url):
    """
    Transcribe audio from a given URL or local file path.
    
    Args:
        file_url (str): URL of the audio file to transcribe or local file path.
    
    Returns:
        str: The generated transcript including speaker labels.
    """
    # Set up the transcription configuration
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcriber = aai.Transcriber()

    # Perform the transcription
    transcript = transcriber.transcribe(
        file_url,
        config=config
    )

    # Extract the transcript with speaker labels
    transcript_generated = "\n".join(f"Speaker {utterance.speaker}: {utterance.text}" for utterance in transcript.utterances)
    
    return transcript_generated