
set pythonpath=%~dp0\venv\Scripts\python.exe
%pythonpath% -m ensurepip
%pythonpath% -m pip install mediapipe
%pythonpath% -m pip install svglib
%pythonpath% -m pip install fvcore
%pythonpath% -m pip install opencv-python>=4.8.0
