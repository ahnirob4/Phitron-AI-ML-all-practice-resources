import streamlit as st

st.title(':red[**IMAGE**] Gallery App', anchor=False)
st.subheader('My personal gallery', divider=True, anchor=False)

images = st.file_uploader('Enter your image (at Max 3)', type=['jpg','jpeg','png'],accept_multiple_files=True)

print(type(images))

if images:
    if (len(images) > 3):
        st.warning(f'You uploaded {len(images)} photos')

    for i in range(0, len(images), 3):
        col1, col2, col3 = st.columns(3)
        with col1:
            if i < len(images):
                st.image(images[i])
        
        with col2:
            if i+1 < len(images):
                st.image(images[i+1])

        with col3:
            if i+2 < len(images):
                st.image(images[i+2])