import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# рассылка писем
def sending_letters(users_list: list[str], body: str, subject: str):
        login: str = ''
        password: str = ''

        msg = MIMEMultipart()
        msg['From'] = login
        # msg['To'] = ''
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))  # Прикрепляем текст письма

        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login(login, password)
        for user in users_list:
                smtp_obj.sendmail(login, user, msg.as_string())

        smtp_obj.quit()


if __name__ == '__main__':
        users_list = ['nastyakononchuk@me.com', 'alexeyshu86@mail.ru']
        text = """
                Арпеджио использует midi-контроллер. Глиссандо трансформирует хамбакер.
                Голос mezzo forte выстраивает пласт, но если бы песен было раз в пять
                меньше, было бы лучше для всех. Райдер, следовательно, использует
                позиционный дисторшн, благодаря употреблению микромотивов (нередко из
                одного звука, а также двух-трех с паузами). Как было показано выше,
                канал синхронно представляет собой ревер, как и реверансы в сторону
                ранних "роллингов". Показательный пример – явление культурологического
                порядка дисгармонично.
        """
        subject = 'Почему ненаблюдаемо явление культурологического порядка?'
        sending_letters(users_list, text, subject)
