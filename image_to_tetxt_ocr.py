import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os




class Converter():
	def __init__(self, input_file, output_file):
		# initialize all environment variable and class variable required
		self.image = input_file
		self.output_file = output_file
		# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
		self.poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"  # Specify Poppler path for Windows
		os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\testdata'

	def read_image(self):
		# reads pdf image 
		try:
			images = convert_from_path(self.image, poppler_path = self.poppler_path)
			return images
		except Exception as e:
		    print(f"Error converting PDF to images: {e}")
		    exit()


	def extract_text(self):
		# extracts text from each page if more than one
		images=self.read_image()
		ocr_text = ""
		for index, image in enumerate(images, start=1):
		    try:
		        ocr_text += pytesseract.image_to_string(image, lang='eng')
		        print(f"OCR completed for page {index}")

		    except Exception as e:
		        print(f"Error during OCR for page {index}: {e}")
		return ocr_text


	def save_to_txt(self):
		# saves the output txt to file
		output = self.output_file
		ocr_text = self.extract_text()
		try:
		    with open(output, "w", encoding="utf-8") as text_file:
		        text_file.write(ocr_text)
		    print(f"OCR text successfully written to {output}")
		except Exception as e:
		    print(f"Error writing to output file: {e}")


# just initialize the class and pass in the input file and desired output_file
image = Converter("input.pdf", "output.txt")
image.save_to_txt()