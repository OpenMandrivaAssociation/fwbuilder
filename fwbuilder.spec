%define name fwbuilder
%define version 2.1.11
%define release %mkrel 1

Name: %{name}
Summary: Firewall Builder
Url: http://www.fwbuilder.org/
Version: %{version}
Release: %{release}
License: GPL
Group: System/Configuration/Networking
Source: http://prdownloads.sourceforge.net/fwbuilder/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gettext-devel
BuildRequires:	glibc-static-devel 
BuildRequires:	libfwbuilder-devel >= %{version}
BuildRequires:	qt3-devel

%description
Firewall administration tool.

%prep
%setup -q

%build
#export QTDIR=%_prefix/%_lib/qt3
#export PATH=${PATH}:${QTDIR}/bin/
#export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${QTDIR}/lib

%{__libtoolize} --force --copy
%{__aclocal}
%{__autoconf}
%configure --enable-auto-docdir \
		--with-templatedir=%{_datadir}/%{name}
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make DDIR="${RPM_BUILD_ROOT}/" install

# delete uneeded hidden files
rm -rf $RPM_BUILD_DIR/%name-%version/doc/.obj
rm -rf $RPM_BUILD_DIR/%name-%version/doc/.moc

%find_lang %{name}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%doc doc


