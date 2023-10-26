

________________________________________________________________________________________________________________________

import qrcode
import cv2

"""
Подгрузить:
pip install qrcode
pip install qrcode[pil]
pip install opencv-python
"""

"""
Создание QR-кода
"""
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data("проверь меня")
qr.make(fit=True)

img = qr.make_image(fill_color="green", back_color="white")
img.save("test.jpg", "JPEG")

img_qrcode = cv2.imread("test.jpg")
detector = cv2.QRCodeDetector()

"""
Расшифровка QR-кода, чтение и вывод данных
"""
data, bbox, clear_qrcode = detector.detectAndDecode(img_qrcode)
print(data)
print(bbox)
cv2.imshow("rez", clear_qrcode)
cv2.waitKey(0)
cv2.destroyAllWindows()

________________________________________________________________________________________________________________________

"""

"""

for i in vacancies['items']:
    name = i['name']
    alternate_url = i['alternate_url']
    payment_from = i['salary']['from'] if i['salary'] and 'from' in i['salary'] else None
    payment_to = i['salary']['to'] if i['salary'] and 'to' in i['salary'] else None

________________________________________________________________________________________________________________________

import psycopg2

"""
Подгрузить:
poetry add psycopg2
poetry add psycopg2-binary
"""

"""
Функции работы с базой данных. Подключение, работа с данными, закрытие.
"""

with psycopg2.connect(host="localhost", database="parsing_hh_company", user="postgres",
                      password="alexia1456") as conn:
    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE vacancy ")
        for item in vacancy_list:
            cur.execute("INSERT INTO company (company_id, company_name) VALUES (%s, %s)"
                        "ON CONFLICT (company_id) DO NOTHING;",
                        (int(item["company_id"]), item["company_name"]))
            cur.execute("SELECT company.company_name, vacancy_name, payment_from, payment_to, url FROM company "
                        "INNER JOIN vacancy USING(company_id) "
                        "GROUP BY company.company_name, vacancy_name, payment_from, payment_to, url "
                        "ORDER BY company_name ")
            cur.execute("SELECT ROUND(AVG(payment_from)) FROM vacancy "
                        "WHERE payment_from > 0 ")

            rows = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

________________________________________________________________________________________________________________________

import requests

"""
Подключение по API к сайту НН и работа с ним.
"""

base_url = 'https://api.hh.ru/'
endpoint = 'vacancies'
vacancy_list = []

params = {'employer_id': 1276,
          'per_page': 5}

response = requests.get(f'{base_url}{endpoint}', params=params)
if response.status_code == 200:
    vacancies = response.json()
