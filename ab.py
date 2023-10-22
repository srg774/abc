import time

message = "Hello, World!"
width = 20  # Adjust the width as needed

while True:
    for i in range(len(message) + width):
        text = message[i:i + width]
        print(text.ljust(width, ' '), end='\r')
        time.sleep(0.1)
