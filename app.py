import os
import requests
from flask import Flask, render_template, request
from main import *
import numpy as np


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    data = ''
    stats= []
    t_title = ''
    signif = ''


    if request.method == "POST":
        # get url that the user has entered
        try:
            data1 = request.form['data1']
            data2 = request.form['data2']
            tailed = request.form['tail']
            signif = request.form['significance']

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
            # True,'small', n1, n2,u_05, stat_a, effect, larger, data1, data2
            show_sig, sample_siz, n1, n2,u_critical, u_stat, effect_siz, huger, d1, d2 = outcomes
            
            # data1 = [a for i in data1.split(',') for a in i.split(' ') if len(a)>0]
            # data2 = [a for i in data2.split(',') for a in i.split(' ') if len(a)>0]
            data = ['Data 1 :\n\n' + (', ').join([str(d) for d in d1]), 'Data 2 :\n' + (', ').join([str(d) for d in d2])]
        
            stats = [('Sample Size', n1, n2),('Mean', round(np.mean(d1),3), round(np.mean(d2),3)), 
                 ('Standard Deviation', round(np.std(d1), 3), round(np.std(d2),3)), ('Median', np.median(d1), np.median(d2))]


            if show_sig:
                s = 'Yes'
            else: s = 'No'
            if sample_siz == 'Small':
                items_name = ['Significance', 
                              'Sample Size', 
                              'U Critical', 
                              'Sample Stat', 'Effect Size', 
                              'Larger Group']
            else:
                items_name = ['Significance', 
                              'Sample Size', 
                              'P Value', 
                              'Sample Stat', 'Effect Size', 
                              'Larger Group']
                u_critical = round(u_critical, 4)
            out = [s, sample_siz, u_critical, u_stat, round(effect_siz, 3), huger]
            results = zip(items_name, out)
        except:
            errors.append(outcomes)



    return render_template('index.html', errors=errors,Datas=data,Stats=stats, Tails=t_title, Sig_level=signif, results=results)


if __name__ == '__main__':
    app.run()