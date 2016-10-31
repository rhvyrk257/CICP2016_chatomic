from PIL import Image
import sys

def __main__():
	filename, x, y = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
	image = Image.open(filename)
	print(image.getpixel((x, y)))

if __name__ == '__main__':
	__main__()
