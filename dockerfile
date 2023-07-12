#Use an official python runtime as a parent image
FROM python:3.11.4-slim

RUN apt-get update
RUN ln -fs /usr/share/zoneinfo/Asia/Phnom_Penh /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get update

#Copy the current directory contents into container /
COPY . /app

WORKDIR /app

#Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Make port to the world outside this container
EXPOSE 88

CMD gunicorn --workers=13 --threads=6 -b 0.0.0.0:88 'run:app'