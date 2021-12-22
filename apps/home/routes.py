# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import requests
import emoji
import requests
import json
from lxml import etree
import re
import pandas as pd
from flask import Flask, render_template, request, url_for,jsonify
import requests
import urllib.parse
import pickle

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

@blueprint.route("/index/predicts", methods=["GET"])
#@login_required
def predicts():
    import numpy as np
    path = 'apps/home/'
    dataset = pd.read_csv(path + 'brfss_final.csv')

    for i in range(2, dataset.shape[1]):
        if not isinstance(dataset[dataset.columns[i]][0], (float, int)):
            dataset[dataset.columns[i]] = dataset[dataset.columns[i]].factorize()[0]

    model = pickle.load(open(path + 'model.pkl', 'rb'))
    n_diseases = 0
    feat_d = ['chccopd1', 'havarth3', 'addepev2', 'chckidny', 'diabete3', 'blind',
              'toldhi2', 'cvdinfr4', 'cvdcrhd4', 'cvdstrk3', 'asthma3', 'chcscncr',
              'chcocncr', 'bphigh4']

    uniqueid = np.int(request.args.get("uniqueid"))

    d = dataset[dataset.ID == uniqueid]
    wtkg = np.float(request.args.get("weight"))
    wtkg3=wtkg * 100
    strength = np.float(request.args.get("strength"))
    exerhmm = np.float(request.args.get("exerhmm1"))
    exact = np.int(request.args.get("exact"))
    sleptim1 = np.float(request.args.get("sleeptime"))
    hlthpln1 = d['hlthpln1'][uniqueid]
    htm4 = d['htm4'][uniqueid]
    marital = d['marital'][uniqueid]
    income2 = d['income2'][uniqueid]
    sex = d['sex'][uniqueid]
    X_ageg5yr = d['X_ageg5yr'][uniqueid]
    chccopd1 = d['chccopd1'][uniqueid]
    if chccopd1==1:
        n_diseases+=1
    havarth3 = d['havarth3'][uniqueid]
    if havarth3==0:
        n_diseases+=1
    addepev2 = d['addepev2'][uniqueid]
    if addepev2==0:
        n_diseases+=1
    chckidny = d['chckidny'][uniqueid]
    if chckidny==1:
        n_diseases+=1
    diabete3 = d['diabete3'][uniqueid]
    if chccopd1==1:
        n_diseases+=1
    blind = d['blind'][uniqueid]
    if chccopd1==1:
        n_diseases+=1
    smokday2 = d['smokday2'][uniqueid]
    toldhi2 = d['toldhi2'][uniqueid]
    if toldhi2==1:
        n_diseases+=1
    cvdinfr4 = d['cvdinfr4'][uniqueid]
    if cvdinfr4==1:
        n_diseases+=1
    cvdcrhd4 = d['cvdcrhd4'][uniqueid]
    if cvdcrhd4==1:
        n_diseases+=1
    cvdstrk3 = d['cvdstrk3'][uniqueid]
    if cvdstrk3==1:
        n_diseases+=1
    asthma3 = d['asthma3'][uniqueid]
    if asthma3==1:
        n_diseases+=1
    chcscncr = d['chcscncr'][uniqueid]
    if chcscncr==1:
        n_diseases+=1
    chcocncr = d['chcocncr'][uniqueid]
    if chcocncr==1:
        n_diseases+=1
    bphigh4 = d['bphigh4'][uniqueid]
    if bphigh4==1:
        n_diseases+=1
    bloodcho = d['bloodcho'][uniqueid]
    X_drnkdy4 = d['X_drnkdy4'][uniqueid]


    int_features = [hlthpln1, htm4, marital, income2, sex,
                    X_ageg5yr, chccopd1, havarth3, addepev2, chckidny, diabete3,
                    blind, smokday2, toldhi2, cvdinfr4, cvdcrhd4, cvdstrk3,
                    asthma3, chcscncr, chcocncr, bphigh4, bloodcho, wtkg3,
                    strength, exerhmm, exact, X_drnkdy4, sleptim1]
    final_features = [np.array(int_features)]

    prediction = model.predict(pd.DataFrame(final_features))

    d = dataset[dataset.ID != uniqueid]
    d_kmeans = d.iloc[:, 2:30]
    d_add = pd.DataFrame(final_features)
    d_add.columns = d_kmeans.columns
    d_kmeans = pd.concat([d_kmeans, d_add]).reset_index(drop=True)

    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=5)

    kmeans.fit(d_kmeans.fillna(0))

    d_kmeans['K_label'] = kmeans.labels_
    groups = d_kmeans[d_kmeans.K_label == d_kmeans.iloc[-1, :].K_label].shape[0]
    groups_ratio = round(100 * groups / (d_kmeans.shape[0]), 1)
    groups_ratio=str(groups_ratio)+'%'

    data_k = d_kmeans[d_kmeans.K_label == d_kmeans.iloc[-1, :].K_label]

    s_sleep = round(np.mean(data_k['sleptim1']), 1)

    s_exerhmm = round(np.mean(data_k['exerhmm']), 1)

    s_strength = round(np.mean(data_k['strength']), 1)

    disease = data_k[feat_d]

    for i in range(disease.shape[1]):
        if disease.columns[i] in ['havarth3', 'addepev2']:
            disease[disease.columns[i]] = np.ones(disease.shape[0]) - disease[disease.columns[i]]

    s_disease = round(np.mean(np.sum(disease, axis=1)), 0)

    s_BMI = round(np.mean(100 * data_k['wtkg3'] / data_k['htm4'] ** 2), 1)

    best = dataset[dataset.genhlth == 3]
    b_sleep = round(np.mean(best['sleptim1']), 1)

    b_exerhmm = round(np.mean(best['exerhmm']), 1)

    b_strength = round(np.mean(best['strength']), 1)

    disease_b = best[feat_d]
    for i in range(disease_b.shape[1]):
        if disease_b.columns[i] in ['havarth3', 'addepev2']:
            disease_b[disease_b.columns[i]] = np.ones(disease_b.shape[0]) - disease_b[disease_b.columns[i]]

    b_disease = round(np.mean(np.sum(disease_b, axis=1)), 0)

    b_BMI = round(np.mean(100 * best['wtkg3'] / best['htm4'] ** 2), 1)

    if sex==1:
        sex_='Male'
    else:
        sex_='Female'
    from random import randint

    BMI=round(100*wtkg3/(htm4)**2,1)

    if BMI<18.5:
        obesity_level='Underweight'
    elif BMI<24.5 and BMI>=18.5:
        obesity_level='Healthy Weight'
    elif BMI < 29.9 and BMI >= 25:
        obesity_level = 'Overweight'
    elif BMI < 40 and BMI >= 30:
        obesity_level = 'Obesity'
    elif BMI >= 40:
        obesity_level = 'Class 3 Obesity'


    if prediction[0]==3:
        pre_score=80+randint(0, 19)
        prediction_level='Excellent'
    elif prediction[0]==2:
        pre_score=60+randint(0, 19)
        prediction_level = 'Very good'
    elif prediction[0] == 0:
        pre_score = 40 + randint(0, 19)
        prediction_level = 'Good'
    elif prediction[0] == 1:
        pre_score = 20 + randint(0, 19)
        prediction_level = 'Fair'
    elif prediction[0] == 4:
        pre_score = 0 + randint(0, 19)
        prediction_level = 'Poor'

    if b_sleep>=sleptim1:
        sleep_tip='increase your sleep time'
    else:
        sleep_tip = 'decrease your sleep time'

    if b_exerhmm>=exerhmm or b_strength>strength:
        exer_tip='increase your aerobic or anaerobic exercise time'
    else:
        exer_tip = 'decrease your aerobic or anaerobic exercise time'

    if b_BMI>=BMI:
        bmi_tip='gain weight and increase your BMI'
    else:
        bmi_tip = 'lose weight and reduce your BMI'


    if X_ageg5yr==0:
        age='55 to 59'
    elif X_ageg5yr==1:
        age='60 to 64'
    elif X_ageg5yr==2:
        age='50 to 54'
    elif X_ageg5yr==3:
        age='65 to 69'
    elif X_ageg5yr==4:
        age='45 to 49'
    elif X_ageg5yr==5:
        age='35 to 39'
    elif X_ageg5yr==6:
        age='40 to 44'
    elif X_ageg5yr==7:
        age='70 to 74'
    elif X_ageg5yr==8:
        age='30 to 34'
    elif X_ageg5yr==9:
        age='75 to 79'
    elif X_ageg5yr==10:
        age='25 to 29'
    elif X_ageg5yr==11:
        age='18 to 24'
    elif X_ageg5yr==12:
        age='80 or older'
    return render_template("home/predicts.html",age=age,sleep_tip=sleep_tip,exer_tip=exer_tip,bmi_tip=bmi_tip,wtkg=wtkg,b_BMI=b_BMI,b_disease=b_disease,b_strength=b_strength,b_exerhmm=b_exerhmm,b_sleep=b_sleep,s_sleep=s_sleep,s_exerhmm=s_exerhmm,s_strength=s_strength,s_disease=s_disease,s_BMI=s_BMI,groups_ratio=groups_ratio,groups=groups,obesity_level=obesity_level,prediction_level=prediction_level,sex=sex_ ,segment='index',BMI=BMI,sleptim1=sleptim1,exerhmm1=exerhmm,strength=strength,n_diseases=n_diseases,prediction_text=pre_score)


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
