#!/bin/bash

set -e

yum update -y
yum -y install \
    emacs \
    gcc \
    gcc-c++ \
    gzip \
    ImageMagick-devel \
    libjpeg-devel \
    libpng-devel \
    libtiff-devel \
    libgcc \
    make \
    python36 \
    tar \
    wget


# sh install_imagemagick.sh
# Install python deps
pip-3.6 install --upgrade pip
