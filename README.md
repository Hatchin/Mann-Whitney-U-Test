# Mann-Whitney Web App

The Mann-Whitney U test is a non-parametric test for testing whether two independent data samples come from the same distribution.

This is a web application for Mann-Whitney U test made with Python and Flask. Add solution to test for small sample size (n < 20).

## Table of Contents


1.    [Demo](#Demo)

2.    [Guide](#user-guide)

      1.    [Data Summary](#1.)  
      2.    [Test Result](#2.)   
      3.    [Interpretation](#3.) 

3.    [Installation](#install)

## 1. Demo <a class ="anchor" id="Demo"></a>

https://mannwhitney.herokuapp.com/

![demo](https://github.com/Hatchin/Mann-Whitney-Extension/blob/master/demo.png)

## 2. Guide <a class ="anchor" id="user-guide"></a>

### Data Summary <a class ="anchor" id="1."></a>

Information summary for two groups of data, including sample size (number of data samples), mean, standard deviation and median for each group.    

### Test Result <a class ="anchor" id="2."></a>

`Sig Diff`: whether or not the two sample data are from different distribution at the user-defined significant level

`Sample Size`: if n <= 20, then small sample size; else, large sample size

`U-critical` or `P Value`: when small sample size, return the U critical value at the significant level; when large sample size, return the P Value computed from U stat

`Sample Stat`: U stat computed from the data samples

`Effect Size`:  a value to measure how large the difference is between the two data groups. 

Formula:

<a href="https://www.codecogs.com/eqnedit.php?latex=\fn_phv&space;EffectSize&space;=&space;1&space;-&space;\frac{2\times&space;U_{stat}}{n1\times&space;n2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\fn_phv&space;EffectSize&space;=&space;1&space;-&space;\frac{2\times&space;U_{stat}}{n1\times&space;n2}" title="EffectSize = 1 - \frac{2\times U_{stat}}{n1\times n2}" /></a>

`Larger Group`: indicates which group has a higher value

### Interpretation <a class ="anchor" id="3."></a>
1. Determine whether or not `Sample Size` is small
   1. if n <20 ,then `Small` size;
   2. else, then `Large` size
2. Determine whether or not there is significant difference
   1. If sample size is `Small`, compare `U-critical` and `Sample Stat` : 
      1. if `U-critical` > `Sample Stat`, then there is significant difference (`Sig Diff` = `Yes`);
      2. else, there is no signifcant difference (`Sig Diff` = `No`), end
   2. If sample size is `Large`, compare `P value` and <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a> : 
      1. if `P value` < <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a>, then there is significant difference (`Sig Diff` = `Yes`);
      2. else, there is no signifcant difference (`Sig Diff` = `No`), end
  3. If there is significant difference (`Sig Diff` = `Yes`), `Effect Size` will explain how the large the difference is. The larger `Effect Size`is, the huger difference is. `Larger Group` explicitly indicate the larger group. 
  


## 3. Installation <a class ="anchor" id="install"></a>
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



