# Fakes
## Find fakes and scam websites
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Project for finding fake and malicious websites.
	
## Technologies
Project is created with:
* Django version: 4.1.5
* Scrapy version: 2.7.1
* Scikit-learn version: 0.0.post1

## Setup *(windows)*
1. Run ```pipenv shell``` in the directory
2. ```pip install -r requirements.txt```
3. ```python manage.py makemigrations```
4. ```python manage.py migrate --run-syncdb```
5. ```python manage.py runserver ```
6. Run second **cmd** for **Scrapy**
```cd scrapy_app```
7. ```scrapyd```

Now access the website: **127.0.0.1:8000**

