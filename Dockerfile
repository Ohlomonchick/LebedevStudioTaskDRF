FROM python:3.11-bookworm

COPY ./minkult_django ./app
COPY ./requirements.txt ./app

WORKDIR /app

RUN pip install pip --upgrade
RUN pip install wheel --upgrade
RUN pip install pip -r requirements.txt
RUN chmod +x entrypoint.sh

EXPOSE 8000

CMD [ "/app/entrypoint.sh" ]