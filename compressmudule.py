import zlib, base64

def compress(inputfile, outputfile):
    data = open(inputfile, 'r').read()
    data_byte = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_byte, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(outputfile, 'w')
    compressed_file.write(decoded_data)

def compress(inputfile,outputfile):
    open(inputfile, 'r').read()
    file_content = open(inputfile, 'r').read()
    encode_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encode_data))
    decoded_data = decompressed_data.decode('utf-8')
    file = open(outputfile, 'w')
    file.write(decoded_data)
    file.close()    

compress('compressed.txt', 'c1.txt')


 
        
