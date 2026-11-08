# Will be using this for the Colab and Baremetal check

import sys, platform
print("Python", sys.version.split()[0], "on", platform.platform())
try:
    import torch
    print("PyTorch", torch.__version__, "| CUDA available:", torch.cuda.is_available())
except ImportError:
    print("PyTorch not installed here (fine for a local laptop).")

import sklearn, numpy, pandas
print("scikit-learn", sklearn.__version__, "| numpy", numpy.__version__,
    "| pandas", pandas.__version__)