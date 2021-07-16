from .libsProject import *
from .functionProject import *


def recognizerDisease(text):

    model_BOW = keras.models.load_model('D:\medExcursion\\app\models\model_BOW_best202107152')
    # model_Emb = keras.models.load_model('models/model_Embd202107151')
    # загружаем словарь параметров для обработки данных
    with open('D:\medExcursion\\app\models\model_best20210715.pickle', 'rb') as f:
        libs = pickle.load(f)

    dictClass = {
        "Acute appendicitis": "Острый аппендицит",
        "Duodenitis": "Дуоденит",
        "Acute pancreatitis": "Острый панкреатит",
        "Peptic ulcer and gastritis": "Язвенная болезнь желудка и гастрит",
        "Peritonitis": "Перитонит",
        "Pyloroduodenal stenosis": "Стеноз пилородуоденальный",
        "Ulcer perforation": "Перфорация язвы",
        "Ulcerative bleeding": "Язвенное кровотечение",
        "Acute cholecystitis": "Острый холецистит",
    }

    vocabulary = libs['vocabulary']
    classes = libs['classes']
    nClasses = len(classes)
    xLen = libs['xLen']
    maxConceptsCount = len(vocabulary) + 1

    loaded_test = text2Words(text)

    # преобразуем полученный массив концептов в массив индексов согласно словаря
    conceptIndexes = []
    conceptIndexes.append(words2Indexes(loaded_test, vocabulary, maxConceptsCount))

    print(conceptIndexes)
    xTest = changeSetTo01(conceptIndexes, maxConceptsCount)
    print(xTest)
    out_BOW = model_BOW.predict([xTest])
    # out_Emb = model_Emb.predict(xTest)
    # print(out_BOW)
    # print(np.argmax(out_BOW))

    data = list(out_BOW[0])

    dic = {}
    for num in out_BOW[0]:
        if ((num * 100) > 1):
            dic[classes[data.index(num)]] = num * 100

    def translateDis(dictClass, item):
        for k, v in dictClass.items():
            if k == item:
                return v

    result = {}
    for key, value in dic.items():
        sym = translateDis(dictClass, key)
        result[sym] = round(value, 2)

    return result
#
# loaded_test = conceptId  # загружаем полученные концепты
# # определяем параметры для обработки концептов
# vocabulary = libs['vocabulary']
# classes = libs['classes']
# nClasses = len(classes)
# xLen = libs['xLen']
# maxConceptsCount = len(vocabulary)
#
# # преобразуем полученный массив концептов в массив индексов согласно словаря
# conceptIndexes = []
#
# conceptIndexes.append(concept2Indexes(loaded_test, vocabulary, maxConceptsCount))
#
# xTest = changeSetTo01(conceptIndexes, maxConceptsCount)
#
# out = model.predict(xTest)
# # print(out)
# # print(np.argmax(out))
# data = list(out[0])
# dic = {}
# for num in data:
#     if ((num * 100) > 1):
#         dic[classes[data.index(num)]] = num * 100
#
# # print('Распознала сеть - ', classes[np.argmax(out)])
# # diagnosis1 = classes[np.argmax(out)]
