***API доступа к БД на Django Rest Framework***

**[Использованая таблица из реестра Министерства культуры](https://opendata.mkrf.ru/opendata/7705851331-patriot_music)**  

**[Документация к API на SwaggerHUB](https://app.swaggerhub.com/apis/PROSKURINDIMA16/minkult_api/v1)**  
(Также лежит в данном репозитории в .yaml формате)  

Для реализации API кроме DRF была использована библиотека *drf-writable-nested* для поддержки полного функционала API для вложенных сущностей many-to-many.  
На всех страницах реализована пагинация с лимитом в 25 записей, поиск по названию или ключевым словам, а также в для хендлера songs имеется фильтрация записей по параметрам.

*[Docker-образ с сервером и встроенной в него парсером и БД с sqlite3](https://hub.docker.com/r/ohlomonchick/minkult_django/tags)*
```
docker pull ohlomonchick/minkult_django:latest
```
Образ также поддерживает работу с PostgerSQL, для чего имеет в себе переменную окружения *POSTGRES*, по умолчанию равную 0.  
При *POSTGRES=1* будет использовать движок Postgres и подлючаться к *POSTGRES_HOST*.

Пример конфигурации сети с PostgreSQL в docker-compose.yaml





