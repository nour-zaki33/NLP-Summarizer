import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import spacy
import nltk 
nltk.download('punkt')
nlp = spacy.load("en_core_web_sm")

def summarize_text_sumy(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return "\n".join(str(sentence) for sentence in summary)

def extract_entities_spacy(text):
    doc = nlp(text)
    entities = {ent.text: ent.label_ for ent in doc.ents}
    return entities
 
st.title(" Summarization App")

user_input = st.text_area("Enter text to summarize:")
num_sentences = st.slider("Number of sentences in summary:", 1, 10, 3)

if st.button("Summarize"):
    if user_input.strip():
        summary = summarize_text_sumy(user_input, num_sentences)
        entities = extract_entities_spacy(user_input)
        st.subheader("Summary ...")
        st.write(summary)
        st.subheader("Name Entities... ")
        if entities:
            for entity, label in entities.items():
                st.write(f"{entity} ({label})")
        else:
            st.write("No named entities found.")
    else:
        st.warning("Please enter text to summarize.")

st.caption(" Python, NLTK, SpaCy, Sumy, and Streamlit")
