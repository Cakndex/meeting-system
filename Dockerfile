FROM python:3.9-slim

EXPOSE 8000
WORKDIR /service

# install requirements
COPY requirements.txt .
RUN pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn
RUN pip install --no-cache-dir --upgrade -r requirements.txt \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN rm requirements.txt


COPY app ./app/

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000