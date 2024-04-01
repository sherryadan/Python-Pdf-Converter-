import tkinter as tk
from tkinter import filedialog


class ImagetoPDFconverter:
    def __init__(self, root):
        self.root = root
        self.image_path = []
        self.output_pdfname = tk.StringVar()
        self.Selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="PDF Converter App in Python", font=("Times New Roman", 16, "bold"))
        title_label.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImagetoPDFconverter(root)
    root.title("Image to PDF Converter")
    root.geometry("400x600")
    root.mainloop()

