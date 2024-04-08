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
Description: NVIDIA GSP firmware
    The GPU System Processor (GSP) was first introduced in the Turing architecture and supports accelerating tasks traditionally performed by the driver on the CPU.
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
    libcuda.so.1 (= {DRIVER_VERSION_MAJOR}),
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
Description: NVIDIA CUDA Debugger Library
    The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
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
Description: NVIDIA binary EGL library
    EGL provides a platform-agnostic mechanism for creating rendering surfaces for use with other graphics libraries, such as OpenGL|ES.
    See the description of the nvidia-driver package or /usr/share/doc/libgl1-nvidia-glx/README.txt.gz for a complete list of supported GPUs and PCI IDs.
    This package contains the driver specific binary EGL implementation provided by NVIDIA that is accessed via GLVND.

Package: libgl1-nvidia-glvnd-glx-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Depends:
    libgl1 (>= 0.2.999) | libgl1-glvnd-nvidia-glx-{DRIVER_VERSION_MAJOR},
    libglx-nvidia0-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    ${misc:Depends}
Provides:
    libgl1-nvidia-glx-any,
    libgl1-nvidia-glvnd-glx (= ${binary:Version})
Conflicts:
    libgl1-nvidia-glvnd-glx
Description: NVIDIA binary OpenGL/GLX library (GLVND variant)
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    See the description of the nvidia-driver package or /usr/share/doc/libgl1-nvidia-glvnd-glx/README.txt.gz for a complete list of supported GPUs and PCI IDs.
    This metapackage depends on the NVIDIA binary OpenGL/GLX implementation using GLVND and the corresponding GLVND loader library.

Package: libgles-nvidia1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    libgles1 (>= 0.2.999) | libgles1-glvnd-nvidia-{DRIVER_VERSION_MAJOR},
    libnvidia-eglcore-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    ${shlibs:Depends}, ${misc:Depends}
Provides:
    libgles-nvidia1 (= ${binary:Version})
Conflicts:
    libgles-nvidia1
Description: NVIDIA binary OpenGL|ES 1.x library
    OpenGL|ES is a cross-platform API for full-function 2D and 3D graphics on embedded systems - including consoles, phones, appliances and vehicles. It contains a subset of OpenGL plus a number of extensions for the special needs of embedded systems.
    OpenGL|ES 1.x provides an API for fixed-function hardware.
    See the description of the nvidia-driver package or /usr/share/doc/libgl1-nvidia-glx/README.txt.gz for a complete list of supported GPUs and PCI IDs.
    This package contains the driver specific binary OpenGL|ES 1.x implementation by NVIDIA that is accessed via GLVND.

Package: libgles-nvidia2-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    libgles2 (>= 0.2.999) | libgles2-glvnd-nvidia-{DRIVER_VERSION_MAJOR},
    libnvidia-eglcore-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    ${shlibs:Depends}, ${misc:Depends}
Provides:
    libgles-nvidia2 (= ${binary:Version})
Conflicts:
    libgles-nvidia2
Description: NVIDIA binary OpenGL|ES 2.x library
    OpenGL|ES is a cross-platform API for full-function 2D and 3D graphics on embedded systems - including consoles, phones, appliances and vehicles. It contains a subset of OpenGL plus a number of extensions for the special needs of embedded systems.
    OpenGL|ES 2.x provides an API for programmable hardware including vertex and fragment shaders.
    See the description of the nvidia-driver package or /usr/share/doc/libgl1-nvidia-glx/README.txt.gz for a complete list of supported GPUs and PCI IDs.
    This package contains the driver specific binary OpenGL|ES 2.x implementation by NVIDIA that is accessed via GLVND.

Package: libglx-nvidia0-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    libglx0 | libglx0-glvnd-nvidia-{DRIVER_VERSION_MAJOR},
    ${shlibs:Depends}, ${misc:Depends}
Provides:
    libglx-vendor,
    libglx-nvidia0 (= ${binary:Version})
Conflicts:
    libglx-nvidia0
Description: NVIDIA binary GLX library
    GLX ("OpenGL Extension to the X Window System") provides an interface between OpenGL and the X Window System as well as extensions to OpenGL itself.
    See the description of the nvidia-driver package or /usr/share/doc/libgl1-nvidia-glx/README.txt.gz for a complete list of supported GPUs and PCI IDs.
    This package contains the driver specific binary GLX implementation by NVIDIA that is accessed via GLVND.

Package: libnvcuvid1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    libcuda1-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    ${shlibs:Depends}, ${misc:Depends}
Provides:
    libnvcuvid1 (= ${binary:Version})
Conflicts:
    libnvcuvid1
Description: NVIDIA CUDA Video Decoder runtime library
    The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
    The NVIDIA CUDA Video Decoder (NVCUVID) library provides an interface to hardware video decoding capabilities on NVIDIA GPUs with CUDA.

Package: libnvidia-allocator1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    ${shlibs:Depends}, ${misc:Depends}
Recommends:
    libnvidia-egl-gbm1-{DRIVER_VERSION_MAJOR},
Provides:
    libnvidia-allocator1 (= ${binary:Version})
Conflicts:
    libnvidia-allocator1
Description: NVIDIA allocator runtime library
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    This package contains the private nvidia-allocator runtime library which is used by other driver components.

Package: libnvidia-api1-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    ${shlibs:Depends}, ${misc:Depends}
Provides:
    libnvidia-api1 (= ${binary:Version})
Conflicts:
    libnvidia-api1
Description: NVAPI runtime library
    NVAPI provides an interface for managing properties of GPUs.
    This package contains the NVAPI runtime library.

Package: libnvidia-cfg1-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${misc:Pre-Depends}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${binary:Version}),
    ${shlibs:Depends}, ${misc:Depends}
Provides:
    libnvidia-cfg.so.1 (= {DRIVER_VERSION_MAJOR}),
    libnvidia-cfg1-any,
    libnvidia-cfg1 (= ${binary:Version})
Conflicts:
    libnvidia-cfg1
Description: NVIDIA binary OpenGL/GLX configuration library
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    This package contains the private libnvidia-cfg runtime library which is used by other driver components.


"""
