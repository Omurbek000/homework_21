def send_email(to, subject):
    print("Email sent!")  #  отправка письма


def notify_user(user_email):
    send_email(user_email, "Welcome!")
