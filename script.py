import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("42.069")

        # Variables
        self.url_var = tk.StringVar()
        self.start_video_var = tk.IntVar()
        self.end_video_var = tk.IntVar()

        # Glassmorphism Style
        style = ttk.Style()
        style.configure("TFrame", background="#fff")
        style.configure("TLabel", background="#999")
        style.configure("TEntry", fieldbackground="#fff")
        style.configure("TButton", background="#fff")
        style.configure("TMenubutton", background="#fff")

        # GUI Elements
        frame = ttk.Frame(root, style="TFrame")
        frame.grid(row=0, column=0, columnspan=3, pady=5, padx=5)

        ttk.Label(frame, text="URL:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.url_var).grid(row=0, column=1, columnspan=2, pady=5, padx=5)

        ttk.Button(frame, text="Download Audio", command=self.download_audio).grid(row=3, column=0, pady=10, padx=10)
        ttk.Button(frame, text="Download Video", command=self.download_video).grid(row=3, column=1, pady=10, padx=10)

    def download_audio(self):
        self.download("Audio")

    def download_video(self):
        self.download("Video")

    def download(self, download_type):
        url = self.url_var.get()
        format_option = "-x --extract-audio --audio-format mp3" if download_type == "Audio" else ""

        command = f'python -m youtube_dl -i "{url}" --max-filesize 42000000 {format_option}'

        try:
            subprocess.run(command, check=True, shell=True)
            messagebox.showinfo("Success", f"Download {download_type} completed successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
