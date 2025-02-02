import zlib, base64

data = open('demo.txt', 'r').read()
data_byte = bytes(data, 'utf-8')
compressed_data = base64.b16decode(zlib.compress(data_byte)) 
print(compressed_data)