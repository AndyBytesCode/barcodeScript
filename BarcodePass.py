from barcode import Code128
from barcode.writer import ImageWriter

number = "w#@t3v3R"
barcode = Code128(number, writer= ImageWriter())


barcode.save('Barcode')
