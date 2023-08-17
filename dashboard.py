# External Libraries
import streamlit as st

# Internal Libraries
from ellie import Ellie

class App:
    def __init__(self, agent) -> None:
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        if 'agent' not in st.session_state:
            st.session_state.agent = agent

    def run(self):
        st.title("ELLIE")

        with st.sidebar:
            st.button("Clear Chat", on_click=self.clear_messages)
        
        for message in st.session_state.messages:
            message_cont = st.chat_message(message['user'])
            message_cont.write(message['content'])

        prompt = st.chat_input("")
        if prompt:
            st.session_state.messages.append({"user": "user", "content": prompt})
            response = st.session_state.agent.get_response(prompt)
            message_cont = st.chat_message("user")
            message_cont.write(prompt)
            st.session_state.messages.append({"user": "assistant", "content": response})
            message_cont = st.chat_message('assistant')
            message_cont.write(response)

    def clear_messages(self):
        st.session_state.messages = []


if __name__ == "__main__":
    ellie = Ellie()
    app = App(ellie)
    app.run()