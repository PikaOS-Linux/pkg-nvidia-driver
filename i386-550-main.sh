#! /bin/bash
DRIVER_VERSION_MAJOR="550"
DRIVER_VERSION_FULL="550.67"
DRIVER_ARCH="Linux-x86_64"
DEBIAN_ARCH="i386"
DEBIAN_FRONTEND=noninteractive

# Setup build dir
mkdir -p ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR
cp -rvf ./$DRIVER_VERSION_MAJOR/debian-$DRIVER_VERSION_MAJOR ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR/debian
cp -rvf ./$DRIVER_VERSION_MAJOR/extra_files ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR/
cd ./nvidia-graphics-drivers-$DRIVER_VERSION_MAJOR/
cd ./debian
../../$DRIVER_VERSION_MAJOR/gen-$DEBIAN_ARCH-control-$DRIVER_VERSION_MAJOR.py
cd ../

# Get nvidia run file
wget https://us.download.nvidia.com/XFree86/$DRIVER_ARCH/$DRIVER_VERSION_FULL/NVIDIA-$DRIVER_ARCH-$DRIVER_VERSION_FULL.run -O nvidia-installer.run
chmod +x nvidia-installer.run

# Get build deps
apt-get build-dep ./ -y

# Build package
dpkg-buildpackage --no-sign

# Move the debs to output
cd ../
mkdir -p ./output
mv ./*.deb ./output/
