from .libsProject import *


# преобразуем текст в слова
def text2Words(text):
    # удаляем(заменяем на пробел), все знаки припенания
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
    text = text.lower()  # приводим к нижниму регистру

    # собираем массив из слов текста
    words = []
    currWord = ""
    for symbol in text:

        if (symbol != " "):
            currWord += symbol
        else:
            if (currWord != ""):
                words.append(currWord)
                currWord = ""

    if (currWord != ""):
        words.append(currWord)

    return words


def concept2Indexes(concepts, vocabulary, maxConceptCount):
    '''
      concept2Indexes - Функция создание индексов концептов
      вход:
        concepts - концепты
        vocabulary - словарь концептов
        maxConceptCount - максимальное количество всех концептов словаря
      выход:
        список индексов всх концептов
    '''

    conceptsIndexes = []

    for concept in concepts:
        conceptIndex = 0
        conceptInVocabulary = concept in vocabulary

        if (conceptInVocabulary):
            index = vocabulary[concept]
            if (index < maxConceptCount):
                conceptIndex = index

        conceptsIndexes.append(conceptIndex)

    return conceptsIndexes


def getSetFromIndexes(conceptIndexes, xLen, step):
    '''
        getSetFromIndexes - Функция формирование xTrain (обучающей выборки) по листу индексов концептов
        (разделение на короткие векторы) одного класса
        вход:
            conceptIndexes - индоксы концептов
            xLen - длина вектора
            step - шаг смещения
        выход:
            xTrain
    '''

    xTrain = []
    conceptLen = len(conceptIndexes)
    index = 0
    while (index + xLen <= conceptLen):
        xTrain.append(conceptIndexes[index:index + xLen])
        index += step
    return xTrain


def createSetsMultiClasses(conceptIndexes, xLen, step):
    '''
        createSetsMultiClasses - Функция формирование xTrain, yTrain (обучающей выборки)
        по листу индексов концептов одного класса
        вход:
            conceptIndexes - индоксы концептов
            xLen - длина вектора
            step - шаг смещения
        выход:
            xTrain, yTrain
    '''

    # Формирование обучающей и проверочной выборки выборки из 10 листов индексов от 10 классов
    nClasses = len(conceptIndexes)
    classesXTrain = []
    for cI in conceptIndexes:  # Для каждого из 10 классов
        classesXTrain.append(getSetFromIndexes(cI, xLen, step))  # Создаём обучающую выборку из индексов

    xTrain = []  # Формируем один общий xTrain
    yTrain = []

    for t in range(nClasses):
        xT = classesXTrain[t]
        for i in range(len(xT)):
            xTrain.append(xT[i])

        currY = utils.to_categorical(t, nClasses)  # Формируем yTrain по номеру класса
        for i in range(len(xT)):
            yTrain.append(currY)

    xTrain = np.array(xTrain)
    yTrain = np.array(yTrain)

    return (xTrain, yTrain)


def createSetsMultiClassesBallanced(conceptIndexes, xLen, step, classSize):
    '''
        createSetsMultiClasses - Функция формирование xTrain, yTrain (обучающей выборки)
        по листу индексов концептов нескольких классов
        вход:
            conceptIndexes - индоксы концептов
            xLen - длина вектора
            step - шаг смещения
            classSize - размер класса
        выход:
            xTrain, yTrain
    '''

    # Формирование обучающей и проверочной выборки выборки # Из 10 листов индексов от 10 классов

    nClasses = len(conceptIndexes)
    classesXTrain = []
    for cI in conceptIndexes:
        classesXTrain.append(getSetFromIndexes(cI, xLen, step))  # Создаём обучающую выборку из индексов

    xTrain = []  # Формируем один общий xTrain
    yTrain = []

    for t in range(nClasses):
        xT = classesXTrain[t]
        for i in range(classSize):
            xTrain.append(xT[i])

        currY = utils.to_categorical(t, nClasses)  # Формируем yTrain по номеру класса
        for i in range(classSize):
            yTrain.append(currY)

    xTrain = np.array(xTrain)
    yTrain = np.array(yTrain)

    return (xTrain, yTrain)


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


def createTestsClasses(allIndexes, train_size):
    '''
        createTestsClasses - Функция создания обучающей и тестовой выборки с использованием
        стандартного метода библиотеки sklearn
        вход:
            allIndexes - массив
            conceptsCount - длина библиотеки концептов
        выход:
            X_train, y_train, X_test, y_test
    '''

    # Формируем общий xTrain и общий xTest
    X_train, X_test, y_train, y_test = np.array(
        train_test_split(allIndexes, np.ones(len(allIndexes), 'int'), train_size=train_size))

    return (X_train, y_train, X_test, y_test)
