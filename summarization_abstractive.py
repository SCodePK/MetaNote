import os
import openai
import streamlit as st


def setgptapi(api):
    openai.api_key = api


def davinci_request(
    prompt_request,
    temperature=0.5,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
):
    """Uses OpenAI's API to interact with 'gpt-3.5-turbo' model"""
   
    
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt_request,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    return response["choices"][0]["text"].strip()

@st.cache_data
def get_meeting_summary(filepath):
    try:
        if(openai.api_key=="OPEN_API_KEY"):
            st.markdown("Enter API KEY")
        """Function for getting the meeting summary from a meeting transcript file"""
        with open(filepath, 'r') as file:
            content = file.read()

        prompt_request = "Summarize this meeting transcript: " + content
        meeting_summary = davinci_request(prompt_request)
        return meeting_summary
    except Exception as e:
        st.error("An error occurred while processing the file. Please try again.")
        st.error(f"Details: {e}")

@st.cache_data
def get_action_items(filepath):
    try:
        if(openai.api_key=="OPEN_API_KEY"):
            st.markdown("Enter API KEY")
        """Function for getting the action items from a meeting transcript file"""
        with open(filepath, 'r') as file:
            content = file.read()

        prompt_request = (
            "Provide a list of action items with a due date from the provided meeting transcript text: "
            + content
        )
        meeting_action_items = davinci_request(prompt_request)
        return meeting_action_items
    except Exception as e:
        st.error("An error occurred while processing the file. Please try again.")
        st.error(f"Details: {e}")
