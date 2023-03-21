import os
import openai
import gradio as gr
import webbrowser



class chatbot():
    def __init__(self):
        pass

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


def browser_launch():
    block = gr.Blocks()

    with block:
        gr.Markdown("""<h1><center>Ramsey's ChatGPT with OpenAI API & Gradio</center></h1>
        """)
        chatbot = gr.Chatbot()
        message = gr.Textbox(placeholder=prompt)
        state = gr.State()
        submit = gr.Button("SEND")
        submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
        # webbrowser.open("http://127.0.0.1:7860")
        block.launch()
        

    
browser_launch()