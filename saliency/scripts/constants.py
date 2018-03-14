# Work space directory
HOME_DIR = '/home/mg2015started/saliency/saliency-w-salgan/'

# Path to SALICON raw data
pathToImages = '/home/mg2015started/saliency/salicon_data/images'
pathToMaps = '/home/mg2015started/saliency/salicon_data/saliency'
pathToFixationMaps = '/home/mg2015started/saliency/salicon_data/fixation'

# Path to processed data
pathOutputImages = '/home/mg2015started/saliency/lsun2016/data/salicon/images320x240'
pathOutputMaps = '/home/mg2015started/saliency/lsun2016/data/salicon/saliency320x240'
pathToPickle = '/home/mg2015started/saliency/scratch-local/salicon_data/320x240'

# Path to pickles which contains processed data
TRAIN_DATA_DIR = '/home/mg2015started/saliency/scratch-local/salicon_data/320x240/trainData.pickle'
VAL_DATA_DIR = '/home/mg2015started/saliency//scratch-local/salicon_data/320x240/validationData.pickle'
TEST_DATA_DIR = '/home/mg2015started/saliency/scratch-local/salicon_data/256x192/testData.pickle'

# Path to vgg19 pre-trained weights
PATH_TO_VGG19_WEIGHTS = '/home/mg2015started/saliency/saliency-w-salgan/vgg19.pkl'

# Input image and saliency map size
INPUT_SIZE = (256, 192)

# Directory to keep snapshots
DIR_TO_SAVE = 'test'
