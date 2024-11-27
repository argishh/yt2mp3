import os
import streamlit as st
from utils import FOOTER
from pytubefix import YouTube
from pytubefix.cli import on_progress
from url_validator import is_valid_youtube_url


st.markdown('## **YouTube to MP3 Converter**')
st.markdown(FOOTER,unsafe_allow_html=True)

try:
    URL = st.text_input(label='Paste YouTube URL here..') 
    
    left, _, _ = st.columns(3)
    
    if left.button("Download Audio", icon="⬇️", type='primary', use_container_width=True):
        with st.spinner():
            if not is_valid_youtube_url(URL):
                raise Exception('Error: Invalid URL!')

            # audio = YouTube(URL, on_progress_callback=on_progress)    # displays progerss during download
            audio = YouTube(URL)
            title = audio.title
            audio_stream = audio.streams.filter(only_audio=True).first()
            
            audio_stream.download(filename=f'{title}.mp3')
            
        st.markdown('## ') # seperator
        # st.success('Audio downloaded succesfully!', icon="✅")
        
        if os.path.isfile(f'{title}.mp3'):
            st.write(f'{title}.mp3')
            st.audio(f"{title}.mp3", format="audio/mpeg", loop=True)
            
except Exception as e:
    st.text(f'Ran into an unexpected error!\nError: {e}')