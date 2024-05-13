FROM python
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements-unix.txt
CMD uvicorn main:app --reload
