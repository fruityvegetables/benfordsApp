FROM python:3

ADD benfordsProduction.py /

RUN pip install requests flask matplotlib numpy pandas

CMD [ "python", "./benfordsProduction.py"]


