# B dio zadatka prikazuje kanale RGB te YCbCr prostora boja
import cv2 as opencv
import zadatak4a as kanali

# Pomoćna funkcija za dohvaćanje kanala
def get(argument):
	switcher = {
		0: kanali.b,
		1: kanali.g,
		2: kanali.r,
		3: kanali.y,
		4: kanali.cr,
		5: kanali.cb
	}

	return switcher.get(argument, kanali.lena_bgr)

# Petlja koja iscrtava kanale obiju slika
for i in range(6):
	opencv.namedWindow(f"Prozor {i}")
	opencv.imshow(f"Prozor {i}", get(i))

opencv.waitKey(0)
opencv.destroyAllWindows()

# Iz rastavljanja slike u YCbCr prostoru boja može se vidjeti kako su pikseli svjetliji (bliže bijeloj - 255) nego u RGB prostoru boja
