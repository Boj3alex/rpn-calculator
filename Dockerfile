FROM python:3

ADD app/evaluation.py /

CMD ["python","./evaluation.py"]
