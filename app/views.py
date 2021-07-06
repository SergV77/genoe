from flask import render_template, redirect, session, request, url_for, flash
from app import app
from . import forms
from .forms import RequestForm, NameForm
from .recognizerDisease import *



@app.route('/',  methods=['GET', 'POST'])
def index():
    form = RequestForm()
    if form.validate_on_submit():
        session['messages'] = form.text.data
        url = 'https://cs.socmedica.com/api/pars/ParsingConcept'

        param = {'key': '9244f7d34ca284b1',
                 'lib': [25],
                 'text': session['messages']
                 }

        response = requests.post(url, param)
        outs = response.json()
        print(outs)

        conceptName = []
        conceptId = []
        conceptCh = []

        for out in outs:
            # print(out['nameConcept'])
            # print(out['idConcept'])
            # print(out['id'])
            # print(out['chance'])
            conceptName.append(out['nameConcept'])
            conceptId.append(out['idConcept'])
            conceptCh.append(out['chance'])

        diagnosis = recognizerDisease(conceptId)

        result = {}
        for keys, values in diagnosis.items():
            result[keys] = round(values, 2)

        session['messages'] = result
        form.text.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=session.get('messages'))




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

