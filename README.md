# MetaNote 🤖
MetaNote is a web app designed for audio transcription, meeting summarization, and action item extraction. This tool leverages both extractive and abstractive summarization techniques to help streamline meeting documentation.

## Extractive vs Abstractive Summarization 📝

# Extractive Summarization
Extractive summarization selects key sentences, phrases, or paragraphs directly from the source text. It aims to gather the most relevant information to provide a summary based on the original content.

# Abstractive Summarization
Abstractive summarization generates a summary by paraphrasing and restructuring the information. It uses natural language processing to understand the main ideas and present them in a new way.


## Features 🌟

- Audio Transcription: Convert audio files to text.
- Extractive Summarization: Identify and extract key sentences from the transcript.
- Abstractive Summarization: Generate a concise summary by rephrasing the main ideas.
- Action Items Extraction: Extract actionable tasks from meeting transcripts.
- PDF Summarization: Summarize text from PDF files.


## Setup

1. __Clone the repository:__
`git clone https://github.com/SCodePK/MetaNote.git`

2. __Install dependencies:__
`pip install -r requirements.txt`

3. __Set Up API Keys:__
DEEPSPEECH_API_KEY=your_deepspeech_api_key
OPENAI_API_KEY=your_openai_api_key

4. __Streamlit run:__
`streamlit run app.py`


## Testing and Limitations
The model has been tested with audio clips ranging from 14 to 90 minutes in length.
## Note
 Note: Due to file size limitations, the actual large files used for testing could not be uploaded to GitHub. For screenshots, please refer to the Images folder.

