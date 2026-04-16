import streamlit as st

st.title(':red[**IMAGE**] Gallery App', anchor=False)
st.subheader('My personal gallery', divider=True, anchor=False)

images = st.file_uploader('Enter your image (at Max 3)', type=['jpg','jpeg','png'],accept_multiple_files=True)



if len(images) >= 3:
    st.success(f'You uploaded {len(images)} images.')
    col = st.columns(len(images))

    for i , per_image in enumerate(images):
        with col[i]:
            st.image(per_image)
    if len(images) > 3:
        st.error('You exceeded your maximum limit.')
        
