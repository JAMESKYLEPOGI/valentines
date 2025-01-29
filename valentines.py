import tkinter as tk
import smtplib
from email.message import EmailMessage
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window

# Show an information message box

root.iconbitmap("F:\in-love.ico")

root.iconphoto(True, tk.PhotoImage(file="F:\in-love.png"))



# Email sender function
class Email:
    def rejected_email(self,subject,body):
        sender_email = "sample@gmail.com"  # Replace with your email
        receiver_email = "sample@gmail.com"  # Replace with recipient's email
        password = "puxr ewon cgxf lmwc"  # Replace with your email password (use app passwords for security)

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(body)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, password)
                server.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

def valentines():

    messagebox.showinfo("crushie", "hi")
    date = messagebox.askyesno("crushie", "pwede ba kita date") #customize
    email = Email()

    if not date:
        messagebox.showerror("Ouch","Thank you anyway")

        email.rejected_email(subject="Rejected 😢",body="Sorry, your request was declined. Better luck next time!")
        root.destroy()

    else:
        messagebox.showinfo("Yay!", "See you on our date! ❤️")
        email.rejected_email(subject="Accepted! 🎉",body="Your date has been accepted! Get ready for the special day! ❤️")
        root.destroy()


valentines()
root.mainloop()  # Start the event loop