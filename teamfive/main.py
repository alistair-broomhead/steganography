#theheadofabroom
from PIL import Image
import unittest

HEADER = "ENCODED"
im = Image.open("pony2.png")
text = 'This is a dead parrot'
TERMINATOR = '\x00'

width, height = im.size

pixels = list(im.getdata())
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

#print pixels
def iter_image(im):
	pixels = img.load()
	for i in xrange(im.size[0]):
		for j in xrange(im.size[1]):
			for part in pixels[i,j]:
				yield part

class  TestEncode(unittest.TestCase):
	"""docstring for  TestEncode"""

	def test_works(self):
		message = "Hello, World!"
		file_in = "pony2.png"
		file_out = "shifty_pony.png"
		encode(message, file_in, file_out)
		self.assertEqual(message, decode(file_out))

def binary_out(message):
	from pdb import set_trace; set_trace()
	def chr_to_byte(chr_in):
		byte_out = bin(ord(c)).lstrip('0b')
		return "0"*(8 - len(byte_out)) + byte_out
	return "".join([chr_to_byte(c) for c in message])

def encode(message, image, outImage):
	inImage = Image.open(image)
	pixels_in = inImage.load()
	outIm = Image.open(image)
	pixels_out = outIm.load()
	pix = [0, 0, 0]

	def do(bit):
		i, j, rgb = pix
		rbg_val = list(pixels_out[i, j])
		pix_in = pixels_in[i, j][rgb]
		rbg_val[rgb] = pix_in - (pix_in % 2) - (bit == '1')*20
		pixels_out[i,j] = tuple(rbg_val)
		pix[2] += 1
		if pix[2] == 3:
			pix[0] += 1
			pix[2] = 0
		if pix[0] == inImage.size[1]:
			pix[0] = 0
			pix[1] += 1

	for bit in binary_out(HEADER):
		do(bit)
	for bit in binary_out(message):
		do(bit)
	do(TERMINATOR)
	outIm.save(outImage)


def decode(outImage):
	outIm = Image.open(outImage)
	pixels = outIm.load()
	header = []
	output = []
	current = []
	l = header
	for i in xrange(outIm.size[0]):
		for j in xrange(outIm.size[1]):
			current += [str(x%2) for x in pixels[i,j]]
			if len(current) >= 8:
				cc = int(''.join(current[:8]), 2)
				cc = chr(cc)
				l.append(cc)
				current = current[8:]
				if l is header and len(l) == len(HEADER):
					l = current
					if ''.join(header) != HEADER:
						return ""
				elif cc == TERMINATOR:
					l.pop()
					return "".join(l)


	for byte in xrange(len(HEADER)):
		h = []
		for b in range(8):
			h.append(it.next()%2)


	clearText = "" #empty placeholder

	return 'message'

if __name__ == "__main__":
	unittest.main()
