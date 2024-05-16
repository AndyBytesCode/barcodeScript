from barcode import Code128
from barcode.writer import ImageWriter

number = input("enter The barcode sample ")
barcode = Code128(number, writer= ImageWriter())


barcode.save('Barcode')

print("This is a Test")