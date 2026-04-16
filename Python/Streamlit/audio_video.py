import streamlit as st



"""Audio player"""
st.title(':red[**AUDIO**] Player App', anchor=False)
st.divider()

file = st.file_uploader('Upload your audio', type=['mp3','ogg', 'flac'])

print(type(file))

if not file:
    if st.button('Play Audio',key='play_audio_1' ):
        st.error('Your audio file has not been uploaded yet.')
    else:
        st.warning('Upload the file first.')
elif st.button('Play Audio', key='play_audio_1'):
    st.audio(file)

"""Video player"""
st.title(':orange[**VIDEO**] Player App', anchor=False)
st.divider()

video = st.file_uploader('Upload your video', type=['mp4', 'mkv'])

if not video:
    if st.button('Play Video',key='play_video_1'):
        st.error('Your video file has not been upload yet.')
    else:
        st.warning('Upload the file first')

elif st.button('Play Video', key='play_video_2'):
    st.video(video)
