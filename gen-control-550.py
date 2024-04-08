#! python3

CONTROL_FILE_PREQ = """Source: nvidia-graphics-drivers-{DRIVER_VERSION_MAJOR}
Section: non-free/libs
Priority: optional
Maintainer: Debian NVIDIA Maintainers <pkg-nvidia-devel@lists.alioth.debian.org>
Uploaders:
 Andreas Beckmann <anbe@debian.org>,
 Luca Boccassi <bluca@debian.org>,
Vcs-Browser: https://salsa.debian.org/nvidia-team/nvidia-graphics-drivers
Vcs-Git: https://salsa.debian.org/nvidia-team/nvidia-graphics-drivers.git -b 545
Build-Depends:
 debhelper-compat (= 13),
Build-Depends-Arch:
 dh-sequence-dkms,
 dh-exec,
 libnvidia-egl-wayland1,
 libvulkan1 (>= 1.0.42),
 libxext6,
 po-debconf,
 quilt,
 xz-utils,
 zstd,
 linux-headers-amd64 [amd64] <!nocheck>,
 linux-headers-arm64 [arm64] <!nocheck>,
 linux-headers-powerpc64le [ppc64el] <!nocheck>,
 libglvnd-dev,
Rules-Requires-Root: no
Standards-Version: 4.6.2
Homepage: https://www.nvidia.com
Testsuite: autopkgtest-pkg-dkms
XS-Autobuild: yes

Package: firmware-nvidia-gsp-{DRIVER_VERSION_MAJOR}
Section: non-free-firmware/kernel
Architecture: amd64 arm64
Multi-Arch: foreign
Depends:
    ${misc:Depends}
Provides:
    firmware-nvidia-gsp (= ${binary:Version}),
Conflicts:
    firmware-nvidia-gsp
Description: The GPU System Processor (GSP) was first introduced in the Turing architecture and supports accelerating tasks traditionally performed by the driver on the CPU.
    This package provides the firmware to drive the GSP.

Package: libcuda1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    nvidia-support-{DRIVER_VERSION_MAJOR},
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    libnvidia-ptxjitcompiler1-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    libnvidia-pkcs11-openssl3-{DRIVER_VERSION_MAJOR} (= ${binary:Version}) [amd64],
    ${shlibs:Depends}, ${misc:Depends}
Recommends:
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    nvidia-smi-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    libnvidia-cfg1-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    nvidia-persistenced-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    libcuda1-{DRIVER_VERSION_MAJOR}:i386 (= ${binary:Version}) [amd64],
Suggests:
    nvidia-cuda-mps-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR} (= ${binary:Version})
Provides:
    libcuda.so.1 (= 550),
    libcuda1-any,
    libcuda-5.0-1,
    libcuda-5.0-1-i386 [i386],
    libcuda-5.5-1,
    libcuda-5.5-1-i386 [i386],
    libcuda-6.0-1,
    libcuda-6.0-1-i386 [i386],
    libcuda-6.5-1,
    libcuda-6.5-1-i386 [i386],
    libcuda-7.0-1,
    libcuda-7.5-1,
    libcuda-8.0-1,
    libcuda-9.0-1,
    libcuda-9.1-1,
    libcuda-9.2-1,
    libcuda-10.0-1,
    libcuda-10.1-1,
    libcuda-10.2-1,
    libcuda-11.0-1,
    libcuda-11.1-1,
    libcuda-11.2-1,
    libcuda-11.3-1,
    libcuda-11.4-1,
    libcuda-11.5-1,
    libcuda-11.6-1,
    libcuda-11.7-1,
    libcuda-11.8-1,
    libcuda-12.0-1,
    libcuda-12.1-1,
    libcuda-12.2-1,
    libcuda-12.3-1,
    libcuda1 (= ${binary:Version})
Confilicts:
    libcuda1
Homepage: https://www.nvidia.com/CUDA
Description: NVIDIA CUDA Driver Library

Package: libcudadebugger1-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: same
Depends:
 nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
 libcuda1-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
 ${shlibs:Depends}, ${misc:Depends}
Provides:
    libcudadebugger1 (= ${binary:Version})
Conflicts:
    libcudadebugger1
Homepage: https://www.nvidia.com/CUDA
Description: The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
    This package contains the CUDA Debugger library for Pascal and later GPUs.

Package: libegl-nvidia0-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
 ${misc:Pre-Depends}
Depends:
 nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
 ${shlibs:Depends}, ${misc:Depends}
Provides:
    libegl-nvidia0 (= ${binary:Version})
Conflicts:
    libegl-nvidia0
Description: EGL provides a platform-agnostic mechanism for creating rendering surfaces for use with other graphics libraries, such as OpenGL|ES.
    See the description of the nvidia-driver package or /usr/share/doc/libgl1-nvidia-glx/README.txt.gz for a complete list of supported GPUs and PCI IDs.
    This package contains the driver specific binary EGL implementation provided by NVIDIA that is accessed via GLVND.

"""
