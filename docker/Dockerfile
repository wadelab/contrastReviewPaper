FROM rocker/verse:4.2.2

RUN apt-get update -qq
RUN apt-get -y install cmake
RUN apt-get -y --no-install-recommends install libglu1-mesa-dev
RUN apt-get -y install libxml2-dev
RUN apt-get -y install ghostscript
RUN apt-get -y install libxt-dev
RUN apt-get -y install git
RUN apt-get -y install -y libpython3-dev
RUN apt-get -y install python3-pip
RUN apt-get -y install jupyter

RUN pip3 install numpy
RUN pip3 install scipy
RUN pip3 install matplotlib
RUN pip3 install scikit-learn

RUN install2.r –error \
--deps TRUE \
quarto \
reticulate

RUN R 'reticulate::use_python("/usr/bin/python3")'