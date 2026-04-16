import streamlit as st

# st.title('My first app.', anchor=None)
# st.write('Hello my first streamlit app.')
# st.write('I am excited to publish my first web app.')

# st.title('Hello Brothers', anchor=None)

# name = st.text_input('Name:', placeholder='Please enter your name.')
# age = st.number_input('Age:', placeholder='How old are you?')

# if name:
#     st.write('Hello', name,'!',f'\nI am {age} years old.' )

# """Name and age input"""

# name = st.text_input('Name', placeholder='What is your name?')
# age = st.number_input('Age', placeholder='How old are you?')

# if st.button('Submit'):
#     st.write(f'Hello {name}. Your age is {age}')

# else:
#     st.error('Please Enter your name first.')


# """Dropdown box"""

# option = st.selectbox(
#     'Choose your favourite option:',
#     ['C++', 'Java', 'Python'],
# )

# if option:
#     st.write(f'You selected: {option}')

# """Even and Odd checker"""

st.title('Even and ODD checker')

num = st.number_input('Enter your number: ',min_value=0,step=1, format="%d") # int value

if st.button('Submit'):
    if num % 2 ==0:
        st.write(f'{num} is EVEN')

    else:
        st.write(f'{num} is ODD.')

