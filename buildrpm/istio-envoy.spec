# Generate devel rpm
%global with_devel 0
# Build with debug info rpm
%global with_debug 0

{{{$version := printf "%s.%s.%s" .major .minor .patch}}}
%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global _buildhost build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:		istio-envoy
Version:	{{{$version}}}
Release:	1%{?dist}
Summary:	Envoy is an L7 proxy and communication bus designed for large modern service oriented architectures.
License:	Apache License 2.0
Vendor:		Oracle America
URL:		https://github.com/istio/envoy
{{{- if semverCompare "<1.18.0" $version }}}
ExclusiveArch:  x86_64
{{{- end }}}
Source0:        %{name}-%{version}.tar.bz2

%description
Envoy is a high performance C++ distributed proxy designed for single services and applications,
as well as a communication bus and “universal data plane” designed for large microservice “service mesh” architectures

%prep
%setup -q -n %{name}-%{version}

%files
%license LICENSE

%changelog
* {{{.changelog_timestamp}}} - {{{$version}}}-1
- Added Oracle specific files
