from pytubefix import YouTube
from pytubefix.cli import on_progress
from url_validator import is_valid_youtube_url
import os
import streamlit as st


st.markdown('## **YouTube to MP3 Converter**')

try:
    URL = st.text_input(label='Paste YouTube URL here..') 
    
    left, _, _ = st.columns(3)
    
    if left.button("Download Audio", icon="⬇️", type='primary', use_container_width=True):
        with st.spinner():
            if not is_valid_youtube_url(URL):
                raise Exception('Error: Invalid URL!')

            current_run = 1
            # audio = YouTube(URL, on_progress_callback=on_progress)    # displays progerss during download
            audio = YouTube(URL)
            title = audio.title
            audio_stream = audio.streams.filter(only_audio=True).first()
            
            if current_run > 1:
                audio_stream.download(filename=f'{title}_{current_run}.mp3')
            
            else:
                audio_stream.download(filename=f'{title}.mp3')
            current_run += 1
        
        st.success('Audio downloaded succesfully!', icon="✅")
        
        if os.path.isfile(f'{title}.mp3'):
            st.write(f'{title}.mp3')
            st.audio(f"{title}.mp3", format="audio/mpeg", loop=True)

        elif os.path.isfile(f'{title}_{current_run}.mp3'):
            st.write(f'{title}_{current_run}.mp3')
            st.audio(f"{title}_{current_run}.mp3", format="audio/mpeg", loop=True)

except Exception as e:
    st.text(f'Ran into an unexpected error!\nError: {e}')