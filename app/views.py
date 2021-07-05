from flask import render_template, redirect, request, url_for
from app import app
from . import forms
from .forms import RequestForm

@app.route('/')
@app.route('/index',  methods=['GET', 'POST'])
def index():
    form = RequestForm()
    if request.method == "POST":
        messages = ''
        if form.validate_on_submit():
            return f'''<h1> Welcome {form.text.data} </h1>'''
    return render_template("index.html", form=form)



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

@app.route('/test', methods=['POST'])
def test():
    symptoms_list = request.json['symptom']

    result = {'болезнь1': 0.9, 'болезнь2': 0.1}
    return result