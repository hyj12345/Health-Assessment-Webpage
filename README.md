# Health-Assessment-Webpage


[![INFO](https://img.shields.io/badge/YJ-Homepage-orange)](https://github.com/hyj12345/Health-Assessment-Webpage)




Health Assessment Webpage is the final project of BIS634, which helps to predict the daily health of the user. The webpage is based on the following three websites. They are [flask-dashboard-atlantis-dark](https://github.com/app-generator/flask-dashboard-atlantis-dark), [chartjs](https://www.chartjs.org/) and [Bootstrap4](https://bootstrap-flask.readthedocs.io/en/stable/)


- [Directory Structure](#directory-structure)
- [Download and Run the webpage](#download-and-run-the-webpage)
- [Register and Login](#register-and-login)
- [Data Visualisation Webpage](#data-visualisation-webpage)
- [Prediction Webpage](#prediction-webpage)
- [Profile page](#profile-page)
- [Final Report and Slide](#report-and-slide)






## Directory Structure


```bash
.
├── CHANGELOG.md
├── Dockerfile
├── LICENSE.md
├── Procfile
├── __pycache__
│   └── run.cpython-39.pyc
├── apps
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   └── config.cpython-39.pyc
│   ├── authentication
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── util.py
│   ├── config.py
│   ├── db.sqlite3
│   ├── home
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── brfss_final.csv
│   │   ├── data_proprocessing.py
│   │   ├── model.pkl
│   │   ├── model.py
│   │   └── routes.py
│   ├── static
│   │   ├── Bean.gif
│   │   └── assets
│   └── templates
│       ├── accounts
│       ├── home
│       ├── includes
│       └── layouts
├── docker-compose.yml
├── gunicorn-cfg.py
├── media
│   ├── flask-dashboard-atlantis-dark-card-low.jpg
│   ├── flask-dashboard-atlantis-dark-card-low.png
│   ├── flask-dashboard-atlantis-dark-card.jpg
│   ├── flask-dashboard-atlantis-dark-card.png
│   ├── flask-dashboard-atlantis-dark-content-image-low.png
│   ├── flask-dashboard-atlantis-dark-content-image.png
│   ├── flask-dashboard-atlantis-dark-intro.gif
│   ├── flask-dashboard-atlantis-dark-screen-1-low.png
│   ├── flask-dashboard-atlantis-dark-screen-1.png
│   ├── flask-dashboard-atlantis-dark-screen-2-low.png
│   ├── flask-dashboard-atlantis-dark-screen-2.png
│   ├── flask-dashboard-atlantis-dark-screen-3-low.png
│   ├── flask-dashboard-atlantis-dark-screen-3.png
│   ├── flask-dashboard-atlantis-dark-screen-4-low.png
│   ├── flask-dashboard-atlantis-dark-screen-4.png
│   ├── flask-dashboard-atlantis-dark-screen-login-low.png
│   ├── flask-dashboard-atlantis-dark-screen-login.png
│   ├── flask-dashboard-atlantis-dark-screen-low.png
│   ├── flask-dashboard-atlantis-dark-screen-register-low.png
│   ├── flask-dashboard-atlantis-dark-screen-register.png
│   └── flask-dashboard-atlantis-dark-screen.png
├── nginx
│   └── appseed-app.conf
├── package.json
├── requirements-mysql.txt
├── requirements-pgsql.txt
├── requirements.txt
├── run.py
└── runtime.txt

```


## Download and Run the webpage

```python
git clone https://github.com/hyj12345/Health-Assessment-Webpage.git
cd Health-Assessment-Webpage
pip3 install -r requirements.txt
export FLASK_APP=run.py
flask run
```

## Register and Login

You can enter **any** information to **register** and **log in**.



![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/12801640201087_.pic.jpg)


![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/12791640200820_.pic.jpg)


## Data Visualisation Webpage

This page focuses on the visualisation of the BRFSS-2013 dataset.

![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.25.17.png)
![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.25.24.png)
![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.25.31.png)


Enter your personal unique id（0-489791） and health information in this panel and click to make a prediction.


![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.27.14.png)


## Prediction Webpage

This page shows the final prediction results and you can see the prediction scores, data visualisation and health recommendations for the results

![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.27.33.png)
![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.27.40.png)
![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.27.46.png)


You can click on the link below the Tips to go to a more specialist website for help.
![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.42.16.png)
![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.42.26.png)
![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.42.35.png)


## Profile page
The last page is the user information page

![image-20211031113158927](https://github.com/hyj12345/Health-Assessment-Webpage/blob/main/png/%E6%88%AA%E5%B1%8F2021-12-22%2014.27.53.png)


## Report and Slide
You can view my [final report and slide](https://github.com/hyj12345/Health-Assessment-Webpage/tree/main/Report) here.

