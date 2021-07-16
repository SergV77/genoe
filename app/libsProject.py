import os # Модуль функций для работы с операционной системой, не зависящие от используемой операционной системы
import collections #Модуль специализированных типов данных, на основе словарей , кортежей , множеств , списков
import math # Библиотека математических функций
import pandas as pd # Библиотека pandas
import numpy as np # Библиотека работы с массивами
import matplotlib.pyplot as plt # Отрисовка изображений
import json
import pickle
import requests

from tensorflow.keras.models import Sequential # НС прямого распространения
from tensorflow.keras.layers import Dense, Activation, Dropout, SpatialDropout1D, BatchNormalization, Embedding, Flatten # Основные слои
from tensorflow.keras import utils # Утилиты для to_categorical
from tensorflow.keras.preprocessing import image # Для отрисовки изображения
from tensorflow.keras.optimizers import Adam, Adadelta, RMSprop # Алгоритмы оптимизации, для настройки скорости обучения
from tensorflow.keras.models import load_model # загрузка сохраненных моделей
from tensorflow.keras.preprocessing.sequence import pad_sequences # Модуль для возврата списка дополненных последовательностей

#from keras.utils import plot_model # Построение графика модели и сохранене в файле
#from keras.callbacks import ModelCheckpoint # Модуль для работы с колбэками (сохранение наилучших результатов)

from sklearn.preprocessing import LabelEncoder, StandardScaler # Функции для нормализации данных
from sklearn import preprocessing # Пакет предварительной обработки данных
from sklearn.model_selection import train_test_split


from flask import Flask
from flask import request

import os
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model, Sequential, load_model

import pickle
