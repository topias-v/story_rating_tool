import tkinter as tk
from tkinter import filedialog
from psychopy import core
import pandas as pd
import random
import sys


def select_stories():
    # Use tkinter to open file dialog
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    file_path = filedialog.askopenfilename(
        title="Select the story CSV file",
        filetypes=[("CSV files", "*.csv")]
    )

    if not file_path:
        print("No file selected. Exiting...")
        try:
            root.destroy()
        except Exception:
            pass
        try:
            core.quit()
        except Exception:
            pass
        sys.exit(0)
    
    # Load semicolon-separated CSV
    df = pd.read_csv(file_path, sep=';')

    # Create a dict {category: list_of_stories}
    story_dict = {}
    for col in df.columns:
        stories = df[col].dropna().tolist()
        if stories:
            story_dict[col] = stories
    
    return story_dict
    