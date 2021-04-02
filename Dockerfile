FROM python:3.9.2-slim-buster

LABEL maintainer="lucky.wirasakti@icloud.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /core/
COPY . /core/

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

RUN useradd user
RUN chown -R user:user /core/

EXPOSE 8000
USER user

ENTRYPOINT ["sh","entrypoint.sh"]
