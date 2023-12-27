#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ecdsa
Version  : 0.18.0
Release  : 91
URL      : https://files.pythonhosted.org/packages/ff/7b/ba6547a76c468a0d22de93e89ae60d9561ec911f59532907e72b0d8bc0f1/ecdsa-0.18.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/7b/ba6547a76c468a0d22de93e89ae60d9561ec911f59532907e72b0d8bc0f1/ecdsa-0.18.0.tar.gz
Summary  : ECDSA cryptographic signature library (pure python)
Group    : Development/Tools
License  : MIT
Requires: pypi-ecdsa-license = %{version}-%{release}
Requires: pypi-ecdsa-python = %{version}-%{release}
Requires: pypi-ecdsa-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : pypi(py)
BuildRequires : pypi(six)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Pure-Python ECDSA and ECDH
[![Build Status](https://github.com/tlsfuzzer/python-ecdsa/workflows/GitHub%20CI/badge.svg?branch=master)](https://github.com/tlsfuzzer/python-ecdsa/actions?query=workflow%3A%22GitHub+CI%22+branch%3Amaster)
[![Documentation Status](https://readthedocs.org/projects/ecdsa/badge/?version=latest)](https://ecdsa.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/tlsfuzzer/python-ecdsa/badge.svg?branch=master)](https://coveralls.io/github/tlsfuzzer/python-ecdsa?branch=master)
![condition coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/tomato42/9b6ca1f3410207fbeca785a178781651/raw/python-ecdsa-condition-coverage.json)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/tlsfuzzer/python-ecdsa.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tlsfuzzer/python-ecdsa/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/tlsfuzzer/python-ecdsa.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tlsfuzzer/python-ecdsa/alerts/)
[![Latest Version](https://img.shields.io/pypi/v/ecdsa.svg?style=flat)](https://pypi.python.org/pypi/ecdsa/)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat)

%package license
Summary: license components for the pypi-ecdsa package.
Group: Default

%description license
license components for the pypi-ecdsa package.


%package python
Summary: python components for the pypi-ecdsa package.
Group: Default
Requires: pypi-ecdsa-python3 = %{version}-%{release}

%description python
python components for the pypi-ecdsa package.


%package python3
Summary: python3 components for the pypi-ecdsa package.
Group: Default
Requires: python3-core
Provides: pypi(ecdsa)
Requires: pypi(six)

%description python3
python3 components for the pypi-ecdsa package.


%prep
%setup -q -n ecdsa-0.18.0
cd %{_builddir}/ecdsa-0.18.0
pushd ..
cp -a ecdsa-0.18.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672269913
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ecdsa
cp %{_builddir}/ecdsa-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ecdsa/a76ad7941d20352544795c378b35864426999206 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ecdsa/a76ad7941d20352544795c378b35864426999206

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
