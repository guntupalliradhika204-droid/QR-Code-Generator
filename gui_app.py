import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

# Function to generate QR Code
def generate_qr():
    data = text_entry.get()
    filename = file_entry.get()

    if data == "" or filename == "":
        messagebox.showerror("Error", "Please fill all fields!")
        return

    # Generate QR Code
    img = qrcode.make(data)

    # Save image
    img.save(filename + ".png")

    # Resize image for preview
    preview = img.resize((180, 180))

    # Convert image for Tkinter
    photo = ImageTk.PhotoImage(preview)

    # Show preview
    qr_label.config(image=photo)
    qr_label.image = photo

    messagebox.showinfo("Success", f"{filename}.png saved successfully!")

# Main Window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x550")

# Heading
heading = tk.Label(root, text="QR Code Generator", font=("Arial", 18, "bold"))
heading.pack(pady=10)

# URL/Text
tk.Label(root, text="Enter Text or URL").pack()

text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

# File Name
tk.Label(root, text="Enter File Name").pack()

file_entry = tk.Entry(root, width=40)
file_entry.pack(pady=5)

# Button
generate_btn = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    width=20
)
generate_btn.pack(pady=15)

# QR Preview
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run App
root.mainloop()