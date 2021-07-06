from .libsProject import *
from .functionProject import *


def recognizerDisease(conceptId):

    #загружаем словарь параметров для обработки данных
    with open('models/model_best090421.pickle', 'rb') as infile:
        libs = pickle.load(infile)

    # загружаем обученную модель нейросети
    model = load_model('models/model_best090421.hdf5')

    loaded_test = conceptId  # загружаем полученные концепты
    # определяем параметры для обработки концептов

    vocabulary = libs['vocabulary']
    classes = libs['classes']
    nClasses = len(classes)
    xLen = libs['xLen']
    maxConceptsCount = len(vocabulary)

    # преобразуем полученный массив концептов в массив индексов согласно словаря
    conceptIndexes = []

    conceptIndexes.append(concept2Indexes(loaded_test, vocabulary, maxConceptsCount))

    xTest = changeSetTo01(conceptIndexes, maxConceptsCount)

    out = model.predict(xTest)
    # print(out)
    # print(np.argmax(out))
    data = list(out[0])
    dic = {}
    for num in data:
        if ((num * 100) > 1):
            dic[classes[data.index(num)]] = num * 100

    # print('Распознала сеть - ', classes[np.argmax(out)])
    # diagnosis1 = classes[np.argmax(out)]

    return dic  # diagnosis2
