# Begin Django REST API
```
py -m venv .venv

.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip

pip install django

django-admin startproject mystore

cd mystore

py manage.py runserver 4097

py manage.py migrate

py manage.py startapp product

python manage.py makemigrations

py manage.py migrate

pip install djangorestframework

pip install django-cors-headers


```

## Create React App
```
# npm 7+, extra double-dash is needed:
npm create vite@latest my-react-app -- --template react-ts
cd my-react-app
npm install
npm run dev
```