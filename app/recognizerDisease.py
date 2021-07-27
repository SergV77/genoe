from .libsProject import *
from .functionProject import *

# загрузка моделей нейросети
model_BOW = keras.models.load_model('D:\medExcursion\\app\models\model_BOW_best202107152')  # Обычная модель
# model_BOW = keras.models.load_model('D:\medExcursion\\app\models\model_BOW_best202107261')  # Улучшенная модель
model_BOW_umkb = keras.models.load_model('D:\medExcursion\\app\models\model_BOW_best202107272')  # Модель по данным из umkb
# model_Emb = keras.models.load_model('models/model_Embd202107151')

# загрузка вспомогательной информации (словарь, шаг и т.п.)
libs = open_dict('D:\medExcursion\\app\models\model_best20210715.pickle')    # Словарь по обычной модельи
# libs = open_dict('D:\medExcursion\\app\models\\train_info_202107261.pickle') # Словарь по улучшенной модели
libs_umkb = open_dict('D:\medExcursion\\app\models\\train_info_202107271.pickle') # Словарь по данным из umkb

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

# dictClass = {
#         "Acute appendicitis": "Острый аппендицит",
#         "Acute cholecystitis": "Острый холецистит",
#         "Acute pancreatitis": "Острый панкреатит",
#         "Duodenitis": "Дуоденит",
#         "Peptic ulcer and gastritis": "Язвенная болезнь желудка и гастрит",
#         "Peritonitis": "Перитонит",
#         "Pyloroduodenal stenosis": "Стеноз пилородуоденальный",
#         "Ulcer perforation": "Перфорация язвы",
#         "Ulcerative bleeding": "Язвенное кровотечение",
#
#     }

dictClass_umkb = {
    "saved_allConceptId0": "Острый аппендицит",
    "saved_allConceptId1": "Острый холецистит",
    "saved_allConceptId2": "Острый панкреатит",
    "saved_allConceptId3": "Дуоденит",
    "saved_allConceptId4": "Язвенная болезнь желудка и гастрит",
    "saved_allConceptId5": "Перитонит",
    "saved_allConceptId6": "Стеноз пилородуоденальный",
    "saved_allConceptId7": "Перфорация язвы",
    "saved_allConceptId8": "Язвенное кровотечение",

}


def recognizerDisease(text):

    vocabulary = libs['vocabulary']
    classes = libs['classes']
    nClasses = len(classes)
    xLen = libs['xLen']
    maxConceptsCount = len(vocabulary) + 1
    print(classes)
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


def recognizerDiseaseConcepts(concepts):

    vocabulary = libs_umkb['vocabulary']
    classes = libs_umkb['classes']
    nClasses = len(classes)
    xLen = libs_umkb['xLen']
    maxConceptsCount = len(vocabulary)
    print(classes)

    # преобразуем полученный массив концептов в массив индексов согласно словаря
    conceptIndexes = []
    conceptIndexes.append(words2Indexes(concepts, vocabulary, maxConceptsCount))
    print(conceptIndexes)
    xTest = changeSetTo01(conceptIndexes, maxConceptsCount)
    print(xTest)
    out_BOW = model_BOW_umkb.predict([xTest])
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
        sym = translateDis(dictClass_umkb, key)
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
