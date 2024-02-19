## Use the official Python image as the base image
#FROM python:3.11.7-slim
## Set the working directory in the container
#WORKDIR /backend
## Copy the requirements file into the container
#COPY requirements.txt .
## Install dependencies
#RUN pip install -r requirements.txt
##copy the rest of the backend into the container
#COPY . .
## Run the app
#CMD ["uvicorn", "main:app", "--reload"]
#
#EXPOSE 8000

FROM python:3.11.7-slim
WORKDIR /app
COPY ./source/ source/
COPY ./main.py main.py
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["sh", "-c", "pytest test.py || true && python main.py"]
#CMD ["uvicorn", "main:app", "--reload"]


