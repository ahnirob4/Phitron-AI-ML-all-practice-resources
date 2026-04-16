import streamlit as st

st.title('Personal Info Card App')
st.divider()

name = st.text_input('Name:', placeholder='Enter your name...')
age = st.number_input('Age', placeholder='Enter your age...', min_value=0, step=1,)
option = st.selectbox(
    'Select your option',['Student', 'Employee', 'Businessman','Freelancer']
)

if st.button('Submit'):
    st.write(f'Your name is {name}, Your age is {age}, Your are a {option}.')
    st.success('Great job!')
else:
    st.warning('Please complete your input field!')