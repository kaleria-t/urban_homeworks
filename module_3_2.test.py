def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    n = 0
    if ('@' in recipient) and ('@' in sender):
        if recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net"):
            if sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net"):
                n = 0
            else:
                n = 1
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        else:
            n = 1
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    else:
        n = 1
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

    if (str(sender) == str(recipient)) and n == 0:
        n = 1
        print ("Нельзя отправить письмо самому себе!")

    if sender == 'university.help@gmail.com' and n == 0:
        print (f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != 'university.help@gmail.com' and n == 0 :
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
