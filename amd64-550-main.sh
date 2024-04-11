#! /bin/bash
DRIVER_VERSION_MAJOR="550"
DRIVER_VERSION_FULL="550.67"
DEBIAN_FRONTEND=noninteractive

# Setup build dir
mkdir -p ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR
cp -rvf ./debian-$DRIVER_VERSION_MAJOR ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR/debian
cp -rvf ./$DRIVER_VERSION_MAJOR ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR/
cd ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR/
cd ./debian
../../gen-amd64-control-550.py
cd ../

# Get nvidia run file
wget https://us.download.nvidia.com/XFree86/Linux-x86_64/$DRIVER_VERSION_FULL/NVIDIA-Linux-x86_64-$DRIVER_VERSION_FULL.run -O nvidia-installer.run
chmod +x nvidia-installer.run

# Get build deps
apt-get build-dep ./ -y

# Build package
dpkg-buildpackage --no-sign

# Move the debs to output
cd ../
mkdir -p ./output
mv ./*.deb ./output/
