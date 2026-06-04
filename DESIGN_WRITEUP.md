# Design Decisions and Service Choices

VoiceLog is a simple web application that converts audio files into text and generates concise summaries. The application was developed using Streamlit because it allows rapid development of interactive web interfaces using Python with minimal frontend code.

For speech-to-text conversion, OpenAI Whisper was selected because it is open source, highly accurate, and can run locally without requiring paid API access. This makes the application cost-effective and suitable for educational and demonstration purposes.

For summarization, the Hugging Face Transformers library was used with a pre-trained summarization model. This approach eliminates dependency on paid AI APIs while still providing meaningful summaries from generated transcripts.

The user workflow is straightforward. Users upload an MP3 or WAV file, the audio is transcribed into text, and the resulting transcript is passed to the summarization model. Both the transcript and generated summary are displayed in the same interface.

Special attention was given to simplicity, ease of use, and maintainability. Temporary audio files are excluded through the .gitignore configuration. Documentation is provided through the README file, and the project is released under the MIT License to encourage open-source usage and modification.

The overall design prioritizes accessibility, zero-cost deployment, and clear separation between transcription and summarization components.