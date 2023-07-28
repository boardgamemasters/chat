import streamlit as st

from streamlit_chat import message
liste = ['hallo', 'was']
game = ''
alt = ''
selecthor = 0
def on_input_change(x=selecthor):
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)
    if x=0:
        if liste.loc[liste.isin(user_input)]:
            game = user_input
            selecthor = 1
        else:
            message('I dont know this game. Please enter another Boardgame')
    if x =1:
        if user_input.isnumeric():
            if user_input > 4:
                alt = 4
                message('I can only recommend 4 Games at a time. So I will do so.')
                selecthor = 2
            if user_input <1:
                alt = 1
                message('I have to recommend you at least 1 Game. So I will do so.')
                selecthor = 2
            else:
                alt = user_input
                selecthor = 2
        else:
            message('Please enter a numeric Value')
        

def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']
    game = ''
    alt = ''

st.session_state.setdefault('questions', [])

st.title("Survey QA Bot")
questions_list = ['''I would like to recommend you some Boardgames. 
Do you have a favorite one?''', 'How many Games should i recommend for you?', f'''You want {alt} for Games like {game}.
Is that Correct?''','Do you want to get more recommendations?']

if 'responses' not in st.session_state.keys():
    st.session_state.questions.extend(questions_list)
    st.session_state.responses = []

chat_placeholder = st.empty()
st.button("Clear message", on_click=on_btn_click)

message(st.session_state.questions[0]) 

with st.container():
    for response, question in zip(st.session_state.responses, st.session_state.questions[1:]):
        message(response, is_user = True)
        message(question)


with st.container():
    st.text_input("User Response:", on_change=on_input_change, key="user_input")


# import streamlit as st
# from streamlit_chat import message
# import requests
# from streamlit.components.v1 import html

# st.set_page_config(
#     page_title="Streamlit Chat - Demo",
#     page_icon=":robot:"
# )

# API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
# # headers = {"Authorization": st.secrets['api_key']}

# st.header("Streamlit Chat - Demo")
# st.markdown("[Github](https://github.com/ai-yash/st-chat)")

# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []

# if 'past' not in st.session_state:
#     st.session_state['past'] = []

# def query(payload):
# 	response = requests.post(API_URL, json=payload)	#	headers=headers, 
# 	return response.json()

# def get_text():
#     input_text = st.text_input("You: ","Hello, how are you?", key="input")
#     return input_text 


# user_input = get_text()

# if user_input:
#     output = query({
#         "inputs": {
#             "past_user_inputs": st.session_state.past,
#             "generated_responses": st.session_state.generated,
#             "text": user_input,
#         },"parameters": {"repetition_penalty": 1.33},
#     })

#     st.session_state.past.append(user_input)
#     st.session_state.generated.append(output["generated_text"])

# if st.session_state['generated']:

#     for i in range(len(st.session_state['generated'])-1, -1, -1):
#         message(st.session_state["generated"][i], key=str(i))
#         message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

