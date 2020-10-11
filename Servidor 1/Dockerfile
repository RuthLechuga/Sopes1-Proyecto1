FROM python

WORKDIR /code/

RUN pip3 install --upgrade pip
RUN pip3 install  pymongo
RUN pip3 install Flask
RUN pip3 install Flask-PyMongo
RUN pip3 install requests
RUN pip3 install flask-cors

EXPOSE 5000
ADD ./app/* /code/
COPY ./app/* /code/
CMD python run.py
