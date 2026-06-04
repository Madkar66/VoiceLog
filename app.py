import streamlit as st
import whisper
from transformers import pipeline

st.set_page_config(page_title="VoiceLog")

st.title("VoiceLog")
st.write("Voice to Text + AI Summarizer")

audio_file = st.file_uploader(
    "Upload Audio",
    type=["mp3", "wav"]
)

if audio_file:

    st.audio(audio_file)
    st.success("Audio uploaded successfully!")

    # Save uploaded file
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_file.read())

    # Speech to Text
    with st.spinner("Transcribing audio..."):
        model = whisper.load_model("base")
        result = model.transcribe("temp_audio.mp3")
        transcript = result["text"]

    # AI Summary
    with st.spinner("Generating summary..."):
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

        summary_result = summarizer(
            transcript[:1000],
            max_length=120,
            min_length=30,
            do_sample=False
        )

        summary = summary_result[0]["summary_text"]

    st.subheader("Transcript")
    st.write(transcript)

    st.subheader("AI Summary")
    st.write(summary)