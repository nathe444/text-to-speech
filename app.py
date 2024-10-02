import streamlit as st
from gtts import gTTS
from io import BytesIO
from langdetect import detect
from PyPDF2 import PdfReader
import docx

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    body {
        background-color: #bd9595;
        color: #f1f1f1;
    }
    .sidebar .sidebar-content {
        background-color: #1c1c1c;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stTextArea textarea, .stTextInput input {
        background-color: #333;
        color: #f1f1f1;
        border-radius: 8px;
        border: 1px solid #666;
    }
    .stFileUploader > div {
        background-color: #444;
    }
    h1{
        color: #4CAF50;
    }
    .sidebar .sidebar-title {
        color: #4CAF50;
    }
            
      @media (max-width: 768px) {
        h1 {
            font-size: 22px;
        }
        .stTextArea textarea, .stTextInput input {
            font-size: 12px;
            padding: 6px;
        }
        .stButton button {
            font-size: 14px;
            padding: 8px 16px;
        }
        .stSubheader {
            font-size: 14px;
        }
        .stFileUploader > div {
            font-size: 12px;
        }
        .sidebar .sidebar-title {
            font-size: 16px;
        }
    }

    @media (max-width: 480px) {
        h1 {
            font-size: 22px;
        }
        .stTextArea textarea, .stTextInput input {
            font-size: 10px;
            padding: 4px;
        }
        .stButton button {
            font-size: 12px;
            padding: 6px 12px;
        }
        .stSubheader {
            font-size: 12px;
        }
    }
        
    </style>
    """, unsafe_allow_html=True)

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ''
    for page in pdf_reader.pages:
        try:
            extracted_text += page.extract_text()
        except Exception as e:
            st.error(f"Error extracting text from page: {e}")
    return extracted_text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    extracted_text = '\n'.join([para.text for para in doc.paragraphs])
    return extracted_text

st.title("🎤 Text to Speech Application")

st.sidebar.title("📂 Upload Your File and Generate Speech")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.type == 'application/pdf':
        extracted_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        extracted_text = extract_text_from_docx(uploaded_file)

    if extracted_text:
        detected_lang_document = detect(extracted_text)

    if st.sidebar.button("Convert My File to Speech"):
        if extracted_text:
            tts = gTTS(extracted_text, lang=detected_lang_document)
            audio_stream = BytesIO()
            tts.write_to_fp(audio_stream)
            st.write('✅ Generated Audio from Document')
            st.audio(audio_stream)
        else:
            st.write("❌ Error: No text extracted from the document")

st.subheader("Enter Text to Convert to Speech:")
text = st.text_area("Enter text to convert to speech:")

if text:
    detected_lang = detect(text)

if st.button("Convert to Speech"):
    if text:
        tts = gTTS(text, lang=detected_lang)
        audio_stream = BytesIO()
        tts.write_to_fp(audio_stream)
        st.audio(audio_stream)
    else:
        st.write("❌ Error: No text entered")

