FROM python:3.5

RUN useradd --user-group --create-home --shell /bin/false app

ENV INSTALL_PATH /isserviceup
RUN mkdir -p $INSTALL_PATH && chown app:app $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

USER app

COPY . .

CMD gunicorn -c "isserviceup/config/gunicorn.py" isserviceup.app:app
