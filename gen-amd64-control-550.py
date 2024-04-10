#! /usr/bin/python3

### Basic configuration
DRIVER_VERSION_MAJOR = "550"
DRIVER_VERSION_FULL = "550.67"
DRIVER_VERSION_DPKG = "550.67-101pika1"
DEB_HOST_MULTIARCH = "x86_64-linux-gnu"
### End of Basic configuration


### Notice
# All versioned packages must depend on nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}})
# nvidia-alternative-{DRIVER_VERSION_MAJOR} must conflict with all older nvidia-alternative flavours
### End of Notice

### Important for future Updates (Make sure to update)
# Incase debian adds or removes a packages to the nvidia-graphics-drivers dpkg source make sure to replicate with pika flavour and kernek module adaptations.
# Debian nvidia comes with 49 Packages in 550.
# Pika takes out nvidia-driver-full, nvidia-detect, nvidia-legacy-check.
# Pika add nvidia-kernel-common, nvidia-modprobe, nvidia-persistenced, nvidia-settings, nvidia-support
# So...
# Pika nvidia comes with 51 Packages in 550.
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
Vcs-Git: https://salsa.debian.org/nvidia-team/nvidia-graphics-drivers.git -b 550
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
Confilicts:
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
    nvidia-alternative-525
    nvidia-alternative-530
    nvidia-alternative-535
    nvidia-alternative-545
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
    libnvidia-ngx1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}), [amd64],
    libnvidia-api1-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-opencl-icd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-powerd-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}), [amd64],
    nvidia-cuda-mps-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-suspend-common-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-persistenced-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-settings-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Recommends:
    nvidia-vaapi-driver,
Suggests:
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR},
Provides:
    nvidia-driver (= ${{binary:Version}}),
    nvidia-driver-full (= ${{binary:Version}}),
    nvidia-driver-any,
    nvidia-glx-any,
Description: NVIDIA {DRIVER_VERSION_FULL} metapackage
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
Conflicts:
    nvidia-kernel-common
Description: NVIDIA binary kernel module support files
    This package contains support files used for any version of the NVIDIA
    kernel module. It sets up udev and ConsoleKit rules, ensures the NVIDIA
    control device is created, and performs any other tasks required for the
    module to work properly.

Package: nvidia-kernel-dkms-{DRIVER_VERSION_MAJOR}
Section: non-free/kernel
Architecture: amd64 arm64 ppc64el
Depends:
    firmware-nvidia-gsp-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-source-{DRIVER_VERSION_MAJOR}  (= ${{binary:Version}}),
    nvidia-kernel-support-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    dkms,
    ${{misc:Depends}}
Recommends:
    nvidia-driver-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
Provides:
    nvidia-kernel-module-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    nvidia-kernel-dkms (= ${{binary:Version}}),
    nvidia-kernel-dkms-any (= ${{binary:Version}}),
Conflicts:
    nvidia-kernel-dkms,
    nvidia-kernel-pikaos-module-{DRIVER_VERSION_MAJOR},
    nvidia-kernel-pikaos-module,
Description: NVIDIA binary kernel DKMS module
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
Conflicts:
    nvidia-kernel-source
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
Conflicts:
    nvidia-kernel-support
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
Provides: nvidia-modprobe = ${{binary:Version}})
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
    nvidia-alternative-{DRIVER_VERSION_MAJOR} (= ${{binary:Version}}),
    ${{misc:Depends}}
Provides: nvidia-support (= ${{binary:Version}}),
Conflicts: nvidia-support
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

Package: xserver-xorg-video-nvidia
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
Confilicts:
    xserver-xorg-video-nvidia
Description: NVIDIA binary Xorg driver
"""

# end of control

# firmware-nvidia-gsp

FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PREQ = """firmware/gsp*.bin	lib/firmware/nvidia/{DRIVER_VERSION_FULL}/
RIM_GH100PROD.swidtag	usr/share/nvidia/rim/{DRIVER_VERSION_FULL}/
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

# libegl-nvidia0

LIBEGL_NVIDIA0_INSTALL_FILE_PREQ = """#! /usr/bin/dh-exec
libEGL_nvidia.so.{DRIVER_VERSION_FULL}	usr/lib/${{DEB_HOST_MULTIARCH}}/nvidia/current/"""

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
NVIDIA-Linux-amd64/README.txt"""

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
		update-alternatives --install /usr/lib/nvidia/nvidia nvidia /usr/lib/nvidia/current# {DRIVER_VERSION_MAJOR} $slaves $conf_slaves $kmod_slaves $libnvidia_ml_so_slave
	else
		update-alternatives --remove nvidia /usr/lib/nvidia/current#
	fi
	if [ "$open_alternative" = 1 ]; then
		update-alternatives --install /usr/lib/nvidia/nvidia nvidia /usr/lib/nvidia/current#-open $(({DRIVER_VERSION_MAJOR} - 1)) $slaves $conf_slaves $kmod_open_slaves $libnvidia_ml_so_slave
	else
		update-alternatives --remove nvidia /usr/lib/nvidia/current#-open
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

interest-await /usr/include/nvml.h"""

# end of nvidia-alternative

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

# firmware-nvidia-gsp
FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PATH = 'firmware-nvidia-gsp-' + DRIVER_VERSION_MAJOR + '.install'
with open(FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PATH, "w") as FIRMWARE_NVIDIA_GSP_INSTALL_FILE:
    FIRMWARE_NVIDIA_GSP_INSTALL_FILECONTENT = FIRMWARE_NVIDIA_GSP_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    FIRMWARE_NVIDIA_GSP_INSTALL_FILE.write(FIRMWARE_NVIDIA_GSP_INSTALL_FILECONTENT)
    
FIRMWARE_NVIDIA_GSP_LINTIAN_FILE_PATH = 'firmware-nvidia-gsp-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(FIRMWARE_NVIDIA_GSP_LINTIAN_FILE_PATH, "w") as FIRMWARE_NVIDIA_GSP_LINTIAN_FILE:
    FIRMWARE_NVIDIA_GSP_LINTIAN_FILECONTENT = FIRMWARE_NVIDIA_GSP_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    FIRMWARE_NVIDIA_GSP_LINTIAN_FILE.write(FIRMWARE_NVIDIA_GSP_LINTIAN_FILECONTENT)

# end of firmware-nvidia-gsp

# libcuda1

LIBCUDA1_INSTALL_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBCUDA1_INSTALL_FILE_PATH, "w") as LIBCUDA1_INSTALL_FILE:
    LIBCUDA1_INSTALL_FILECONTENT = LIBCUDA1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBCUDA1_INSTALL_FILE.write(LIBCUDA1_INSTALL_FILECONTENT)

LIBCUDA1_LINTIAN_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBCUDA1_LINTIAN_FILE_PATH, "w") as LIBCUDA1_LINTIAN_FILE:
    LIBCUDA1_LINTIAN_FILECONTENT = LIBCUDA1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBCUDA1_LINTIAN_FILE.write(LIBCUDA1_LINTIAN_FILECONTENT)

LIBCUDA1_LINKS_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBCUDA1_LINKS_FILE_PATH, "w") as LIBCUDA1_LINKS_FILE:
    LIBCUDA1_LINKS_FILECONTENT = LIBCUDA1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBCUDA1_LINKS_FILE.write(LIBCUDA1_LINKS_FILECONTENT)

LIBCUDA1_POSTINST_FILE_PATH = 'libcuda1-' + DRIVER_VERSION_MAJOR + '.postinst'
with open(LIBCUDA1_POSTINST_FILE_PATH, "w") as LIBCUDA1_POSTINST_FILE:
    LIBCUDA1_POSTINST_FILECONTENT = LIBCUDA1_POSTINST_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBCUDA1_POSTINST_FILE.write(LIBCUDA1_POSTINST_FILECONTENT)

# end of libcuda1

# libcudadebugger1

LIBCUDADEBUGGER1_INSTALL_FILE_PATH = 'libcudadebugger1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBCUDADEBUGGER1_INSTALL_FILE_PATH, "w") as LIBCUDADEBUGGER1_INSTALL_FILE:
    LIBCUDADEBUGGER1_INSTALL_FILECONTENT = LIBCUDADEBUGGER1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBCUDADEBUGGER1_INSTALL_FILE.write(LIBCUDADEBUGGER1_INSTALL_FILECONTENT)

LIBCUDADEBUGGER1_LINTIAN_FILE_PATH = 'libcudadebugger1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBCUDADEBUGGER1_LINTIAN_FILE_PATH, "w") as LIBCUDADEBUGGER1_LINTIAN_FILE:
    LIBCUDADEBUGGER1_LINTIAN_FILECONTENT = LIBCUDADEBUGGER1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBCUDADEBUGGER1_LINTIAN_FILE.write(LIBCUDADEBUGGER1_LINTIAN_FILECONTENT)

LIBCUDADEBUGGER1_LINKS_FILE_PATH = 'libcudadebugger1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBCUDADEBUGGER1_LINKS_FILE_PATH, "w") as LIBCUDADEBUGGER1_LINKS_FILE:
    LIBCUDADEBUGGER1_LINKS_FILECONTENT = LIBCUDADEBUGGER1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBCUDADEBUGGER1_LINKS_FILE.write(LIBCUDADEBUGGER1_LINKS_FILECONTENT)

# end of libcudadebugger1

# libegl-nvidia0

LIBEGL_NVIDIA0_INSTALL_FILE_PATH = 'libegl-nvidia0-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBEGL_NVIDIA0_INSTALL_FILE_PATH, "w") as LIBEGL_NVIDIA0_INSTALL_FILE:
    LIBEGL_NVIDIA0_INSTALL_FILECONTENT = LIBEGL_NVIDIA0_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBEGL_NVIDIA0_INSTALL_FILE.write(LIBEGL_NVIDIA0_INSTALL_FILECONTENT)

LIBEGL_NVIDIA0_LINTIAN_FILE_PATH = 'libegl-nvidia0-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBEGL_NVIDIA0_LINTIAN_FILE_PATH, "w") as LIBEGL_NVIDIA0_LINTIAN_FILE:
    LIBEGL_NVIDIA0_LINTIAN_FILECONTENT = LIBEGL_NVIDIA0_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBEGL_NVIDIA0_LINTIAN_FILE.write(LIBEGL_NVIDIA0_LINTIAN_FILECONTENT)

LIBEGL_NVIDIA0_LINKS_FILE_PATH = 'libegl-nvidia0-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBEGL_NVIDIA0_LINKS_FILE_PATH, "w") as LIBEGL_NVIDIA0_LINKS_FILE:
    LIBEGL_NVIDIA0_LINKS_FILECONTENT = LIBEGL_NVIDIA0_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBEGL_NVIDIA0_LINKS_FILE.write(LIBEGL_NVIDIA0_LINKS_FILECONTENT)

# end of libegl-nvidia0

# libgl1-nvidia-glvnd-glx

LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE_PATH = 'libgl1-nvidia-glvnd-glx-' + DRIVER_VERSION_MAJOR + '.docs'
with open(LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE_PATH, "w") as LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE:
    LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILECONTENT = LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILE.write(LIBGL1_NVIDIA_GLVND_GLX_DOCS_FILECONTENT)

# end of libgl1-nvidia-glvnd-glx

# libgles-nvidia1

LIBGLES_NVIDIA1_INSTALL_FILE_PATH = 'libgles-nvidia1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBGLES_NVIDIA1_INSTALL_FILE_PATH, "w") as LIBGLES_NVIDIA1_INSTALL_FILE:
    LIBGLES_NVIDIA1_INSTALL_FILECONTENT = LIBGLES_NVIDIA1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLES_NVIDIA1_INSTALL_FILE.write(LIBGLES_NVIDIA1_INSTALL_FILECONTENT)

LIBGLES_NVIDIA1_LINTIAN_FILE_PATH = 'libgles-nvidia1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBGLES_NVIDIA1_LINTIAN_FILE_PATH, "w") as LIBGLES_NVIDIA1_LINTIAN_FILE:
    LIBGLES_NVIDIA1_LINTIAN_FILECONTENT = LIBGLES_NVIDIA1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLES_NVIDIA1_LINTIAN_FILE.write(LIBGLES_NVIDIA1_LINTIAN_FILECONTENT)

LIBGLES_NVIDIA1_LINKS_FILE_PATH = 'libgles-nvidia1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBGLES_NVIDIA1_LINKS_FILE_PATH, "w") as LIBGLES_NVIDIA1_LINKS_FILE:
    LIBGLES_NVIDIA1_LINKS_FILECONTENT = LIBGLES_NVIDIA1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLES_NVIDIA1_LINKS_FILE.write(LIBGLES_NVIDIA1_LINKS_FILECONTENT)

# end libgles-nvidia1

# libgles-nvidia2

LIBGLES_NVIDIA2_INSTALL_FILE_PATH = 'libgles-nvidia2-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBGLES_NVIDIA2_INSTALL_FILE_PATH, "w") as LIBGLES_NVIDIA2_INSTALL_FILE:
    LIBGLES_NVIDIA2_INSTALL_FILECONTENT = LIBGLES_NVIDIA2_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLES_NVIDIA2_INSTALL_FILE.write(LIBGLES_NVIDIA2_INSTALL_FILECONTENT)

LIBGLES_NVIDIA2_LINTIAN_FILE_PATH = 'libgles-nvidia2-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBGLES_NVIDIA2_LINTIAN_FILE_PATH, "w") as LIBGLES_NVIDIA2_LINTIAN_FILE:
    LIBGLES_NVIDIA2_LINTIAN_FILECONTENT = LIBGLES_NVIDIA2_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLES_NVIDIA2_LINTIAN_FILE.write(LIBGLES_NVIDIA2_LINTIAN_FILECONTENT)

LIBGLES_NVIDIA2_LINKS_FILE_PATH = 'libgles-nvidia2-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBGLES_NVIDIA2_LINKS_FILE_PATH, "w") as LIBGLES_NVIDIA2_LINKS_FILE:
    LIBGLES_NVIDIA2_LINKS_FILECONTENT = LIBGLES_NVIDIA2_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLES_NVIDIA2_LINKS_FILE.write(LIBGLES_NVIDIA2_LINKS_FILECONTENT)

# end libgles-nvidia2

# libglx-nvidia0

LIBGLX_NVIDIA0_INSTALL_FILE_PATH = 'libglx-nvidia0-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBGLX_NVIDIA0_INSTALL_FILE_PATH, "w") as LIBGLX_NVIDIA0_INSTALL_FILE:
    LIBGLX_NVIDIA0_INSTALL_FILECONTENT = LIBGLX_NVIDIA0_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLX_NVIDIA0_INSTALL_FILE.write(LIBGLX_NVIDIA0_INSTALL_FILECONTENT)

LIBGLX_NVIDIA0_LINTIAN_FILE_PATH = 'libglx-nvidia0-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBGLX_NVIDIA0_LINTIAN_FILE_PATH, "w") as LIBGLX_NVIDIA0_LINTIAN_FILE:
    LIBGLX_NVIDIA0_LINTIAN_FILECONTENT = LIBGLX_NVIDIA0_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLX_NVIDIA0_LINTIAN_FILE.write(LIBGLX_NVIDIA0_LINTIAN_FILECONTENT)

LIBGLX_NVIDIA0_LINKS_FILE_PATH = 'libglx-nvidia0-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBGLX_NVIDIA0_LINKS_FILE_PATH, "w") as LIBGLX_NVIDIA0_LINKS_FILE:
    LIBGLX_NVIDIA0_LINKS_FILECONTENT = LIBGLX_NVIDIA0_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBGLX_NVIDIA0_LINKS_FILE.write(LIBGLX_NVIDIA0_LINKS_FILECONTENT)


# end of libglx-nvidia0

# libnvcuvid1

LIBNVCUVID1_INSTALL_FILE_PATH = 'libnvcuvid1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVCUVID1_INSTALL_FILE_PATH, "w") as LIBNVCUVID1_INSTALL_FILE:
    LIBNVCUVID1_INSTALL_FILECONTENT = LIBNVCUVID1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVCUVID1_INSTALL_FILE.write(LIBNVCUVID1_INSTALL_FILECONTENT)

LIBNVCUVID1_LINTIAN_FILE_PATH = 'libnvcuvid1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVCUVID1_LINTIAN_FILE_PATH, "w") as LIBNVCUVID1_LINTIAN_FILE:
    LIBNVCUVID1_LINTIAN_FILECONTENT = LIBNVCUVID1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVCUVID1_LINTIAN_FILE.write(LIBNVCUVID1_LINTIAN_FILECONTENT)

LIBNVCUVID1_LINKS_FILE_PATH = 'libnvcuvid1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVCUVID1_LINKS_FILE_PATH, "w") as LIBNVCUVID1_LINKS_FILE:
    LIBNVCUVID1_LINKS_FILECONTENT = LIBNVCUVID1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVCUVID1_LINKS_FILE.write(LIBNVCUVID1_LINKS_FILECONTENT)
    
# end of libnvcuvid1

# libnvidia-allocator1

LIBNVIDIA_ALLOCATOR1_INSTALL_FILE_PATH = 'libnvidia-allocator1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_ALLOCATOR1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_ALLOCATOR1_INSTALL_FILE:
    LIBNVIDIA_ALLOCATOR1_INSTALL_FILECONTENT = LIBNVIDIA_ALLOCATOR1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ALLOCATOR1_INSTALL_FILE.write(LIBNVIDIA_ALLOCATOR1_INSTALL_FILECONTENT)

LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE_PATH = 'libnvidia-allocator1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE:
    LIBNVIDIA_ALLOCATOR1_LINTIAN_FILECONTENT = LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ALLOCATOR1_LINTIAN_FILE.write(LIBNVIDIA_ALLOCATOR1_LINTIAN_FILECONTENT)

LIBNVIDIA_ALLOCATOR1_LINKS_FILE_PATH = 'libnvidia-allocator1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_ALLOCATOR1_LINKS_FILE_PATH, "w") as LIBNVIDIA_ALLOCATOR1_LINKS_FILE:
    LIBNVIDIA_ALLOCATOR1_LINKS_FILECONTENT = LIBNVIDIA_ALLOCATOR1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ALLOCATOR1_LINKS_FILE.write(LIBNVIDIA_ALLOCATOR1_LINKS_FILECONTENT)

# end of libnvidia-allocator1

# libnvidia-api1

LIBNVIDIA_API1_INSTALL_FILE_PATH = 'libnvidia-api1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_API1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_API1_INSTALL_FILE:
    LIBNVIDIA_API1_INSTALL_FILECONTENT = LIBNVIDIA_API1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_API1_INSTALL_FILE.write(LIBNVIDIA_API1_INSTALL_FILECONTENT)

LIBNVIDIA_API1_LINTIAN_FILE_PATH = 'libnvidia-api1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_API1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_API1_LINTIAN_FILE:
    LIBNVIDIA_API1_LINTIAN_FILECONTENT = LIBNVIDIA_API1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_API1_LINTIAN_FILE.write(LIBNVIDIA_API1_LINTIAN_FILECONTENT)

# end of libnvidia-api1

# libnvidia-cfg1

LIBNVIDIA_CFG1_INSTALL_FILE_PATH = 'libnvidia-cfg1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_CFG1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_CFG1_INSTALL_FILE:
    LIBNVIDIA_CFG1_INSTALL_FILECONTENT = LIBNVIDIA_CFG1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_CFG1_INSTALL_FILE.write(LIBNVIDIA_CFG1_INSTALL_FILECONTENT)

LIBNVIDIA_CFG1_LINTIAN_FILE_PATH = 'libnvidia-cfg1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_CFG1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_CFG1_LINTIAN_FILE:
    LIBNVIDIA_CFG1_LINTIAN_FILECONTENT = LIBNVIDIA_CFG1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_CFG1_LINTIAN_FILE.write(LIBNVIDIA_CFG1_LINTIAN_FILECONTENT)

LIBNVIDIA_CFG1_LINKS_FILE_PATH = 'libnvidia-cfg1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_CFG1_LINKS_FILE_PATH, "w") as LIBNVIDIA_CFG1_LINKS_FILE:
    LIBNVIDIA_CFG1_LINKS_FILECONTENT = LIBNVIDIA_CFG1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_CFG1_LINKS_FILE.write(LIBNVIDIA_CFG1_LINKS_FILECONTENT)

# end of libnvidia-cfg1

# libnvidia-eglcore

LIBNVIDIA_EGLCORE_INSTALL_FILE_PATH = 'libnvidia-eglcore-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_EGLCORE_INSTALL_FILE_PATH, "w") as LIBNVIDIA_EGLCORE_INSTALL_FILE:
    LIBNVIDIA_EGLCORE_INSTALL_FILECONTENT = LIBNVIDIA_EGLCORE_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_EGLCORE_INSTALL_FILE.write(LIBNVIDIA_EGLCORE_INSTALL_FILECONTENT)

LIBNVIDIA_EGLCORE_LINTIAN_FILE_PATH = 'libnvidia-eglcore-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_EGLCORE_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_EGLCORE_LINTIAN_FILE:
    LIBNVIDIA_EGLCORE_LINTIAN_FILECONTENT = LIBNVIDIA_EGLCORE_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_EGLCORE_LINTIAN_FILE.write(LIBNVIDIA_EGLCORE_LINTIAN_FILECONTENT)

# end of libnvidia-eglcore

# libnvidia-encode1

LIBNVIDIA_ENCODE1_INSTALL_FILE_PATH = 'libnvidia-encode1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_ENCODE1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_ENCODE1_INSTALL_FILE:
    LIBNVIDIA_ENCODE1_INSTALL_FILECONTENT = LIBNVIDIA_ENCODE1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ENCODE1_INSTALL_FILE.write(LIBNVIDIA_ENCODE1_INSTALL_FILECONTENT)

LIBNVIDIA_ENCODE1_LINTIAN_FILE_PATH = 'libnvidia-encode1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_ENCODE1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_ENCODE1_LINTIAN_FILE:
    LIBNVIDIA_ENCODE1_LINTIAN_FILECONTENT = LIBNVIDIA_ENCODE1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ENCODE1_LINTIAN_FILE.write(LIBNVIDIA_ENCODE1_LINTIAN_FILECONTENT)

LIBNVIDIA_ENCODE1_LINKS_FILE_PATH = 'libnvidia-encode1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_ENCODE1_LINKS_FILE_PATH, "w") as LIBNVIDIA_ENCODE1_LINKS_FILE:
    LIBNVIDIA_ENCODE1_LINKS_FILECONTENT = LIBNVIDIA_ENCODE1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ENCODE1_LINKS_FILE.write(LIBNVIDIA_ENCODE1_LINKS_FILECONTENT)

# end of libnvidia-encode1

# libnvidia-fbc1

LIBNVIDIA_FBC1_INSTALL_FILE_PATH = 'libnvidia-fbc1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_FBC1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_FBC1_INSTALL_FILE:
    LIBNVIDIA_FBC1_INSTALL_FILECONTENT = LIBNVIDIA_FBC1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_FBC1_INSTALL_FILE.write(LIBNVIDIA_FBC1_INSTALL_FILECONTENT)

LIBNVIDIA_FBC1_LINTIAN_FILE_PATH = 'libnvidia-fbc1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_FBC1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_FBC1_LINTIAN_FILE:
    LIBNVIDIA_FBC1_LINTIAN_FILECONTENT = LIBNVIDIA_FBC1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_FBC1_LINTIAN_FILE.write(LIBNVIDIA_FBC1_LINTIAN_FILECONTENT)

LIBNVIDIA_FBC1_LINKS_FILE_PATH = 'libnvidia-fbc1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_FBC1_LINKS_FILE_PATH, "w") as LIBNVIDIA_FBC1_LINKS_FILE:
    LIBNVIDIA_FBC1_LINKS_FILECONTENT = LIBNVIDIA_FBC1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_FBC1_LINKS_FILE.write(LIBNVIDIA_FBC1_LINKS_FILECONTENT)
    
# end of libnvidia-fbc1

# libnvidia-glcore

LIBNVIDIA_GLCORE_INSTALL_FILE_PATH = 'libnvidia-glcore-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_GLCORE_INSTALL_FILE_PATH, "w") as LIBNVIDIA_GLCORE_INSTALL_FILE:
    LIBNVIDIA_GLCORE_INSTALL_FILECONTENT = LIBNVIDIA_GLCORE_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_GLCORE_INSTALL_FILE.write(LIBNVIDIA_GLCORE_INSTALL_FILECONTENT)

LIBNVIDIA_GLCORE_LINTIAN_FILE_PATH = 'libnvidia-glcore-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_GLCORE_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_GLCORE_LINTIAN_FILE:
    LIBNVIDIA_GLCORE_LINTIAN_FILECONTENT = LIBNVIDIA_GLCORE_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_GLCORE_LINTIAN_FILE.write(LIBNVIDIA_GLCORE_LINTIAN_FILECONTENT)
    
# end of libnvidia-glcore

# libnvidia-glvkspirv

LIBNVIDIA_GLVKSPIRV_INSTALL_FILE_PATH = 'libnvidia-glvkspirv-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_GLVKSPIRV_INSTALL_FILE_PATH, "w") as LIBNVIDIA_GLVKSPIRV_INSTALL_FILE:
    LIBNVIDIA_GLVKSPIRV_INSTALL_FILECONTENT = LIBNVIDIA_GLVKSPIRV_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_GLVKSPIRV_INSTALL_FILE.write(LIBNVIDIA_GLVKSPIRV_INSTALL_FILECONTENT)

LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE_PATH = 'libnvidia-glvkspirv-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE:
    LIBNVIDIA_GLVKSPIRV_LINTIAN_FILECONTENT = LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_GLVKSPIRV_LINTIAN_FILE.write(LIBNVIDIA_GLVKSPIRV_LINTIAN_FILECONTENT)
    
# end of libnvidia-glvkspirv

# libnvidia-gpucomp

LIBNVIDIA_GPUCOMP_INSTALL_FILE_PATH = 'libnvidia-gpucomp-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_GPUCOMP_INSTALL_FILE_PATH, "w") as LIBNVIDIA_GPUCOMP_INSTALL_FILE:
    LIBNVIDIA_GPUCOMP_INSTALL_FILECONTENT = LIBNVIDIA_GPUCOMP_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_GPUCOMP_INSTALL_FILE.write(LIBNVIDIA_GPUCOMP_INSTALL_FILECONTENT)

LIBNVIDIA_GPUCOMP_LINTIAN_FILE_PATH = 'libnvidia-gpucomp-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_GPUCOMP_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_GPUCOMP_LINTIAN_FILE:
    LIBNVIDIA_GPUCOMP_LINTIAN_FILECONTENT = LIBNVIDIA_GPUCOMP_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_GPUCOMP_LINTIAN_FILE.write(LIBNVIDIA_GPUCOMP_LINTIAN_FILECONTENT)
    
# end of libnvidia-gpucomp

# libnvidia-ml1

LIBNVIDIA_ML1_INSTALL_FILE_PATH = 'libnvidia-ml1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_ML1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_ML1_INSTALL_FILE:
    LIBNVIDIA_ML1_INSTALL_FILECONTENT = LIBNVIDIA_ML1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ML1_INSTALL_FILE.write(LIBNVIDIA_ML1_INSTALL_FILECONTENT)

LIBNVIDIA_ML1_LINTIAN_FILE_PATH = 'libnvidia-ml1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_ML1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_ML1_LINTIAN_FILE:
    LIBNVIDIA_ML1_LINTIAN_FILECONTENT = LIBNVIDIA_ML1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ML1_LINTIAN_FILE.write(LIBNVIDIA_ML1_LINTIAN_FILECONTENT)

LIBNVIDIA_ML1_LINKS_FILE_PATH = 'libnvidia-ml1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_ML1_LINKS_FILE_PATH, "w") as LIBNVIDIA_ML1_LINKS_FILE:
    LIBNVIDIA_ML1_LINKS_FILECONTENT = LIBNVIDIA_ML1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_ML1_LINKS_FILE.write(LIBNVIDIA_ML1_LINKS_FILECONTENT)
    
# end of libnvidia-ml1

# libnvidia-ngx1

LIBNVIDIA_NGX1_INSTALL_FILE_PATH = 'libnvidia-ngx1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_NGX1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_NGX1_INSTALL_FILE:
    LIBNVIDIA_NGX1_INSTALL_FILECONTENT = LIBNVIDIA_NGX1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_NGX1_INSTALL_FILE.write(LIBNVIDIA_NGX1_INSTALL_FILECONTENT)

LIBNVIDIA_NGX1_LINTIAN_FILE_PATH = 'libnvidia-ngx1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_NGX1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_NGX1_LINTIAN_FILE:
    LIBNVIDIA_NGX1_LINTIAN_FILECONTENT = LIBNVIDIA_NGX1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_NGX1_LINTIAN_FILE.write(LIBNVIDIA_NGX1_LINTIAN_FILECONTENT)

LIBNVIDIA_NGX1_LINKS_FILE_PATH = 'libnvidia-ngx1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_NGX1_LINKS_FILE_PATH, "w") as LIBNVIDIA_NGX1_LINKS_FILE:
    LIBNVIDIA_NGX1_LINKS_FILECONTENT = LIBNVIDIA_NGX1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_NGX1_LINKS_FILE.write(LIBNVIDIA_NGX1_LINKS_FILECONTENT)
    
# end of libnvidia-ngx1

# libnvidia-nvvm4

LIBNVIDIA_NVVM4_INSTALL_FILE_PATH = 'libnvidia-nvvm4-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_NVVM4_INSTALL_FILE_PATH, "w") as LIBNVIDIA_NVVM4_INSTALL_FILE:
    LIBNVIDIA_NVVM4_INSTALL_FILECONTENT = LIBNVIDIA_NVVM4_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_NVVM4_INSTALL_FILE.write(LIBNVIDIA_NVVM4_INSTALL_FILECONTENT)

LIBNVIDIA_NVVM4_LINTIAN_FILE_PATH = 'libnvidia-nvvm4-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_NVVM4_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_NVVM4_LINTIAN_FILE:
    LIBNVIDIA_NVVM4_LINTIAN_FILECONTENT = LIBNVIDIA_NVVM4_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_NVVM4_LINTIAN_FILE.write(LIBNVIDIA_NVVM4_LINTIAN_FILECONTENT)

LIBNVIDIA_NVVM4_LINKS_FILE_PATH = 'libnvidia-nvvm4-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_NVVM4_LINKS_FILE_PATH, "w") as LIBNVIDIA_NVVM4_LINKS_FILE:
    LIBNVIDIA_NVVM4_LINKS_FILECONTENT = LIBNVIDIA_NVVM4_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_NVVM4_LINKS_FILE.write(LIBNVIDIA_NVVM4_LINKS_FILECONTENT)
    
# end of libnvidia-nvvm4

# libnvidia-opticalflow1

LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE_PATH = 'libnvidia-opticalflow1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE:
    LIBNVIDIA_OPTICALFLOW1_INSTALL_FILECONTENT = LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_OPTICALFLOW1_INSTALL_FILE.write(LIBNVIDIA_OPTICALFLOW1_INSTALL_FILECONTENT)

LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE_PATH = 'libnvidia-opticalflow1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE:
    LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILECONTENT = LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILE.write(LIBNVIDIA_OPTICALFLOW1_LINTIAN_FILECONTENT)

LIBNVIDIA_OPTICALFLOW1_LINKS_FILE_PATH = 'libnvidia-opticalflow1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_OPTICALFLOW1_LINKS_FILE_PATH, "w") as LIBNVIDIA_OPTICALFLOW1_LINKS_FILE:
    LIBNVIDIA_OPTICALFLOW1_LINKS_FILECONTENT = LIBNVIDIA_OPTICALFLOW1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_OPTICALFLOW1_LINKS_FILE.write(LIBNVIDIA_OPTICALFLOW1_LINKS_FILECONTENT)
    
# end of libnvidia-opticalflow1

# libnvidia-pkcs11-openssl3

LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE_PATH = 'libnvidia-pkcs11-openssl3-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE_PATH, "w") as LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE:
    LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILECONTENT = LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILE.write(LIBNVIDIA_PKCS11_OPENSSL3_INSTALL_FILECONTENT)

LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE_PATH = 'libnvidia-pkcs11-openssl3-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE:
    LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILECONTENT = LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILE.write(LIBNVIDIA_PKCS11_OPENSSL3_LINTIAN_FILECONTENT)
    
# end of libnvidia-pkcs11-openssl3

# libnvidia-ptxjitcompiler1

LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE_PATH = 'libnvidia-ptxjitcompiler1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE_PATH, "w") as LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE:
    LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILECONTENT = LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILE.write(LIBNVIDIA_PTXJITCOMPILER1_INSTALL_FILECONTENT)

LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE_PATH = 'libnvidia-ptxjitcompiler1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE:
    LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILECONTENT = LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILE.write(LIBNVIDIA_PTXJITCOMPILER1_LINTIAN_FILECONTENT)

LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE_PATH = 'libnvidia-ptxjitcompiler1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE_PATH, "w") as LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE:
    LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILECONTENT = LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILE.write(LIBNVIDIA_PTXJITCOMPILER1_LINKS_FILECONTENT)
    
# end of libnvidia-ptxjitcompiler1

# libnvidia-rtcore

LIBNVIDIA_RTCORE_INSTALL_FILE_PATH = 'libnvidia-rtcore-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVIDIA_RTCORE_INSTALL_FILE_PATH, "w") as LIBNVIDIA_RTCORE_INSTALL_FILE:
    LIBNVIDIA_RTCORE_INSTALL_FILECONTENT = LIBNVIDIA_RTCORE_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_RTCORE_INSTALL_FILE.write(LIBNVIDIA_RTCORE_INSTALL_FILECONTENT)

LIBNVIDIA_RTCORE_LINTIAN_FILE_PATH = 'libnvidia-rtcore-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVIDIA_RTCORE_LINTIAN_FILE_PATH, "w") as LIBNVIDIA_RTCORE_LINTIAN_FILE:
    LIBNVIDIA_RTCORE_LINTIAN_FILECONTENT = LIBNVIDIA_RTCORE_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVIDIA_RTCORE_LINTIAN_FILE.write(LIBNVIDIA_RTCORE_LINTIAN_FILECONTENT)
    
# end of libnvidia-rtcore

# libnvoptix1

LIBNVOPTIX1_INSTALL_FILE_PATH = 'libnvoptix1-' + DRIVER_VERSION_MAJOR + '.install'
with open(LIBNVOPTIX1_INSTALL_FILE_PATH, "w") as LIBNVOPTIX1_INSTALL_FILE:
    LIBNVOPTIX1_INSTALL_FILECONTENT = LIBNVOPTIX1_INSTALL_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVOPTIX1_INSTALL_FILE.write(LIBNVOPTIX1_INSTALL_FILECONTENT)

LIBNVOPTIX1_LINTIAN_FILE_PATH = 'libnvoptix1-' + DRIVER_VERSION_MAJOR + '.lintian-overrides'
with open(LIBNVOPTIX1_LINTIAN_FILE_PATH, "w") as LIBNVOPTIX1_LINTIAN_FILE:
    LIBNVOPTIX1_LINTIAN_FILECONTENT = LIBNVOPTIX1_LINTIAN_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVOPTIX1_LINTIAN_FILE.write(LIBNVOPTIX1_LINTIAN_FILECONTENT)

LIBNVOPTIX1_LINKS_FILE_PATH = 'libnvoptix1-' + DRIVER_VERSION_MAJOR + '.links'
with open(LIBNVOPTIX1_LINKS_FILE_PATH, "w") as LIBNVOPTIX1_LINKS_FILE:
    LIBNVOPTIX1_LINKS_FILECONTENT = LIBNVOPTIX1_LINKS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
    )
    LIBNVOPTIX1_LINKS_FILE.write(LIBNVOPTIX1_LINKS_FILECONTENT)
    
# end of libnvoptix1

# nvidia-alternative

NVIDIA_ALTERNATIVE_DIRS_FILE_PATH = 'nvidia-alternative-' + DRIVER_VERSION_MAJOR + '.dirs'
with open(NVIDIA_ALTERNATIVE_DIRS_FILE_PATH, "w") as NVIDIA_ALTERNATIVE_DIRS_FILE:
    NVIDIA_ALTERNATIVE_DIRS_FILECONTENT = NVIDIA_ALTERNATIVE_DIRS_FILE_PREQ.format(
        DRIVER_VERSION_FULL=DRIVER_VERSION_FULL,
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
    )
    NVIDIA_ALTERNATIVE_TRIGGERS_FILE.write(NVIDIA_ALTERNATIVE_TRIGGERS_FILECONTENT)

# end of nvidia-alternative
