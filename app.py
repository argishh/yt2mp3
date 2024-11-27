import os
import streamlit as st
from utils import FOOTER
from pytubefix import YouTube
from pytubefix.cli import on_progress
from url_validator import is_valid_youtube_url
from pytubefix.helpers import reset_cache

reset_cache()

st.markdown('## **YouTube to MP3 Converter**')
st.markdown(FOOTER,unsafe_allow_html=True)

try:
    URL = st.text_input(label='Paste YouTube URL here..') 
    
    left, _, _ = st.columns(3)
    
    if left.button("Download Audio", icon="⬇️", type='primary', use_container_width=True):
        with st.status('downloading audio..'):
            st.write('1. validating URL..')
            if not is_valid_youtube_url(URL):
                raise Exception('Error: Invalid URL!')
            
            st.write('2. looking for audio..')
            st.write('> Warning: If search takes too long, clone the repository and run the app locally')
            # audio = YouTube(URL, on_progress_callback=on_progress)    # displays progerss during download
            audio = YouTube(URL)
            title = audio.title
            audio_stream = audio.streams.filter(only_audio=True).first()
            st.write('audio found!')
            
            st.write('3. downloading audio..')
            audio_stream.download(filename=f'{title}.mp3')
            st.write('audio downloaded!')
            
        st.markdown('## ') # seperator
        # st.success('Audio downloaded succesfully!', icon="✅")
        
        if os.path.isfile(f'{title}.mp3'):
            st.write(f'{title}.mp3')
            st.audio(f"{title}.mp3", format="audio/mpeg", loop=True)
            
except Exception as e:
    st.text(f'Ran into an unexpected error!\nError: {e}')
    st.write('> Try cloning the repository and run the app locally')
    st.write("(Click the github logo at the top right corner)")