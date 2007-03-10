Summary:	Python module for MusicBrainz 2nd generation
Summary(pl.UTF-8):	Moduł języka Python dla MusicBrainz drugiej generacji
Name:		python-musicbrainz2
Version:	0.4.1
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/python-musicbrainz2/%{name}-%{version}.tar.gz
# Source0-md5:	c61079631f453059b56c8bcab525018c
URL:		http://icepick.info/projects/python-musicbrainz/
BuildRequires:	python-ctypes
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-ctypes
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package python-musicbrainz2 is a client library written in python,
which provides easy object oriented access to the MusicBrainz Database
using the XMLWebService. It has been written from scratch and uses a
different model than PythonMusicbrainz, the first generation python
bindings.


%description -l pl.UTF-8
Pakiet python-musicbrainz2 jest biblioteką napisaną w pythonie,
która dostarcza łatwy obiektowo zorientowany dostęp do Bazy
MusicBrainz używając XMLWebService.


%prep
%setup -q

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/musicbrainz2
%{_examplesdir}/%{name}-%{version}
