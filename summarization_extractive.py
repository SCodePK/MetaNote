import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from rake_nltk import Rake
import numpy as np
import streamlit as st


# Download required NLTK data
col1, col2 = st.columns(2)
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into words
    words = [word_tokenize(sentence.lower()) for sentence in sentences]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [[word for word in sentence if word.isalnum() and word not in stop_words] for sentence in words]
    
    return sentences, filtered_words

def get_top_n_sentences(text, n=10):
    sentences, filtered_words = preprocess_text(text)
    
    # Join the words back into sentences
    filtered_sentences = [' '.join(words) for words in filtered_words]
    
    # Calculate TF-IDF scores
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(filtered_sentences)
    
    # Get the sum of TF-IDF scores for each sentence
    sentence_scores = np.sum(tfidf_matrix.toarray(), axis=1)
    
    # Get the indices of the top N sentences
    top_n_indices = sentence_scores.argsort()[-n:][::-1]
    
    # Get the top N sentences
    top_n_sentences = [sentences[i] for i in top_n_indices]
    
    return top_n_sentences

def extract_keywords(text):
    r = Rake(stopwords=stopwords.words('english'))
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()

# Example meeting text

def summarize(filename):
# Get the top 10 points
    text=open(filename,"r")
    text1=str(text.read())
    keywords = extract_keywords(text1)
    summary_title = ' '.join(keywords[:2]) if len(keywords) >= 2 else keywords[0] if keywords else "Meeting Summary"
    st.write(f"Title:\t **{summary_title}**")
    top_points = get_top_n_sentences(text1, n=10)

# Print the top points
    print("Top Points:")
    for i, point in enumerate(top_points, 1):
        st.write(f"Point {i}: {point}")

    # Extract keywords
    keywords = extract_keywords(text1)

    # Print the keywords
def summarize_pdf(text1):
    """keywords = extract_keywords(text1)
    summary_title = ' '.join(keywords[:2]) if len(keywords) >= 2 else keywords[0] if keywords else "Meeting Summary"
    st.subheader(f"Title:\t **{summary_title}**")"""
    status=st.header("Extractive Summarization")
    top_points = get_top_n_sentences(text1, n=10)

# Print the top points
    print("Top Points:")
    for i, point in enumerate(top_points, 1):
        st.write(f"Point {i}: {point}")

    # Extract keywords
    keywords = extract_keywords(text1)


