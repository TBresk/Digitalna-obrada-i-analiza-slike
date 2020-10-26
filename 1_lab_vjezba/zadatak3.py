import cv2 as opencv

# Učitavanje slike
lena = opencv.imread('../lena-color.jpg')

# Rastavljanje slike na kanale
b, g, r = opencv.split(lena)

# Prikaz plavog, zelenog i crvenog kanala odvojeno
opencv.namedWindow("Lena blue canal")
opencv.imshow("Lena blue canal", b)

opencv.namedWindow("Lena green canal")
opencv.imshow("Lena green canal", g)

opencv.namedWindow("Lena blue canal")
opencv.imshow("Lena red canal", r)

opencv.waitKey(0)
opencv.destroyAllWindows()

# Nakon pregleda prikazanih kanala zaključujem da je zeleni kanal najprirodniji
# Razlog tome može biti taj što zelena boja zahvaća najširi raspon valnih duljina vidljivih ljudskom oku 
