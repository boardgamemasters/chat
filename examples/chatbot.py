import streamlit as st
from time import sleep 
import pandas as pd
from streamlit_chat import message

games = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama',
               'hippo'])

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)

def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']

st.session_state.setdefault('questions', [])

st.title("Survey QA Bot")
questions_list = [
    # 0
    '''I would like to recommend you some Boardgames.
    What is your favorite one?'''    
    # 1
    , '''I dont know this Game.
    Please enter another one'''
    # 2
    , '''How many recommendations do you want to get?
    'Please enter a Number between 1 and 5'''
]

if 'responses' not in st.session_state.keys():
    st.session_state.questions.extend(questions_list)
    st.session_state.responses = []

chat_placeholder = st.empty()
st.button("Clear message", on_click=on_btn_click)

message(st.session_state.questions[0]) 

with st.container():
    selecthor = 0
    while 1==1:
        if selecthor == 0:
            message(response, is_user = True)
            if games.isin([response]):
                sel_game = response
                selecthor = 1
            else:
                message(st.session_state.questions[1])
        if selecthor == 1:
            message(st.session_state.questions[2])
            message(response2, is_user = True)
            if response2.isnumeric():
                alt = response2
                selecthor = 2
            else:
                message('Please enter a numeric value')
        if selecthor== 2:
            message(f'''Your favorite boardgame is {sel_game}.
            And you would like to get {alt} recommendations for similar games.
            Is that correct?
            (y) , (n)''')
            selecthor = 3
        if selecthor== 3:
            message(response3, is_user = True)
            if (pd.Series(['y', 'Y', 'yes', 'Yes'])).isin([selecthor3]):
                message('I can recommend you the following games:')
            elif (pd.Series(['n', 'N', 'no', 'No'])).isin([selecthor3]):
                message('Lets try again')
                selecthor = 0
            else:
                message(f'''{response3} is not a valid input. Please try again
                What is your favorite Boardgame?''')
                
                
                     
                   
    
    # for response, question in zip(st.session_state.responses, st.session_state.questions[1:]):
    #     message(response, is_user = True)
    #     message(response)
    #     message(question)


with st.container():
    st.text_input("User Response:", on_change=on_input_change, key="user_input")

