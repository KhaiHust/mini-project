FROM amazon/aws-lambda-python:3.9

RUN pip install --upgrade pip
RUN pip install poetry

RUN curl -fsSL https://rpm.nodesource.com/setup_16.x | bash - && yum install -y nodejs

ENV POETRY_VIRTUALENVS_IN_PROJECT=true