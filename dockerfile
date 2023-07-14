FROM amazonlinux:2
RUN amazon-linux-extras install epel -y && \
    yum update -y && \
    yum install -y python3 python3-pip tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Phnom_Penh /etc/localtime && \
    rm -rf /var/cache/yum && \
    yum clean all

# Set Python version
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the current directory contents into the container
COPY . /app

WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

CMD gunicorn --workers=4 -b 0.0.0.0:8080 'run:app'
