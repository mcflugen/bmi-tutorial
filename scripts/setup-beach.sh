VERSION="2015-27-04"
PREFIX="/home/csdms/wmt/bmi-tutorial"

PATH=$PREFIX/bin:$PATH
PATH=$PREFIX/local/bin:$PATH
PATH=$PREFIX/opt/conda/envs/wmt/bin:$PATH
export PATH

PYTHONPATH=$PREFIX/local/lib/python2.7/site-packages
PYTHONPATH=$PREFIX/lib/python2.7/site-packages:$PYTHONPATH
PYTHONPATH=$PREFIX/opt/conda/envs/wmt/lib/python2.7/site-packages:$PYTHONPATH
PYTHONPATH=$PREFIX/opt/conda/envs/wmt/lib/python2.7:$PYTHONPATH
PYTHONPATH=$PREFIX/local/Cellar/cca-spec-babel/0.8.6/lib/cca-spec-babel-0_8_6-babel-1.4.0/python2.7/site-packages:$PYTHONPATH
PYTHONPATH=$PREFIX/local/Cellar/babel/1.4.0/lib/python2.7/site-packages:$PYTHONPATH
PYTHONPATH=$PREFIX/csdms/install/lib/python2.7/site-packages:$PYTHONPATH
export PYTHONPATH

LD_LIBRARY_PATH=$PREFIX/local/lib
LD_LIBRARY_PATH=$PREFIX/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=$PREFIX/opt/conda/envs/wmt/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=$PREFIX/local/Cellar/babel/1.4.0/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=$PREFIX/csdms/install/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH

export CLASSPATH=$PREFIX/local/lib/java
export SIDL_DLL_PATH=$PREFIX/csdms/install/share/cca
