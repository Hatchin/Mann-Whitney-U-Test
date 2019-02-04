import os
import requests
from flask import Flask, render_template, request
from main import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    data = ''
    t_title = ''
    signif = ''


    if request.method == "POST":
        # get url that the user has entered
        try:
            data1 = request.form['data1']
            data2 = request.form['data2']
            tailed = request.form['tail']
            signif = request.form['significance']

            data1 = [a for i in data1.split(',') for a in i.split(' ') if len(a)>0]
            data2 = [a for i in data2.split(',') for a in i.split(' ') if len(a)>0]
            data = [data1, data2]


            if tailed == 'two':
                t_title = 'Two Tailed'
            elif tailed == 'less':
                t_title = 'One Tailed (smaller)'
            else:
                t_title = 'one Tailed (larger)'
            

            
        except:
            errors.append(
                "Unable to get necessary input, please try again."
            )
        outcomes = mann_whitney(data1, data2, tail=tailed, significant_level=signif)

        try:
            show_sig, sample_siz, n1, n2,u_critical, u_stat, effect_siz, huger = outcomes
            if show_sig:
                s = 'Yes'
            else: s = 'No'
            if sample_siz == 'small':
                items_name = ['Sig Diff', 
                              'Sample Size', 
                              'n1', 'n2', 'U Critical', 
                              'Sample Stat', 'Effect Size', 
                              'Larger Group']
            else:
                items_name = ['Sig Diff', 
                              'Sample Size', 
                              'n1', 'n2', 'P Value', 
                              'Sample Stat', 'Effect Size', 
                              'Larger Group']
            out = [s, sample_siz, n1, n2,u_critical, u_stat, effect_siz, huger]
            results = zip(items_name, out)
        except:
            errors.append(outcomes)



    return render_template('index.html', errors=errors,Datas=data, Tails=t_title, Sig_level=signif, results=results)


if __name__ == '__main__':
    app.run()