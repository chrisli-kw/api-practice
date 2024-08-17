FROM ubuntu:22.04

# Install programs
RUN mkdir -p /root/API-Practice && \
    apt-get update && \
    apt-get install -y \
    curl \
    bash\
    python3.11 \
    python3-pip && \
    apt-get remove --purge -yqq gpg 

# Copy files
COPY . /root/API-Practice

# Update pip and install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /root/API-Practice/requirements.txt && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

EXPOSE 8080
WORKDIR /root/API-Practice
CMD ["python3", "/root/API-Practice/app.py"]
