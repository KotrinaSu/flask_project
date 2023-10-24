from flask import render_template, request, redirect, url_for

from app import app, db
from app.forms import ContactForm

from app.models import Vyras



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ladies')
def ladies():
    return render_template('ladies.html')


@app.route('/men')
def men():
    vyrai = Vyras.query.all()
    return render_template('men.html', vyrai=vyrai)


# @app.route('/add_mens', methods=['GET', 'POST'])
# def add_mens():
#     if request.method == "POST":
#         print(request.form)
#         vardas = request.form['vardas']
#         amzius = request.form['amzius']
#         ugis = request.form['ugis']
#         svoris = request.form['svoris']
#         vyrai[vardas] = {
#                 'amzius': amzius,
#                 'ugis': ugis,
#                 'svoris': svoris,
#             }
#         return redirect(url_for('men'))
#     return render_template('add_mens.html')



@app.route('/men/<string:title>')
def vardas(title):
    return render_template('vardas.html', title=title)



@ app.route('/add_mens', methods=['GET', 'POST'])
def add_mens():
    form = ContactForm()
    if form.validate_on_submit():
        # vyrai[form.vardas.data] = {
        #                 'amzius': form.amzius.data,
        #                 'ugis': form.ugis.data,
        #                 'svoris': form.svoris.data,
        #             }
        vyras = Vyras(vardas=form.vardas.data, amzius=form.amzius.data, ugis=form.ugis.data, svoris=form.svoris.data)
        db.session.add(vyras)
        db.session.commit()
        return redirect(url_for('men'))
    return render_template('contact_us.html', form=form)






