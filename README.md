# QuizProject

## developement 
for developing on this project, first install the packages in **requirements.txt** with the following command :
```bash
pip install -r requirements.txt
```
then make a copy of **sample_settings.ini** to a file named **settings.ini** and fill the environment variables in it correctly\
also don't forget to migrate
```bash
python quiz_project/manage.py migrate
```
then run the following command to run the project :
```bash
python quiz_project/manage.py runserver
```

