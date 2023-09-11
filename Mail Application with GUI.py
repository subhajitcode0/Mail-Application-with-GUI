import tkinter as tk
from tkinter import messagebox
import smtplib

class MailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application")

        self.label_to = tk.Label(root, text="To:")
        self.label_to.pack()

        self.entry_to = tk.Entry(root)
        self.entry_to.pack()

        self.label_subject = tk.Label(root, text="Subject:")
        self.label_subject.pack()

        self.entry_subject = tk.Entry(root)
        self.entry_subject.pack()

        self.label_message = tk.Label(root, text="Message:")
        self.label_message.pack()

        self.text_message = tk.Text(root, height=5, width=40)
        self.text_message.pack()

        self.send_button = tk.Button(root, text="Send", command=self.send_email)
        self.send_button.pack()

    def send_email(self):
        to_email = self.entry_to.get()
        subject = self.entry_subject.get()
        message = self.text_message.get("1.0", tk.END)

        try:
            # Replace these with your own email credentials
            sender_email = "testmail@gmail.com"
            sender_password = "yourpassword"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)

            email_text = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, to_email, email_text)

            server.quit()
            messagebox.showinfo("Success", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MailApp(root)
    root.mainloop()
