improved WSalGAN

###Datasets
MIT300:(http://saliency.mit.edu/BenchmarkIMAGES.zip)
SALCION:(http://lsun.cs.princeton.edu/2016/)

###preparing
implemented in [Lasagne], which at its time is developed over [Theano].
pip install -r requirements.txt
set the dataset input and output paths in scripts/constants.py

### Training
THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32,lib.cnmem=0.8,optimizer_including=cudnn python 02-train.py

###predict
THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32,lib.cnmem=0.8,optimizer_including=cudnn python 03-predict.py
