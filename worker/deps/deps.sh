#!/bin/bash

set -e

yum update -y
yum -y install \
    gcc \
    gcc-c++ \
    gzip \
    libjpeg-devel \
    libpng-devel \
    libtiff-devel \
    libgcc \
    make \
    python36 \
    tar \
    wget

# Install Imagemagick
IMAGE_MAGICK=ImageMagick-7.0.8-8
wget http://www.imagemagick.org/download/$IMAGE_MAGICK.tar.gz
tar -xzvf $IMAGE_MAGICK.tar.gz
cd $IMAGE_MAGICK
./configure \
    --enable-shared=no \
    --enable-static=yes
make && make install

# Install python deps
pip-3.6 install --upgrade pip
