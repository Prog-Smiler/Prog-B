import customtkinter as ctk
import threading
import progb
    
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("1700x1000")
app.title("Prog B")

textbox = ctk.CTkTextbox(app, width=1500, height=800)
textbox.pack(pady=20)

def gui_log(message):
    textbox.insert("end", message + "\n")
    textbox.see("end")

progb.log_callback = gui_log

assistant_thread = None
running = False


def toggle_assistant():
    global running, assistant_thread

    if not running:
        running = True

        button.configure(text="Exit Prog B")

        assistant_thread = threading.Thread(
            target=progb.run_progb,
            daemon=True
        )

        assistant_thread.start()

    else:
        running = False

        progb.stop_progb()

        button.configure(text="Start Prog B")

        gui_log("Assistant stopped.")

button = ctk.CTkButton(
    app,
    text="Start Prog B",
    width=200,
    command=toggle_assistant
)

button.pack(pady=20)

app.mainloop()