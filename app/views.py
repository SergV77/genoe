from flask import render_template, redirect, request, url_for, flash #session,
from app import app
from . import forms
from .forms import RequestForm, NameForm
from .recognizerDisease import *
from .parsConcept import *

# model_BOW = keras.models.load_model('models/model_BOW_best202107152')


@app.route('/',  methods=['GET', 'POST'])
def index():
    form = RequestForm()
    messages = None
    if form.validate_on_submit():
        #messages = form.text.data
        messages = recognizerDisease(form.text.data)
        messages = dict(sorted(messages.items(), key=lambda x: x[1], reverse=True))
        form.text.data = ''

    return render_template('index.html', form=form, messages=messages)

@app.route('/umkb',  methods=['GET', 'POST'])
def umkb():
    form = RequestForm()
    messages = None

    if form.validate_on_submit():
        messages = form.text.data
        messages = post_pars_concept(messages)
        print(messages)
        messages = recognizerDiseaseConcepts(messages)
        messages = dict(sorted(messages.items(), key=lambda x: x[1], reverse=True))
        form.text.data = ''

    return render_template('umkb.html', form=form, messages=messages)

@app.route('/analytics',  methods=['GET', 'POST'])
def analytics():
    return render_template('analytics.html')

@app.route('/information',  methods=['GET', 'POST'])
def information():
    return render_template('information.html')



# @app.route('/greeting', methods=['GET', 'POST'])
# def greeting():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('greeting.html', form=form, name=name)

# def index():
#     form = RequestForm()
#     messages = ''
#     if form.validate_on_submit():
#         messages = form.text.data
#         print(messages)
#         return redirect(url_for('index', form=form))
#
#     if request.method == 'POST':
#         messages = request.form.get('text')
#     return render_template("index.html", title="Главная страница", form=form)

# @app.route('/request', methods=['POST'])
# def index():
#     form = RequestForm()
#     if form.validate_on_submit():
#         symptom_text = request.form[RequestForm.text]
#         print(symptom_text)
#         # result_list = recognize_symptoms(route, symptom_text, True)
#         return render_template('index.html', messages=symptom_text)
#     return render_template("index.html", title="Главная страница", form=form)

# url = 'https://cs.socmedica.com/api/pars/ParsingConcept'
#
#         param = {'key': '9244f7d34ca284b1',
#                  'lib': [25],
#                  'text': session['messages']
#                  }
#
#         response = requests.post(url, param)
#         outs = response.json()
#         print(outs)
#
#         conceptName = []
#         conceptId = []
#         conceptCh = []
#
#         for out in outs:
#             # print(out['nameConcept'])
#             # print(out['idConcept'])
#             # print(out['id'])
#             # print(out['chance'])
#             conceptName.append(out['nameConcept'])
#             conceptId.append(out['idConcept'])
#             conceptCh.append(out['chance'])
#
#         diagnosis = recognizerDisease(conceptId)
#
#         result = {}
#         for keys, values in diagnosis.items():
#             result[keys] = round(values, 2)
# #
# def index():
#     form = RequestForm()
#     if form.validate_on_submit():
#         session['messages'] = form.text.data
#         session['messages'] = recognizerDisease(session['messages'])
#         form.text.data = ''
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, messages=session.get('messages'))
