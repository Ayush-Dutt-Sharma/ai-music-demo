FROM runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04

RUN git clone https://github.com/SociallyIneptWeeb/AICoverGen.git
WORKDIR /AICoverGen
COPY ./src/main01_runpod.py ./src/main.py

COPY ./src/download_runpod.py download_runpod.py
COPY ./src/runpod_process_start.py runpod_process_start.py
COPY rvc_models rvc_models

RUN pip install -q -r requirements.txt && apt update && apt install sox &&  apt-get install ffmpeg
RUN python src/download_models.py


