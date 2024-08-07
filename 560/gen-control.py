#! /usr/bin/python3

### Basic configuration
import config
from config import *
### End of Basic configuration

### Notice
# All versioned packages must depend on nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}})
# nvidia-alternative-{DRIVER_VERSION_MAJOR} must conflict with all older nvidia-alternative flavours
### End of Notice

### Important for future Updates (Make sure to update)
# Incase debian adds or removes a packages to the nvidia-graphics-drivers dpkg source make sure to replicate with pika flavour and kernek module adaptations.
# Debian nvidia comes with 49 Packages in 560.
# Pika takes out nvidia-driver-full, nvidia-detect, nvidia-legacy-check.
# Pika add nvidia-kernel-common, nvidia-modprobe, nvidia-persistenced, nvidia-settings, nvidia-support
# So...
# Pika nvidia comes with 51 Packages in 560.
### End of Important Notes

### Text Preq

# control

CONTROL_FILE_PREQ = """Source: nvidia-graphics-drivers-{DRIVER_VERSION_MAJOR}
Section: non-free/libs
Priority: optional
Maintainer: Debian NVIDIA Maintainers <pkg-nvidia-devel@lists.alioth.debian.org>
Uploaders:
 Andreas Beckmann <anbe@debian.org>,
 Luca Boccassi <bluca@debian.org>,
Vcs-Browser: https://salsa.debian.org/nvidia-team/nvidia-graphics-drivers
Vcs-Git: https://salsa.debian.org/nvidia-team/nvidia-graphics-drivers.git -b 560
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
 libglvnd-dev,
 libgtk2.0-0,
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
    ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    firmware-nvidia-gsp (= ${{binary:Version}}),
    firmware-nvidia-gsp-{DRIVER_VERSION_FULL} (= ${{binary:Version}}),
Conflicts:
    firmware-nvidia-gsp,
    firmware-nvidia-gsp-{DRIVER_VERSION_FULL}
Description: NVIDIA GSP firmware
    The GPU System Processor (GSP) was first introduced in the Turing architecture and supports accelerating tasks traditionally performed by the driver on the CPU.
    This package provides the firmware to drive the GSP.

Package: libcuda1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    nvidia-support-{DRIVER_VERSION_MAJOR},
    ${{misc:Pre-Depends}}
Depends:
    nvidia-support-{DRIVER_VERSION_MAJOR},
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-ptxjitcompiler1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-pkcs11-openssl3-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) [amd64],
    ${{shlibs:Depends}}, ${{misc:Depends}}
Recommends:
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-smi-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-cfg1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-persistenced-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libcuda1-{DRIVER_VERSION_MAJOR}:i386 (= ${{binary:Version}}) [amd64],
Suggests:
    nvidia-cuda-mps-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}})
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
    libcuda1 (= ${{binary:Version}})
Conflicts:
    libcuda1
Homepage: https://www.nvidia.com/CUDA
Description: NVIDIA CUDA Driver Library

Package: libcudadebugger1-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: same
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libcuda1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libcudadebugger1 (= ${{binary:Version}})
Conflicts:
    libcudadebugger1
Homepage: https://www.nvidia.com/CUDA
Description: NVIDIA CUDA Debugger Library
    The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
    This package contains the CUDA Debugger library for Pascal and later GPUs.

### Note Re-sync Upstream once nvidia or upstream package it

Package: libnvidia-vksc-core-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: same
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vulkan-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-vksc-core (= ${{binary:Version}})
Conflicts:
    libnvidia-vksc-core
Description: NVIDIA Vulkan SC Validation layers

Package: libegl-nvidia0-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libegl-nvidia0 (= ${{binary:Version}})
Conflicts:
    libegl-nvidia0
Description: NVIDIA binary EGL library
    EGL provides a platform-agnostic mechanism for creating rendering surfaces for use with other graphics libraries, such as OpenGL|ES.
    See the description of the nvidia-driver package or /usr/share/doc/libgl1-nvidia-glx/README.txt.gz for a complete list of supported GPUs and PCI IDs.
    This package contains the driver specific binary EGL implementation provided by NVIDIA that is accessed via GLVND.
### End of note
    
Package: libgl1-nvidia-glvnd-glx-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Depends:
    libgl1 (>= 0.2.999) | libgl1-glvnd-nvidia-glx-{DRIVER_VERSION_MAJOR},
    libglx-nvidia0-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Provides:
    libgl1-nvidia-glx-any,
    libgl1-nvidia-glvnd-glx (= ${{binary:Version}})
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
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles1 (>= 0.2.999) | libgles1-glvnd-nvidia-{DRIVER_VERSION_MAJOR},
    libnvidia-eglcore-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libgles-nvidia1 (= ${{binary:Version}})
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
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles2 (>= 0.2.999) | libgles2-glvnd-nvidia-{DRIVER_VERSION_MAJOR},
    libnvidia-eglcore-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libgles-nvidia2 (= ${{binary:Version}})
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
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libglx0 | libglx0-glvnd-nvidia-{DRIVER_VERSION_MAJOR},
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libglx-vendor,
    libglx-nvidia0 (= ${{binary:Version}})
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
    ${{misc:Pre-Depends}}
Depends:
    libcuda1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvcuvid1 (= ${{binary:Version}})
Conflicts:
    libnvcuvid1
Description: NVIDIA CUDA Video Decoder runtime library
    The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
    The NVIDIA CUDA Video Decoder (NVCUVID) library provides an interface to hardware video decoding capabilities on NVIDIA GPUs with CUDA.

Package: libnvidia-allocator1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Recommends:
    libnvidia-egl-gbm1-{DRIVER_VERSION_MAJOR},
Provides:
    libnvidia-allocator1 (= ${{binary:Version}})
Conflicts:
    libnvidia-allocator1
Description: NVIDIA allocator runtime library
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    This package contains the private nvidia-allocator runtime library which is used by other driver components.

Package: libnvidia-api1-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-api1 (= ${{binary:Version}})
Conflicts:
    libnvidia-api1
Description: NVAPI runtime library
    NVAPI provides an interface for managing properties of GPUs.
    This package contains the NVAPI runtime library.

Package: libnvidia-cfg1-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-cfg.so.1 (= {DRIVER_VERSION_MAJOR}),
    libnvidia-cfg1-any,
    libnvidia-cfg1 (= ${{binary:Version}})
Conflicts:
    libnvidia-cfg1
Description: NVIDIA binary OpenGL/GLX configuration library
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    This package contains the private libnvidia-cfg runtime library which is used by other driver components.


Package: libnvidia-eglcore-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    libnvidia-glvkspirv-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-eglcore (= ${{binary:Version}}),
Conflicts:
    libnvidia-eglcore,
Description: NVIDIA binary EGL core libraries
    EGL provides a platform-agnostic mechanism for creating rendering surfaces for use with other graphics libraries, such as OpenGL|ES.
    OpenGL|ES is a cross-platform API for full-function 2D and 3D graphics on embedded systems - including consoles, phones, appliances and vehicles. It contains a subset of OpenGL plus a number of extensions for the special needs of embedded systems.
    This package contains the private core libraries used by the NVIDIA implementation of EGL and OpenGL|ES.

Package: libnvidia-encode1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-encode1 (= ${{binary:Version}})
Conflicts:
    libnvidia-encode1
Description: NVENC Video Encoding runtime library
    The NVENC Video Encoding library provides an interface to video encoder hardware on supported NVIDIA GPUs.
    This package contains the nvidia-encode runtime library.

Package: libnvidia-fbc1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    libcuda1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-fbc1 (= ${{binary:Version}})
Conflicts:
    libnvidia-fbc1
Description: NVIDIA OpenGL-based Framebuffer Capture runtime library
    The NVIDIA OpenGL-based Framebuffer Capture (NvFBCOpenGL) library provides a high performance, low latency interface to capture and optionally encode an OpenGL framebuffer. NvFBCOpenGL is a private API that is only available to approved partners for use in remote graphics scenarios.
    This package contains the NvFBCOpenGL runtime library.

Package: libnvidia-glcore-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    libnvidia-glvkspirv-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-glcore (= ${{binary:Version}}),
Conflicts:
    libnvidia-glcore,
Description: NVIDIA binary OpenGL/GLX core libraries
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    This package contains the private core libraries used by the NVIDIA implementation of OpenGL and GLX.

Package: libnvidia-glvkspirv-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-glvkspirv (= ${{binary:Version}}),
Conflicts:
    libnvidia-glvkspirv,
Description: NVIDIA binary Vulkan Spir-V compiler library
    Vulkan is a multivendor open standard by the Khronos Group for 3D graphics.
    This library provides a NVIDIA Vulkan Spir-V compiler which reduces shader compilation time and shader system memory consumption.
    This package contains the private Spir-V compiler libraries used by the NVIDIA implementation of Vulkan.

Package: libnvidia-gpucomp-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-gpucomp (= ${{binary:Version}}),
Conflicts:
    libnvidia-gpucomp,
Description: NVIDIA binary GPU compiler library

Package: libnvidia-ml1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-ml.so.1 (= {DRIVER_VERSION_MAJOR}),
    libnvidia-ml1 (= ${{binary:Version}}),
Conflicts:
    libnvidia-ml1,
Homepage: https://developer.nvidia.com/nvidia-management-library-NVML
Description: NVIDIA Management Library (NVML) runtime library
    The NVIDIA Management Library (NVML) provides a monitoring and management API. It provides a direct access to the queries and commands exposed via nvidia-smi.
    This package contains the nvidia-ml runtime library.

Package: libnvidia-ngx1-{DRIVER_VERSION_MAJOR}
Architecture: amd64
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-ngx1 (= ${{binary:Version}}),
Conflicts:
    libnvidia-ngx1,
Description: NVIDIA NGX runtime library
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    This package contains the NVIDIA NGX runtime library.

Package: libnvidia-nvvm4-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-nvvm4 (= ${{binary:Version}}),
Conflicts:
    libnvidia-nvvm4,
Description: NVIDIA NVVM Compiler library
    The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
    This package contains the NVVM Compiler library.

Package: libnvidia-opticalflow1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-opticalflow1 (= ${{binary:Version}}),
Conflicts:
    libnvidia-opticalflow1,
Homepage: https://developer.nvidia.com/opticalflow-sdk
Description: NVIDIA Optical Flow runtime library
    The NVIDIA Optical Flow SDK exposes the latest hardware capability of Turing GPUs dedicated to computing the relative motion of pixels between images.
    This package contains the Optical Flow runtime library.

Package: libnvidia-pkcs11-openssl3-{DRIVER_VERSION_MAJOR}
Architecture: amd64
Multi-Arch: same
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvidia-pkcs11-openssl3 (= ${{binary:Version}}),
Conflicts:
    libnvidia-pkcs11-openssl3,
Homepage: https://www.nvidia.com/CUDA
Description: NVIDIA PKCS #11 Library (OpenSSL 3)
    The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
    This package contains the NVIDIA PKCS #11 library with OpenSSL 3 backend.

Package: libnvidia-ptxjitcompiler1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-ptxjitcompiler1 (= ${{binary:Version}}),
Conflicts:
    libnvidia-ptxjitcompiler1,
Description: NVIDIA PTX JIT Compiler library
        The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
        This package contains the runtime PTX JIT Compiler library.

Package: libnvidia-rtcore-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    libnvidia-rtcore (= ${{binary:Version}}),
Conflicts:
    libnvidia-rtcore
Description: NVIDIA binary Vulkan ray tracing (rtcore) library
    Vulkan is a multivendor open standard by the Khronos Group for 3D graphics.
    This library is part of the Vulkan real-time ray tracing extensions (VK_NV_raytracing) implementation by NVIDIA.
    This package contains the private rtcore library used by the NVIDIA implementation of Vulkan.

Package: libnvoptix1-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    libcuda1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    libnvoptix1 (= ${{binary:Version}}),
Conflicts:
    libnvoptix1
Description: NVIDIA implementation of the OptiX ray tracing engine
    The OptiX API is an application framework for achieving optimal ray tracing performance on the GPU.
    This package contains runtime library of the OptiX ray tracing engine implementation for NVIDIA CUDA. It is used by liboptix.so.* coming with applications using the OptiX API.

Package: nvidia-alternative-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: foreign
Pre-Depends:
    dpkg (>= 1.17.21),
    nvidia-support-{DRIVER_VERSION_MAJOR},
    ${{misc:Pre-Depends}}
Depends:
    glx-alternative-nvidia (>= 1.2),
    ${{misc:Depends}}
Provides:
    nvidia-alternative (= ${{binary:Version}}),
    nvidia-alternative-any,
    nvidia-alternative-kmod-alias,
    nvidia-alternative--kmod-alias,
    nvidia-alternative-{DRIVER_VERSION_FULL},
    nvidia-alternative-{DRIVER_VERSION_MAJOR}-kmod-alias,
    nvidia-alternative-{DRIVER_VERSION_FULL}-kmod-alias,
Conflicts:
    libglvnd0-nvidia,
    libopengl0-glvnd-nvidia,
    libglx0-glvnd-nvidia,
    libgl1-glvnd-nvidia-glx,
    libegl1-glvnd-nvidia,
    libgles1-glvnd-nvidia,
    libgles2-glvnd-nvidia,
    nvidia-legacy-304xx-alternative,
    nvidia-legacy-340xx-alternative,
    nvidia-legacy-390xx-alternative,
    nvidia-tesla-418-alternative,
    nvidia-tesla-450-alternative,
    nvidia-tesla-460-alternative,
    nvidia-tesla-510-alternative,
    nvidia-tesla-alternative,
    nvidia-alternative-525,
    nvidia-alternative-530,
    nvidia-alternative-535,
    nvidia-alternative-545,
    nvidia-alternative-550,
Description: allows the selection of NVIDIA as GLX provider
    In setups with several NVIDIA driver versions installed (e.g. current and legacy) this metapackage registers an alternative to allow easy switching between the different versions.
    Use 'update-glx --config nvidia' to select a version.
    This package does not depend on the corresponding NVIDIA libraries. In order to install the NVIDIA driver and libraries, install the nvidia-driver package instead.

Package: nvidia-cuda-mps-{DRIVER_VERSION_MAJOR}
Section: non-free/utils
Architecture: amd64 arm64 ppc64el
Depends:
    ${{shlibs:Depends}}, ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-cuda-mps (= ${{binary:Version}}),
Conflicts:
    nvidia-cuda-mps
Description: NVIDIA CUDA Multi Process Service (MPS)
    The Compute Unified Device Architecture (CUDA) enables NVIDIA graphics processing units (GPUs) to be used for massively parallel general purpose computation.
    CUDA MPS is a feature that allows multiple CUDA processes to share a single GPU context. CUDA MPS should be transparent to CUDA programs.
    CUDA MPS requires a device that supports Unified Virtual Address (UVA) and has compute capability SM 3.5 or higher. Pre-CUDA 4.0 APIs are not supported under CUDA MPS.

Package: nvidia-driver-{DRIVER_VERSION_MAJOR}
Section: non-free/x11
Architecture: amd64 arm64 ppc64el
Pre-Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Depends:
    nvidia-driver-libs-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-driver-bin-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    xserver-xorg-video-nvidia-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vdpau-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-closed-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles-nvidia1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles-nvidia2-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-cfg1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-encode1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vulkan-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-allocator1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-rtcore-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-smi-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libcudadebugger1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-fbc1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvoptix1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-opticalflow1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-ngx1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) [amd64],
    libnvidia-api1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-opencl-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-powerd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) [amd64],
    nvidia-cuda-mps-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-suspend-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-persistenced-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-settings-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-modprobe-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-xconfig-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-egl-wayland1,
    libnvidia-egl-gbm1,
# Note: Not Upstream
    libnvidia-vksc-core-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
# End of Note
    ${{misc:Depends}}
Recommends:
    nvidia-vaapi-driver,
Suggests:
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR},
    nvidia-closed-kernel-source-{DRIVER_VERSION_MAJOR},
Provides:
    nvidia-driver (= ${{binary:Version}}),
    nvidia-driver-full (= ${{binary:Version}}),
    nvidia-closed-driver (= ${{binary:Version}}),
    nvidia-closed-driver-full (= ${{binary:Version}}),
    nvidia-driver-any,
    nvidia-glx-any,
Conflicts:
    nvidia-driver,
    nvidia-open-driver,
    nvidia-open-driver-{DRIVER_VERSION_MAJOR},
Description: NVIDIA {DRIVER_VERSION_FULL} metapackage
    This metapackage depends on the NVIDIA binary driver and libraries
    that provide optimized hardware acceleration of
    OpenGL/GLX/EGL/GLES/Vulkan applications via a direct-rendering X Server.

Package: nvidia-open-driver-{DRIVER_VERSION_MAJOR}
Section: non-free/x11
Architecture: amd64 arm64 ppc64el
Pre-Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Depends:
    nvidia-driver-libs-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-driver-bin-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    xserver-xorg-video-nvidia-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vdpau-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-open-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles-nvidia1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles-nvidia2-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-cfg1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-encode1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vulkan-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-allocator1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-rtcore-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-smi-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libcudadebugger1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-fbc1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvoptix1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-opticalflow1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-ngx1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) [amd64],
    libnvidia-api1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-opencl-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-powerd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) [amd64],
    nvidia-cuda-mps-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-suspend-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-persistenced-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-settings-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-modprobe-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-xconfig-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-egl-wayland1,
    libnvidia-egl-gbm1,
# Note: Not Upstream
    libnvidia-vksc-core-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
# End of Note
    ${{misc:Depends}}
Recommends:
    nvidia-vaapi-driver,
Suggests:
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR},
    nvidia-open-kernel-source-{DRIVER_VERSION_MAJOR},
Provides:
    nvidia-driver (= ${{binary:Version}}),
    nvidia-driver-full (= ${{binary:Version}}),
    nvidia-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-open-driver (= ${{binary:Version}}),
    nvidia-open-driver-full (= ${{binary:Version}}),
    nvidia-driver-any,
    nvidia-glx-any,
Conflicts:
    nvidia-driver,
    nvidia-driver-{DRIVER_VERSION_MAJOR},
    nvidia-closed-driver,
    nvidia-closed-driver-{DRIVER_VERSION_MAJOR},
Description: NVIDIA {DRIVER_VERSION_FULL} metapackage (With open kernel modules)
    This metapackage depends on the NVIDIA binary driver and libraries
    that provide optimized hardware acceleration of
    OpenGL/GLX/EGL/GLES/Vulkan applications via a direct-rendering X Server.

Package: nvidia-driver-bin-{DRIVER_VERSION_MAJOR}
Section: non-free/x11
Architecture: amd64 arm64 ppc64el
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Recommends:
    nvidia-driver-{DRIVER_VERSION_MAJOR},
Provides:
    nvidia-driver-bin (= ${{binary:Version}}),
Conflicts:
    nvidia-driver-bin ,
Description: NVIDIA driver support binaries
    The NVIDIA binary driver provides optimized hardware acceleration of OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server for graphics cards using NVIDIA chip sets.
    This package contains supporting binaries for the driver.

Package: nvidia-driver-libs-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Depends:
    libgl1-nvidia-glvnd-glx (= ${{binary:Version}}),
    nvidia-egl-icd (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Recommends:
    nvidia-driver-libs-{DRIVER_VERSION_MAJOR}:i386 (= ${{binary:Version}}) [amd64],
    libopengl0 | libopengl0-glvnd-nvidia-{DRIVER_VERSION_MAJOR},
    libglx-nvidia0-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles-nvidia1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libgles-nvidia2-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-cfg1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-encode1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vulkan-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-allocator1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-driver-libs (= ${{binary:Version}}),
    nvidia-driver-libs-any,
Conflicts:
    nvidia-driver-libs,
    libglvnd0-nvidia,
    libopengl0-glvnd-nvidia,
    libglx0-glvnd-nvidia,
    libgl1-glvnd-nvidia-glx,
    libegl1-glvnd-nvidia,
    libgles1-glvnd-nvidia,
    libgles2-glvnd-nvidia,
Breaks:
    nvidia-driver-libs-nonglvnd,
    libgl1-nvidia-glx,
    libegl1-nvidia,
    nvidia-nonglvnd-vulkan-icd,
Description: NVIDIA metapackage (OpenGL/GLX/EGL/GLES libraries)
    This metapackage depends on the NVIDIA binary libraries
    that provide optimized hardware acceleration of
    OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server.

Package: nvidia-egl-common-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el armhf
Multi-Arch: foreign
Depends:
    ${{misc:Depends}}
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-egl-common (= ${{binary:Version}}),
Conflicts:
    nvidia-egl-common
Suggests:
    libegl-nvidia0
Description: NVIDIA binary EGL driver - common files
    EGL provides a platform-agnostic mechanism for creating rendering surfaces
    for use with other graphics libraries, such as OpenGL|ES.
    .
    This package provides the common files for the NVIDIA installable client
    driver (ICD) for EGL via GLVND.

Package: nvidia-egl-icd-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Depends:
    nvidia-egl-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libegl1 (>= 0.2.999) | libegl1-glvnd-nvidia,
    libegl-nvidia0-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Enhances:
    libegl1,
Provides:
    libegl-vendor,
    egl-icd,
    nvidia-egl-icd (= ${{binary:Version}}),
Conflicts:
    nvidia-egl-icd
Description: NVIDIA EGL installable client driver (ICD)
    EGL provides a platform-agnostic mechanism for creating rendering surfaces
    for use with other graphics libraries, such as OpenGL|ES.
    .
    This metapackage provides the NVIDIA installable client driver (ICD) for
    EGL via GLVND which supports NVIDIA GPUs.

Package: nvidia-kernel-common-{DRIVER_VERSION_MAJOR}
Section: contrib/kernel
Architecture: amd64 i386 armhf arm64 ppc64el
Pre-Depends: ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Provides:
    nvidia-kernel-common (= ${{binary:Version}}),
    nvidia-closed-kernel-common (= ${{binary:Version}}),
    nvidia-closed-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-common,
    nvidia-open-kernel-common,
    nvidia-open-kernel-common-{DRIVER_VERSION_MAJOR},
Description: NVIDIA binary kernel module support files
    This package contains support files used for any version of the NVIDIA
    kernel module. It sets up udev and ConsoleKit rules, ensures the NVIDIA
    control device is created, and performs any other tasks required for the
    module to work properly.

Package: nvidia-open-kernel-common-{DRIVER_VERSION_MAJOR}
Section: contrib/kernel
Architecture: amd64 i386 armhf arm64 ppc64el
Pre-Depends: ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Provides:
    nvidia-kernel-common (= ${{binary:Version}}),
    nvidia-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-open-kernel-common (= ${{binary:Version}}),
    nvidia-open-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-common,
    nvidia-kernel-common-{DRIVER_VERSION_MAJOR},
    nvidia-closed-kernel-common,
    nvidia-closed-kernel-common-{DRIVER_VERSION_MAJOR},
Description: NVIDIA binary kernel module support files (Open)
    This package contains support files used for any version of the NVIDIA
    kernel module. It sets up udev and ConsoleKit rules, ensures the NVIDIA
    control device is created, and performs any other tasks required for the
    module to work properly.

Package: nvidia-kernel-dkms-{DRIVER_VERSION_MAJOR}
Section: non-free/kernel
Architecture: amd64 arm64 ppc64el
Depends:
    firmware-nvidia-gsp-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-closed-kernel-source-{DRIVER_VERSION_MAJOR}  (= ${{binary:Version}}),
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR}  (= ${{binary:Version}}),
    nvidia-closed-kernel-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-closed-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    dkms,
    ${{misc:Depends}}
Recommends:
    nvidia-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-closed-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-closed-kernel-module (= ${{binary:Version}}),
    nvidia-kernel-module (= ${{binary:Version}}),
    nvidia-kernel-dkms (= ${{binary:Version}}),
    nvidia-kernel-dkms-closed (= ${{binary:Version}}),
    nvidia-kernel-dkms-any (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-dkms,
    nvidia-open-kernel-dkms,
    nvidia-open-kernel-dkms-{DRIVER_VERSION_MAJOR},
    nvidia-kernel-pikaos-module-{DRIVER_VERSION_MAJOR},
    nvidia-open-kernel-pikaos-module-{DRIVER_VERSION_MAJOR},
    nvidia-kernel-pikaos-module,
    nvidia-open-kernel-pikaos-module,
Description: NVIDIA binary kernel DKMS module
    This package provides the DKMS build configuration for the source for the NVIDIA binary kernel modules
    needed by nvidia-driver.

Package: nvidia-open-kernel-dkms-{DRIVER_VERSION_MAJOR}
Section: non-free/kernel
Architecture: amd64 arm64 ppc64el
Depends:
    firmware-nvidia-gsp-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-open-kernel-source-{DRIVER_VERSION_MAJOR}  (= ${{binary:Version}}),
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR}  (= ${{binary:Version}}),
    nvidia-open-kernel-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-open-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    dkms,
    ${{misc:Depends}}
Recommends:
    nvidia-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-open-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-open-kernel-module (= ${{binary:Version}}),
    nvidia-kernel-module (= ${{binary:Version}}),
    nvidia-kernel-dkms (= ${{binary:Version}}),
    nvidia-kernel-dkms-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-dkms-open (= ${{binary:Version}}),
    nvidia-kernel-dkms-any (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-dkms,
    nvidia-kernel-dkms-{DRIVER_VERSION_MAJOR},
    nvidia-closed-kernel-dkms,
    nvidia-closed-kernel-dkms-{DRIVER_VERSION_MAJOR},
    nvidia-kernel-pikaos-module-{DRIVER_VERSION_MAJOR},
    nvidia-open-kernel-pikaos-module-{DRIVER_VERSION_MAJOR},
    nvidia-kernel-pikaos-module,
    nvidia-open-kernel-pikaos-module,
Description: NVIDIA binary kernel DKMS module (Open)
    This package provides the DKMS build configuration for the source for the NVIDIA binary kernel modules
    needed by nvidia-driver.    
    
Package: nvidia-kernel-source-{DRIVER_VERSION_MAJOR}
Section: non-free/kernel
Architecture: amd64 arm64 ppc64el
Depends:
    debhelper-compat (= 13),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    module-assistant,
    ${{misc:Depends}}
Recommends:
    firmware-nvidia-gsp-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Suggests:
    nvidia-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-kernel-source (= ${{binary:Version}}),
    nvidia-closed-kernel-source (= ${{binary:Version}}),
    nvidia-closed-kernel-source-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-source,
    nvidia-open-kernel-source-{DRIVER_VERSION_MAJOR},
    nvidia-open-kernel-source,
Description: NVIDIA binary kernel module source
    This package provides the source for the NVIDIA binary kernel modules
    needed by nvidia-driver in a form suitable
    for use by module-assistant.
    .
    The NVIDIA binary driver provides optimized hardware acceleration of
    OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server
    for graphics cards using NVIDIA chip sets.
    .
    PLEASE read /usr/share/doc/nvidia-kernel-source/README.Debian.gz
    for building information. If you want the kernel module to be automatically
    installed via DKMS, install nvidia-kernel-dkms-{DRIVER_VERSION_MAJOR} instead.

Package: nvidia-open-kernel-source-{DRIVER_VERSION_MAJOR}
Section: non-free/kernel
Architecture: amd64 arm64 ppc64el
Depends:
    debhelper-compat (= 13),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    module-assistant,
    ${{misc:Depends}}
Recommends:
    firmware-nvidia-gsp-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Suggests:
    nvidia-open-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-open-kernel-source (= ${{binary:Version}}),
    nvidia-open-kernel-source-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-source (= ${{binary:Version}}),
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-source,
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR},
    nvidia-closed-kernel-source,
    nvidia-closed-kernel-source-{DRIVER_VERSION_MAJOR},
Description: NVIDIA binary kernel module source (Open)
    This package provides the source for the NVIDIA binary kernel modules
    needed by nvidia-driver in a form suitable
    for use by module-assistant.
    .
    The NVIDIA binary driver provides optimized hardware acceleration of
    OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server
    for graphics cards using NVIDIA chip sets.
    .
    PLEASE read /usr/share/doc/nvidia-kernel-source/README.Debian.gz
    for building information. If you want the kernel module to be automatically
    installed via DKMS, install nvidia-open-kernel-dkms-{DRIVER_VERSION_MAJOR} instead.    

Package: nvidia-kernel-support-{DRIVER_VERSION_MAJOR}
Section: non-free/kernel
Architecture: amd64 arm64 ppc64el
Multi-Arch: foreign
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-modprobe-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Provides:
    nvidia-kernel-support-any,
    nvidia-kernel-support--v1,
    nvidia-kernel-support (= ${{binary:Version}}),
    nvidia-closed-kernel-support (= ${{binary:Version}}),
    nvidia-closed-kernel-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-open-kernel-support (= ${{binary:Version}}),
    nvidia-open-kernel-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-support,
    nvidia-open-kernel-support,
    nvidia-open-kernel-support-{DRIVER_VERSION_MAJOR},
Description: NVIDIA binary kernel module support files
    The NVIDIA binary driver provides optimized hardware acceleration of
    OpenGL/GLX/EGL/GLES applications via a direct-rendering X Server
    for graphics cards using NVIDIA chip sets.
    .
    This package provides supporting configuration for the kernel module.

Package: nvidia-libopencl1-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Recommends:
    nvidia-opencl-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) | opencl-icd,
Provides:
    libopencl1,
    libopencl-1.1-1,
    libopencl-1.2-1,
    libopencl-2.0-1,
    libopencl-2.1-1,
    libopencl-2.2-1,
    libopencl-3.0-1,
    nvidia-libopencl1 (= ${{binary:Version}}),
Conflicts:
    libopencl1,
    nvidia-libopencl1,
Replaces:
    libopencl1,
Description: NVIDIA OpenCL ICD Loader library
    OpenCL (Open Computing Language) is a multivendor open standard for
    general-purpose parallel programming of heterogeneous systems that include
    CPUs, GPUs and other processors.
    .
    The OpenCL installable client driver loader (ICD Loader) acts as a dispatcher
    between an OpenCL application and one (or more) installable client drivers
    (ICD) that can be from any vendor. At least one ICD (and the corresponding
    hardware) is required to run OpenCL applications.
    .
    This package contains the ICD Loader library provided by NVIDIA.

Package: nvidia-modprobe-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 armhf arm64 ppc64el
Multi-Arch: foreign
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides: nvidia-modprobe (= ${{binary:Version}})
Conflicts: nvidia-modprobe
Description: utility to load NVIDIA kernel modules and create device nodes
     This setuid program is used to create NVIDIA Linux device files and load the
     NVIDIA kernel module, on behalf of NVIDIA Linux driver components which may
     not have sufficient privileges to perform these actions on their own.

Package: nvidia-opencl-common-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: foreign
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Provides:
    nvidia-opencl-common (= ${{binary:Version}}),
Conflicts:
    nvidia-opencl-common
Suggests:
    nvidia-opencl-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}})
Description: NVIDIA OpenCL driver - common files
    OpenCL (Open Computing Language) is a multivendor open standard for
    general-purpose parallel programming of heterogeneous systems that include
    CPUs, GPUs and other processors.
    .
    This package provides the common files for the NVIDIA installable client
    driver (ICD) for OpenCL.

Package: nvidia-opencl-icd-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    nvidia-opencl-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ocl-icd-libopencl1 | nvidia-libopencl1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) | libopencl1,
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libcuda1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-nvvm4-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Enhances:
    libopencl1,
Provides:
    opencl-icd,
    nvidia-opencl-icd (= ${{binary:Version}})
Conflicts:
    nvidia-opencl-icd
Description: NVIDIA OpenCL installable client driver (ICD)
    OpenCL (Open Computing Language) is a multivendor open standard for
    general-purpose parallel programming of heterogeneous systems that include
    CPUs, GPUs and other processors.
    .
    This package provides the NVIDIA installable client driver (ICD) for OpenCL
    which supports NVIDIA GPUs.

Package: nvidia-persistenced-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Multi-Arch: foreign
Pre-Depends:
     ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-cfg1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) [!i386 !armhf],
    adduser,
    ${{shlibs:Depends}},
    ${{misc:Depends}}
Provides:
    nvidia-persistenced (= ${{binary:Version}}),
Conflicts:
    nvidia-persistenced
Description: daemon to maintain persistent software state in the NVIDIA driver
     When persistence mode is enabled, the daemon prevents the driver from
     releasing device state when the device is not in use.
     This can improve the startup time of new clients in this scenario.

Package: nvidia-powerd-{DRIVER_VERSION_MAJOR}
Section: non-free/utils
Architecture: amd64
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Provides:
    nvidia-powerd (= ${{binary:Version}}),
Conflicts:
    nvidia-powerd
Description: NVIDIA Dynamic Boost (daemon)
    The 'nvidia-powerd' daemon provides support for the NVIDIA Dynamic Boost
    feature on Linux platforms. Dynamic Boost is a system-wide power controller
    which manages GPU and CPU power, according to the workload on the system. By
    shifting power between the GPU and the CPU, Dynamic Boost can deliver more
    power to the component that would benefit most from it, without impacting the
    system's total thermal and electrical budgets. This optimizes overall system
    performance per watt.

Package: nvidia-smi-{DRIVER_VERSION_MAJOR}
Section: non-free/utils
Architecture: amd64 arm64 ppc64el
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    libnvidia-ml1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Recommends:
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR}
Provides:
    nvidia-smi (= ${{binary:Version}}),
Conflicts:
    nvidia-smi
Suggests:
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR}
Description: NVIDIA System Management Interface
    The NVIDIA Management Library (NVML) provides a monitoring and management API.
    The application "nvidia-smi" is the NVIDIA System Management Interface (NVSMI)
    and provides a command line interface to this functionality.
    .
    See the output from the --help command line option for supported models and
    further information.

Package: nvidia-suspend-common-{DRIVER_VERSION_MAJOR}
Section: non-free/x11
Architecture: amd64 arm64 ppc64el
Multi-Arch: foreign
Depends:
    kbd,
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Provides:
    nvidia-suspend-common (= ${{binary:Version}}),
Conflicts:
    nvidia-suspend-common
Description: NVIDIA driver - systemd power management scripts
    This package provides the common files for the NVIDIA power management
    integration with systemd.

Package: nvidia-settings-{DRIVER_VERSION_MAJOR}
Architecture: amd64 arm64 ppc64el
Depends:    
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Recommends: 
    libgl1-nvidia-glvnd-glx-{DRIVER_VERSION_MAJOR},
    nvidia-vdpau-driver-{DRIVER_VERSION_MAJOR},
    libnvidia-ml1-{DRIVER_VERSION_MAJOR}
Provides: nvidia-settings-gtk-{DRIVER_VERSION_FULL}, nvidia-settings (= ${{binary:Version}}),
Conflicts: nvidia-settings-gtk-{DRIVER_VERSION_FULL}, nvidia-settings 
Description: tool for configuring the NVIDIA graphics driver
     The nvidia-settings utility is a tool for configuring the NVIDIA
     Linux graphics driver.  It operates by communicating with the NVIDIA
     X driver, querying and updating state as appropriate.  This
     communication is done with the NV-CONTROL X extension.
     .
     Values such as brightness and gamma, XVideo attributes, temperature,
     and OpenGL settings can be queried and configured via nvidia-settings.

Package: nvidia-support-{DRIVER_VERSION_MAJOR}
Architecture: amd64 i386 armhf arm64 ppc64el
Multi-Arch: foreign
Depends: 
    ${{misc:Depends}}
Provides: nvidia-support (= ${{binary:Version}}), nvidia-installer-cleanup (= ${{binary:Version}})
Conflicts: nvidia-support, nvidia-installer-cleanup
Description: NVIDIA binary graphics driver support files
    This package contains support files needed for all current and legacy
    versions of the non-free NVIDIA graphics drivers. These include scripts
    used for warning about a mismatching version of the kernel module.

Package: nvidia-vdpau-driver-{DRIVER_VERSION_MAJOR}
Section: non-free/video
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    libvdpau1 (>= 0.9),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{shlibs:Depends}}, ${{misc:Depends}}
Recommends:
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Suggests:
    nvidia-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Enhances:
    libvdpau1,
Provides:
    vdpau-driver,
    nvidia-vdpau-driver (= ${{binary:Version}}),
Conflicts:
    nvidia-vdpau-driver
Description: Video Decode and Presentation API for Unix - NVIDIA driver

Package: nvidia-vulkan-common-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: foreign
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Suggests:
    nvidia-vulkan-icd-{DRIVER_VERSION_MAJOR}
Provides:
    nvidia-vulkan-common (= ${{binary:Version}}),
Conflicts:
    libgl1-nvidia-glx,
    libgl1-nvidia-tesla-418-glx,
    libgl1-nvidia-legacy-390xx-glx,
    nvidia-nonglvnd-vulkan-common,
    nvidia-vulkan-common
Description: NVIDIA Vulkan driver - common files
    Vulkan is a multivendor open standard by the Khronos Group for 3D graphics.
    .
    This package provides the common files for the NVIDIA installable client
    driver (ICD) for Vulkan (GLVND variant).

Package: nvidia-vulkan-icd-{DRIVER_VERSION_MAJOR}
Architecture: i386 amd64 arm64 ppc64el
Multi-Arch: same
Depends:
    nvidia-vulkan-common-{DRIVER_VERSION_MAJOR},
    libvulkan1 (>= 1.0.42),
    libglx-nvidia0-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Recommends:
    libnvidia-rtcore-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}) [!i386 !ppc64el],
Suggests:
    vulkan-tools,
Enhances:
    libvulkan1,
Provides:
    vulkan-icd,
    nvidia-vulkan-icd-any,
    nvidia-vulkan-icd (= ${{binary:Version}}),
Conflicts:
    nvidia-nonglvnd-vulkan-icd,
    nvidia-vulkan-icd
Description: NVIDIA Vulkan installable client driver (ICD)
    Vulkan is a multivendor open standard by the Khronos Group for 3D graphics.
    .
    This metapackage provides the NVIDIA installable client driver (ICD) for
    Vulkan (GLVND variant) which supports NVIDIA GPUs.

Package: nvidia-xconfig-{DRIVER_VERSION_MAJOR}
Architecture: amd64
Pre-Depends: nvidia-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}})
Depends:
     ${{shlibs:Depends}},
     ${{misc:Depends}}
Recommends: nvidia-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}})
Provides: nvidia-xconfig (= ${{binary:Version}})
Conflicts:  nvidia-xconfig
Description: deprecated X configuration tool for non-free NVIDIA drivers
     This tool is deprecated. The NVIDIA drivers now automatically integrate with
     the Xorg Xserver configuration. Creating an xorg.conf is no longer needed for
     normal setups.
     .
     The nvidia-xconfig program helps with manipulation of X configuration
     files, primarily for systems that use the non-free drivers provided by
     NVIDIA.  It automatically changes the configuration to use the NVIDIA
     driver and can add additional options given on the command line.

Package: xserver-xorg-video-nvidia-{DRIVER_VERSION_MAJOR}
Section: non-free/x11
Architecture: amd64 arm64 ppc64el
Pre-Depends:
    ${{misc:Pre-Depends}}
Depends:
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    xserver-xorg-core,
    ${{shlibs:Depends}}, ${{misc:Depends}}
Recommends:
    nvidia-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vdpau-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-vulkan-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-suspend-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-persistenced-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-settings-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Suggests:
    nvidia-kernel-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    xserver-xorg-video-nvidia-any,
    xserver-xorg-video-nvidia (= ${{binary:Version}}),
Conflicts:
    xserver-xorg-video-nvidia
Description: NVIDIA binary Xorg driver
"""

# end of control

# firmware-nvidia-gsp

FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PREQ = """firmware/gsp*.bin	lib/firmware/nvidia/{DRIVER_VERSION_FULL}/
#RIM_GH100PROD.swidtag	usr/share/nvidia/rim/{DRIVER_VERSION_FULL}/
"""

FIRMWARE_NVIDIA_GSP_LINTIAN_FILE_PREQ = """# Firmware blob.
binary-from-other-architecture [lib/firmware/nvidia/{DRIVER_VERSION_FULL}/gsp*.bin]
spelling-error-in-binary * [lib/firmware/nvidia/{DRIVER_VERSION_FULL}/gsp*.bin]
unstripped-binary-or-object [lib/firmware/nvidia/{DRIVER_VERSION_FULL}/gsp*.bin]
"""

# end of firmware-nvidia-gsp

# libcuda1

LIBCUDA1_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
libcuda.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBCUDA1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[i386]: specific-address-in-shared-library
spelling-error-in-binary
hardening-no-bindnow
[!arm64]: hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBCUDA1_POSTINST_FILE_PREQ = """#!/bin/sh
set -e

. /usr/share/debconf/confmodule

if [ "$1" = "configure" ]
then

	if [ -x /usr/lib/nvidia/check-for-mismatching-nvidia-module ]
	then
		/usr/lib/nvidia/check-for-mismatching-nvidia-module {DRIVER_VERSION_FULL}
	fi

fi


#DEBHELPER#"""

LIBCUDA1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libcuda.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libcuda.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libcuda.so.1		usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libcuda.so"""

# end of libcuda1

# libcudadebugger1

LIBCUDADEBUGGER1_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
libcudadebugger.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBCUDADEBUGGER1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
binary-has-unneeded-section
[i386]: specific-address-in-shared-library
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBCUDADEBUGGER1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libcudadebugger.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libcudadebugger.so.1"""

# end of libcudadebugger1

### Note: Not Upstream

# libegl-nvidia0

LIBEGL_NVIDIA0_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
libEGL_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
libnvidia-egl-xcb.so.1  usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
libnvidia-egl-xlib.so.1	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
20_nvidia_xcb.json  /usr/share/egl/egl_external_platform.d/
20_nvidia_xlib.json /usr/share/egl/egl_external_platform.d/"""

### End of Note

LIBEGL_NVIDIA0_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

LIBEGL_NVIDIA0_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libEGL_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libEGL_nvidia.so.0"""

# end of libegl-nvidia0

# libgl1-nvidia-glvnd-glx

LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE_PREQ = """debian/README.alternatives
README.txt"""

# end of libgl1-nvidia-glvnd-glx

# libgles-nvidia1

LIBGLES_NVIDIA1_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
libGLESv1_CM_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBGLES_NVIDIA1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

LIBGLES_NVIDIA1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libGLESv1_CM_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libGLESv1_CM_nvidia.so.1"""

# end of libgles-nvidia1

# libgles-nvidia2

LIBGLES_NVIDIA2_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
libGLESv2_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBGLES_NVIDIA2_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

LIBGLES_NVIDIA2_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libGLESv2_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libGLESv2_nvidia.so.2"""

# end of libgles-nvidia2

# libglx-nvidia0

LIBGLX_NVIDIA0_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libGLX_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBGLX_NVIDIA0_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
exit-in-shared-library
[i386]: specific-address-in-shared-library
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

LIBGLX_NVIDIA0_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libGLX_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libGLX_nvidia.so.0"""

# end of libglx-nvidia0

# libnvcuvid1

LIBNVCUVID1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvcuvid.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVCUVID1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[i386 ppc64el]: specific-address-in-shared-library
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBNVCUVID1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvcuvid.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvcuvid.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvcuvid.so.1		usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvcuvid.so"""

# end of libnvcuvid1

# libnvidia-allocator1

LIBNVIDIA_ALLOCATOR1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-allocator.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBNVIDIA_ALLOCATOR1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-allocator.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-allocator.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-allocator.so.{DRIVER_VERSION_FULL}		usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/nvidia-drm_gbm.so"""

# end of libnvidia-allocator1

# libnvidia-api1

LIBNVIDIA_API1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-api.so.1	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_API1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

# end of libnvidia-api1

# libnvidia-cfg1

LIBNVIDIA_CFG1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-cfg.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_CFG1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[ppc64el]: specific-address-in-shared-library
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

LIBNVIDIA_CFG1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-cfg.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-cfg.so.1"""

# end of libnvidia-cfg1

# libnvidia-eglcore

LIBNVIDIA_EGLCORE_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-eglcore.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/
libnvidia-glsi.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/"""

LIBNVIDIA_EGLCORE_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
embedded-library libzstd [usr/lib/*/libnvidia-eglcore.so.{DRIVER_VERSION_FULL}]
[i386]: specific-address-in-shared-library
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# The libnvidia-{{eglcore,glsi}}.so.* SONAME changes with every upstream
# release.
# These private libraries are only used (and usable) as plugins
# loaded by other NVIDIA libraries with the same upstream version
# (and a stable SONAME).
# Therefore we do not include the SONAME in this package name to
# avoid going through NEW for every new upstream release.
package-name-doesnt-match-sonames libnvidia-eglcore{DRIVER_VERSION_FULL} libnvidia-glsi{DRIVER_VERSION_FULL}
symbols-file-missing-build-depends-package-field"""

# end of libnvidia-eglcore

# libnvidia-encode1

LIBNVIDIA_ENCODE1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-encode.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_ENCODE1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[i386 ppc64el]: specific-address-in-shared-library
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBNVIDIA_ENCODE1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-encode.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-encode.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-encode.so.1    usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-encode.so"""

# end of libnvidia-encode1

### Note not upstream

# libnvidia-vksc-core

LIBNVIDIA_VKSC_CORE_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-vksc-core.so.{DRIVER_VERSION_FULL}  usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
nvidia_icd_vksc.json usr/share/vulkan/icd.d/
nvidia-pcc usr/bin/"""

LIBNVIDIA_VKSC_CORE_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[i386 ppc64el]: specific-address-in-shared-library
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

# end of libnvidia-vksc-core

### End of note

# libnvidia-fbc1

LIBNVIDIA_FBC1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-fbc.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_FBC1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBNVIDIA_FBC1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-fbc.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-fbc.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-fbc.so.1    usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-fbc.so"""

# end of libnvidia-fbc1

# libnvidia-glcore

LIBNVIDIA_GLCORE_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-glcore.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/
libnvidia-tls.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/"""

LIBNVIDIA_GLCORE_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[arm64 ppc64el]: elf-warning
embedded-library libzstd [usr/lib/*/libnvidia-glcore.so.{DRIVER_VERSION_FULL}]
[i386]: specific-address-in-shared-library
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# The libnvidia-{{glcore,tls}}.so.* SONAME changes with every upstream
# release.
# These private libraries are only used (and usable) as plugins
# loaded by other NVIDIA libraries with the same upstream version
# (and a stable SONAME).
# Therefore we do not include the SONAME in this package name to
# avoid going through NEW for every new upstream release.
package-name-doesnt-match-sonames libnvidia-glcore{DRIVER_VERSION_FULL} libnvidia-tls{DRIVER_VERSION_FULL}
symbols-file-missing-build-depends-package-field"""

# end of libnvidia-glcore

# libnvidia-glvkspirv

LIBNVIDIA_GLVKSPIRV_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-glvkspirv.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/"""

LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# The libnvidia-glvkspirv.so.* SONAME changes with every upstream
# release.
# These private libraries are only used (and usable) as plugins
# loaded by other NVIDIA libraries with the same upstream version
# (and a stable SONAME).
# Therefore we do not include the SONAME in this package name to
# avoid going through NEW for every new upstream release.
package-name-doesnt-match-sonames libnvidia-glvkspirv{DRIVER_VERSION_FULL}
symbols-file-missing-build-depends-package-field"""

# end of libnvidia-glvkspirv

# libnvidia-gpucomp

LIBNVIDIA_GPUCOMP_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-gpucomp.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/"""

LIBNVIDIA_GPUCOMP_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# The libnvidia-{{glcore,tls}}.so.* SONAME changes with every upstream
# release.
# These private libraries are only used (and usable) as plugins
# loaded by other NVIDIA libraries with the same upstream version
# (and a stable SONAME).
# Therefore we do not include the SONAME in this package name to
# avoid going through NEW for every new upstream release.
package-name-doesnt-match-sonames libnvidia-gpucomp{DRIVER_VERSION_FULL}
symbols-file-missing-build-depends-package-field"""

# end of libnvidia-gpucomp

# libnvidia-ml1

LIBNVIDIA_ML1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-ml.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_ML1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBNVIDIA_ML1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ml.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ml.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ml.so.1    usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ml.so"""

# end of libnvidia-ml1

# libnvidia-ngx1

LIBNVIDIA_NGX1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-ngx.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
_nvngx.dll  usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/nvidia/wine
nvngx.dll   usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/nvidia/wine"""

LIBNVIDIA_NGX1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# Location expected by Proton.
repeated-path-segment nvidia [usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/nvidia/]"""

LIBNVIDIA_NGX1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ngx.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ngx.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ngx.so.1    usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ngx.so"""

# end of libnvidia-ngx1

# libnvidia-nvvm4

LIBNVIDIA_NVVM4_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-nvvm.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_NVVM4_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
spelling-error-in-binary
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBNVIDIA_NVVM4_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-nvvm.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-nvvm.so.4
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-nvvm.so.4    usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-nvvm.so"""

# end of libnvidia-nvvm4

# libnvidia-opticalflow1

LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-opticalflow.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386 ppc64el]: specific-address-in-shared-library
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

LIBNVIDIA_OPTICALFLOW1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-opticalflow.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-opticalflow.so.1
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-opticalflow.so.1    usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-opticalflow.so"""

# end of libnvidia-opticalflow1

# libnvidia-pkcs11-openssl3

LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-pkcs11-openssl3.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/"""

LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
hardening-no-bindnow

# Use wildcard instead of exact path substitution, this is a M-A: same package.
library-not-linked-against-libc [usr/lib*/libnvidia-pkcs11-openssl3.so.{DRIVER_VERSION_FULL}]

# The libnvidia-pkcs11-openssl3.so.* SONAME changes with every upstream
# release.
# These private libraries are only used (and usable) as plugins
# loaded by other NVIDIA libraries with the same upstream version
# (and a stable SONAME).
# Therefore we do not include the SONAME in this package name to
# avoid going through NEW for every new upstream release.
package-name-doesnt-match-sonames libnvidia-pkcs11-openssl3-{DRIVER_VERSION_FULL}
symbols-file-missing-build-depends-package-field"""

# end of libnvidia-pkcs11-openssl3

# libnvidia-ptxjitcompiler1

LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-ptxjitcompiler.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
spelling-error-in-binary
[!arm64]: hardening-no-bindnow
[!arm64]: hardening-no-fortify-functions

# Use wildcard instead of exact path substitution, this is a M-A: same package.
embedded-library
embedded-library zlib [usr/lib*/libnvidia-ptxjitcompiler.so.{DRIVER_VERSION_FULL}]

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ptxjitcompiler.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-ptxjitcompiler.so.1"""

# end of libnvidia-ptxjitcompiler1

# libnvidia-rtcore

LIBNVIDIA_RTCORE_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-rtcore.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/"""

LIBNVIDIA_RTCORE_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
spelling-error-in-binary
hardening-no-bindnow
[!arm64]: hardening-no-fortify-functions

# The libnvidia-rtcore.so.* SONAME changes with every upstream
# release.
# These private libraries are only used (and usable) as plugins
# loaded by other NVIDIA libraries with the same upstream version
# (and a stable SONAME).
# Therefore we do not include the SONAME in this package name to
# avoid going through NEW for every new upstream release.
package-name-doesnt-match-sonames libnvidia-rtcore{DRIVER_VERSION_FULL}
symbols-file-missing-build-depends-package-field"""

# end of libnvidia-rtcore

# libnvoptix1

LIBNVOPTIX1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvoptix.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
nvoptix.bin	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

LIBNVOPTIX1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

LIBNVOPTIX1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvoptix.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvoptix.so.1"""

# end of libnvoptix1

# nvidia-alternative

NVIDIA_ALTERNATIVE_INSTALL_FILE_PREQ = """extra_files/nvidia-libdir.conf    etc/ld.so.conf.d/"""

NVIDIA_ALTERNATIVE_DIRS_FILE_PREQ = """#! /usr/bin/dh-exec
etc/modprobe.d
etc/nvidia
usr/lib/nvidia/{DRIVER_VERSION_FULL}
usr/lib/nvidia/{DRIVER_VERSION_FULL}-open
usr/lib/${{DEB_HOST_MULTIARCH}}/gbm
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia
usr/lib/${{DEB_HOST_MULTIARCH}}/vdpau
usr/share/applications
usr/share/man/man1
usr/share/nvidia"""

NVIDIA_ALTERNATIVE_LINTIAN_FILE_PREQ = """# This directory is used as a master alternative.
package-contains-empty-directory [usr/lib/nvidia/{DRIVER_VERSION_FULL}/]
package-contains-empty-directory [usr/lib/nvidia/{DRIVER_VERSION_FULL}-open/]

# Slave alternatives may be installed there.
package-contains-empty-directory [usr/lib/{DEB_HOST_MULTIARCH}/gbm/]
package-contains-empty-directory [usr/lib/{DEB_HOST_MULTIARCH}/nvidia/]
package-contains-empty-directory [usr/lib/{DEB_HOST_MULTIARCH}/vdpau/]
package-contains-empty-directory [usr/share/applications/]
package-contains-empty-directory [usr/share/man/man1/]
package-contains-empty-directory [usr/share/nvidia/]"""

NVIDIA_ALTERNATIVE_PRERM_FILE_PREQ = """#!/bin/sh
set -e


if [ "$1" = "remove" ] || [ "$1" = "deconfigure" ]; then

	update-alternatives --remove nvidia /usr/lib/nvidia/{DRIVER_VERSION_FULL}-open
	update-alternatives --remove nvidia /usr/lib/nvidia/{DRIVER_VERSION_FULL}
	dpkg-trigger --no-await register-glx-alternative-nvidia

fi


#DEBHELPER#"""

NVIDIA_ALTERNATIVE_POSTINST_FILE_PREQ = """#!/bin/sh
set -e


TRIPLETS="/ /i386-linux-gnu/ /x86_64-linux-gnu/ /aarch64-linux-gnu/ /powerpc64le-linux-gnu/"

add_slave()
{{
	local target_link name source_path prefix
	target_link="$1"
	name="$2"
	source_path="$3"
	prefix="nvidia--"

	if [ -f "${{source_path}}" ] && [ -d "$(dirname "${{target_link}}")" ]; then
		echo --slave "${{target_link}}" "${{prefix}}${{name}}" "${{source_path}}"
	fi
}}

add_multiarch_slave()
{{
	local target_dir target_sub_dir file source_dir source_sub_dir prefix suffix triplet
	target_dir="$1"
	target_sub_dir="$2"
	file="$3"
	source_dir="$4"
	source_sub_dir="$5"
	prefix="$6"

	for triplet in $TRIPLETS ; do
		# s|/$||; s|^/|-|;
		suffix="${{triplet%/}}"
		suffix="${{suffix:+-${{suffix#/}}}}"
		add_slave \
			"${{target_dir}}${{triplet}}${{target_sub_dir}}${{file}}" \
			"${{prefix}}${{file}}${{suffix}}" \
			"${{source_dir}}${{triplet}}${{source_sub_dir}}${{file}}"
	done
}}

# A trigger that handles the alternatives for /usr/lib[/<triplet>]/nvidia/*.*
if [ "$1" = "triggered" ]; then

	slaves="
		$(add_slave /usr/lib/nvidia/libglxserver_nvidia.so libglxserver_nvidia.so /usr/lib/nvidia/current/libglxserver_nvidia.so)
		$(add_slave /usr/lib/nvidia/nvidia_drv.so nvidia_drv.so /usr/lib/nvidia/current/nvidia_drv.so)
		$(add_multiarch_slave /usr/lib vdpau/ libvdpau_nvidia.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libGLX_nvidia.so.0 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libEGL_nvidia.so.0 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libGLESv1_CM_nvidia.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libGLESv2_nvidia.so.2 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libcuda.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libcuda.so /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libcudadebugger.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvcuvid.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvcuvid.so /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-allocator.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-api.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-encode.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-fbc.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-ml.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-ngx.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-nvvm.so.4 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-nvvm.so.{DRIVER_VERSION_FULL} /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-opencl.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-opticalflow.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvidia-ptxjitcompiler.so.1 /usr/lib nvidia/current/)
		$(add_multiarch_slave /usr/lib "" libnvoptix.so.1 /usr/lib nvidia/current/)
		$(add_slave /usr/share/nvidia/nvoptix.bin nvoptix.bin /usr/lib/{DEB_HOST_MULTIARCH}/nvidia/current/nvoptix.bin)
		$(add_multiarch_slave /usr/lib gbm/ nvidia-drm_gbm.so /usr/lib nvidia/current/)
		$(add_slave /usr/bin/nvidia-smi nvidia-smi /usr/lib/nvidia/current/nvidia-smi)
		$(add_slave /usr/share/man/man1/nvidia-smi.1.gz nvidia-smi.1.gz /usr/lib/nvidia/current/nvidia-smi.1.gz)
		$(add_slave /usr/lib/nvidia/nvidia-bug-report.sh nvidia-bug-report.sh /usr/lib/nvidia/current/nvidia-bug-report.sh)
		$(add_slave /usr/bin/nvidia-debugdump nvidia-debugdump /usr/lib/nvidia/current/nvidia-debugdump)
		$(add_slave /usr/share/nvidia/nvidia-application-profiles-key-documentation nvidia-application-profiles-key-documentation /usr/share/nvidia/nvidia-application-profiles-{DRIVER_VERSION_FULL}-key-documentation)
		$(add_slave /usr/bin/nvidia-settings nvidia-settings /usr/lib/nvidia/current/nvidia-settings)
		$(add_slave /usr/bin/nv-control-dpy nv-control-dpy /usr/lib/nvidia/current/nv-control-dpy)
		$(add_slave /usr/share/applications/nvidia-settings.desktop nvidia-settings.desktop /usr/lib/nvidia/current/nvidia-settings.desktop)
		$(add_slave /usr/share/man/man1/nvidia-settings.1.gz nvidia-settings.1.gz /usr/lib/nvidia/current/nvidia-settings.1.gz)
"
	conf_slaves="
		$(add_multiarch_slave /usr/lib nvidia/ libnvidia-cfg.so.1 /usr/lib nvidia/current/)
		$(add_slave /etc/nvidia/nvidia-drm-outputclass.conf nvidia-drm-outputclass.conf /etc/nvidia/current/nvidia-drm-outputclass.conf)
"
	kmod_slaves="
		$(add_slave /etc/nvidia/nvidia-blacklists-nouveau.conf nvidia-blacklists-nouveau.conf /etc/nvidia/nvidia-{DRIVER_VERSION_FULL}/nvidia-blacklists-nouveau.conf)
		$(add_slave /etc/nvidia/nvidia-modprobe.conf nvidia-modprobe.conf /etc/nvidia/nvidia-{DRIVER_VERSION_FULL}/nvidia-modprobe.conf)
		$(add_slave /etc/modprobe.d/nvidia-options.conf nvidia-options.conf /etc/nvidia/nvidia-{DRIVER_VERSION_FULL}/nvidia-options.conf)
		$(add_slave /etc/nvidia/nvidia-load.conf nvidia-load.conf /etc/nvidia/nvidia-{DRIVER_VERSION_FULL}/nvidia-load.conf)
"
	kmod_open_slaves="
		$(add_slave /etc/nvidia/nvidia-blacklists-nouveau.conf nvidia-blacklists-nouveau.conf /etc/nvidia/{DRIVER_VERSION_FULL}-open/nvidia-blacklists-nouveau.conf)
		$(add_slave /etc/nvidia/nvidia-modprobe.conf nvidia-modprobe.conf /etc/nvidia/{DRIVER_VERSION_FULL}-open/nvidia-modprobe.conf)
		$(add_slave /etc/modprobe.d/nvidia-options.conf nvidia-options.conf /etc/nvidia/{DRIVER_VERSION_FULL}-open/nvidia-options.conf)
		$(add_slave /etc/nvidia/nvidia-load.conf nvidia-load.conf /etc/nvidia/{DRIVER_VERSION_FULL}-open/nvidia-load.conf)
"
	libnvidia_ml_so_slave=
	if [ -f /usr/include/nvml.h ]; then
		libnvidia_ml_so_slave="$(add_multiarch_slave /usr/lib "" libnvidia-ml.so /usr/lib nvidia/current/)"
	fi
	normal_alternative=0
	open_alternative=0
	if echo "$slaves" | grep -q "slave" ; then
		if echo "${{kmod_slaves}}" | grep -q "slave" ; then
			normal_alternative=1
		fi
		if echo "${{kmod_open_slaves}}" | grep -q "slave" ; then
			open_alternative=1
		else
			# fallback: normal alternative w/o kernel module
			normal_alternative=1
		fi
	fi
	if [ "$normal_alternative" = 1 ]; then
		update-alternatives --install /usr/lib/nvidia/nvidia nvidia /usr/lib/nvidia/current {DRIVER_VERSION_MAJOR} $slaves $conf_slaves $kmod_slaves $libnvidia_ml_so_slave
	else
		update-alternatives --remove nvidia /usr/lib/nvidia/current
	fi
	if [ "$open_alternative" = 1 ]; then
		update-alternatives --install /usr/lib/nvidia/nvidia nvidia /usr/lib/nvidia/current-open $(({DRIVER_VERSION_MAJOR} - 1)) $slaves $conf_slaves $kmod_open_slaves $libnvidia_ml_so_slave
	else
		update-alternatives --remove nvidia /usr/lib/nvidia/current-open
	fi

	# activate the trigger selecting NVIDIA as GLX provider
	dpkg-trigger --no-await register-glx-alternative-nvidia

	# let glx-alternative-mesa take over handling libGLX_indirect.so.0
	dpkg-trigger --no-await register-glx-alternative-mesa

fi


if [ "$1" = "configure" ]; then

	# activate our trigger
	dpkg-trigger register-nvidia-alternative

fi


#DEBHELPER#"""

NVIDIA_ALTERNATIVE_TRIGGERS_FILE_PREQ = """interest-await register-nvidia-alternative

interest-await /etc/nvidia/current
interest-await /etc/nvidia/current-open
interest-await /etc/nvidia/nvidia-{DRIVER_VERSION_FULL}
interest-await /etc/nvidia/{DRIVER_VERSION_FULL}-open

interest-await /usr/lib/nvidia/current
interest-await /usr/lib/i386-linux-gnu/nvidia/current
interest-await /usr/lib/x86_64-linux-gnu/nvidia/current
interest-await /usr/lib/aarch64-linux-gnu/nvidia/current
interest-await /usr/lib/powerpc64le-linux-gnu/nvidia/current

interest-await /usr/include/nvml.h

"""

# end of nvidia-alternative

# nvidia-cuda-mps

NVIDIA_CUDA_MPS_INSTALL_FILE_PREQ =  """nvidia-cuda-mps-control	usr/bin/
nvidia-cuda-mps-server	usr/sbin/"""

NVIDIA_CUDA_MPS_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions
hardening-no-pie"""

NVIDIA_CUDA_MPS_LINKS_FILE_PREQ = """usr/share/man/man1/nvidia-cuda-mps-control.1 usr/share/man/man8/nvidia-cuda-mps-server.8"""

NVIDIA_CUDA_MPS_MANPAGES_FILE_PREQ = """nvidia-cuda-mps-control.1"""

NVIDIA_CUDA_MPS_DIRS_FILE_PREQ = """var/log/nvidia-mps"""

# end of nvidia-cuda-mps

# nvidia-driver

NVIDIA_DRIVER_DOCS_FILE_PREQ = """README.txt
html/
debian/README.alternatives
supported-gpus/supported-gpus.json"""

# end of nvidia-driver

# nvidia-open-driver

NVIDIA_OPEN_DRIVER_DOCS_FILE_PREQ = """README.txt
html/
debian/README.alternatives
supported-gpus/supported-gpus.json"""

# end of nvidia-open-driver

# nvidia-driver-bin

NVIDIA_DRIVER_BIN_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
nvidia-bug-report.sh	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
nvidia-debugdump	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
nvidia-application-profiles-{DRIVER_VERSION_FULL}-rc	usr/share/nvidia/
nvidia-application-profiles-{DRIVER_VERSION_FULL}-key-documentation	usr/share/nvidia/"""

NVIDIA_DRIVER_BIN_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
hardening-no-bindnow
hardening-no-fortify-functions
hardening-no-pie

# The current setup involving multiple chained alternatives would be very
# hard to migrate to /usr/libexec.
executable-in-usr-lib"""

# end of nvidia-driver-bin

# nvidia-driver-libs

NVIDIA_DRIVER_LIBS_LINTIAN_FILE_PREQ = """breaks-without-version"""

NVIDIA_DRIVER_LIBS_POSTINST_FILE_PREQ = """#!/bin/sh
set -e

. /usr/share/debconf/confmodule

if [ "$1" = "configure" ]
then

	if [ -x /usr/lib/nvidia/check-for-conflicting-opengl-libraries ]
	then
		/usr/lib/nvidia/check-for-conflicting-opengl-libraries
	fi

	if [ -x /usr/lib/nvidia/check-for-mismatching-nvidia-module ]
	then
		/usr/lib/nvidia/check-for-mismatching-nvidia-module {DRIVER_VERSION_FULL}
	fi

fi


#DEBHELPER#"""

# end of nvidia-driver-libs

# nvidia-egl-common

NVIDIA_EGL_COMMON_INSTALL_FILE_PREQ = """10_nvidia.json		/usr/share/glvnd/egl_vendor.d/"""

NVIDIA_EGL_COMMON_LINTIAN_FILE_PREQ = """# We do not build arch:all packages from the proprietary driver.
package-contains-no-arch-dependent-files"""

# end of nvidia-egl-common

# nvidia-egl-icd

# nvidia-egl-icd doesn't have any dh files

# end of nvidia-egl-icd

# nvidia-kernel-common

NVIDIA_KERNEL_COMMON_INSTALL_FILE_PREQ  = """extra_files/nvidia_helper.ck /usr/lib/ConsoleKit/run-seat.d/
extra_files/nvidia_helper /usr/lib/udev/
"""

NVIDIA_KERNEL_COMMON_LINTIAN_FILE_PREQ = """# Hook location.
executable-in-usr-lib [usr/lib/ConsoleKit/run-seat.d/nvidia_helper.ck]

# We do not build arch:all packages for the proprietary driver.
package-contains-no-arch-dependent-files
"""

NVIDIA_KERNEL_COMMON_UDEV_FILE_PREQ = """# Set ACLs for console users on /dev/nvidia*
# This is necessary until the driver uses some other form of auth
ENV{{ACL_MANAGE}}=="0", GOTO="nvidia_end"
DRIVER=="nvidia",ENV{{NVIDIA_DEVICE}}="1"
ENV{{NVIDIA_DEVICE}}!="1", GOTO="nvidia_end"
ENV{{ACL_MANAGE}}="1"
TEST!="/lib/libglib-2.0.so.0", GOTO="nvidia_end"
# apply ACL for all locally logged in users
TEST=="/var/run/ConsoleKit/database", \
  RUN+="nvidia_helper --action=$env{{ACTION}} --device=$env{{DEVNAME}}"
LABEL="nvidia_end"
"""

# end of nvidia-kernel-common

# nvidia-kernel-dkms

NVIDIA_KERNEL_DKMS_INSTALL_FILE_PREQ  = """kernel/*				usr/src/nvidia-{DRIVER_VERSION_FULL}/"""

NVIDIA_KERNEL_DKMS_LINTIAN_FILE_PREQ = """# These object files are linked into kernel modules.
unstripped-binary-or-object

# False positives in non-string parts.
spelling-error-in-binary"""

NVIDIA_KERNEL_DKMS_DKMS_FILE_PREQ = """# DKMS configuration for the NVIDIA kernel module.  -*- sh -*-

PACKAGE_NAME="nvidia"
PACKAGE_VERSION="{DRIVER_VERSION_FULL}"

# Only kernels from 3.10 onwards are supported.
BUILD_EXCLUSIVE_KERNEL="^(3\.[1-9][0-9]|[4-9]\.)"

# The NVIDIA driver does not support real-time kernels.
BUILD_EXCLUSIVE_CONFIG="!CONFIG_PREEMPT_RT !CONFIG_PREEMPT_RT_FULL"

AUTOINSTALL=yes

MAKE[0]="env NV_VERBOSE=1 \
    make ${{parallel_jobs+-j$parallel_jobs}} modules KERNEL_UNAME=${{kernelver}}"
CLEAN="make KERNEL_UNAME=${{kernelver}} clean"

BUILT_MODULE_NAME[0]="nvidia"
DEST_MODULE_NAME[0]="$PACKAGE_NAME"
DEST_MODULE_LOCATION[0]="/updates/dkms"

BUILT_MODULE_NAME[1]="nvidia-modeset"
DEST_MODULE_NAME[1]="$PACKAGE_NAME-modeset"
DEST_MODULE_LOCATION[1]="/updates/dkms"

BUILT_MODULE_NAME[2]="nvidia-drm"
DEST_MODULE_NAME[2]="$PACKAGE_NAME-drm"
DEST_MODULE_LOCATION[2]="/updates/dkms"

BUILT_MODULE_NAME[3]="nvidia-uvm"
DEST_MODULE_NAME[3]="$PACKAGE_NAME-uvm"
DEST_MODULE_LOCATION[3]="/updates/dkms"

BUILT_MODULE_NAME[4]="nvidia-peermem"
DEST_MODULE_NAME[4]="$PACKAGE_NAME-peermem"
DEST_MODULE_LOCATION[4]="/updates/dkms"
"""

NVIDIA_KERNEL_DKMS_DOCS_FILE_PREQ = """README.txt"""

# end of nvidia-kernel-dkms

# nvidia-kernel-source

NVIDIA_KERNEL_SOURCE_INSTALL_FILE_PREQ = """kernel/*		usr/src/modules/nvidia-kernel/
extra_files/bug-script	usr/src/modules/nvidia-kernel/debian/
debian/changelog	usr/src/modules/nvidia-kernel/debian/
extra_files/control.models	usr/src/modules/nvidia-kernel/debian/
debian/copyright	usr/src/modules/nvidia-kernel/debian/
# debian/module/debian/*	usr/src/modules/nvidia-kernel/debian/"""

NVIDIA_KERNEL_SOURCE_DOCS_FILE_PREQ = """README.txt
extra_files/build-module-packages.sh"""

# end of nvidia-kernel-source

# nvidia-open-kernel-common

NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILE_PREQ  = """extra_files/nvidia_helper.ck /usr/lib/ConsoleKit/run-seat.d/
extra_files/nvidia_helper /usr/lib/udev/
"""

NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILE_PREQ = """# Hook location.
executable-in-usr-lib [usr/lib/ConsoleKit/run-seat.d/nvidia_helper.ck]

# We do not build arch:all packages for the proprietary driver.
package-contains-no-arch-dependent-files
"""

NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILE_PREQ = """# Set ACLs for console users on /dev/nvidia*
# This is necessary until the driver uses some other form of auth
ENV{{ACL_MANAGE}}=="0", GOTO="nvidia_end"
DRIVER=="nvidia",ENV{{NVIDIA_DEVICE}}="1"
ENV{{NVIDIA_DEVICE}}!="1", GOTO="nvidia_end"
ENV{{ACL_MANAGE}}="1"
TEST!="/lib/libglib-2.0.so.0", GOTO="nvidia_end"
# apply ACL for all locally logged in users
TEST=="/var/run/ConsoleKit/database", \
  RUN+="nvidia_helper --action=$env{{ACTION}} --device=$env{{DEVNAME}}"
LABEL="nvidia_end"
"""

# end of nvidia-open-kernel-common

# nvidia-open-kernel-dkms

NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILE_PREQ  = """kernel-open/*				usr/src/nvidia-open-{DRIVER_VERSION_FULL}/"""

NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILE_PREQ = """# These object files are linked into kernel modules.
unstripped-binary-or-object

# False positives in non-string parts.
spelling-error-in-binary"""

NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILE_PREQ = """# DKMS configuration for the NVIDIA Open kernel module.  -*- sh -*-

PACKAGE_NAME="nvidia-open"
PACKAGE_VERSION="{DRIVER_VERSION_FULL}"

# Only kernels from 3.10 onwards are supported.
BUILD_EXCLUSIVE_KERNEL="^(3\.[1-9][0-9]|[4-9]\.)"

# The NVIDIA Open driver does not support real-time kernels.
BUILD_EXCLUSIVE_CONFIG="!CONFIG_PREEMPT_RT !CONFIG_PREEMPT_RT_FULL"

AUTOINSTALL=yes

MAKE[0]="env NV_VERBOSE=1 \
    make ${{parallel_jobs+-j$parallel_jobs}} modules KERNEL_UNAME=${{kernelver}}"
CLEAN="make KERNEL_UNAME=${{kernelver}} clean"

BUILT_MODULE_NAME[0]="nvidia"
DEST_MODULE_NAME[0]="$PACKAGE_NAME"
DEST_MODULE_LOCATION[0]="/updates/dkms"

BUILT_MODULE_NAME[1]="nvidia-modeset"
DEST_MODULE_NAME[1]="$PACKAGE_NAME-modeset"
DEST_MODULE_LOCATION[1]="/updates/dkms"

BUILT_MODULE_NAME[2]="nvidia-drm"
DEST_MODULE_NAME[2]="$PACKAGE_NAME-drm"
DEST_MODULE_LOCATION[2]="/updates/dkms"

BUILT_MODULE_NAME[3]="nvidia-uvm"
DEST_MODULE_NAME[3]="$PACKAGE_NAME-uvm"
DEST_MODULE_LOCATION[3]="/updates/dkms"

BUILT_MODULE_NAME[4]="nvidia-peermem"
DEST_MODULE_NAME[4]="$PACKAGE_NAME-peermem"
DEST_MODULE_LOCATION[4]="/updates/dkms"
"""

NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILE_PREQ = """README.txt"""

# end of nvidia-open-kernel-dkms

# nvidia-open-kernel-source

NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILE_PREQ = """kernel-open/*		usr/src/modules/nvidia-open-kernel/
extra_files/bug-script	usr/src/modules/nvidia-open-kernel/debian/
debian/changelog	usr/src/modules/nvidia-open-kernel/debian/
extra_files/control.models	usr/src/modules/nvidia-open-kernel/debian/
debian/copyright	usr/src/modules/nvidia-open-kernel/debian/
# debian/module/debian/*	usr/src/modules/nvidia-open-kernel/debian/"""

NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILE_PREQ = """README.txt
extra_files/build-open-module-packages.sh"""

# end of nvidia-open-kernel-source

# nvidia-kernel-support

NVIDIA_KERNEL_SUPPORT_INSTALL_FILE_PREQ = """extra_files/nvidia-load.conf			etc/nvidia/current/
extra_files/nvidia-modprobe.conf		etc/nvidia/current/
extra_files/nvidia-options.conf		etc/nvidia/current/
extra_files/nvidia-blacklists-nouveau.conf	etc/nvidia/current/"""

NVIDIA_KERNEL_SUPPORT_LINTIAN_FILE_PREQ = """# We do not build arch:all packages from the proprietary driver.
package-contains-no-arch-dependent-files"""

NVIDIA_KERNEL_SUPPORT_LINKS_FILE_PREQ = """etc/nvidia/current   etc/nvidia/nvidia-{DRIVER_VERSION_FULL}"""

NVIDIA_KERNEL_SUPPORT_POSTRM_FILE_PREQ = """#!/bin/sh
set -e


if [ "$1" = "remove" ] || [ "$1" = "purge" ] ; then

	# activate our trigger
	dpkg-trigger register-nvidia-alternative

fi

#DEBHELPER#"""

NVIDIA_KERNEL_SUPPORT_POSTINST_FILE_PREQ = """#!/bin/sh
set -e

if [ "$1" = "configure" ]
then

	if [ -f /etc/nvidia/current/nvidia-modprobe.conf.dpkg-old ] && [ ! -f /etc/nvidia/current/nvidia-modprobe.conf ]
	then

		# restore modprobe.conf erroneously obsoleted due to bugs in
		# debhelper (#994919) and dpkg (#995387), causing #994971
		mv -v /etc/nvidia/current/nvidia-modprobe.conf.dpkg-old /etc/nvidia/current/nvidia-modprobe.conf
		dpkg-trigger --no-await register-nvidia-alternative

	fi

fi

###DEBHELPER###"""

# end of nvidia-kernel-support

# nvidia-libopencl1

NVIDIA_LIBOPENCL1_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libOpenCL.so.1.0.0	usr/lib/${{DEB_HOST_MULTIARCH}}/"""

NVIDIA_LIBOPENCL1_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[i386]: specific-address-in-shared-library
hardening-no-bindnow
hardening-no-fortify-functions

# There are multiple vendors providing this library.
package-name-doesnt-match-sonames libOpenCL1

# The free libOpenCL.so.1 library is preferred.
symbols-declares-dependency-on-other-package ocl-icd-libopencl1 (libOpenCL.so.1) [symbols]
symbols-declares-dependency-on-other-package ocl-icd-libopencl1 (>= *) (libOpenCL.so.1) [symbols]
symbols-file-missing-build-depends-package-field"""

NVIDIA_LIBOPENCL1_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/libOpenCL.so.1.0.0	usr/lib/${{DEB_HOST_MULTIARCH}}/libOpenCL.so.1"""

# end of nvidia-libopencl1

# nvidia-modprobe

NVIDIA_MODPROBE_INSTALL_FILE_PREQ =  """nvidia-modprobe     /usr/bin/"""

NVIDIA_MODPROBE_LINTIAN_FILE_PREQ = """elevated-privileges 4755 root/root [usr/bin/nvidia-modprobe]"""

NVIDIA_MODPROBE_UDEV_FILE_PREQ = """# Make sure device nodes are present even when the DDX is not started for the Wayland/EGLStream case
KERNEL=="nvidia", RUN+="/usr/bin/bash -c '/usr/bin/mknod -Z -m 666 /dev/nvidiactl c $$(grep nvidia$ /proc/devices | cut -d \  -f 1) 255'"
KERNEL=="nvidia", RUN+="/usr/bin/bash -c 'for i in $$(cat /proc/driver/nvidia/gpus/*/information | grep Minor | cut -d \  -f 4); do /usr/bin/mknod -Z -m 666 /dev/nvidia$${{i}} c $$(grep nvidia$ /proc/devices | cut -d \  -f 1) $${{i}}; done'"
KERNEL=="nvidia_modeset", RUN+="/usr/bin/bash -c '/usr/bin/mknod -Z -m 666 /dev/nvidia-modeset c $$(grep nvidia$ /proc/devices | cut -d \  -f 1) 254'"
KERNEL=="nvidia_uvm", RUN+="/usr/bin/bash -c '/usr/bin/mknod -Z -m 666 /dev/nvidia-uvm c $$(grep nvidia-uvm /proc/devices | cut -d \  -f 1) 0'"
KERNEL=="nvidia_uvm", RUN+="/usr/bin/bash -c '/usr/bin/mknod -Z -m 666 /dev/nvidia-uvm-tools c $$(grep nvidia-uvm /proc/devices | cut -d \  -f 1) 1'"
ACTION=="add" DEVPATH=="/module/nvidia" SUBSYSTEM=="module" RUN+="/usr/bin/nvidia-smi"

"""

# end of nvidia-modprobe

# nvidia-opencl-common

NVIDIA_OPENCL_COMMON_INSTALL_FILE_PREQ =  """nvidia.icd	etc/OpenCL/vendors/"""

NVIDIA_OPENCL_COMMON_LINTIAN_FILE_PREQ = """# We do not build arch:all packages from the proprietary driver.
package-contains-no-arch-dependent-files"""

# end of nvidia-opencl-common

# nvidia-opencl-icd

NVIDIA_OPENCL_ICD_INSTALL_FILE_PREQ =  """#! /usr/bin/dh-exec
libnvidia-opencl.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

NVIDIA_OPENCL_ICD_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[i386]: specific-address-in-shared-library
spelling-error-in-binary
hardening-no-bindnow
[!arm64]: hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger

# There is no .so link.
symbols-file-missing-build-depends-package-field"""

NVIDIA_OPENCL_ICD_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-opencl.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libnvidia-opencl.so.1"""

# end of nvidia-opencl-icd

# nvidia-persistenced

NVIDIA_PERSISTENCED_INSTALL_FILE_PREQ = """extra_files/nvidia-persistenced-init/sysv/nvidia-persistenced   /etc/init.d/
extra_files/nvidia-persistenced-init/systemd/nvidia-persistenced.service /usr/lib/systemd/system/
nvidia-persistenced     /usr/bin/"""

NVIDIA_PERSISTENCED_LINTIAN_FILE_PREQ = """# Upstream uses /var/run/nvidia-persistenced in various locations.
adduser-with-home-var-run [postinst:*]
"""

NVIDIA_PERSISTENCED_POSTINST_FILE_PREQ = """#!/bin/sh
set -e

if [ "$1" = "configure" ]; then
     if ! getent passwd nvpd >/dev/null; then
       # Create ad-hoc system user/group
       adduser --system --group \
               --home /var/run/nvpd/ \
               --gecos 'NVIDIA Persistence Daemon' \
               --no-create-home \
               nvpd
     fi
fi

#DEBHELPER#
"""

# end of nvidia-persistenced

# nvidia-powerd

NVIDIA_POWERD_INSTALL_FILE_PREQ = """#nvidia-dbus.conf	usr/share/dbus-1/system.d/
nvidia-powerd		usr/sbin/"""

NVIDIA_POWERD_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
hardening-no-bindnow
hardening-no-fortify-functions
hardening-no-pie"""

NVIDIA_POWERD_EXAMPLES_FILE_PREQ = """nvidia-dbus.conf
systemd/system/nvidia-powerd.service"""

# end of nvidia-powerd

# nvidia-smi

NVIDIA_SMI_INSTALL_FILE_PREQ = """nvidia-smi	usr/lib/nvidia/current/
nvidia-smi.1.gz	usr/lib/nvidia/current/"""

NVIDIA_SMI_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions
hardening-no-pie

# The current setup involving multiple chained alternatives would be very
# hard to migrate to /usr/libexec.
executable-in-usr-lib"""

# end of nvidia-smi

# nvidia-suspend-common

NVIDIA_SUSPEND_COMMON_INSTALL_FILE_PREQ = """systemd/system/nvidia-suspend.service	usr/lib/systemd/system/
systemd/system/nvidia-hibernate.service	usr/lib/systemd/system/
systemd/system/nvidia-resume.service	usr/lib/systemd/system/
systemd/system-sleep/nvidia		usr/lib/systemd/system-sleep/
systemd/nvidia-sleep.sh			usr/bin/"""

NVIDIA_SUSPEND_COMMON_LINTIAN_FILE_PREQ = """# Names and locations required by the .service files.
no-manual-page [usr/bin/nvidia-sleep.sh]
script-with-language-extension [usr/bin/nvidia-sleep.sh]
executable-in-usr-lib [usr/lib/systemd/system-sleep/nvidia]

systemd-service-file-refers-to-unusual-wantedby-target systemd-hibernate.service [usr/lib/systemd/system/nvidia-hibernate.service]
systemd-service-file-refers-to-unusual-wantedby-target systemd-hibernate.service [usr/lib/systemd/system/nvidia-resume.service]
systemd-service-file-refers-to-unusual-wantedby-target systemd-suspend.service [usr/lib/systemd/system/nvidia-resume.service]
systemd-service-file-refers-to-unusual-wantedby-target systemd-suspend.service [usr/lib/systemd/system/nvidia-suspend.service]
systemd-service-file-missing-documentation-key [usr/lib/systemd/system/nvidia-hibernate.service]
systemd-service-file-missing-documentation-key [usr/lib/systemd/system/nvidia-resume.service]
systemd-service-file-missing-documentation-key [usr/lib/systemd/system/nvidia-suspend.service]

# We do not build arch:all packages from the proprietary driver.
package-contains-no-arch-dependent-files"""

# end of nvidia-suspend-common

# nvidia-settings

NVIDIA_SETTINGS_INSTALL_FILE_PREQ = """nvidia-settings				    usr/lib/nvidia/current/
extra_files/nvidia-settings.desktop			    usr/lib/nvidia/current/
nvidia-settings.1.gz		usr/lib/nvidia/current/
libnvidia-gtk2.so.{DRIVER_VERSION_FULL}                 usr/lib/nvidia/current/
libnvidia-gtk3.so.{DRIVER_VERSION_FULL}                 usr/lib/nvidia/current/
libnvidia-wayland-client.so.{DRIVER_VERSION_FULL}       usr/lib/nvidia/current/
nvidia-settings.png                         usr/share/icons/hicolor/128x128/apps/"""

NVIDIA_SETTINGS_LINTIAN_FILE_PREQ = """# The shared libraries are actually version-specific plugins.
package-name-doesnt-match-sonames
exit-in-shared-library
no-symbols-control-file

# The current setup involving multiple chained alternatives would be very
# hard to migrate to /usr/libexec.
executable-in-usr-lib
"""

# end of nvidia-settings

# nvidia-support

NVIDIA_SUPPORT_INSTALL_FILE_PREQ = """extra_files/check-for-mismatching-nvidia-module	usr/lib/nvidia/
extra_files/alternate-install-present		usr/lib/nvidia/
extra_files/pre-install				usr/lib/nvidia/
extra_files/check-for-conflicting-opengl-libraries	usr/lib/nvidia/
"""

NVIDIA_SUPPORT_CONFIG_FILE_PREQ = """#!/bin/sh
set -e

. /usr/share/debconf/confmodule

if [ "$1" = "configure" ]
then

	if	false && \
		[ -d /etc/X11 ] && \
		[ ! -f /etc/X11/nvidia.conf ] && \
		[ ! -f /etc/X11/xorg.conf ]
	then
		db_input high nvidia-support/create-nvidia-conf || true
		db_go
	fi

fi

#DEBHELPER#
"""

NVIDIA_SUPPORT_LINTIAN_FILE_PREQ = """# The check for mismatching nvidia kernel module version has been moved to a
# script that is called from several postinst scripts only.
debconf-is-not-a-registry [usr/lib/nvidia/check-for-mismatching-nvidia-module:6]
executable-in-usr-lib [usr/lib/nvidia/check-for-mismatching-nvidia-module]
unused-debconf-template nvidia-support/check-running-module-version [templates:*]
unused-debconf-template nvidia-support/last-mismatching-module-version [templates:*]
unused-debconf-template nvidia-support/warn-mismatching-module-version [templates:*]
unused-debconf-template nvidia-support/warn-nouveau-module-loaded [templates:*]

# The notes about needing a xorg.conf or leftover xorg.conf are displayed by
# xserver-xorg-video-nvidia.
unused-debconf-template nvidia-support/needs-xorg-conf-to-enable [templates:*]
unused-debconf-template nvidia-support/check-xorg-conf-on-removal [templates:*]
unused-debconf-template nvidia-support/removed-but-enabled-in-xorg-conf [templates:*]

# The script is shipped by several driver packages depending on us.
spare-manual-page [usr/share/man/man1/nvidia-bug-report.sh.1.gz]

# We do not build arch:all packages for the proprietary driver.
package-contains-no-arch-dependent-files

"""

NVIDIA_SUPPORT_MANPAGES_FILE_PREQ = """extra_files/nvidia-bug-report.sh.1"""

NVIDIA_SUPPORT_TEMPLATES_FILE_PREQ = """Template: nvidia-support/check-running-module-version
Type: boolean
Default: true
Description: for internal use
 Can be preseeded.  If set to false, disables the nouveau module check
 and nvidia module version check entirely.

Template: nvidia-support/last-mismatching-module-version
Type: string
Default: none
Description: for internal use
 Remembers the last version for which we displayed the warning, so that we
 warn only once for each version.

Template: nvidia-support/warn-mismatching-module-version
Type: error
Description: Mismatching nvidia kernel module loaded
 The NVIDIA driver that is being installed (version ${{new-version}})
 does not match the nvidia kernel module currently loaded
 (version ${{running-version}}).
 .
 The X server, OpenGL, and GPGPU applications may not work properly.
 .
 The easiest way to fix this is to reboot the machine once the
 installation has finished. You can also stop the X server (usually by
 stopping the login manager, e.g. gdm3, sddm, or xdm), manually unload the
 module ("modprobe -r nvidia"), and restart the X server.

Template: nvidia-support/warn-nouveau-module-loaded
Type: error
Description: Conflicting nouveau kernel module loaded
 The free nouveau kernel module is currently loaded and conflicts with the
 non-free nvidia kernel module.
 .
 The easiest way to fix this is to reboot the machine once the
 installation has finished.

Template: nvidia-support/needs-xorg-conf-to-enable
Type: note
Description: Manual configuration required to enable NVIDIA driver
 The NVIDIA driver is not yet configured; it needs to be enabled in
 xorg.conf before it can be used.
 .
 Please see the package documentation for instructions.

Template: nvidia-support/check-xorg-conf-on-removal
Type: boolean
Default: true
Description: for internal use
 Can be preseeded.  If set to false, does not warn about fglrx still being
 enabled in xorg.conf(.d/) when removing the package.

Template: nvidia-support/removed-but-enabled-in-xorg-conf
Type: error
Description: NVIDIA driver is still enabled in xorg.conf
 The NVIDIA driver was just removed, but it is still enabled in the
 Xorg configuration. X cannot be (re-)started successfully until NVIDIA
 is disabled.
"""

NVIDIA_SUPPORT_POSTRM_FILE_PREQ = """#!/bin/sh
set -e

if [ "$1" = "purge" ]
then

	rm -f /etc/X11/nvidia.conf

fi

#DEBHELPER#
"""

NVIDIA_SUPPORT_POSTINST_FILE_PREQ = """#!/bin/sh
set -e

# dummy postinst to ensure that the templates get imported and the config script is executed
. /usr/share/debconf/confmodule

#DEBHELPER#
"""

# end of nvidia-support

# nvidia-vdpau-driver

NVIDIA_VDPAU_DRIVER_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
libvdpau_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

NVIDIA_VDPAU_DRIVER_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
[i386]: binary-file-built-without-LFS-support
[i386 ppc64el]: specific-address-in-shared-library
hardening-no-bindnow
hardening-no-fortify-functions

# Lintian and debhelper disagree w.r.t. a library in a private directory.
package-has-unnecessary-activation-of-ldconfig-trigger"""

NVIDIA_VDPAU_DRIVER_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libvdpau_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libvdpau_nvidia.so.1"""

NVIDIA_VDPAU_DRIVER_DOCS_FILE_PREQ = """README.txt"""

# end of nvidia-vdpau-driver

# nvidia-vulkan-common

NVIDIA_VULKAN_COMMON_INSTALL_FILE_PREQ = """nvidia_icd.json	usr/share/vulkan/icd.d/
nvidia_layers.json	usr/share/vulkan/implicit_layer.d/"""

NVIDIA_VULKAN_COMMON_LINTIAN_FILE_PREQ = """# We do not build arch:all packages from the proprietary driver.
package-contains-no-arch-dependent-files"""

# end of nvidia-vulkan-common

# nvidia-vulkan-icd

# nvidia-vulkan-icd doesn't have any dh files

# end of nvidia-vulkan-icd

# nvidia-xconfig

NVIDIA_XCONFIG_INSTALL_FILE_PREQ = """nvidia-xconfig	usr/bin/
nvidia-xconfig.1.gz	usr/share/man/man1/"""

NVIDIA_XCONFIG_DIRS_FILE_PREQ = """etc/X11"""

# xserver-xorg-video-nvidia

XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
nvidia_drv.so		usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
libglxserver_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
extra_files/nvidia.ids		usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/
nvidia-drm-outputclass.conf	etc/nvidia/current/
extra_files/10-nvidia-amd64-module.conf     usr/share/X11/xorg.conf.d/"""

XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILE_PREQ = """# The NVIDIA license does not allow any form of modification.
spelling-error-in-binary
hardening-no-bindnow
hardening-no-fortify-functions"""

XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILE_PREQ = """#! /usr/bin/dh-exec
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libglxserver_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/libglxserver_nvidia.so
usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/nvidia_drv.so    usr/lib/nvidia/current/nvidia_drv.so"""

XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILE_PREQ = """README.txt"""

XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILE_PREQ = """#!/bin/sh
set -e

. /usr/share/debconf/confmodule

warn_about_remaining_xorg_configuration()
{{
	# allow to disable the check via preseeding
	db_get nvidia-support/check-xorg-conf-on-removal || true
	test "$RET" = "true" || return 0

	XORG_CONF=$(grep -l '^[^#]*nvidia' /etc/X11/xorg.conf /etc/X11/xorg.conf.d/*.conf 2>/dev/null || true)

	test -n "$XORG_CONF" || return 0

	db_subst nvidia-support/removed-but-enabled-in-xorg-conf config-files "$XORG_CONF"
	db_fset nvidia-support/removed-but-enabled-in-xorg-conf seen false
	db_input high nvidia-support/removed-but-enabled-in-xorg-conf || true
	db_go

}}

if [ "$1" = "remove" ]; then

	warn_about_remaining_xorg_configuration

fi

#DEBHELPER#"""

XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILE_PREQ = """#!/bin/sh
set -e

. /usr/share/debconf/confmodule

if [ "$1" = "configure" ]
then

	if [ -x /usr/lib/nvidia/check-for-conflicting-opengl-libraries ]
	then
		/usr/lib/nvidia/check-for-conflicting-opengl-libraries
	fi

	if [ -x /usr/lib/nvidia/check-for-mismatching-nvidia-module ]
	then
		/usr/lib/nvidia/check-for-mismatching-nvidia-module {DRIVER_VERSION_FULL}
	fi

fi


#DEBHELPER#"""

# end of xserver-xorg-video-nvidia

### End of Text Preq


### Write files

# control
CONTROL_FILE_PATH = 'control'
with open(CONTROL_FILE_PATH, "w") as CONTROL_FILE:
    CONTROL_FILECONTENT = CONTROL_FILE_PREQ.format(
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    CONTROL_FILE.write(CONTROL_FILECONTENT)
# end of control

# Note: Not Upstream
# libnvidia-vksc-core

LIBNVIDIA_VKSC_CORE_INSTALL_FILE_PATH = 'libnvidia-vksc-core-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_VKSC_CORE_INSTALL_FILE_PATH, "w") as LIBNVIDIA_VKSC_CORE_INSTALL_FILE:
    LIBNVIDIA_VKSC_CORE_INSTALL_FILECONTENT = LIBNVIDIA_VKSC_CORE_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_VKSC_CORE_INSTALL_FILE.write(LIBNVIDIA_VKSC_CORE_INSTALL_FILECONTENT)
    
LIBNVIDIA_VKSC_CORE_LINTIAN_FILE_PATH = 'libnvidia-vksc-core-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_VKSC_CORE_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_VKSC_CORE_LINTIAN_FILE:
    LIBNVIDIA_VKSC_CORE_LINTIAN_FILECONTENT = LIBNVIDIA_VKSC_CORE_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_VKSC_CORE_LINTIAN_FILE.write(LIBNVIDIA_VKSC_CORE_LINTIAN_FILECONTENT)


# end of libnvidia-vksc-core
# End of note

# firmware-nvidia-gsp
FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PATH = 'firmware-nvidia-gsp-' + DRIVER_VERSION_MAJOR + '.install'
with open(FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PATH, "w") as FIRMWARE_NVIDIA_GSP_INSTALL_FILE:
    FIRMWARE_NVIDIA_GSP_INSTALL_FILECONTENT = FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    FIRMWARE_NVIDIA_GSP_INSTALL_FILE.write(FIRMWARE_NVIDIA_GSP_INSTALL_FILECONTENT)
    
FIRMWARE_NVIDIA_GSP_LINTIAN_FILE_PATH = 'firmware-nvidia-gsp-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(FIRMWARE_NVIDIA_GSP_LINTIAN_FILE_PATH, "w") as FIRMWARE_NVIDIA_GSP_LINTIAN_FILE:
    FIRMWARE_NVIDIA_GSP_LINTIAN_FILECONTENT = FIRMWARE_NVIDIA_GSP_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    FIRMWARE_NVIDIA_GSP_LINTIAN_FILE.write(FIRMWARE_NVIDIA_GSP_LINTIAN_FILECONTENT)

# end of firmware-nvidia-gsp

# libcuda1

LIBCUDA1_INSTALL_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBCUDA1_INSTALL_FILE_PATH, "w") as LIBCUDA1_INSTALL_FILE:
    LIBCUDA1_INSTALL_FILECONTENT = LIBCUDA1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBCUDA1_INSTALL_FILE.write(LIBCUDA1_INSTALL_FILECONTENT)

LIBCUDA1_LINTIAN_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBCUDA1_LINTIAN_FILE_PATH, "w") as LIBCUDA1_LINTIAN_FILE:
    LIBCUDA1_LINTIAN_FILECONTENT = LIBCUDA1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBCUDA1_LINTIAN_FILE.write(LIBCUDA1_LINTIAN_FILECONTENT)

LIBCUDA1_LINKS_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBCUDA1_LINKS_FILE_PATH, "w") as LIBCUDA1_LINKS_FILE:
    LIBCUDA1_LINKS_FILECONTENT = LIBCUDA1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBCUDA1_LINKS_FILE.write(LIBCUDA1_LINKS_FILECONTENT)

LIBCUDA1_POSTINST_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(LIBCUDA1_POSTINST_FILE_PATH, "w") as LIBCUDA1_POSTINST_FILE:
    LIBCUDA1_POSTINST_FILECONTENT = LIBCUDA1_POSTINST_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBCUDA1_POSTINST_FILE.write(LIBCUDA1_POSTINST_FILECONTENT)

# end of libcuda1

# libcudadebugger1

LIBCUDADEBUGGER1_INSTALL_FILE_PATH = 'libcudadebugger1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBCUDADEBUGGER1_INSTALL_FILE_PATH, "w") as LIBCUDADEBUGGER1_INSTALL_FILE:
    LIBCUDADEBUGGER1_INSTALL_FILECONTENT = LIBCUDADEBUGGER1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBCUDADEBUGGER1_INSTALL_FILE.write(LIBCUDADEBUGGER1_INSTALL_FILECONTENT)

LIBCUDADEBUGGER1_LINTIAN_FILE_PATH = 'libcudadebugger1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBCUDADEBUGGER1_LINTIAN_FILE_PATH, "w") as LIBCUDADEBUGGER1_LINTIAN_FILE:
    LIBCUDADEBUGGER1_LINTIAN_FILECONTENT = LIBCUDADEBUGGER1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBCUDADEBUGGER1_LINTIAN_FILE.write(LIBCUDADEBUGGER1_LINTIAN_FILECONTENT)

LIBCUDADEBUGGER1_LINKS_FILE_PATH = 'libcudadebugger1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBCUDADEBUGGER1_LINKS_FILE_PATH, "w") as LIBCUDADEBUGGER1_LINKS_FILE:
    LIBCUDADEBUGGER1_LINKS_FILECONTENT = LIBCUDADEBUGGER1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBCUDADEBUGGER1_LINKS_FILE.write(LIBCUDADEBUGGER1_LINKS_FILECONTENT)

# end of libcudadebugger1

# libegl-nvidia0

LIBEGL_NVIDIA0_INSTALL_FILE_PATH = 'libegl-nvidia0-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBEGL_NVIDIA0_INSTALL_FILE_PATH, "w") as LIBEGL_NVIDIA0_INSTALL_FILE:
    LIBEGL_NVIDIA0_INSTALL_FILECONTENT = LIBEGL_NVIDIA0_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBEGL_NVIDIA0_INSTALL_FILE.write(LIBEGL_NVIDIA0_INSTALL_FILECONTENT)

LIBEGL_NVIDIA0_LINTIAN_FILE_PATH = 'libegl-nvidia0-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBEGL_NVIDIA0_LINTIAN_FILE_PATH, "w") as LIBEGL_NVIDIA0_LINTIAN_FILE:
    LIBEGL_NVIDIA0_LINTIAN_FILECONTENT = LIBEGL_NVIDIA0_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBEGL_NVIDIA0_LINTIAN_FILE.write(LIBEGL_NVIDIA0_LINTIAN_FILECONTENT)

LIBEGL_NVIDIA0_LINKS_FILE_PATH = 'libegl-nvidia0-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBEGL_NVIDIA0_LINKS_FILE_PATH, "w") as LIBEGL_NVIDIA0_LINKS_FILE:
    LIBEGL_NVIDIA0_LINKS_FILECONTENT = LIBEGL_NVIDIA0_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBEGL_NVIDIA0_LINKS_FILE.write(LIBEGL_NVIDIA0_LINKS_FILECONTENT)

# end of libegl-nvidia0

# libgl1-nvidia-glvnd-glx

LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE_PATH = 'libgl1-nvidia-glvnd-glx-' + DRIVER_VERSION_MAJOR + '.docs'
with open(LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE_PATH, "w") as LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE:
    LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILECONTENT = LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE.write(LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILECONTENT)

# end of libgl1-nvidia-glvnd-glx

# libgles-nvidia1

LIBGLES_NVIDIA1_INSTALL_FILE_PATH = 'libgles-nvidia1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBGLES_NVIDIA1_INSTALL_FILE_PATH, "w") as LIBGLES_NVIDIA1_INSTALL_FILE:
    LIBGLES_NVIDIA1_INSTALL_FILECONTENT = LIBGLES_NVIDIA1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLES_NVIDIA1_INSTALL_FILE.write(LIBGLES_NVIDIA1_INSTALL_FILECONTENT)

LIBGLES_NVIDIA1_LINTIAN_FILE_PATH = 'libgles-nvidia1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBGLES_NVIDIA1_LINTIAN_FILE_PATH, "w") as LIBGLES_NVIDIA1_LINTIAN_FILE:
    LIBGLES_NVIDIA1_LINTIAN_FILECONTENT = LIBGLES_NVIDIA1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLES_NVIDIA1_LINTIAN_FILE.write(LIBGLES_NVIDIA1_LINTIAN_FILECONTENT)

LIBGLES_NVIDIA1_LINKS_FILE_PATH = 'libgles-nvidia1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBGLES_NVIDIA1_LINKS_FILE_PATH, "w") as LIBGLES_NVIDIA1_LINKS_FILE:
    LIBGLES_NVIDIA1_LINKS_FILECONTENT = LIBGLES_NVIDIA1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLES_NVIDIA1_LINKS_FILE.write(LIBGLES_NVIDIA1_LINKS_FILECONTENT)

# end libgles-nvidia1

# libgles-nvidia2

LIBGLES_NVIDIA2_INSTALL_FILE_PATH = 'libgles-nvidia2-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBGLES_NVIDIA2_INSTALL_FILE_PATH, "w") as LIBGLES_NVIDIA2_INSTALL_FILE:
    LIBGLES_NVIDIA2_INSTALL_FILECONTENT = LIBGLES_NVIDIA2_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLES_NVIDIA2_INSTALL_FILE.write(LIBGLES_NVIDIA2_INSTALL_FILECONTENT)

LIBGLES_NVIDIA2_LINTIAN_FILE_PATH = 'libgles-nvidia2-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBGLES_NVIDIA2_LINTIAN_FILE_PATH, "w") as LIBGLES_NVIDIA2_LINTIAN_FILE:
    LIBGLES_NVIDIA2_LINTIAN_FILECONTENT = LIBGLES_NVIDIA2_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLES_NVIDIA2_LINTIAN_FILE.write(LIBGLES_NVIDIA2_LINTIAN_FILECONTENT)

LIBGLES_NVIDIA2_LINKS_FILE_PATH = 'libgles-nvidia2-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBGLES_NVIDIA2_LINKS_FILE_PATH, "w") as LIBGLES_NVIDIA2_LINKS_FILE:
    LIBGLES_NVIDIA2_LINKS_FILECONTENT = LIBGLES_NVIDIA2_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLES_NVIDIA2_LINKS_FILE.write(LIBGLES_NVIDIA2_LINKS_FILECONTENT)

# end libgles-nvidia2

# libglx-nvidia0

LIBGLX_NVIDIA0_INSTALL_FILE_PATH = 'libglx-nvidia0-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBGLX_NVIDIA0_INSTALL_FILE_PATH, "w") as LIBGLX_NVIDIA0_INSTALL_FILE:
    LIBGLX_NVIDIA0_INSTALL_FILECONTENT = LIBGLX_NVIDIA0_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLX_NVIDIA0_INSTALL_FILE.write(LIBGLX_NVIDIA0_INSTALL_FILECONTENT)

LIBGLX_NVIDIA0_LINTIAN_FILE_PATH = 'libglx-nvidia0-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBGLX_NVIDIA0_LINTIAN_FILE_PATH, "w") as LIBGLX_NVIDIA0_LINTIAN_FILE:
    LIBGLX_NVIDIA0_LINTIAN_FILECONTENT = LIBGLX_NVIDIA0_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLX_NVIDIA0_LINTIAN_FILE.write(LIBGLX_NVIDIA0_LINTIAN_FILECONTENT)

LIBGLX_NVIDIA0_LINKS_FILE_PATH = 'libglx-nvidia0-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBGLX_NVIDIA0_LINKS_FILE_PATH, "w") as LIBGLX_NVIDIA0_LINKS_FILE:
    LIBGLX_NVIDIA0_LINKS_FILECONTENT = LIBGLX_NVIDIA0_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBGLX_NVIDIA0_LINKS_FILE.write(LIBGLX_NVIDIA0_LINKS_FILECONTENT)


# end of libglx-nvidia0

# libnvcuvid1

LIBNVCUVID1_INSTALL_FILE_PATH = 'libnvcuvid1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVCUVID1_INSTALL_FILE_PATH, "w") as LIBNVCUVID1_INSTALL_FILE:
    LIBNVCUVID1_INSTALL_FILECONTENT = LIBNVCUVID1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVCUVID1_INSTALL_FILE.write(LIBNVCUVID1_INSTALL_FILECONTENT)

LIBNVCUVID1_LINTIAN_FILE_PATH = 'libnvcuvid1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVCUVID1_LINTIAN_FILE_PATH, "w") as LIBNVCUVID1_LINTIAN_FILE:
    LIBNVCUVID1_LINTIAN_FILECONTENT = LIBNVCUVID1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVCUVID1_LINTIAN_FILE.write(LIBNVCUVID1_LINTIAN_FILECONTENT)

LIBNVCUVID1_LINKS_FILE_PATH = 'libnvcuvid1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVCUVID1_LINKS_FILE_PATH, "w") as LIBNVCUVID1_LINKS_FILE:
    LIBNVCUVID1_LINKS_FILECONTENT = LIBNVCUVID1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVCUVID1_LINKS_FILE.write(LIBNVCUVID1_LINKS_FILECONTENT)
    
# end of libnvcuvid1

# libnvidia-allocator1

LIBNVIDIA_ALLOCATOR1_INSTALL_FILE_PATH = 'libnvidia-allocator1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_ALLOCATOR1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_ALLOCATOR1_INSTALL_FILE:
    LIBNVIDIA_ALLOCATOR1_INSTALL_FILECONTENT = LIBNVIDIA_ALLOCATOR1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ALLOCATOR1_INSTALL_FILE.write(LIBNVIDIA_ALLOCATOR1_INSTALL_FILECONTENT)

LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE_PATH = 'libnvidia-allocator1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE:
    LIBNVIDIA_ALLOCATOR1_LINTIAN_FILECONTENT = LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE.write(LIBNVIDIA_ALLOCATOR1_LINTIAN_FILECONTENT)

LIBNVIDIA_ALLOCATOR1_LINKS_FILE_PATH = 'libnvidia-allocator1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_ALLOCATOR1_LINKS_FILE_PATH, "w") as LIBNVIDIA_ALLOCATOR1_LINKS_FILE:
    LIBNVIDIA_ALLOCATOR1_LINKS_FILECONTENT = LIBNVIDIA_ALLOCATOR1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ALLOCATOR1_LINKS_FILE.write(LIBNVIDIA_ALLOCATOR1_LINKS_FILECONTENT)

# end of libnvidia-allocator1

# libnvidia-api1

LIBNVIDIA_API1_INSTALL_FILE_PATH = 'libnvidia-api1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_API1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_API1_INSTALL_FILE:
    LIBNVIDIA_API1_INSTALL_FILECONTENT = LIBNVIDIA_API1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_API1_INSTALL_FILE.write(LIBNVIDIA_API1_INSTALL_FILECONTENT)

LIBNVIDIA_API1_LINTIAN_FILE_PATH = 'libnvidia-api1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_API1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_API1_LINTIAN_FILE:
    LIBNVIDIA_API1_LINTIAN_FILECONTENT = LIBNVIDIA_API1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_API1_LINTIAN_FILE.write(LIBNVIDIA_API1_LINTIAN_FILECONTENT)

# end of libnvidia-api1

# libnvidia-cfg1

LIBNVIDIA_CFG1_INSTALL_FILE_PATH = 'libnvidia-cfg1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_CFG1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_CFG1_INSTALL_FILE:
    LIBNVIDIA_CFG1_INSTALL_FILECONTENT = LIBNVIDIA_CFG1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_CFG1_INSTALL_FILE.write(LIBNVIDIA_CFG1_INSTALL_FILECONTENT)

LIBNVIDIA_CFG1_LINTIAN_FILE_PATH = 'libnvidia-cfg1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_CFG1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_CFG1_LINTIAN_FILE:
    LIBNVIDIA_CFG1_LINTIAN_FILECONTENT = LIBNVIDIA_CFG1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_CFG1_LINTIAN_FILE.write(LIBNVIDIA_CFG1_LINTIAN_FILECONTENT)

LIBNVIDIA_CFG1_LINKS_FILE_PATH = 'libnvidia-cfg1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_CFG1_LINKS_FILE_PATH, "w") as LIBNVIDIA_CFG1_LINKS_FILE:
    LIBNVIDIA_CFG1_LINKS_FILECONTENT = LIBNVIDIA_CFG1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_CFG1_LINKS_FILE.write(LIBNVIDIA_CFG1_LINKS_FILECONTENT)

# end of libnvidia-cfg1

# libnvidia-eglcore

LIBNVIDIA_EGLCORE_INSTALL_FILE_PATH = 'libnvidia-eglcore-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_EGLCORE_INSTALL_FILE_PATH, "w") as LIBNVIDIA_EGLCORE_INSTALL_FILE:
    LIBNVIDIA_EGLCORE_INSTALL_FILECONTENT = LIBNVIDIA_EGLCORE_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_EGLCORE_INSTALL_FILE.write(LIBNVIDIA_EGLCORE_INSTALL_FILECONTENT)

LIBNVIDIA_EGLCORE_LINTIAN_FILE_PATH = 'libnvidia-eglcore-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_EGLCORE_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_EGLCORE_LINTIAN_FILE:
    LIBNVIDIA_EGLCORE_LINTIAN_FILECONTENT = LIBNVIDIA_EGLCORE_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_EGLCORE_LINTIAN_FILE.write(LIBNVIDIA_EGLCORE_LINTIAN_FILECONTENT)

# end of libnvidia-eglcore

# libnvidia-encode1

LIBNVIDIA_ENCODE1_INSTALL_FILE_PATH = 'libnvidia-encode1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_ENCODE1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_ENCODE1_INSTALL_FILE:
    LIBNVIDIA_ENCODE1_INSTALL_FILECONTENT = LIBNVIDIA_ENCODE1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ENCODE1_INSTALL_FILE.write(LIBNVIDIA_ENCODE1_INSTALL_FILECONTENT)

LIBNVIDIA_ENCODE1_LINTIAN_FILE_PATH = 'libnvidia-encode1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_ENCODE1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_ENCODE1_LINTIAN_FILE:
    LIBNVIDIA_ENCODE1_LINTIAN_FILECONTENT = LIBNVIDIA_ENCODE1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ENCODE1_LINTIAN_FILE.write(LIBNVIDIA_ENCODE1_LINTIAN_FILECONTENT)

LIBNVIDIA_ENCODE1_LINKS_FILE_PATH = 'libnvidia-encode1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_ENCODE1_LINKS_FILE_PATH, "w") as LIBNVIDIA_ENCODE1_LINKS_FILE:
    LIBNVIDIA_ENCODE1_LINKS_FILECONTENT = LIBNVIDIA_ENCODE1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ENCODE1_LINKS_FILE.write(LIBNVIDIA_ENCODE1_LINKS_FILECONTENT)

# end of libnvidia-encode1

# libnvidia-fbc1

LIBNVIDIA_FBC1_INSTALL_FILE_PATH = 'libnvidia-fbc1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_FBC1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_FBC1_INSTALL_FILE:
    LIBNVIDIA_FBC1_INSTALL_FILECONTENT = LIBNVIDIA_FBC1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_FBC1_INSTALL_FILE.write(LIBNVIDIA_FBC1_INSTALL_FILECONTENT)

LIBNVIDIA_FBC1_LINTIAN_FILE_PATH = 'libnvidia-fbc1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_FBC1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_FBC1_LINTIAN_FILE:
    LIBNVIDIA_FBC1_LINTIAN_FILECONTENT = LIBNVIDIA_FBC1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_FBC1_LINTIAN_FILE.write(LIBNVIDIA_FBC1_LINTIAN_FILECONTENT)

LIBNVIDIA_FBC1_LINKS_FILE_PATH = 'libnvidia-fbc1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_FBC1_LINKS_FILE_PATH, "w") as LIBNVIDIA_FBC1_LINKS_FILE:
    LIBNVIDIA_FBC1_LINKS_FILECONTENT = LIBNVIDIA_FBC1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_FBC1_LINKS_FILE.write(LIBNVIDIA_FBC1_LINKS_FILECONTENT)
    
# end of libnvidia-fbc1

# libnvidia-glcore

LIBNVIDIA_GLCORE_INSTALL_FILE_PATH = 'libnvidia-glcore-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_GLCORE_INSTALL_FILE_PATH, "w") as LIBNVIDIA_GLCORE_INSTALL_FILE:
    LIBNVIDIA_GLCORE_INSTALL_FILECONTENT = LIBNVIDIA_GLCORE_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_GLCORE_INSTALL_FILE.write(LIBNVIDIA_GLCORE_INSTALL_FILECONTENT)

LIBNVIDIA_GLCORE_LINTIAN_FILE_PATH = 'libnvidia-glcore-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_GLCORE_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_GLCORE_LINTIAN_FILE:
    LIBNVIDIA_GLCORE_LINTIAN_FILECONTENT = LIBNVIDIA_GLCORE_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_GLCORE_LINTIAN_FILE.write(LIBNVIDIA_GLCORE_LINTIAN_FILECONTENT)
    
# end of libnvidia-glcore

# libnvidia-glvkspirv

LIBNVIDIA_GLVKSPIRV_INSTALL_FILE_PATH = 'libnvidia-glvkspirv-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_GLVKSPIRV_INSTALL_FILE_PATH, "w") as LIBNVIDIA_GLVKSPIRV_INSTALL_FILE:
    LIBNVIDIA_GLVKSPIRV_INSTALL_FILECONTENT = LIBNVIDIA_GLVKSPIRV_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_GLVKSPIRV_INSTALL_FILE.write(LIBNVIDIA_GLVKSPIRV_INSTALL_FILECONTENT)

LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE_PATH = 'libnvidia-glvkspirv-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE:
    LIBNVIDIA_GLVKSPIRV_LINTIAN_FILECONTENT = LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE.write(LIBNVIDIA_GLVKSPIRV_LINTIAN_FILECONTENT)
    
# end of libnvidia-glvkspirv

# libnvidia-gpucomp

LIBNVIDIA_GPUCOMP_INSTALL_FILE_PATH = 'libnvidia-gpucomp-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_GPUCOMP_INSTALL_FILE_PATH, "w") as LIBNVIDIA_GPUCOMP_INSTALL_FILE:
    LIBNVIDIA_GPUCOMP_INSTALL_FILECONTENT = LIBNVIDIA_GPUCOMP_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_GPUCOMP_INSTALL_FILE.write(LIBNVIDIA_GPUCOMP_INSTALL_FILECONTENT)

LIBNVIDIA_GPUCOMP_LINTIAN_FILE_PATH = 'libnvidia-gpucomp-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_GPUCOMP_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_GPUCOMP_LINTIAN_FILE:
    LIBNVIDIA_GPUCOMP_LINTIAN_FILECONTENT = LIBNVIDIA_GPUCOMP_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_GPUCOMP_LINTIAN_FILE.write(LIBNVIDIA_GPUCOMP_LINTIAN_FILECONTENT)
    
# end of libnvidia-gpucomp

# libnvidia-ml1

LIBNVIDIA_ML1_INSTALL_FILE_PATH = 'libnvidia-ml1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_ML1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_ML1_INSTALL_FILE:
    LIBNVIDIA_ML1_INSTALL_FILECONTENT = LIBNVIDIA_ML1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ML1_INSTALL_FILE.write(LIBNVIDIA_ML1_INSTALL_FILECONTENT)

LIBNVIDIA_ML1_LINTIAN_FILE_PATH = 'libnvidia-ml1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_ML1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_ML1_LINTIAN_FILE:
    LIBNVIDIA_ML1_LINTIAN_FILECONTENT = LIBNVIDIA_ML1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ML1_LINTIAN_FILE.write(LIBNVIDIA_ML1_LINTIAN_FILECONTENT)

LIBNVIDIA_ML1_LINKS_FILE_PATH = 'libnvidia-ml1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_ML1_LINKS_FILE_PATH, "w") as LIBNVIDIA_ML1_LINKS_FILE:
    LIBNVIDIA_ML1_LINKS_FILECONTENT = LIBNVIDIA_ML1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_ML1_LINKS_FILE.write(LIBNVIDIA_ML1_LINKS_FILECONTENT)
    
# end of libnvidia-ml1

# libnvidia-ngx1

LIBNVIDIA_NGX1_INSTALL_FILE_PATH = 'libnvidia-ngx1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_NGX1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_NGX1_INSTALL_FILE:
    LIBNVIDIA_NGX1_INSTALL_FILECONTENT = LIBNVIDIA_NGX1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_NGX1_INSTALL_FILE.write(LIBNVIDIA_NGX1_INSTALL_FILECONTENT)

LIBNVIDIA_NGX1_LINTIAN_FILE_PATH = 'libnvidia-ngx1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_NGX1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_NGX1_LINTIAN_FILE:
    LIBNVIDIA_NGX1_LINTIAN_FILECONTENT = LIBNVIDIA_NGX1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_NGX1_LINTIAN_FILE.write(LIBNVIDIA_NGX1_LINTIAN_FILECONTENT)

LIBNVIDIA_NGX1_LINKS_FILE_PATH = 'libnvidia-ngx1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_NGX1_LINKS_FILE_PATH, "w") as LIBNVIDIA_NGX1_LINKS_FILE:
    LIBNVIDIA_NGX1_LINKS_FILECONTENT = LIBNVIDIA_NGX1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_NGX1_LINKS_FILE.write(LIBNVIDIA_NGX1_LINKS_FILECONTENT)
    
# end of libnvidia-ngx1

# libnvidia-nvvm4

LIBNVIDIA_NVVM4_INSTALL_FILE_PATH = 'libnvidia-nvvm4-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_NVVM4_INSTALL_FILE_PATH, "w") as LIBNVIDIA_NVVM4_INSTALL_FILE:
    LIBNVIDIA_NVVM4_INSTALL_FILECONTENT = LIBNVIDIA_NVVM4_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_NVVM4_INSTALL_FILE.write(LIBNVIDIA_NVVM4_INSTALL_FILECONTENT)

LIBNVIDIA_NVVM4_LINTIAN_FILE_PATH = 'libnvidia-nvvm4-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_NVVM4_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_NVVM4_LINTIAN_FILE:
    LIBNVIDIA_NVVM4_LINTIAN_FILECONTENT = LIBNVIDIA_NVVM4_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_NVVM4_LINTIAN_FILE.write(LIBNVIDIA_NVVM4_LINTIAN_FILECONTENT)

LIBNVIDIA_NVVM4_LINKS_FILE_PATH = 'libnvidia-nvvm4-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_NVVM4_LINKS_FILE_PATH, "w") as LIBNVIDIA_NVVM4_LINKS_FILE:
    LIBNVIDIA_NVVM4_LINKS_FILECONTENT = LIBNVIDIA_NVVM4_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_NVVM4_LINKS_FILE.write(LIBNVIDIA_NVVM4_LINKS_FILECONTENT)
    
# end of libnvidia-nvvm4

# libnvidia-opticalflow1

LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE_PATH = 'libnvidia-opticalflow1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE:
    LIBNVIDIA_OPTICALFLOW1_INSTALL_FILECONTENT = LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE.write(LIBNVIDIA_OPTICALFLOW1_INSTALL_FILECONTENT)

LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE_PATH = 'libnvidia-opticalflow1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE:
    LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILECONTENT = LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE.write(LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILECONTENT)

LIBNVIDIA_OPTICALFLOW1_LINKS_FILE_PATH = 'libnvidia-opticalflow1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_OPTICALFLOW1_LINKS_FILE_PATH, "w") as LIBNVIDIA_OPTICALFLOW1_LINKS_FILE:
    LIBNVIDIA_OPTICALFLOW1_LINKS_FILECONTENT = LIBNVIDIA_OPTICALFLOW1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_OPTICALFLOW1_LINKS_FILE.write(LIBNVIDIA_OPTICALFLOW1_LINKS_FILECONTENT)
    
# end of libnvidia-opticalflow1

# libnvidia-pkcs11-openssl3

LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE_PATH = 'libnvidia-pkcs11-openssl3-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE_PATH, "w") as LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE:
    LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILECONTENT = LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE.write(LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILECONTENT)

LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE_PATH = 'libnvidia-pkcs11-openssl3-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE:
    LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILECONTENT = LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE.write(LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILECONTENT)
    
# end of libnvidia-pkcs11-openssl3

# libnvidia-ptxjitcompiler1

LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE_PATH = 'libnvidia-ptxjitcompiler1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE:
    LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILECONTENT = LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE.write(LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILECONTENT)

LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE_PATH = 'libnvidia-ptxjitcompiler1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE:
    LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILECONTENT = LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE.write(LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILECONTENT)

LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE_PATH = 'libnvidia-ptxjitcompiler1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE_PATH, "w") as LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE:
    LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILECONTENT = LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE.write(LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILECONTENT)
    
# end of libnvidia-ptxjitcompiler1

# libnvidia-rtcore

LIBNVIDIA_RTCORE_INSTALL_FILE_PATH = 'libnvidia-rtcore-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_RTCORE_INSTALL_FILE_PATH, "w") as LIBNVIDIA_RTCORE_INSTALL_FILE:
    LIBNVIDIA_RTCORE_INSTALL_FILECONTENT = LIBNVIDIA_RTCORE_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_RTCORE_INSTALL_FILE.write(LIBNVIDIA_RTCORE_INSTALL_FILECONTENT)

LIBNVIDIA_RTCORE_LINTIAN_FILE_PATH = 'libnvidia-rtcore-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_RTCORE_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_RTCORE_LINTIAN_FILE:
    LIBNVIDIA_RTCORE_LINTIAN_FILECONTENT = LIBNVIDIA_RTCORE_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVIDIA_RTCORE_LINTIAN_FILE.write(LIBNVIDIA_RTCORE_LINTIAN_FILECONTENT)
    
# end of libnvidia-rtcore

# libnvoptix1

LIBNVOPTIX1_INSTALL_FILE_PATH = 'libnvoptix1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVOPTIX1_INSTALL_FILE_PATH, "w") as LIBNVOPTIX1_INSTALL_FILE:
    LIBNVOPTIX1_INSTALL_FILECONTENT = LIBNVOPTIX1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVOPTIX1_INSTALL_FILE.write(LIBNVOPTIX1_INSTALL_FILECONTENT)

LIBNVOPTIX1_LINTIAN_FILE_PATH = 'libnvoptix1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVOPTIX1_LINTIAN_FILE_PATH, "w") as LIBNVOPTIX1_LINTIAN_FILE:
    LIBNVOPTIX1_LINTIAN_FILECONTENT = LIBNVOPTIX1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVOPTIX1_LINTIAN_FILE.write(LIBNVOPTIX1_LINTIAN_FILECONTENT)

LIBNVOPTIX1_LINKS_FILE_PATH = 'libnvoptix1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVOPTIX1_LINKS_FILE_PATH, "w") as LIBNVOPTIX1_LINKS_FILE:
    LIBNVOPTIX1_LINKS_FILECONTENT = LIBNVOPTIX1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    LIBNVOPTIX1_LINKS_FILE.write(LIBNVOPTIX1_LINKS_FILECONTENT)
    
# end of libnvoptix1

# nvidia-alternative

NVIDIA_ALTERNATIVE_INSTALL_FILE_PATH = 'nvidia-alternative-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_ALTERNATIVE_INSTALL_FILE_PATH, "w") as NVIDIA_ALTERNATIVE_INSTALL_FILE:
    NVIDIA_ALTERNATIVE_INSTALL_FILECONTENT = NVIDIA_ALTERNATIVE_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_ALTERNATIVE_INSTALL_FILE.write(NVIDIA_ALTERNATIVE_INSTALL_FILECONTENT)

NVIDIA_ALTERNATIVE_DIRS_FILE_PATH = 'nvidia-alternative-' + DRIVER_VERSION_MAJOR + '.dirs'
with open(NVIDIA_ALTERNATIVE_DIRS_FILE_PATH, "w") as NVIDIA_ALTERNATIVE_DIRS_FILE:
    NVIDIA_ALTERNATIVE_DIRS_FILECONTENT = NVIDIA_ALTERNATIVE_DIRS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_ALTERNATIVE_DIRS_FILE.write(NVIDIA_ALTERNATIVE_DIRS_FILECONTENT)

NVIDIA_ALTERNATIVE_LINTIAN_FILE_PATH = 'nvidia-alternative-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_ALTERNATIVE_LINTIAN_FILE_PATH, "w") as NVIDIA_ALTERNATIVE_LINTIAN_FILE:
    NVIDIA_ALTERNATIVE_LINTIAN_FILECONTENT = NVIDIA_ALTERNATIVE_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DEB_HOST_MULTIARCH=DEB_HOST_MULTIARCH,
    )
    NVIDIA_ALTERNATIVE_LINTIAN_FILE.write(NVIDIA_ALTERNATIVE_LINTIAN_FILECONTENT)

NVIDIA_ALTERNATIVE_PRERM_FILE_PATH = 'nvidia-alternative-' + DRIVER_VERSION_MAJOR + '.prerm'
with open(NVIDIA_ALTERNATIVE_PRERM_FILE_PATH, "w") as NVIDIA_ALTERNATIVE_PRERM_FILE:
    NVIDIA_ALTERNATIVE_PRERM_FILECONTENT = NVIDIA_ALTERNATIVE_PRERM_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_ALTERNATIVE_PRERM_FILE.write(NVIDIA_ALTERNATIVE_PRERM_FILECONTENT)

NVIDIA_ALTERNATIVE_POSTINST_FILE_PATH = 'nvidia-alternative-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(NVIDIA_ALTERNATIVE_POSTINST_FILE_PATH, "w") as NVIDIA_ALTERNATIVE_POSTINST_FILE:
    NVIDIA_ALTERNATIVE_POSTINST_FILECONTENT = NVIDIA_ALTERNATIVE_POSTINST_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
        DEB_HOST_MULTIARCH=DEB_HOST_MULTIARCH,
    )
    NVIDIA_ALTERNATIVE_POSTINST_FILE.write(NVIDIA_ALTERNATIVE_POSTINST_FILECONTENT)

NVIDIA_ALTERNATIVE_TRIGGERS_FILE_PATH = 'nvidia-alternative-' + DRIVER_VERSION_MAJOR + '.triggers'
with open(NVIDIA_ALTERNATIVE_TRIGGERS_FILE_PATH, "w") as NVIDIA_ALTERNATIVE_TRIGGERS_FILE:
    NVIDIA_ALTERNATIVE_TRIGGERS_FILECONTENT = NVIDIA_ALTERNATIVE_TRIGGERS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_ALTERNATIVE_TRIGGERS_FILE.write(NVIDIA_ALTERNATIVE_TRIGGERS_FILECONTENT)

# end of nvidia-alternative

# nvidia-cuda-mps

NVIDIA_CUDA_MPS_INSTALL_FILE_PATH = 'nvidia-cuda-mps-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_CUDA_MPS_INSTALL_FILE_PATH, "w") as NVIDIA_CUDA_MPS_INSTALL_FILE:
    NVIDIA_CUDA_MPS_INSTALL_FILECONTENT = NVIDIA_CUDA_MPS_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_CUDA_MPS_INSTALL_FILE.write(NVIDIA_CUDA_MPS_INSTALL_FILECONTENT)

NVIDIA_CUDA_MPS_LINTIAN_FILE_PATH = 'nvidia-cuda-mps-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_CUDA_MPS_LINTIAN_FILE_PATH, "w") as NVIDIA_CUDA_MPS_LINTIAN_FILE:
    NVIDIA_CUDA_MPS_LINTIAN_FILECONTENT = NVIDIA_CUDA_MPS_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_CUDA_MPS_LINTIAN_FILE.write(NVIDIA_CUDA_MPS_LINTIAN_FILECONTENT)

NVIDIA_CUDA_MPS_LINKS_FILE_PATH = 'nvidia-cuda-mps-' + DRIVER_VERSION_MAJOR + '.links'
with open(NVIDIA_CUDA_MPS_LINKS_FILE_PATH, "w") as NVIDIA_CUDA_MPS_LINKS_FILE:
    NVIDIA_CUDA_MPS_LINKS_FILECONTENT = NVIDIA_CUDA_MPS_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_CUDA_MPS_LINKS_FILE.write(NVIDIA_CUDA_MPS_LINKS_FILECONTENT)

NVIDIA_CUDA_MPS_MANPAGES_FILE_PATH = 'nvidia-cuda-mps-' + DRIVER_VERSION_MAJOR + '.manpages'
with open(NVIDIA_CUDA_MPS_MANPAGES_FILE_PATH, "w") as NVIDIA_CUDA_MPS_MANPAGES_FILE:
    NVIDIA_CUDA_MPS_MANPAGES_FILECONTENT = NVIDIA_CUDA_MPS_MANPAGES_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_CUDA_MPS_MANPAGES_FILE.write(NVIDIA_CUDA_MPS_MANPAGES_FILECONTENT)
    
NVIDIA_CUDA_MPS_DIRS_FILE_PATH = 'nvidia-cuda-mps-' + DRIVER_VERSION_MAJOR + '.dirs'
with open(NVIDIA_CUDA_MPS_DIRS_FILE_PATH, "w") as NVIDIA_CUDA_MPS_DIRS_FILE:
    NVIDIA_CUDA_MPS_DIRS_FILECONTENT = NVIDIA_CUDA_MPS_DIRS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_CUDA_MPS_DIRS_FILE.write(NVIDIA_CUDA_MPS_DIRS_FILECONTENT)
    
# end of nvidia-cuda-mps

# nvidia-driver

NVIDIA_DRIVER_DOCS_FILE_PATH = 'nvidia-driver-' + DRIVER_VERSION_MAJOR + '.docs'
with open(NVIDIA_DRIVER_DOCS_FILE_PATH, "w") as NVIDIA_DRIVER_DOCS_FILE:
    NVIDIA_DRIVER_DOCS_FILECONTENT = NVIDIA_DRIVER_DOCS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_DRIVER_DOCS_FILE.write(NVIDIA_DRIVER_DOCS_FILECONTENT)
    
# end of nvidia-driver

# nvidia-open-driver

NVIDIA_OPEN_DRIVER_DOCS_FILE_PATH = 'nvidia-open-driver-' + DRIVER_VERSION_MAJOR + '.docs'
with open(NVIDIA_OPEN_DRIVER_DOCS_FILE_PATH, "w") as NVIDIA_OPEN_DRIVER_DOCS_FILE:
    NVIDIA_OPEN_DRIVER_DOCS_FILECONTENT = NVIDIA_OPEN_DRIVER_DOCS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_DRIVER_DOCS_FILE.write(NVIDIA_OPEN_DRIVER_DOCS_FILECONTENT)
    
# end of nvidia-open-driver

# nvidia-driver-bin

NVIDIA_DRIVER_BIN_INSTALL_FILE_PATH = 'nvidia-driver-bin-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_DRIVER_BIN_INSTALL_FILE_PATH, "w") as NVIDIA_DRIVER_BIN_INSTALL_FILE:
    NVIDIA_DRIVER_BIN_INSTALL_FILECONTENT = NVIDIA_DRIVER_BIN_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_DRIVER_BIN_INSTALL_FILE.write(NVIDIA_DRIVER_BIN_INSTALL_FILECONTENT)

NVIDIA_DRIVER_BIN_LINTIAN_FILE_PATH = 'nvidia-driver-bin-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_DRIVER_BIN_LINTIAN_FILE_PATH, "w") as NVIDIA_DRIVER_BIN_LINTIAN_FILE:
    NVIDIA_DRIVER_BIN_LINTIAN_FILECONTENT = NVIDIA_DRIVER_BIN_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_DRIVER_BIN_LINTIAN_FILE.write(NVIDIA_DRIVER_BIN_LINTIAN_FILECONTENT)
    
# end of nvidia-driver-bin

# nvidia-driver-libs

NVIDIA_DRIVER_LIBS_LINTIAN_FILE_PATH = 'nvidia-driver-libs-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_DRIVER_LIBS_LINTIAN_FILE_PATH, "w") as NVIDIA_DRIVER_LIBS_LINTIAN_FILE:
    NVIDIA_DRIVER_LIBS_LINTIAN_FILECONTENT = NVIDIA_DRIVER_LIBS_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_DRIVER_LIBS_LINTIAN_FILE.write(NVIDIA_DRIVER_LIBS_LINTIAN_FILECONTENT)
    
NVIDIA_DRIVER_LIBS_POSTINST_FILE_PATH = 'nvidia-driver-libs-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(NVIDIA_DRIVER_LIBS_POSTINST_FILE_PATH, "w") as NVIDIA_DRIVER_LIBS_POSTINST_FILE:
    NVIDIA_DRIVER_LIBS_POSTINST_FILECONTENT = NVIDIA_DRIVER_LIBS_POSTINST_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_DRIVER_LIBS_POSTINST_FILE.write(NVIDIA_DRIVER_LIBS_POSTINST_FILECONTENT)
    
# end of nvidia-driver-libs

# nvidia-egl-common

NVIDIA_EGL_COMMON_INSTALL_FILE_PATH = 'nvidia-egl-common-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_EGL_COMMON_INSTALL_FILE_PATH, "w") as NVIDIA_EGL_COMMON_INSTALL_FILE:
    NVIDIA_EGL_COMMON_INSTALL_FILECONTENT = NVIDIA_EGL_COMMON_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_EGL_COMMON_INSTALL_FILE.write(NVIDIA_EGL_COMMON_INSTALL_FILECONTENT)

NVIDIA_EGL_COMMON_LINTIAN_FILE_PATH = 'nvidia-egl-common-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_EGL_COMMON_LINTIAN_FILE_PATH, "w") as NVIDIA_EGL_COMMON_LINTIAN_FILE:
    NVIDIA_EGL_COMMON_LINTIAN_FILECONTENT = NVIDIA_EGL_COMMON_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_EGL_COMMON_LINTIAN_FILE.write(NVIDIA_EGL_COMMON_LINTIAN_FILECONTENT)
    
# end of nvidia-egl-common

# nvidia-egl-icd

# nvidia-egl-icd doesn't have any dh files

# end of nvidia-egl-icd

# nvidia-kernel-common

NVIDIA_KERNEL_COMMON_INSTALL_FILE_PATH = 'nvidia-kernel-common-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_KERNEL_COMMON_INSTALL_FILE_PATH, "w") as NVIDIA_KERNEL_COMMON_INSTALL_FILE:
    NVIDIA_KERNEL_COMMON_INSTALL_FILECONTENT = NVIDIA_KERNEL_COMMON_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_COMMON_INSTALL_FILE.write(NVIDIA_KERNEL_COMMON_INSTALL_FILECONTENT)

NVIDIA_KERNEL_COMMON_LINTIAN_FILE_PATH = 'nvidia-kernel-common-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_KERNEL_COMMON_LINTIAN_FILE_PATH, "w") as NVIDIA_KERNEL_COMMON_LINTIAN_FILE:
    NVIDIA_KERNEL_COMMON_LINTIAN_FILECONTENT = NVIDIA_KERNEL_COMMON_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_COMMON_LINTIAN_FILE.write(NVIDIA_KERNEL_COMMON_LINTIAN_FILECONTENT)

NVIDIA_KERNEL_COMMON_UDEV_FILE_PATH = 'nvidia-kernel-common-' + DRIVER_VERSION_MAJOR + '.udev'
with open(NVIDIA_KERNEL_COMMON_UDEV_FILE_PATH, "w") as NVIDIA_KERNEL_COMMON_UDEV_FILE:
    NVIDIA_KERNEL_COMMON_UDEV_FILECONTENT = NVIDIA_KERNEL_COMMON_UDEV_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_COMMON_UDEV_FILE.write(NVIDIA_KERNEL_COMMON_UDEV_FILECONTENT)
    
# end of nvidia-kernel-common

# nvidia-kernel-dkms

NVIDIA_KERNEL_DKMS_INSTALL_FILE_PATH = 'nvidia-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_KERNEL_DKMS_INSTALL_FILE_PATH, "w") as NVIDIA_KERNEL_DKMS_INSTALL_FILE:
    NVIDIA_KERNEL_DKMS_INSTALL_FILECONTENT = NVIDIA_KERNEL_DKMS_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_DKMS_INSTALL_FILE.write(NVIDIA_KERNEL_DKMS_INSTALL_FILECONTENT)

NVIDIA_KERNEL_DKMS_LINTIAN_FILE_PATH = 'nvidia-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_KERNEL_DKMS_LINTIAN_FILE_PATH, "w") as NVIDIA_KERNEL_DKMS_LINTIAN_FILE:
    NVIDIA_KERNEL_DKMS_LINTIAN_FILECONTENT = NVIDIA_KERNEL_DKMS_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_DKMS_LINTIAN_FILE.write(NVIDIA_KERNEL_DKMS_LINTIAN_FILECONTENT)

NVIDIA_KERNEL_DKMS_DKMS_FILE_PATH = 'nvidia-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.dkms'
with open(NVIDIA_KERNEL_DKMS_DKMS_FILE_PATH, "w") as NVIDIA_KERNEL_DKMS_DKMS_FILE:
    NVIDIA_KERNEL_DKMS_DKMS_FILECONTENT = NVIDIA_KERNEL_DKMS_DKMS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_DKMS_DKMS_FILE.write(NVIDIA_KERNEL_DKMS_DKMS_FILECONTENT)

NVIDIA_KERNEL_DKMS_DOCS_FILE_PATH = 'nvidia-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.docs'
with open(NVIDIA_KERNEL_DKMS_DOCS_FILE_PATH, "w") as NVIDIA_KERNEL_DKMS_DOCS_FILE:
    NVIDIA_KERNEL_DKMS_DOCS_FILECONTENT = NVIDIA_KERNEL_DKMS_DOCS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_DKMS_DOCS_FILE.write(NVIDIA_KERNEL_DKMS_DOCS_FILECONTENT)
    
# end of nvidia-kernel-dkms

# nvidia-kernel-source

NVIDIA_KERNEL_SOURCE_INSTALL_FILE_PATH = 'nvidia-kernel-source-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_KERNEL_SOURCE_INSTALL_FILE_PATH, "w") as NVIDIA_KERNEL_SOURCE_INSTALL_FILE:
    NVIDIA_KERNEL_SOURCE_INSTALL_FILECONTENT = NVIDIA_KERNEL_SOURCE_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_SOURCE_INSTALL_FILE.write(NVIDIA_KERNEL_SOURCE_INSTALL_FILECONTENT)

NVIDIA_KERNEL_SOURCE_DOCS_FILE_PATH = 'nvidia-kernel-source-' + DRIVER_VERSION_MAJOR + '.docs'
with open(NVIDIA_KERNEL_SOURCE_DOCS_FILE_PATH, "w") as NVIDIA_KERNEL_SOURCE_DOCS_FILE:
    NVIDIA_KERNEL_SOURCE_DOCS_FILECONTENT = NVIDIA_KERNEL_SOURCE_DOCS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_SOURCE_DOCS_FILE.write(NVIDIA_KERNEL_SOURCE_DOCS_FILECONTENT)
    
# end of nvidia-kernel-source

# nvidia-open-kernel-common

NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILE_PATH = 'nvidia-open-kernel-common-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILE:
    NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILECONTENT = NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILE.write(NVIDIA_OPEN_KERNEL_COMMON_INSTALL_FILECONTENT)

NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILE_PATH = 'nvidia-open-kernel-common-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILE:
    NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILECONTENT = NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILE.write(NVIDIA_OPEN_KERNEL_COMMON_LINTIAN_FILECONTENT)

NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILE_PATH = 'nvidia-open-kernel-common-' + DRIVER_VERSION_MAJOR + '.udev'
with open(NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILE:
    NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILECONTENT = NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILE.write(NVIDIA_OPEN_KERNEL_COMMON_UDEV_FILECONTENT)
    
# end of nvidia-open-kernel-common

# nvidia-open-kernel-dkms

NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILE_PATH = 'nvidia-open-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILE:
    NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILECONTENT = NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILE.write(NVIDIA_OPEN_KERNEL_DKMS_INSTALL_FILECONTENT)

NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILE_PATH = 'nvidia-open-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILE:
    NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILECONTENT = NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILE.write(NVIDIA_OPEN_KERNEL_DKMS_LINTIAN_FILECONTENT)

NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILE_PATH = 'nvidia-open-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.dkms'
with open(NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILE:
    NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILECONTENT = NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILE.write(NVIDIA_OPEN_KERNEL_DKMS_DKMS_FILECONTENT)

NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILE_PATH = 'nvidia-open-kernel-dkms-' + DRIVER_VERSION_MAJOR + '.docs'
with open(NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILE:
    NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILECONTENT = NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILE.write(NVIDIA_OPEN_KERNEL_DKMS_DOCS_FILECONTENT)
    
# end of nvidia-open-kernel-dkms

# nvidia-open-kernel-source

NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILE_PATH = 'nvidia-open-kernel-source-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILE:
    NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILECONTENT = NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILE.write(NVIDIA_OPEN_KERNEL_SOURCE_INSTALL_FILECONTENT)

NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILE_PATH = 'nvidia-open-kernel-source-' + DRIVER_VERSION_MAJOR + '.docs'
with open(NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILE_PATH, "w") as NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILE:
    NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILECONTENT = NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILE.write(NVIDIA_OPEN_KERNEL_SOURCE_DOCS_FILECONTENT)
    
# end of nvidia-open-kernel-source

# nvidia-kernel-support

NVIDIA_KERNEL_SUPPORT_INSTALL_FILE_PATH = 'nvidia-kernel-support-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_KERNEL_SUPPORT_INSTALL_FILE_PATH, "w") as NVIDIA_KERNEL_SUPPORT_INSTALL_FILE:
    NVIDIA_KERNEL_SUPPORT_INSTALL_FILECONTENT = NVIDIA_KERNEL_SUPPORT_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_SUPPORT_INSTALL_FILE.write(NVIDIA_KERNEL_SUPPORT_INSTALL_FILECONTENT)

NVIDIA_KERNEL_SUPPORT_LINTIAN_FILE_PATH = 'nvidia-kernel-support-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_KERNEL_SUPPORT_LINTIAN_FILE_PATH, "w") as NVIDIA_KERNEL_SUPPORT_LINTIAN_FILE:
    NVIDIA_KERNEL_SUPPORT_LINTIAN_FILECONTENT = NVIDIA_KERNEL_SUPPORT_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_SUPPORT_LINTIAN_FILE.write(NVIDIA_KERNEL_SUPPORT_LINTIAN_FILECONTENT)

NVIDIA_KERNEL_SUPPORT_LINKS_FILE_PATH = 'nvidia-kernel-support-' + DRIVER_VERSION_MAJOR + '.links'
with open(NVIDIA_KERNEL_SUPPORT_LINKS_FILE_PATH, "w") as NVIDIA_KERNEL_SUPPORT_LINKS_FILE:
    NVIDIA_KERNEL_SUPPORT_LINKS_FILECONTENT = NVIDIA_KERNEL_SUPPORT_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_SUPPORT_LINKS_FILE.write(NVIDIA_KERNEL_SUPPORT_LINKS_FILECONTENT)
    
NVIDIA_KERNEL_SUPPORT_POSTRM_FILE_PATH = 'nvidia-kernel-support-' + DRIVER_VERSION_MAJOR + '.postrm'
with open(NVIDIA_KERNEL_SUPPORT_POSTRM_FILE_PATH, "w") as NVIDIA_KERNEL_SUPPORT_POSTRM_FILE:
    NVIDIA_KERNEL_SUPPORT_POSTRM_FILECONTENT = NVIDIA_KERNEL_SUPPORT_POSTRM_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_SUPPORT_POSTRM_FILE.write(NVIDIA_KERNEL_SUPPORT_POSTRM_FILECONTENT)
    
NVIDIA_KERNEL_SUPPORT_POSTINST_FILE_PATH = 'nvidia-kernel-support-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(NVIDIA_KERNEL_SUPPORT_POSTINST_FILE_PATH, "w") as NVIDIA_KERNEL_SUPPORT_POSTINST_FILE:
    NVIDIA_KERNEL_SUPPORT_POSTINST_FILECONTENT = NVIDIA_KERNEL_SUPPORT_POSTINST_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_KERNEL_SUPPORT_POSTINST_FILE.write(NVIDIA_KERNEL_SUPPORT_POSTINST_FILECONTENT)
    
# end of nvidia-kernel-support

# nvidia-libopencl1

NVIDIA_LIBOPENCL1_INSTALL_FILE_PATH = 'nvidia-libopencl1-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_LIBOPENCL1_INSTALL_FILE_PATH, "w") as NVIDIA_LIBOPENCL1_INSTALL_FILE:
    NVIDIA_LIBOPENCL1_INSTALL_FILECONTENT = NVIDIA_LIBOPENCL1_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_LIBOPENCL1_INSTALL_FILE.write(NVIDIA_LIBOPENCL1_INSTALL_FILECONTENT)

NVIDIA_LIBOPENCL1_LINTIAN_FILE_PATH = 'nvidia-libopencl1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_LIBOPENCL1_LINTIAN_FILE_PATH, "w") as NVIDIA_LIBOPENCL1_LINTIAN_FILE:
    NVIDIA_LIBOPENCL1_LINTIAN_FILECONTENT = NVIDIA_LIBOPENCL1_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_LIBOPENCL1_LINTIAN_FILE.write(NVIDIA_LIBOPENCL1_LINTIAN_FILECONTENT)

NVIDIA_LIBOPENCL1_LINKS_FILE_PATH = 'nvidia-libopencl1-' + DRIVER_VERSION_MAJOR + '.links'
with open(NVIDIA_LIBOPENCL1_LINKS_FILE_PATH, "w") as NVIDIA_LIBOPENCL1_LINKS_FILE:
    NVIDIA_LIBOPENCL1_LINKS_FILECONTENT = NVIDIA_LIBOPENCL1_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_LIBOPENCL1_LINKS_FILE.write(NVIDIA_LIBOPENCL1_LINKS_FILECONTENT)
    
# end of nvidia-libopencl1

# nvidia-modprobe

NVIDIA_MODPROBE_INSTALL_FILE_PATH = 'nvidia-modprobe-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_MODPROBE_INSTALL_FILE_PATH, "w") as NVIDIA_MODPROBE_INSTALL_FILE:
    NVIDIA_MODPROBE_INSTALL_FILECONTENT = NVIDIA_MODPROBE_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_MODPROBE_INSTALL_FILE.write(NVIDIA_MODPROBE_INSTALL_FILECONTENT)

NVIDIA_MODPROBE_LINTIAN_FILE_PATH = 'nvidia-modprobe-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_MODPROBE_LINTIAN_FILE_PATH, "w") as NVIDIA_MODPROBE_LINTIAN_FILE:
    NVIDIA_MODPROBE_LINTIAN_FILECONTENT = NVIDIA_MODPROBE_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_MODPROBE_LINTIAN_FILE.write(NVIDIA_MODPROBE_LINTIAN_FILECONTENT)
    
NVIDIA_MODPROBE_UDEV_FILE_PATH = 'nvidia-modprobe-' + DRIVER_VERSION_MAJOR + '.udev'
with open(NVIDIA_MODPROBE_UDEV_FILE_PATH, "w") as NVIDIA_MODPROBE_UDEV_FILE:
    NVIDIA_MODPROBE_UDEV_FILECONTENT = NVIDIA_MODPROBE_UDEV_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_MODPROBE_UDEV_FILE.write(NVIDIA_MODPROBE_UDEV_FILECONTENT)  
    
# end of nvidia-modprobe

# nvidia-opencl-common

NVIDIA_OPENCL_COMMON_INSTALL_FILE_PATH = 'nvidia-opencl-common-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_OPENCL_COMMON_INSTALL_FILE_PATH, "w") as NVIDIA_OPENCL_COMMON_INSTALL_FILE:
    NVIDIA_OPENCL_COMMON_INSTALL_FILECONTENT = NVIDIA_OPENCL_COMMON_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPENCL_COMMON_INSTALL_FILE.write(NVIDIA_OPENCL_COMMON_INSTALL_FILECONTENT)

NVIDIA_OPENCL_COMMON_LINTIAN_FILE_PATH = 'nvidia-opencl-common-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_OPENCL_COMMON_LINTIAN_FILE_PATH, "w") as NVIDIA_OPENCL_COMMON_LINTIAN_FILE:
    NVIDIA_OPENCL_COMMON_LINTIAN_FILECONTENT = NVIDIA_OPENCL_COMMON_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPENCL_COMMON_LINTIAN_FILE.write(NVIDIA_OPENCL_COMMON_LINTIAN_FILECONTENT)
    
# end of nvidia-opencl-common

# nvidia-opencl-icd

NVIDIA_OPENCL_ICD_INSTALL_FILE_PATH = 'nvidia-opencl-icd-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_OPENCL_ICD_INSTALL_FILE_PATH, "w") as NVIDIA_OPENCL_ICD_INSTALL_FILE:
    NVIDIA_OPENCL_ICD_INSTALL_FILECONTENT = NVIDIA_OPENCL_ICD_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPENCL_ICD_INSTALL_FILE.write(NVIDIA_OPENCL_ICD_INSTALL_FILECONTENT)

NVIDIA_OPENCL_ICD_LINTIAN_FILE_PATH = 'nvidia-opencl-icd-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_OPENCL_ICD_LINTIAN_FILE_PATH, "w") as NVIDIA_OPENCL_ICD_LINTIAN_FILE:
    NVIDIA_OPENCL_ICD_LINTIAN_FILECONTENT = NVIDIA_OPENCL_ICD_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPENCL_ICD_LINTIAN_FILE.write(NVIDIA_OPENCL_ICD_LINTIAN_FILECONTENT)

NVIDIA_OPENCL_ICD_LINKS_FILE_PATH = 'nvidia-opencl-icd-' + DRIVER_VERSION_MAJOR + '.links'
with open(NVIDIA_OPENCL_ICD_LINKS_FILE_PATH, "w") as NVIDIA_OPENCL_ICD_LINKS_FILE:
    NVIDIA_OPENCL_ICD_LINKS_FILECONTENT = NVIDIA_OPENCL_ICD_LINKS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_OPENCL_ICD_LINKS_FILE.write(NVIDIA_OPENCL_ICD_LINKS_FILECONTENT)
    
# end of nvidia-opencl-icd

# nvidia-persistenced

NVIDIA_PERSISTENCED_INSTALL_FILE_PATH = 'nvidia-persistenced-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_PERSISTENCED_INSTALL_FILE_PATH, "w") as NVIDIA_PERSISTENCED_INSTALL_FILE:
    NVIDIA_PERSISTENCED_INSTALL_FILECONTENT = NVIDIA_PERSISTENCED_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_PERSISTENCED_INSTALL_FILE.write(NVIDIA_PERSISTENCED_INSTALL_FILECONTENT)

NVIDIA_PERSISTENCED_LINTIAN_FILE_PATH = 'nvidia-persistenced-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_PERSISTENCED_LINTIAN_FILE_PATH, "w") as NVIDIA_PERSISTENCED_LINTIAN_FILE:
    NVIDIA_PERSISTENCED_LINTIAN_FILECONTENT = NVIDIA_PERSISTENCED_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_PERSISTENCED_LINTIAN_FILE.write(NVIDIA_PERSISTENCED_LINTIAN_FILECONTENT)
    
NVIDIA_PERSISTENCED_POSTINST_FILE_PATH = 'nvidia-persistenced-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(NVIDIA_PERSISTENCED_POSTINST_FILE_PATH, "w") as NVIDIA_PERSISTENCED_POSTINST_FILE:
    NVIDIA_PERSISTENCED_POSTINST_FILECONTENT = NVIDIA_PERSISTENCED_POSTINST_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_PERSISTENCED_POSTINST_FILE.write(NVIDIA_PERSISTENCED_POSTINST_FILECONTENT)
    
# end of nvidia-persistenced

# nvidia-powerd

NVIDIA_POWERD_INSTALL_FILE_PATH = 'nvidia-powerd-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_POWERD_INSTALL_FILE_PATH, "w") as NVIDIA_POWERD_INSTALL_FILE:
    NVIDIA_POWERD_INSTALL_FILECONTENT = NVIDIA_POWERD_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_POWERD_INSTALL_FILE.write(NVIDIA_POWERD_INSTALL_FILECONTENT)

NVIDIA_POWERD_LINTIAN_FILE_PATH = 'nvidia-powerd-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_POWERD_LINTIAN_FILE_PATH, "w") as NVIDIA_POWERD_LINTIAN_FILE:
    NVIDIA_POWERD_LINTIAN_FILECONTENT = NVIDIA_POWERD_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_POWERD_LINTIAN_FILE.write(NVIDIA_POWERD_LINTIAN_FILECONTENT)

NVIDIA_POWERD_EXAMPLES_FILE_PATH = 'nvidia-powerd-' + DRIVER_VERSION_MAJOR + '.examples'
with open(NVIDIA_POWERD_EXAMPLES_FILE_PATH, "w") as NVIDIA_POWERD_EXAMPLES_FILE:
    NVIDIA_POWERD_EXAMPLES_FILECONTENT = NVIDIA_POWERD_EXAMPLES_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_POWERD_EXAMPLES_FILE.write(NVIDIA_POWERD_EXAMPLES_FILECONTENT)
    
# end of nvidia-powerd

# nvidia-smi

NVIDIA_SMI_INSTALL_FILE_PATH = 'nvidia-smi-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_SMI_INSTALL_FILE_PATH, "w") as NVIDIA_SMI_INSTALL_FILE:
    NVIDIA_SMI_INSTALL_FILECONTENT = NVIDIA_SMI_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SMI_INSTALL_FILE.write(NVIDIA_SMI_INSTALL_FILECONTENT)

NVIDIA_SMI_LINTIAN_FILE_PATH = 'nvidia-smi-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_SMI_LINTIAN_FILE_PATH, "w") as NVIDIA_SMI_LINTIAN_FILE:
    NVIDIA_SMI_LINTIAN_FILECONTENT = NVIDIA_SMI_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SMI_LINTIAN_FILE.write(NVIDIA_SMI_LINTIAN_FILECONTENT)
    
# end of nvidia-smi

# nvidia-suspend-common

NVIDIA_SUSPEND_COMMON_INSTALL_FILE_PATH = 'nvidia-suspend-common-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_SUSPEND_COMMON_INSTALL_FILE_PATH, "w") as NVIDIA_SUSPEND_COMMON_INSTALL_FILE:
    NVIDIA_SUSPEND_COMMON_INSTALL_FILECONTENT = NVIDIA_SUSPEND_COMMON_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUSPEND_COMMON_INSTALL_FILE.write(NVIDIA_SUSPEND_COMMON_INSTALL_FILECONTENT)

NVIDIA_SUSPEND_COMMON_LINTIAN_FILE_PATH = 'nvidia-suspend-common-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_SUSPEND_COMMON_LINTIAN_FILE_PATH, "w") as NVIDIA_SUSPEND_COMMON_LINTIAN_FILE:
    NVIDIA_SUSPEND_COMMON_LINTIAN_FILECONTENT = NVIDIA_SUSPEND_COMMON_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUSPEND_COMMON_LINTIAN_FILE.write(NVIDIA_SUSPEND_COMMON_LINTIAN_FILECONTENT)
    
# end of nvidia-suspend-common

# nvidia-settings

NVIDIA_SETTINGS_INSTALL_FILE_PATH = 'nvidia-settings-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_SETTINGS_INSTALL_FILE_PATH, "w") as NVIDIA_SETTINGS_INSTALL_FILE:
    NVIDIA_SETTINGS_INSTALL_FILECONTENT = NVIDIA_SETTINGS_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SETTINGS_INSTALL_FILE.write(NVIDIA_SETTINGS_INSTALL_FILECONTENT)

NVIDIA_SETTINGS_LINTIAN_FILE_PATH = 'nvidia-settings-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_SETTINGS_LINTIAN_FILE_PATH, "w") as NVIDIA_SETTINGS_LINTIAN_FILE:
    NVIDIA_SETTINGS_LINTIAN_FILECONTENT = NVIDIA_SETTINGS_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SETTINGS_LINTIAN_FILE.write(NVIDIA_SETTINGS_LINTIAN_FILECONTENT)

# end of nvidia-settings

# nvidia-support

NVIDIA_SUPPORT_INSTALL_FILE_PATH = 'nvidia-support-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_SUPPORT_INSTALL_FILE_PATH, "w") as NVIDIA_SUPPORT_INSTALL_FILE:
    NVIDIA_SUPPORT_INSTALL_FILECONTENT = NVIDIA_SUPPORT_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUPPORT_INSTALL_FILE.write(NVIDIA_SUPPORT_INSTALL_FILECONTENT)

NVIDIA_SUPPORT_LINTIAN_FILE_PATH = 'nvidia-support-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_SUPPORT_LINTIAN_FILE_PATH, "w") as NVIDIA_SUPPORT_LINTIAN_FILE:
    NVIDIA_SUPPORT_LINTIAN_FILECONTENT = NVIDIA_SUPPORT_LINTIAN_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUPPORT_LINTIAN_FILE.write(NVIDIA_SUPPORT_LINTIAN_FILECONTENT)
    
NVIDIA_SUPPORT_MANPAGES_FILE_PATH = 'nvidia-support-' + DRIVER_VERSION_MAJOR + '.manpages'
with open(NVIDIA_SUPPORT_MANPAGES_FILE_PATH, "w") as NVIDIA_SUPPORT_MANPAGES_FILE:
    NVIDIA_SUPPORT_MANPAGES_FILECONTENT = NVIDIA_SUPPORT_MANPAGES_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUPPORT_MANPAGES_FILE.write(NVIDIA_SUPPORT_MANPAGES_FILECONTENT)
    
NVIDIA_SUPPORT_TEMPLATES_FILE_PATH = 'nvidia-support-' + DRIVER_VERSION_MAJOR + '.templates'
with open(NVIDIA_SUPPORT_TEMPLATES_FILE_PATH, "w") as NVIDIA_SUPPORT_TEMPLATES_FILE:
    NVIDIA_SUPPORT_TEMPLATES_FILECONTENT = NVIDIA_SUPPORT_TEMPLATES_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUPPORT_TEMPLATES_FILE.write(NVIDIA_SUPPORT_TEMPLATES_FILECONTENT)
    
NVIDIA_SUPPORT_POSTRM_FILE_PATH = 'nvidia-support-' + DRIVER_VERSION_MAJOR + '.postrm'
with open(NVIDIA_SUPPORT_POSTRM_FILE_PATH, "w") as NVIDIA_SUPPORT_POSTRM_FILE:
    NVIDIA_SUPPORT_POSTRM_FILECONTENT = NVIDIA_SUPPORT_POSTRM_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUPPORT_POSTRM_FILE.write(NVIDIA_SUPPORT_POSTRM_FILECONTENT)
    
NVIDIA_SUPPORT_POSTINST_FILE_PATH = 'nvidia-support-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(NVIDIA_SUPPORT_POSTINST_FILE_PATH, "w") as NVIDIA_SUPPORT_POSTINST_FILE:
    NVIDIA_SUPPORT_POSTINST_FILECONTENT = NVIDIA_SUPPORT_POSTINST_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUPPORT_POSTINST_FILE.write(NVIDIA_SUPPORT_POSTINST_FILECONTENT)
    
NVIDIA_SUPPORT_CONFIG_FILE_PATH = 'nvidia-support-' + DRIVER_VERSION_MAJOR + '.config'
with open(NVIDIA_SUPPORT_CONFIG_FILE_PATH, "w") as NVIDIA_SUPPORT_CONFIG_FILE:
    NVIDIA_SUPPORT_CONFIG_FILECONTENT = NVIDIA_SUPPORT_CONFIG_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_SUPPORT_CONFIG_FILE.write(NVIDIA_SUPPORT_CONFIG_FILECONTENT)
    
# end of nvidia-support

# nvidia-vdpau-driver

NVIDIA_VDPAU_DRIVER_INSTALL_FILE_PATH = 'nvidia-vdpau-driver-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_VDPAU_DRIVER_INSTALL_FILE_PATH, "w") as NVIDIA_VDPAU_DRIVER_INSTALL_FILE:
    NVIDIA_VDPAU_DRIVER_INSTALL_FILECONTENT = NVIDIA_VDPAU_DRIVER_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_VDPAU_DRIVER_INSTALL_FILE.write(NVIDIA_VDPAU_DRIVER_INSTALL_FILECONTENT)

NVIDIA_VDPAU_DRIVER_LINTIAN_FILE_PATH = 'nvidia-vdpau-driver-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_VDPAU_DRIVER_LINTIAN_FILE_PATH, "w") as NVIDIA_VDPAU_DRIVER_LINTIAN_FILE:
    NVIDIA_VDPAU_DRIVER_LINTIAN_FILECONTENT = NVIDIA_VDPAU_DRIVER_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_VDPAU_DRIVER_LINTIAN_FILE.write(NVIDIA_VDPAU_DRIVER_LINTIAN_FILECONTENT)

NVIDIA_VDPAU_DRIVER_LINKS_FILE_PATH = 'nvidia-vdpau-driver-' + DRIVER_VERSION_MAJOR + '.links'
with open(NVIDIA_VDPAU_DRIVER_LINKS_FILE_PATH, "w") as NVIDIA_VDPAU_DRIVER_LINKS_FILE:
    NVIDIA_VDPAU_DRIVER_LINKS_FILECONTENT = NVIDIA_VDPAU_DRIVER_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_VDPAU_DRIVER_LINKS_FILE.write(NVIDIA_VDPAU_DRIVER_LINKS_FILECONTENT)

NVIDIA_VDPAU_DRIVER_DOCS_FILE_PATH = 'nvidia-vdpau-driver-' + DRIVER_VERSION_MAJOR + '.docs'
with open(NVIDIA_VDPAU_DRIVER_DOCS_FILE_PATH, "w") as NVIDIA_VDPAU_DRIVER_DOCS_FILE:
    NVIDIA_VDPAU_DRIVER_DOCS_FILECONTENT = NVIDIA_VDPAU_DRIVER_DOCS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_VDPAU_DRIVER_DOCS_FILE.write(NVIDIA_VDPAU_DRIVER_DOCS_FILECONTENT)
    
# end of nvidia-vdpau-driver

# nvidia-vulkan-common

NVIDIA_VULKAN_COMMON_INSTALL_FILE_PATH = 'nvidia-vulkan-common-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_VULKAN_COMMON_INSTALL_FILE_PATH, "w") as NVIDIA_VULKAN_COMMON_INSTALL_FILE:
    NVIDIA_VULKAN_COMMON_INSTALL_FILECONTENT = NVIDIA_VULKAN_COMMON_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_VULKAN_COMMON_INSTALL_FILE.write(NVIDIA_VULKAN_COMMON_INSTALL_FILECONTENT)

NVIDIA_VULKAN_COMMON_LINTIAN_FILE_PATH = 'nvidia-vulkan-common-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_VULKAN_COMMON_LINTIAN_FILE_PATH, "w") as NVIDIA_VULKAN_COMMON_LINTIAN_FILE:
    NVIDIA_VULKAN_COMMON_LINTIAN_FILECONTENT = NVIDIA_VULKAN_COMMON_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_VULKAN_COMMON_LINTIAN_FILE.write(NVIDIA_VULKAN_COMMON_LINTIAN_FILECONTENT)
    
# end of nvidia-vulkan-common

# xserver-xorg-video-nvidia

XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILE_PATH = 'xserver-xorg-video-nvidia-' + DRIVER_VERSION_MAJOR + '.install'
with open(XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILE_PATH, "w") as XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILE:
    XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILECONTENT = XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILE.write(XSERVER_XORG_VIDEO_NVIDIA_INSTALL_FILECONTENT)

XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILE_PATH = 'xserver-xorg-video-nvidia-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILE_PATH, "w") as XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILE:
    XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILECONTENT = XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILE.write(XSERVER_XORG_VIDEO_NVIDIA_LINTIAN_FILECONTENT)

XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILE_PATH = 'xserver-xorg-video-nvidia-' + DRIVER_VERSION_MAJOR + '.links'
with open(XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILE_PATH, "w") as XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILE:
    XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILECONTENT = XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILE.write(XSERVER_XORG_VIDEO_NVIDIA_LINKS_FILECONTENT)

XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILE_PATH = 'xserver-xorg-video-nvidia-' + DRIVER_VERSION_MAJOR + '.docs'
with open(XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILE_PATH, "w") as XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILE:
    XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILECONTENT = XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILE.write(XSERVER_XORG_VIDEO_NVIDIA_DOCS_FILECONTENT)
    
XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILE_PATH = 'xserver-xorg-video-nvidia-' + DRIVER_VERSION_MAJOR + '.postrm'
with open(XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILE_PATH, "w") as XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILE:
    XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILECONTENT = XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILE.write(XSERVER_XORG_VIDEO_NVIDIA_POSTRM_FILECONTENT)
    
XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILE_PATH = 'xserver-xorg-video-nvidia-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILE_PATH, "w") as XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILE:
    XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILECONTENT = XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILE.write(XSERVER_XORG_VIDEO_NVIDIA_POSTINST_FILECONTENT)
    
# end of xserver-xorg-video-nvidia

# nvidia-xconfig

NVIDIA_XCONFIG_INSTALL_FILE_PATH = 'nvidia-xconfig-' + DRIVER_VERSION_MAJOR + '.install'
with open(NVIDIA_XCONFIG_INSTALL_FILE_PATH, "w") as NVIDIA_XCONFIG_INSTALL_FILE:
    NVIDIA_XCONFIG_INSTALL_FILECONTENT = NVIDIA_XCONFIG_INSTALL_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_XCONFIG_INSTALL_FILE.write(NVIDIA_XCONFIG_INSTALL_FILECONTENT)

NVIDIA_XCONFIG_DIRS_FILE_PATH = 'nvidia-xconfig-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(NVIDIA_XCONFIG_DIRS_FILE_PATH, "w") as NVIDIA_XCONFIG_DIRS_FILE:
    NVIDIA_XCONFIG_DIRS_FILECONTENT = NVIDIA_XCONFIG_DIRS_FILE_PREQ.format(
                DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
        DRIVER_VERSION_MAJOR=DRIVER_VERSION_MAJOR,
    )
    NVIDIA_XCONFIG_DIRS_FILE.write(NVIDIA_XCONFIG_DIRS_FILECONTENT)
    
# end of nvidia-xconfig
