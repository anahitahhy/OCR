import cv2
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

kernelx = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)

gradx = cv2.filter2D(blurred, -1, kernelx)
grady = cv2.filter2D(blurred, -1, kernely)
edges = cv2.sqrt(cv2.add(cv2.multiply(gradx, gradx), cv2.multiply(grady, grady)))
cv2.imshow('Original Image', img)
cv2.imshow('Prewitt Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
