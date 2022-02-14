# Install stablebaseline3
## Create new conda env with torch GPU - conda create -n torch_gpu python=3.8.10
## Install torch GPU - conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c conda-forge
## pip install stable-baselines3[extra]
## Fix 'swig.exe' missing error - https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed
## pip install gym[box2d]
