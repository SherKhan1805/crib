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

data, bbox, clear_qrcode = detector.detectAndDecode(img_qrcode)
print(data)
print(bbox)
cv2.imshow("rez", clear_qrcode)
cv2.waitKey(0)
cv2.destroyAllWindows()
