import cv2 as opencv

# Učitavanje slike
lena = opencv.imread('../lena-color.jpg')

# Prikaz slike
opencv.namedWindow('Lena')
opencv.imshow('Lena', lena)

# Broj stupaca, readaka i kanala
retci, stupci, kanali = lena.shape
print(f"Retci = {retci}, stupci = {stupci}, kanali = {kanali}.")

opencv.waitKey(0)
opencv.destroyAllWindows()
