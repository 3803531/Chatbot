import tkinter as tk
import speech_recognition as sr
import socket
import os

class SpeechRecorder:
    def __init__(self, master):
        self.master = master
        master.title("Speech Recorder")

        self.recording_time = tk.StringVar()
        self.recording_time.set("5")

        self.recorded_text = tk.StringVar()
        self.recorded_text.set("")

        self.microphone_on = False
        self.recording = False

        self.time_label = tk.Label(master, text="Recording Time (in seconds):")
        self.time_entry = tk.Entry(master, textvariable=self.recording_time)
        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.play_button = tk.Button(master, text="Play Recording", command=self.play_recording, state=tk.DISABLED)
        self.save_button = tk.Button(master, text="Save Recording", command=self.save_recording, state=tk.DISABLED)
        self.text_label = tk.Label(master, text="Recorded Text:")
        self.text_box = tk.Text(master, state=tk.DISABLED)

        self.time_label.grid(row=0, column=0, padx=10, pady=10)
        self.time_entry.grid(row=0, column=1, padx=10, pady=10)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)
        self.play_button.grid(row=2, column=0, padx=10, pady=10)
        self.save_button.grid(row=2, column=1, padx=10, pady=10)
        self.text_label.grid(row=3, column=0, padx=10, pady=10)
        self.text_box.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def start_recording(self):
        # Check if device is connected to the internet
        if not self.is_connected():
            self.text_box.config(state=tk.NORMAL)
            self.text_box.insert(tk.END, "Error: Device not connected to the internet\n")
            self.text_box.config(state=tk.DISABLED)
            return
        self.recording = True
        self.microphone_on = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.play_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.DISABLED)
        self.text_box.config(state=tk.NORMAL)
        self.text_box.delete(1.0, tk.END)
        self.text_box.config(state=tk.DISABLED)

        # Initialize the recognizer
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        
        # Adjust for ambient noise levels
        #with microphone as source:
          #  recognizer.adjust_for_ambient_noise(source)

        # Start recording
        with microphone as source:
           
            audio = recognizer.listen(source, timeout=int(self.recording_time.get()))

        # Stop recording
        self.microphone_on = False

        # Recognize speech
        try:
            self.recorded_text.set(recognizer.recognize_google(audio,language='fr-FR'))
            self.text_box.config(state=tk.NORMAL)
            self.text_box.insert(tk.END, self.recorded_text.get() + "\n")
            self.text_box.config(state=tk.DISABLED)
            self.play_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL)
        except sr.UnknownValueError:
            self.text_box.config(state=tk.NORMAL)
            self.text_box.insert(tk.END, "Error: Speech could not be recognized\n")
            self.text_box.config(state=tk.DISABLED)
        except sr.RequestError as e:
            self.text_box.config(state=tk.NORMAL)
            self.text_box.insert(tk.END, "Error: Could not request results from Google Speech Recognition service; {0}\n".format(e))
            self.text_box.config(state=tk.DISABLED)

    def stop_recording(self):
        self.recording = False
        self.microphone_on = False

    def play_recording(self):
         os.system("say " + self.recorded_text.get())

    def save_recording(self):
        with open("recording.txt", "w") as file:
            file.write(self.recorded_text.get())

    def is_connected(self):
        try:
            # Connect to a public website to check for internet connectivity
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False


root = tk.Tk()
app = SpeechRecorder(root)
root.mainloop()

