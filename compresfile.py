import zlib, base64

data = open('demo.txt', 'r').read()
data_byte = bytes(data, 'utf-8')
compressed_data = base64.b64encode(zlib.compress(data_byte, 9))
decoded_data = compressed_data.decode('utf-8')
compressed_file = open('compressed.txt', 'w')
compressed_file.write(decoded_data)

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data.decode('utf-8'))

