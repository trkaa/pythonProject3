FROM ubuntu:latest
LABEL authors="trkaa"
FROM python:3-slim
RUN apt-get clean && apt-get update
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/trkaa/pythonProject3
RUN pip install -r /pythonProject3/requirements.txt
ENV TOKEN="6898273558:AAFt530TVrvjZqJ2C6umibp6Gj4LyFgPyYc"
WORKDIR /pythonProject3
RUN echo "git pull && python3 main.py" > start2.sh
CMD [ "bash", "start2.sh" ]
ENTRYPOINT ["top", "-b"]