# Summarization App

This application allows users to summarize text and extract named entities using Python, NLTK, SpaCy, Sumy, and Streamlit.

## Features

- **Text Summarization**: Summarizes the input text using the LSA (Latent Semantic Analysis) algorithm from the Sumy library.
- **Named Entity Recognition**: Extracts named entities from the input text using SpaCy.

## Requirements

- Python 3.x
- Streamlit
- Sumy
- SpaCy
- NLTK

## Installation

1. Clone the repository or download the `nlp.py` file.
2. Install the required Python packages:
    ```bash
    pip install streamlit sumy spacy nltk
    ```
3. Download the SpaCy language model:
    ```bash
    python -m spacy download en_core_web_sm
    ```
4. Run the Streamlit app:
    ```bash
    streamlit run /C:/Users/Finance/Downloads/nlp.py
    ```

## Usage

1. Open the Streamlit app in your browser.
2. Enter the text you want to summarize in the text area.
3. Adjust the number of sentences for the summary using the slider.
4. Click the "Summarize" button to generate the summary and extract named entities.

## Example

1. Enter text in the text area:
    ```
    Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes.
    ```
2. Set the number of sentences to 2.
3. Click "Summarize".

The app will display the summarized text and the named entities found in the input text.

## License

This project is licensed under the MIT License.
