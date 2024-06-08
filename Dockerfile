FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip python3-notebook
RUN mkdir /home/app/
WORKDIR /home/app/
ENTRYPOINT ["jupyter","notebook","--allow-root","--no-browser","--port=8888", "--ip=0.0.0.0","--NotebookApp.token=''","--NotebookApp.password=''"]