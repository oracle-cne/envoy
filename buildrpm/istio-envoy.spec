# Generate devel rpm
%global with_devel 0
# Build with debug info rpm
%global with_debug 0


%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

# Preserve source files rather than applying binary and script post-processing.
%global __os_install_post %{nil}

%global envoy_srcdir /opt/istio-envoy

%global _buildhost build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:		istio-envoy
Version:	1.31.3
Release:	1%{?dist}
Summary:	Envoy is an L7 proxy and communication bus designed for large modern service oriented architectures.
License:	Apache License 2.0
Vendor:		Oracle America
URL:		https://github.com/istio/envoy
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch
AutoReqProv:    no

%description
Envoy is a high performance C++ distributed proxy designed for single services and applications,
as well as a communication bus and “universal data plane” designed for large microservice “service mesh” architectures

This package provides the Envoy source tree used to build istio-proxy.

%prep
%setup -q -n %{name}-%{version}

%install
echo "Installing Envoy source tree to %{envoy_srcdir}"
install -d -m755 %{buildroot}%{envoy_srcdir}
cp -av . %{buildroot}%{envoy_srcdir}/
echo "Removing buildrpm and olm from the packaged Envoy source tree"
rm -rfv -- %{buildroot}%{envoy_srcdir}/buildrpm %{buildroot}%{envoy_srcdir}/olm

%files
%license LICENSE
%{envoy_srcdir}

%changelog
* Fri Oct 23 2026 Oracle Cloud Native Environment Authors <noreply@oracle.com> - 1.31.3-1
- Added Oracle specific files
