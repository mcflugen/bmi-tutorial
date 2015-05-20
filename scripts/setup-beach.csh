set VERSION="2015-27-04"
set PREFIX="/home/csdms/wmt/bmi-tutorial"

setenv PATH $PREFIX/bin:$PATH
setenv PATH $PREFIX/local/bin:$PATH
setenv PATH $PREFIX/opt/conda/envs/wmt/bin:$PATH

setenv PYTHONPATH $PREFIX/local/lib/python2.7/site-packages
setenv PYTHONPATH $PREFIX/lib/python2.7/site-packages:$PYTHONPATH
setenv PYTHONPATH $PREFIX/opt/conda/envs/wmt/lib/python2.7/site-packages:$PYTHONPATH
setenv PYTHONPATH $PREFIX/opt/conda/envs/wmt/lib/python2.7:$PYTHONPATH
setenv PYTHONPATH $PREFIX/local/Cellar/cca-spec-babel/0.8.6/lib/cca-spec-babel-0_8_6-babel-1.4.0/python2.7/site-packages:$PYTHONPATH
setenv PYTHONPATH $PREFIX/local/Cellar/babel/1.4.0/lib/python2.7/site-packages:$PYTHONPATH
setenv PYTHONPATH $PREFIX/csdms/install/lib/python2.7/site-packages:$PYTHONPATH

setenv LD_LIBRARY_PATH $PREFIX/local/lib
setenv LD_LIBRARY_PATH $PREFIX/lib:$LD_LIBRARY_PATH
setenv LD_LIBRARY_PATH $PREFIX/opt/conda/envs/wmt/lib:$LD_LIBRARY_PATH
setenv LD_LIBRARY_PATH $PREFIX/local/Cellar/babel/1.4.0/lib:$LD_LIBRARY_PATH
setenv LD_LIBRARY_PATH $PREFIX/csdms/install/lib:$LD_LIBRARY_PATH

setenv CLASSPATH $PREFIX/local/lib/java
setenv SIDL_DLL_PATH $PREFIX/csdms/install/share/cca
