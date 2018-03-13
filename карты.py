import pygame
import requests
import sys
import os
def drow(x,y,Format):
    response = None
    try:
        map_request = "https://static-maps.yandex.ru/1.x/?ll={},{}&z={}&size=600,450&l=map".format(y, x, Format)
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(geocoder_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
    except:
        print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

    # Инициализируем pygame
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()

    # Удаляем за собой файл с изображением.
    os.remove(map_file)

def obrab(i):
    global X
    global Y
    global FORM
    print(sdvig)
    if i == pygame.K_PAGEDOWN:
        FORM -= 1
    if i == pygame.K_PAGEUP:
        FORM += 1
    if i == pygame.K_UP:
        X += sdvig
    if i == pygame.K_DOWN:
        X -= sdvig
    if i == pygame.K_LEFT:
        Y -= sdvig
    if i == pygame.K_RIGHT:
        Y += sdvig
    if X >= -180 and X <= 180 and Y >= -90 and Y <= 90 and FORM >= 0 and FORM <= 17:
        drow(X,Y,FORM)

pygame.init()
screen = pygame.display.set_mode((600, 450))
X, Y = 38.870962, -77.055942
FORM = 0
running = True
drow(X,Y,FORM)
while running:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                obrab(event.key)
pygame.quit()