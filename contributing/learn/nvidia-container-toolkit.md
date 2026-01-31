# nvidia-container-toolkit

```bash

export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.18.2-1

apt-get install nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}

$ apt-get install nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  libnvidia-container-tools libnvidia-container1 nvidia-container-toolkit nvidia-container-toolkit-base

$ dpkg -L libnvidia-container-tools
/.
/usr
/usr/bin
/usr/bin/nvidia-container-cli
/usr/share
/usr/share/doc
/usr/share/doc/libnvidia-container-tools
/usr/share/doc/libnvidia-container-tools/changelog.Debian.gz
/usr/share/doc/libnvidia-container-tools/copyright
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/libnvidia-container-tools
$

$ dpkg -L libnvidia-container1
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/libnvidia-container-go.so.1.18.2
/usr/lib/x86_64-linux-gnu/libnvidia-container.so.1.18.2
/usr/share
/usr/share/doc
/usr/share/doc/libnvidia-container1
/usr/share/doc/libnvidia-container1/changelog.Debian.gz
/usr/share/doc/libnvidia-container1/copyright
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/libnvidia-container1
/usr/lib/x86_64-linux-gnu/libnvidia-container-go.so.1
/usr/lib/x86_64-linux-gnu/libnvidia-container.so.1
$

$ dpkg -L nvidia-container-toolkit
/.
/usr
/usr/bin
/usr/bin/nvidia-container-runtime-hook
/usr/share
/usr/share/doc
/usr/share/doc/nvidia-container-toolkit
/usr/share/doc/nvidia-container-toolkit/changelog.Debian.gz
/usr/share/doc/nvidia-container-toolkit/copyright
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/nvidia-container-toolkit
$

$ dpkg -L nvidia-container-toolkit-base
/.
/etc
/etc/nvidia-container-toolkit
/etc/nvidia-container-toolkit/nvidia-cdi-refresh.env
/etc/systemd
/etc/systemd/system
/etc/systemd/system/nvidia-cdi-refresh.path
/etc/systemd/system/nvidia-cdi-refresh.service
/usr
/usr/bin
/usr/bin/nvidia-cdi-hook
/usr/bin/nvidia-container-runtime
/usr/bin/nvidia-ctk
/usr/share
/usr/share/doc
/usr/share/doc/nvidia-container-toolkit-base
/usr/share/doc/nvidia-container-toolkit-base/changelog.Debian.gz
/usr/share/doc/nvidia-container-toolkit-base/copyright
$

$ nvidia-ctk runtime configure --runtime=containerd
INFO[0000] Using config version 2
INFO[0000] Using CRI runtime plugin name "io.containerd.grpc.v1.cri"
WARN[0000] Could not infer options from runtimes [runc crun]
INFO[0000] Wrote updated config to /etc/containerd/conf.d/99-nvidia.toml
INFO[0000] It is recommended that containerd daemon be restarted.
$

$ tree -a /etc/containerd/
/etc/containerd/
├── conf.d
│   └── 99-nvidia.toml
└── config.toml

1 directory, 2 files
$

$ cat /etc/containerd/config.toml
imports = ["/etc/containerd/conf.d/*.toml"]
version = 2
$

$ cat /etc/containerd/conf.d/99-nvidia.toml
version = 2

[plugins]

  [plugins."io.containerd.grpc.v1.cri"]

    [plugins."io.containerd.grpc.v1.cri".containerd]

      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes]

        [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia]
          privileged_without_host_devices = false
          runtime_engine = ""
          runtime_root = ""
          runtime_type = "io.containerd.runc.v2"

          [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.nvidia.options]
            BinaryName = "/usr/bin/nvidia-container-runtime"
$

```
