FROM python:3-onbuild
COPY . /usr/src/app
CMD ["python", "./product/api.py"]
