"""Put demo messages into GreenMail for demo@local.test (run from WSL: python3 seed.py)."""
import smtplib
from datetime import datetime, timedelta
from email.message import EmailMessage
from email.utils import format_datetime

TO = "demo@local.test"
now = datetime.now().astimezone()
# (from, subject, body, days ago, attachment name or None)
msgs = [
    ("Анна Смирнова <anna@studio.example>", "Макеты главной страницы", "Привет! Скинула новые макеты, посмотри до пятницы.", 0, "mockups.pdf"),
    ("Cloud Hosting <noreply@cloud.example>", "Your verification code is 249738", "To ensure that only you have access, enter the code 249738.", 0, None),
    ("Книжный клуб <news@books.example>", "Чёрная пятница: скидки до 50%", "С 23 по 27 ноября действуют максимальные скидки.", 0, None),
    ("Billing <billing@cloud.example>", "Invoice 083001334346", "Enclosed you will find your current invoice in PDF format.", 1, "invoice.pdf"),
    ("Дмитрий Орлов <d.orlov@team.example>", "Re: Планёрка в четверг", "Давай перенесём на 11:00, у меня созвон с клиентом.", 1, None),
    ("Music Weekly <music@stream.example>", "Скоро ваша Распаковка", "Осталось меньше месяца.", 3, None),
    ("Server Panel <root@lab.example>", "Update Installed - v1.10.9", "lab has been upgraded to v1.10.9.", 4, None),
    ("Maria Lopez <maria@design.example>", "Conference slides", "Here are the slides from yesterday's talk. Thanks again!", 9, "slides.pdf"),
    ("Рекламный кабинет <ads@market.example>", "Счёт аккаунта пополнен", "Счёт в аккаунте пополнен на 16 393.44 руб.", 12, None),
    ("Travel Club <hello@travel.example>", "Ваш маршрут на выходные", "Подборка коротких поездок на два дня.", 20, None),
]

with smtplib.SMTP("127.0.0.1", 3025) as s:
    for frm, subj, body, days_ago, attach in msgs:
        m = EmailMessage()
        m["From"], m["To"], m["Subject"] = frm, TO, subj
        m["Date"] = format_datetime(now - timedelta(days=days_ago, minutes=len(subj)))
        m.set_content(body)
        if attach:
            m.add_attachment(b"%PDF-1.4 demo", maintype="application", subtype="pdf", filename=attach)
        s.send_message(m)
print(f"sent {len(msgs)} messages to {TO}")
