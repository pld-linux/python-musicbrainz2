Summary:	Python module for MusicBrainz 2nd generation
Summary(pl.UTF-8):	Moduł języka Python dla MusicBrainz drugiej generacji
Name:		python-musicbrainz2
Version:	0.7.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/python-musicbrainz2/%{name}-%{version}.tar.gz
# Source0-md5:	7aa39add30fcd7e1724d4b29ba1f050e
URL:		http://musicbrainz.org/doc/PythonMusicBrainz2
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package python-musicbrainz2 is a client library written in python,
which provides easy object oriented access to the MusicBrainz Database
using the XMLWebService. It has been written from scratch and uses a
different model than PythonMusicbrainz, the first generation Python
bindings.

%description -l pl.UTF-8
Pakiet python-musicbrainz2 jest biblioteką napisaną w pythonie, która
dostarcza łatwy obiektowo zorientowany dostęp do bazy MusicBrainz przy
użyciu XMLWebService. Został napisany od zera i wykorzystuje inny
model niż PythonMusicbrainz - wiązania Pythona pierwszej generacji.

%prep
%setup -q

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} ./setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt CHANGES.txt COPYING.txt README.txt
%attr(755,root,root) %{_bindir}/mb-submit-disc
%{py_sitescriptdir}/musicbrainz2
%{py_sitescriptdir}/python_musicbrainz2-*.egg-info
%{_examplesdir}/%{name}-%{version}
