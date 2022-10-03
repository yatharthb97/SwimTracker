class Lights:
	"""
	Object used to control the LED panel for lighting.
	"""

	def __init__(pin, no_pixels):
		"""
		pin: The dataline digital pin
		no_pixels: Pixels on the board. For 8 X 8 board - 64 pixels.
		"""
		import neopixel
		import board

		self.pixels = neopixel.Neopixel(board.__dict__[str(pin)], \
					  no_pixels, auto_write=False, pixel_order=neoxpixel.RGB)

		# Construct in off mode
		# self.off()

	def on(lum=1.0):
		"""
		Turns on the LED array and sets the color to white.
		lum: Brighness of the pixels: [0.0, 1.0]
		"""
		for i in range(len(self.pixels)):
			self.pixels[i] = (255, 255, 255, lum)
		self.pixels.show()

	def off():
		"""
		Turns off the LED array.s
		"""
		for i in range(len(self.pixels)):
			self.pixels[i] = (0, 0, 0, 0)
		self.pixels.show()

	def red(lum=1.0):
		"""
		Change panel color to red.
		lum: Brighness of the pixels: [0.0, 1.0]
		"""
		for i in range(len(self.pixels)):
			self.pixels[i] = (255, 0, 0, lum)
		self.pixels.show()

	def green(lum=1.0):
		"""
		Change panel color to green.
		lum: Brighness of the pixels: [0.0, 1.0]
		"""
		for i in range(len(self.pixels)):
			self.pixels[i] = (0, 255, 0, lum)
		self.pixels.show()

	def blue(lum=1.0):
		"""
		Change panel color to blue.
		lum: Brighness of the pixels: [0.0, 1.0]
		"""
		for i in range(len(self.pixels)):
			self.pixels[i] = (0, 0, 255, lum)
		self.pixels.show()


	def set_color(color_value):
		assert len(color_value) == 3
		for i in range(len(self.pixels)):
			self.pixels[i] = color_value
		self.pixels.show()

	
	def set_brightness(new_brightness):
		for i in range(len(self.pixels)):
			self.pixels[i][3] = new_brightness
		self.pixels.show()


	def set_sequence(sequence):
		"""
		Set a light sequence operation seperately on a seperate thread or
		a microcontroller.
		sequence is a container with -> [color_px, time_in_ms]
		"""
		pass
	
dict_ = dict()
i = 0
for p in prob:
	i = i +1
	dict_[i]["prob"] = p
	dict_[i]["percentages"] = rbinom(...)
