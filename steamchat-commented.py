# Import necessary libraries
import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html

# Define a function to handle user input changes
def on_input_change():
    # Get the user input from the text input widget
    user_input = st.session_state.user_input
    # Append the user input to the list 'past' in the session state
    st.session_state.past.append(user_input)

    # Bot generates a response (a constant string in this case) and appends it to the list 'generated'
    # It's just a placeholder for the actual chatbot logic, which should generate appropriate responses based on user input
    st.session_state.generated.append("The messages from Bot\nWith new line")

# Define a function to handle the "Clear message" button click
def on_btn_click():
    # Clear the lists 'past' and 'generated' in the session state
    del st.session_state.past[:]
    del st.session_state.generated[:]

# Define URLs for audio, image, and YouTube video embed
audio_path = "https://docs.google.com/uc?export=open&id=16QSvoLWNxeqco_Wb2JvzaReSAw5ow6Cl"
img_path = "https://www.groundzeroweb.com/wp-content/uploads/2017/05/Funny-Cat-Memes-11.jpg"
youtube_embed = '''
<iframe width="400" height="215" src="https://www.youtube.com/embed/LMQ5Gauy17k" title="YouTube video player" frameborder="0" allow="accelerometer; encrypted-media;"></iframe>
'''

# Define a sample Markdown text containing HTML, lists, math equation, and code blocks
markdown = """
### HTML in markdown is ~quite~ **unsafe**
<blockquote>
  However, if you are in a trusted environment (you trust the markdown). You can use allow_html props to enable support for html.
</blockquote>

* Lists
* [ ] todo
* [x] done

Math:

Lift($L$) can be determined by Lift Coefficient ($C_L$) like the following
equation.

$$
L = \\frac{1}{2} \\rho v^2 S C_L
$$

~~~py
import streamlit as st

st.write("Python code block")
~~~

~~~js
console.log("Here is some JavaScript code")
~~~

"""

# Define a sample Markdown table
table_markdown = '''
A Table:

| Feature     | Support              |
| ----------: | :------------------- |
| CommonMark  | 100%                 |
| GFM         | 100% w/ `remark-gfm` |
'''

# Initialize session state for the user's past responses
st.session_state.setdefault(
    'past', 
    ['plan text with line break',
     'play the song "Dancing Vegetables"', 
     'show me image of cat', 
     'and video of it',
     'show me some markdown sample',
     'table in markdown']
)

# Initialize session state for the bot's generated responses
st.session_state.setdefault(
    'generated', 
    [{'type': 'normal', 'data': 'Line 1 \n Line 2 \n Line 3'},
     {'type': 'normal', 'data': f'<audio controls src="{audio_path}"></audio>'}, 
     {'type': 'normal', 'data': f'<img width="100%" height="200" src="{img_path}"/>'}, 
     {'type': 'normal', 'data': f'{youtube_embed}'},
     {'type': 'normal', 'data': f'{markdown}'},
     {'type': 'table', 'data': f'{table_markdown}'}]
)

# Set the Streamlit app title
st.title("Chat placeholder")

# Create a placeholder to display the chat messages
chat_placeholder = st.empty()

# Inside the chat_placeholder container, loop through the past responses and generated bot responses
with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):                
        # Display the user's past response on the left side of the chat
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        # Display the bot's generated response on the right side of the chat
        message(
            st.session_state['generated'][i]['data'], 
            key=f"{i}", 
            allow_html=True,
            is_table=True if st.session_state['generated'][i]['type']=='table' else False
        )
    
    # Add a "Clear message" button at the end of the chat to clear the chat history
    st.button("Clear message", on_click=on_btn_click)

# Outside the chat_placeholder container, display a text input widget for the user to type their messages
with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
