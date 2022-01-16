FROM 107292555468.dkr.ecr.eu-central-1.amazonaws.com/spark/emr-6.2.0-20210129
USER root

COPY main.py /usr/spark-app/
COPY requirements.txt /usr/spark-app/
COPY src /usr/spark-app/

RUN pip3 install --upgrade pip
RUN pip3 install -r /usr/spark-app/requirements.txt

USER hadoop:hadoop