import streamlit as st
import os
from DeepSpeech import transcribe, setapi
from summarization_extractive import summarize, summarize_pdf
from summarization_abstractive import get_action_items, setgptapi, get_meeting_summary
import pdfplumber


def main():
    st.markdown("# Welcome to MetaNote 🤗")
    st.markdown(
        "##### This app lets you create summary, discussion points, and action times in real time using Machine Learning."
    )
    st.markdown(
        "##### Additionally, you can transcribe meeting transcripts or PDF files using this tool. 🤖"
    )
    st.markdown("")

    upload_file = st.file_uploader("Upload the Meeting File", type=["mp3", "wav", "m4a", "pdf"])

    col1, col2 = st.columns(2)
    with col1:
        text_input1 = st.text_input("Enter DeepSpeech API_KEY 👇",type="password")
        speechurl = "https://www.assemblyai.com/"
        st.write(f"Get API from [AssemblyAI]({speechurl})")
        
    with col2:
        text_input2 = st.text_input("Enter OPENAI API_KEY 👇",type="password")
        gpturl = "https://openai.com/index/openai-api/"
        st.write(f"Get API from [OpenAI]({gpturl})")

    def extract_data(feed):
        with pdfplumber.open(feed) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()
        return text

    def check_ds_api():
        if text_input1 and upload_file.type == "audio/mpeg":
            st.success("Transcribing Audio")
            setapi(text_input1)
        elif upload_file.type == "application/pdf":
            st.success("Summarizing PDF")
            data = extract_data(upload_file)
            summarize_pdf(data)
            st.balloons()
            check_gpt_api()
        else:
            st.error("Please enter DeepSpeech API_KEY or upload a PDF file.")

    def check_gpt_api():
        if text_input2:
            setgptapi(text_input2)
        else:
            st.success("Thank you for using MetaNote")
            st.warning("To generate Abstractive Summarization and Action items, add OPENAI_API_KEY")
            
    def transcribed_file(filename):
        fn = filename.name
        file_name = f"{fn}.txt"
        directory = './transcribed/'
        file_path = os.path.join(directory, file_name)
        transcription = transcribe(upload_file)
        
        if not os.path.isdir(directory):
            os.mkdir(directory)
        
        with open(file_path, "w") as file:
            file.write(transcription)
            
        return file_path

    if upload_file:
        st.audio(upload_file)
        
        if st.button("Summarize"):
            check_ds_api()
            tb_file = transcribed_file(upload_file)
            st.success("Transcribed Successfully")
            
            st.header("Extractive Summarization")
            summarize(tb_file)
            st.balloons()
            
            check_gpt_api()
            st.header(f"Abstractive Summary: {get_meeting_summary(tb_file)}")
            st.header(f"Action Items: {get_action_items(tb_file)}")
            st.success("Summary Generated Successfully")
            st.balloons()
    else:
        st.error("Please upload an audio or PDF file.")

main()
