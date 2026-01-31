# containerd

* https://github.com/containerd/containerd/blob/main/docs/getting-started.md

```bash
$ tree -a .
.
├── cni-plugins-linux-amd64-v1.9.0.tgz
├── containerd-2.2.1-linux-amd64.tar.gz
├── containerd.service
└── runc.amd64

0 directories, 4 files

$ tar -zxvf containerd-2.2.1-linux-amd64.tar.gz
bin/
bin/containerd-stress
bin/containerd
bin/ctr
bin/containerd-shim-runc-v2

$ tree -a .
.
├── bin
│   ├── containerd
│   ├── containerd-shim-runc-v2
│   ├── containerd-stress
│   └── ctr
├── cni-plugins-linux-amd64-v1.9.0.tgz
├── containerd-2.2.1-linux-amd64.tar.gz
├── containerd.service
└── runc.amd64

1 directory, 8 files

$ tar -zxvf cni-plugins-linux-amd64-v1.9.0.tgz
./
./bandwidth
./host-device
./LICENSE
./loopback
./ptp
./vrf
./tuning
./host-local
./static
./tap
./bridge
./README.md
./macvlan
./firewall
./dummy
./sbr
./ipvlan
./portmap
./dhcp
./vlan

$ tree -a .
.
├── LICENSE
├── README.md
├── bandwidth
├── bin
│   ├── containerd
│   ├── containerd-shim-runc-v2
│   ├── containerd-stress
│   └── ctr
├── bridge
├── cni-plugins-linux-amd64-v1.9.0.tgz
├── containerd-2.2.1-linux-amd64.tar.gz
├── containerd.service
├── dhcp
├── dummy
├── firewall
├── host-device
├── host-local
├── ipvlan
├── loopback
├── macvlan
├── portmap
├── ptp
├── runc.amd64
├── sbr
├── static
├── tap
├── tuning
├── vlan
└── vrf

1 directory, 28 files
$

$ tar Cxzvf /usr/local containerd-1.6.2-linux-amd64.tar.gz
$ containerd --version
containerd github.com/containerd/containerd/v2 v2.2.1 dea7da592f5d1d2b7755e3a161be07f43fad8f75
$

$ mkdir -p /usr/local/lib/systemd/system/
$ cp containerd.service /usr/local/lib/systemd/system/
$

$ install -m 755 runc.amd64 /usr/local/sbin/runc
$ runc --version
runc version 1.4.0
commit: v1.4.0-0-g8bd78a99
spec: 1.3.0
go: go1.24.10
libseccomp: 2.5.6
$

$ mkdir -p /opt/cni/bin
$ tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.9.0.tgz

$ systemctl daemon-reload
$ systemctl enable --now containerd
$ systemctl status containerd

```

# nerdctl

```
$ tar -zxvf nerdctl-full-2.2.1-linux-amd64.tar.gz
bin/
bin/buildctl
bin/buildg
bin/buildkit-cni-bandwidth
bin/buildkit-cni-bridge
bin/buildkit-cni-dhcp
bin/buildkit-cni-dummy
bin/buildkit-cni-firewall
bin/buildkit-cni-host-device
bin/buildkit-cni-host-local
bin/buildkit-cni-ipvlan
bin/buildkit-cni-loopback
bin/buildkit-cni-macvlan
bin/buildkit-cni-portmap
bin/buildkit-cni-ptp
bin/buildkit-cni-sbr
bin/buildkit-cni-static
bin/buildkit-cni-tap
bin/buildkit-cni-tuning
bin/buildkit-cni-vlan
bin/buildkit-cni-vrf
bin/buildkitd
bin/bypass4netns
bin/bypass4netnsd
bin/containerd
bin/containerd-fuse-overlayfs-grpc
bin/containerd-rootless-setuptool.sh
bin/containerd-rootless.sh
bin/containerd-shim-runc-v2
bin/containerd-stargz-grpc
bin/ctd-decoder
bin/ctr
bin/ctr-enc
bin/ctr-remote
bin/fuse-overlayfs
bin/gomodjail
bin/nerdctl
bin/nerdctl.gomodjail
bin/rootlessctl
bin/rootlesskit
bin/runc
bin/slirp4netns
bin/stargz-fuse-manager
bin/stargz-store-helper
bin/tini
lib/
lib/systemd/
lib/systemd/system/
lib/systemd/system/buildkit.service
lib/systemd/system/containerd.service
lib/systemd/system/stargz-snapshotter.service
libexec/
libexec/cni/
libexec/cni/LICENSE
libexec/cni/README.md
libexec/cni/bandwidth
libexec/cni/bridge
libexec/cni/dhcp
libexec/cni/dummy
libexec/cni/firewall
libexec/cni/host-device
libexec/cni/host-local
libexec/cni/ipvlan
libexec/cni/loopback
libexec/cni/macvlan
libexec/cni/portmap
libexec/cni/ptp
libexec/cni/sbr
libexec/cni/static
libexec/cni/tap
libexec/cni/tuning
libexec/cni/vlan
libexec/cni/vrf
share/
share/doc/
share/doc/nerdctl/
share/doc/nerdctl/README.md
share/doc/nerdctl/docs/
share/doc/nerdctl/docs/build.md
share/doc/nerdctl/docs/builder-debug.md
share/doc/nerdctl/docs/cni.md
share/doc/nerdctl/docs/command-reference.md
share/doc/nerdctl/docs/compose.md
share/doc/nerdctl/docs/config.md
share/doc/nerdctl/docs/cosign.md
share/doc/nerdctl/docs/cvmfs.md
share/doc/nerdctl/docs/dev/
share/doc/nerdctl/docs/dev/auditing_dockerfile.md
share/doc/nerdctl/docs/dev/store.md
share/doc/nerdctl/docs/dir.md
share/doc/nerdctl/docs/experimental.md
share/doc/nerdctl/docs/faq.md
share/doc/nerdctl/docs/freebsd.md
share/doc/nerdctl/docs/gpu.md
share/doc/nerdctl/docs/healthchecks.md
share/doc/nerdctl/docs/images/
share/doc/nerdctl/docs/images/nerdctl-white.svg
share/doc/nerdctl/docs/images/nerdctl.svg
share/doc/nerdctl/docs/images/rootlessKit-network-design.png
share/doc/nerdctl/docs/ipfs.md
share/doc/nerdctl/docs/multi-platform.md
share/doc/nerdctl/docs/notation.md
share/doc/nerdctl/docs/nydus.md
share/doc/nerdctl/docs/ocicrypt.md
share/doc/nerdctl/docs/overlaybd.md
share/doc/nerdctl/docs/registry.md
share/doc/nerdctl/docs/rootless.md
share/doc/nerdctl/docs/soci.md
share/doc/nerdctl/docs/stargz.md
share/doc/nerdctl/docs/testing/
share/doc/nerdctl/docs/testing/README.md
share/doc/nerdctl/docs/testing/tools.md
share/doc/nerdctl-full/
share/doc/nerdctl-full/README.md
share/doc/nerdctl-full/SHA256SUMS
$
```


