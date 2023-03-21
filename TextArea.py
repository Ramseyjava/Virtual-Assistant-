import tkinter as tk
import sys
import subprocess
import threading 

# --- Alexa import----
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# --- classes ---

class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.window1 = root
        self.window1.title("Virtual Assistant Home")
        self.window1.geometry("1280x800+0+0")
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll
        
    #def flush(self):
    #    pass

# --- functions ---

def Ram_speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            voice_data = listener.recognize_google(voice)
            voice_data = voice_data.lower()
            if 'alexa' in voice_data:
                voice_data = voice_data.replace('alexa', '')
                return voice_data
    except:
        print("No voice_data")
        
    


def run_alexa():
    voice_data = take_command()
    print(voice_data)
    if 'play' in voice_data:
        song = voice_data.replace('play', '')
        Ram_speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in voice_data:
        time = datetime.datetime.now().strftime('%I:%M %p')
        Ram_speak('Current time is ' + time)
    elif 'who the heck is' in voice_data:
        person = voice_data.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        Ram_speak(info)
    elif 'date' in voice_data:
        Ram_speak('sorry, I have a headache')
    elif 'are you single' in voice_data:
        Ram_speak('I am in a relationship with wifi')
    elif 'joke' in voice_data:
        Ram_speak(pyjokes.get_joke())
    else:
        Ram_speak('Please say the voice_data again.')


def alexa_call():
    while True:
        run_alexa()




# def run():
#     threading.Thread(target=run_alexa).start()

# def test():
#     print("Thread: start")

#     p = subprocess.Popen("ping -c 4 stackoverflow.com".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
#     while p.poll() is None:
#         msg = p.stdout.readline().strip() # read a line from the process output
#         if msg:
#             print(msg)

#     print("Thread: end")

# --- main ---    

root = tk.Tk()

# - Frame with Text and Scrollbar -

frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

text = tk.Text(frame)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

text['yscrollcommand'] = scrollbar.set
scrollbar['voice_data'] = text.yview

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

# - rest -

button = tk.Button(root, text='launch', voice_data=alexa_call)
button.pack()

root.mainloop()

# - after close window -

sys.stdout = old_stdout