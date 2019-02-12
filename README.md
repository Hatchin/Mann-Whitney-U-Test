# Mann-Whitney Web App

A web application for mann whitney test made with Python and Flask. Add solution to test for small sample size (n < 20).

## Demo
https://mannwhitney.herokuapp.com/


![demo](https://github.com/Hatchin/Mann-Whitney-Extension/blob/master/demo.png)

## Handbook

### Data Summary

Information summary for two groups of data, including sample size (number of data samples), mean, standard deviation and median for each group. 

### Test Result

`Sig Diff`: whether or not the two sample data are from different distribution at the custom significant level

`Sample Size`: if n <= 20, then small sample size; else large sample size

`U-critical` or `P Value`: when small sample size, display the U critical value at the significant level; when large sample size, display the P Value computed from U stat

`Sample Stat`: U stat computed from the data samples

`Effect Size`:  a value to measure how large the difference is between the two data groups. 

Formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_phv&space;EffectSize&space;=&space;1&space;-&space;\frac{2\times&space;U_{stat}}{n1\times&space;n2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;EffectSize&space;=&space;1&space;-&space;\frac{2\times&space;U_{stat}}{n1\times&space;n2}" title="EffectSize = 1 - \frac{2\times U_{stat}}{n1\times n2}" /></a>

`Larger Group`: indicates which group has a higher value

## Versions
Flask==0.12.2

Pandas>=0.21.1

Numpy>=1.14.3

Scipy>=1.1.0

Request>=2.7.0

## Installation
Change to app directory, use `virtualenv` create and activate virtual enviroment.  
Then use `pip` to install requirements：  
```
pip install -r requirements.txt
```
Run:  
```
python app.py runserver
```

Go to http://127.0.0.1:5000/



