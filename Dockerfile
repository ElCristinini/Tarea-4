FROM python:3.10-slim

RUN apt update && apt install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY BrazoRobotico.py .
COPY two_joint_robot_custom.urdf .

RUN pip install pybullet numpy

CMD ["python3", "BrazoRobotico.py"]
