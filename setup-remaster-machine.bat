@echo off

echo checking out sd-webui-controlnet
pushd %~dp0
cd extensions
git clone https://github.com/Mikubill/sd-webui-controlnet.git
cd sd-webui-controlnet
git checkout 54f7c64b4dc4a4206e76a152651d5f0b0fac248f
popd

echo creating venv..
if not exist %~dp0venv\Scripts\python.exe (
    python -m venv %~dp0venv
)

echo installing dependencies..
%~dp0venv\Scripts\python.exe -m ensurepip
%~dp0venv\Scripts\python.exe -m pip install mediapipe
%~dp0venv\Scripts\python.exe -m pip install svglib
%~dp0venv\Scripts\python.exe -m pip install fvcore
%~dp0venv\Scripts\python.exe -m pip install opencv-python

echo downloading models...
%~dp0venv\Scripts\python.exe %~dp0download-models.py