from .libsProject import *

def open_dict(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


# преобразуем текст в слова
def text2Words(text):
    # Удаляем лишние знаки
    text = text.replace(".", " ")
    text = text.replace("—", " ")
    text = text.replace(",", " ")
    text = text.replace("!", " ")
    text = text.replace("?", " ")
    text = text.replace("…", " ")
    text = text.replace("-", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace(";", " ")
    text = text.replace(",", " ")
    text = text.lower()  # переводим в нижний регистр

    words = []  # создаем пустой список, в который будем записывать все слова
    currWord = ""  # здесь будет накапливаться текущее слово (между двумя пробелами)

    for symbol in text:  # проходим по каждому символу в тексте

        if (symbol != "\ufeff"):  # игнорируем системный символ в начале строки
            if (symbol != " "):  # если символ не является пробелом
                currWord += symbol  # то добавляем символ в текущее слово
            else:  # если символ является пробелом:
                if (currWord != ""):  # и текущее слово не пустое
                    words.append(currWord)  # то добавляем текущее слово в список слов
                    currWord = ""  # затем обнуляем текущее слово

    # Добавляем финальное слово, если оно не пустое
    # Если не сделать, то потеряем финальное слово, потому что текст чаще всего заканчивается не на пробел
    if (currWord != ""):  # если слово не пустое
        words.append(currWord)  # то добавляем финальное слово в список слов

    return words  # фунция возвращает набор слов


def words2Indexes(words, vocabulary, maxWordsCount):
    '''
      concept2Indexes - Функция создание индексов концептов
      вход:
        concepts - концепты
        vocabulary - словарь концептов
        maxConceptCount - максимальное количество всех концептов словаря
      выход:
        список индексов всх концептов
    '''

    wordsIndexes = []

    for word in words:
        wordIndex = 0
        wordInVocabulary = word in vocabulary

        if (wordInVocabulary):
            index = vocabulary[word]
            if (index < maxWordsCount):
                wordIndex = index

        wordsIndexes.append(wordIndex)

    return wordsIndexes


def changeXTo01(trainVector, conceptsCount):
    '''
        changeXTo01 - Функция создания words of bag (преобразование одного короткого вектора
        в вектор из 0 и 1)
        вход:
            trainVector - обучающий ветор
            conceptsCount - длина библиотеки концептов
        выход:
            words of bag xTrain, yTrain
    '''

    out = np.zeros(conceptsCount)
    for x in trainVector:
        out[x] = 1
    return out

def changeSetTo01(trainSet, conceptsCount):
    '''
        changeSetTo01 - Функция создания words of bag обучающей и проверочной выборки
        (преобразование одного короткого вектора в вектор из 0 и 1)
        вход:
            trainVector - обучающий ветор
            conceptsCount - длина библиотеки концептов
        выход:
            массив words of bag xTrain, yTrain
    '''

    out = []
    for x in trainSet:
        out.append(changeXTo01(x, conceptsCount))
    return np.array(out)

def changeXTo01Multi(trainVector, conceptsCount):
    '''
        changeXTo01Multi - Функция создания words of bag обучающей и проверочной выборки
        (преобразование одного короткого вектора в вектор из 0 и 1) с множественным вхождением
        вход:
            trainVector - обучающий ветор
            conceptsCount - длина библиотеки концептов
        выход:
            words of bag xTrain, yTrain
    '''

    out = np.zeros(conceptsCount)
    for x in trainVector:
        out[x] += 1
    return out

def changeSetTo01Multi(trainSet, conceptsCount):
    '''
        changeSetTo01Multi - Функция создания words of bag обучающей и проверочной выборки
        (преобразование одного короткого вектора в вектор из 0 и 1) с множественным вхождением
        вход:
            trainSet - обучающий массив веторов
            conceptsCount - длина библиотеки концептов
        выход:
            массив words of bag xTrain, yTrain
    '''

    out = []
    for x in trainSet:
        out.append(changeXTo01Multi(x, conceptsCount))
    return np.array(out)

