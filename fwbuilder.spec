%define name fwbuilder
%define version 3.0.0
%define svn 504
%define release %mkrel -c %svn 1

Name: %{name}
Summary: Firewall Builder
Url: http://www.fwbuilder.org/
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Configuration/Networking
Source: http://www.fwbuilder.org/nightly_builds/fwbuilder-3.0/build-%{svn}/%{name}-%{version}.tar.gz
Patch0: fwbuilder-3.0.0-recognize-mandriva.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gettext-devel
BuildRequires:	glibc-static-devel 
BuildRequires:	libfwbuilder-devel >= %{version}
BuildRequires:	qt4-devel

%description
Firewall administration tool.

%prep
%setup -q
%patch0 -p0

%build

%{__libtoolize} --force --copy
%{__aclocal}
%{__autoconf}
%configure2_5x \
		--with-templatedir=%{_datadir}/%{name} --with-docdir=%{_datadir}/doc/%{name}
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make INSTALL_ROOT="${RPM_BUILD_ROOT}/" install

# delete uneeded hidden files
rm -rf $RPM_BUILD_DIR/%name-%version/doc/.obj
rm -rf $RPM_BUILD_DIR/%name-%version/doc/.moc

%find_lang %{name}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
