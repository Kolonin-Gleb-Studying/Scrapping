import numpy as np  # Импортируем библиотеку numpy
import time
import random
import os  # Импортируем библиотеку os для раоты с фаловой системой
from PIL import Image  # импортируем модель Image для работы с изображениями
from tensorflow.keras import utils

width = 352  # ширина картинки без сжатия
height = 256  # высота картинки без сжатия

dataset = './cityscapes'  # Путь к датасету
dataset_train = dataset + "/train"  # Путь к обучающей выборке
dataset_val = dataset + "/val"  # Путь к провероной выборке

num_classes = 8


# Функции загрузки датасета

# Функция разделения одной картинки на две - xTrain и yTrain
def separate_train(name):
    image = Image.open(name)

    x = image.crop((0, 0, 255, 255)).resize((width, height), Image.ANTIALIAS)
    y = image.crop((256, 0, 511, 255)).resize((width, height), Image.ANTIALIAS)

    return x, y


def pixel_segmentation(pixel):
    index = 0
    color = [0, 0, 0]

    if (110 >= pixel[0] >= 50) and (150 >= pixel[1] >= 115) and (190 >= pixel[2] >= 160):  # небо
        index = 0
        color = [70, 130, 180]

    elif (157 >= pixel[0] >= 109) and (42 >= pixel[1] >= 0) and (72 >= pixel[2] >= 34):  # велосипеды
        index = 1  # велосипеды + люди
        color = [255, 0, 0]
    elif (255 >= pixel[0] >= 185) and (50 >= pixel[1] >= 0) and (86 >= pixel[2] >= 0):  # люди
        index = 1  # велосипеды + люди
        color = [255, 0, 0]

    elif (80 >= pixel[0] >= 60) and (80 >= pixel[1] >= 60) and (80 >= pixel[2] >= 60):  # здания
        index = 2  # здания + тумбы + заборы
        color = [70, 70, 70]
    elif (115 >= pixel[0] >= 95) and (110 >= pixel[1] >= 90) and (170 >= pixel[2] >= 150):  # тумбы
        index = 2  # здания + тумбы + заборы
        color = [70, 70, 70]
    elif (200 >= pixel[0] >= 180) and (160 >= pixel[1] >= 140) and (160 >= pixel[2] >= 140):  # заборы
        index = 2  # здания + тумбы + заборы
        color = [70, 70, 70]

    elif (190 >= pixel[0] >= 120) and (255 >= pixel[1] >= 240) and (185 >= pixel[2] >= 115):  # трава
        index = 3  # трава и деревья
        color = [120, 145, 20]
    elif (120 >= pixel[0] >= 60) and (160 >= pixel[1] >= 110) and (70 >= pixel[2] >= 20):  # деревья
        index = 3  # трава и деревья
        color = [120, 145, 20]

    elif (235 >= pixel[0] >= 160) and (230 >= pixel[1] >= 200) and (135 >= pixel[2] >= 0):  # дорожные знаки
        index = 4  # дорожные знаки и светофоры
        color = [250, 250, 0]
    elif (255 >= pixel[0] >= 140) and (180 >= pixel[1] >= 143) and (80 >= pixel[2] >= 0):  # светофоры
        index = 4  # дорожные знаки и светофоры
        color = [250, 250, 0]

    elif (30 >= pixel[0] >= 0) and (30 >= pixel[1] >= 0) and (255 >= pixel[2] >= 125):  # машины
        index = 5  # машины и автобусы
        color = [20, 20, 255]
    elif (30 >= pixel[0] >= 0) and (80 >= pixel[1] >= 40) and (120 >= pixel[2] >= 0):  # автобусы
        index = 5  # машины и автобусы
        color = [20, 20, 255]

    elif (160 >= pixel[0] >= 105) and (75 >= pixel[1] >= 55) and (150 >= pixel[2] >= 120):  # проезжая часть
        index = 6  # проезжая часть
        color = [130, 65, 128]

    elif (255 >= pixel[0] >= 210) and (70 >= pixel[1] >= 25) and (255 >= pixel[2] >= 200):  # пешеходные зоны
        index = 7  # пешеходные зоны и парковки
        color = [220, 180, 200]
    elif (255 >= pixel[0] >= 240) and (180 >= pixel[1] >= 150) and (220 >= pixel[2] >= 150):  # парковки
        index = 7  # пешеходные зоны и парковки
        color = [220, 180, 200]

    return color, index


# Функция распределения изображения по классам
def segmentation_transform(img_obj):
    img_original = np.array(img_obj)  # преобразовываем изображение в массив
    img_seg = img_original.copy()  # создаем массив для нашей модели сегментации
    y = np.zeros((height, width, num_classes))  # создаем yTrain

    for w in range(width):
        for h in range(height):
            img_seg[h, w], ind = pixel_segmentation(img_original[h, w])
            y[h, w] = utils.to_categorical(ind, num_classes)

    return Image.fromarray(img_seg), y  # Мы должны обратно из массива перевести в объект картинка


# Формируем обучающую выборку
'''
xTrain = []
yTrain = []

cur_time = time.time()  # Получаем текущю метку времени
flist = os.listdir(dataset_train)  # Получаем список файлов
c = 1
for filename in sorted(flist):
    print(c, "из", len(flist))
    # Загружаем картинку, сразу же приводим её к нужным размерам и добавляем в массив
    x, z = separate_train(dataset_train + "/" + filename)  # получаем исходное изображение и сегментированное
    _, yt = segmentation_transform(z)  # сегментированное изображение переводим в OHE
    xTrain.append(np.array(x))
    yTrain.append(yt)
    c += 1

xTrain = np.array(xTrain)
yTrain = np.array(yTrain)
finish_time = time.time()
print('Время загрузки изображений тренировочной:', finish_time - cur_time, 'c')

f_x = open('xTrain.npy', 'wb')
f_y = open('yTrain.npy', 'wb')

np.save(f_x, xTrain)
np.save(f_y, yTrain)
'''

# Формируем проверочную выборку
xVal = []
yVal = []

cur_time = time.time()  # Получаем текущю метку времени
flist = os.listdir(dataset_val)
c = 1
for filename in sorted(flist):  # Получаем список файлов
    print(c, "из", len(flist))
    # Загружаем картинку, сразу же приводим её к нужным размерам и добавляем в массив
    x, z = separate_train(dataset_val + "/" + filename)  # получаем исходное изображение и сегментированное
    _, yt = segmentation_transform(z)  # сегментированное изображение переводим в OHE
    xVal.append(np.array(x))
    yVal.append(yt)
    c += 1

xVal = np.array(xVal)
yVal = np.array(yVal)

finish_time = time.time()
print('Время загрузки изображений проверочной выборки:', finish_time - cur_time, 'c')

f_x = open('xVal.npy', 'wb')
f_y = open('yVal.npy', 'wb')

np.save(f_x, xVal)
np.save(f_y, yVal)

