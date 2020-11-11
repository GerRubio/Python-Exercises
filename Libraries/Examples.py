import csv, datetime, json, os, PIL, random, requests, sqlite3, sys, zlib, qrcode
import matplotlib.pyplot as plt
from fractions import Fraction
from PIL import Image, ImageDraw, ImageFont

# -- OS LIBRARY EXAMPLES --

# See when a file was modified.
def modified_file():
    for iterator in os.listdir():
        ts = os.path.getmtime(iterator)
        dt = datetime.datetime.fromtimestamp(ts)
    
        print(f'The file {iterator} was modified at {dt}')

# Calculate the size of the full directory including sub-directories.
def full_directory_size():
    total_size = 0

    for iterator in os.walk("."):
        dir_path, _, files = iterator
    
        for file_name in files:
            full_path = os.path.join(dir_path, file_name)
            size = os.path.getsize(full_path)
        
            print(full_path, 'fill', size, 'bytes.')
        
            total_size += size

    print(f'Total size: {total_size} bytes.')

# Print size of the files.
def file_size():
    for iterator in os.walk('.'):
        dir_path, _, files = iterator

        print(f'''
            Size: {len(dir_path)} 
            Size: {len(files)}
            ''')

# Ranomd elements.
def game():
    items = ['Stone', 'Paper', 'Scissors']
    
    print(random.choice(items))

# Gauss bell simulation.
def gauss_simulation():
    simulation = [random.gauss(10, 0.0245) for _ in range(10000)]
    
    min(simulation), max(simulation)
    
    plt.hist(simulation, bins = 80, color = "#888888")
    plt.show()

# Random dices.
def random_dices(n_dices):
    dices = 0

    for _ in range(n_dices):
        value = random.randrange(1, 6)
        dices += value
    
    return dices

# Compress a .zip file.
def compress_file():
    compressor = zlib.compressobj(wbits = 9)
    
    original_size = 0
    compressed_size = 0
    
    buffer = bytearray()
    file_name = 'lorem.txt'
    
    print(f'File compression {file_name}', end = ': ')
    
    with open(file_name, 'r') as input:
        while True:
            block = input.read(64).encode('UTF-8')
            
            if not block:
                break
            
            original_size += len(block)
            compressed = compressor.compress(block)
            
            if compressed:
                compressed_size += len(compressed)
                buffer += compressed
                
                print('█', end = '')
            else:
                print('░', end = '')
        
        remaining = compressor.flush()
        compressed_size += len(remaining)
        buffer += remaining

    print('OK')

    f_compress = round(compressed_size * 100.0 / original_size, 2)

    print(f'Compressed file {file_name} with compression rate {f_compress:.02f}')
    print('Original size:', original_size)
    print('Compressed size:', compressed_size)

# -- REQUESTS EXAMPLES --

# Request example.
def request_example():
    urls = [
        'http://google.es',
        'http://es.wikipedia.es/',
        'https://www.python.org/',
        'https://github.com/',
    ]

    for url in urls:
        resp = requests.get(url)
        
        print(url, resp.ok, resp.status_code)

# -- PIL EXAMPLES --

# Red circle.
def clown_noise():
    img = Image.open('wallpaper.jpg')
    img.thumbnail((450, 300))
    draw = ImageDraw.Draw(img, 'RGBA')
    draw.ellipse((260, 50, 330, 120), outline = (255, 255, 255, 128), width = 2)
    img

# -- QR CODE EXAMPLES --

# QR name.
def qr_name():
    nm = qrcode.make('QR Example')
    nm.save('qr_example.png')