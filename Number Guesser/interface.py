import pygame
import numpy
from keras.models import load_model
import time

model = load_model("./number_guesser")

pygame.font.init()
font = pygame.font.SysFont(None, 24)

width = 980
height = 840
prediction = -1
display = True

class Pixel:
    def __init__(self, val, rect):
        self.val = val
        self.rect = rect

pixels = []
for i in range(28):
    for j in range(28):
        pixels.append(Pixel(0, pygame.Rect(width - height + j * 28, i * 28, 30, 30)))

send_button = pygame.Rect(0, 0, width - height, height / 2)
eraser = pygame.Rect(0, height / 2, width - height, height / 2)

pygame.display.set_caption('Number Input')
screen = pygame.display.set_mode((width, height))

predict_text = font.render('Prediction: ', True, (255, 255, 122))
erase_text = font.render('Erase', True, (255, 255, 255))

def draw():
    for pixel in pixels:
        pygame.draw.rect(screen, (pixel.val, pixel.val, pixel.val), pixel.rect)

    pygame.draw.line(screen, (255, 255, 255), (0, height / 2), (width - height, height / 2), 5)
    pygame.draw.line(screen, (255, 255, 255), (width - height, width / 2), (width - height, 0), 5)
    pygame.draw.line(screen, (255, 255, 255), (width - height, width / 2), (width - height, height), 5)

    guess_text = font.render(str(prediction), True, (255, 255, 122))
    screen.blit(predict_text, (20, height / 4) )
    screen.blit(erase_text, (20, height * 3 / 4))
    if display:
         screen.blit(guess_text, (40, height / 4 + 20))
    
    pygame.display.update()

def blot(i):
    pixels[i].val = 255
    if i > 27:
        add(16, i - 28)
    if i < 756:
        add(16, i + 28)
    if i % 28 != 0:
        add(16, i - 1)
    if i % 28 != 27:
        add(16, i + 1)
    if i > 27 and i % 28 != 0:
        add(8, i - 29)
    if i < 756 and i % 28 != 27:
        add(8, i + 29)
    if i > 27 and i % 28 != 27:
        add(8, i - 27)
    if i < 756 and i % 28 != 0:
        add(8, i + 27)

def add(delta, i):
    pixels[i].val += delta
    if pixels[i].val > 255:
        pixels[i].val = 255

def send(la, d, file_name):
    
    string = str(la) + ","
    for i in range(len(d)):
        if i == len(d) - 1:
            string += str(d[i])
        else:
            string += str(d[i]) + ","
    
    ext_file = open(file_name, "a")
    ext_file.write(string + "\n")
    ext_file.close()

running = True
while running:
    #quit on close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]:
        if eraser.collidepoint(pygame.mouse.get_pos()):
            for pixel in pixels:
                pixel.val = 0

        elif send_button.collidepoint(pygame.mouse.get_pos()):
            data = []
            for pixel in pixels:
                data.append(pixel.val)
            prediction = numpy.argmax(model.predict([data]), axis = 1)[0]
            """
            label = ""
            while True:
                
                label = input('What is this number? ')
                if int(label) >= 0 and int(label) <= 9:
                    send(label, data, "new_data.csv")
                    break
                else:
                    print("Try again. 0-9 please")
            """
            print('PREDICTION: ' + str(prediction))
            time.sleep(.1)
        else:
            for i in range(784):
                if pixels[i].rect.collidepoint(pygame.mouse.get_pos()):
                    blot(i)

    draw()
    time.sleep(1/120)