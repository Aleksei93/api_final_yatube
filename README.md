# api_final
Програмный интерфейс для обмена данными (API) проекта yatube.

## :books:Описание:
api_final позвозяет взаимодествовать с базами данных проекта а именно:

  - Получать данные о постах, группах, подписчиках, комментариях (при наличии соотвествующих прав);
  - Создавать новые посты (при наличии соотвествующих прав);
  - Редактировать и удалять свои посты (После прохождения авторизации);
  - Подписываться на других пользователей (После прохождения авторизации);
  - Получить, обновить и проверить JWT-токен;


## :hammer_and_wrench: Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Aleksei93/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

## :performing_arts: Примеры запросов:

  - GET http://127.0.0.1:8000/api/v1/posts/;
  - POST http://127.0.0.1:8000/api/v1/posts/;
  - GET http://127.0.0.1:8000/api/v1/posts/{id}/;
  - PUT http://127.0.0.1:8000/api/v1/posts/{id}/;
  - PATH http://127.0.0.1:8000/api/v1/posts/{id}/;
  - DELETE http://127.0.0.1:8000/api/v1/posts/{id}/;
  - GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/;
  - POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/;
  - GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/;
  - PUT http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/;
  - PATH http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/;
  - DELETE http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/;
  - GET http://127.0.0.1:8000/api/v1/groups/;
  - GET http://127.0.0.1:8000/api/v1/groups/{id}/;
  - GET http://127.0.0.1:8000/api/v1/follow/;
  - POST http://127.0.0.1:8000/api/v1/follow/;
  - POST http://127.0.0.1:8000/api/v1/jwt/create/;
  - POST http://127.0.0.1:8000/api/v1/jwt/refresh/;
  - POST http://127.0.0.1:8000/api/v1/jwt/verify/
  

## :satellite: Технологии: 
  
  - Python
  - Django REST Framework
  - API REST
  - Postman
  - Simple-JWT
  
  
## :office_worker: Об авторе: 
  
Автор проекта [Плотников Алексей](https://github.com/Aleksei93).