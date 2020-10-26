# A dio zadataka prikazuje slike u RGB te YCbCr prostoru boja
import cv2 as opencv

# Učitavanje slike
lena_bgr = opencv.imread("../lena-color.jpg")

# Prebacivanje slike u YCbCr prostor boja
lena_ycbcr = opencv.cvtColor(lena_bgr, opencv.COLOR_BGR2YCrCb)

# Prikaz RGB slike
opencv.namedWindow('Lena RGB')
opencv.imshow('Lena RGB', lena_bgr)

# Prikaz YCbCr slike
opencv.namedWindow('Lena YCbCr')
opencv.imshow('Lena YCbCr', lena_ycbcr)

# Kanali 
b, g, r = opencv.split(lena_bgr)
y, cr, cb = opencv.split(lena_ycbcr)

opencv.waitKey(0)
opencv.destroyAllWindows()



