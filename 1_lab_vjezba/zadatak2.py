import cv2 as opencv

# Učitavanje slike
lena = opencv.imread('../lena-color.jpg')

# Uvećavanje slike
lena_resize = opencv.resize(lena, (0, 0), fx = 2.0 , fy = 2.0)

# Prikaz ne uvećane slike
opencv.namedWindow('Lena')
opencv.imshow('Lena', lena)
print(f"Dimenzije ne uvećane slike = {lena.shape}.")

# Prikaz uvećane slike
opencv.namedWindow('Lena resize')
opencv.imshow('Lena resize', lena_resize)
print(f"Dimenzije uvećane slike = {lena_resize.shape}.")

opencv.waitKey(0)
opencv.destroyAllWindows()
