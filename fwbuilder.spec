%define name fwbuilder
%define version 3.0.0
%define svn 445
%define release %mkrel -c %svn 1

Name: %{name}
Summary: Firewall Builder
Url: http://www.fwbuilder.org/
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Configuration/Networking
Source: http://www.fwbuilder.org/nightly_builds/fwbuilder-3.0/build-%{svn}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gettext-devel
BuildRequires:	glibc-static-devel 
BuildRequires:	libfwbuilder-devel >= %{version}
BuildRequires:	qt4-devel

%description
Firewall administration tool.

%prep
%setup -q

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

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Firewall Builder
Comment=Design and manage firewall configuration
Icon=fwbuilder
Categories=System;Settings;Security;Qt;
Exec=fwbuilder
Type=Application
StartupNotify=true
Terminal=false
EOF

# delete uneeded hidden files
rm -rf $RPM_BUILD_DIR/%name-%version/doc/.obj
rm -rf $RPM_BUILD_DIR/%name-%version/doc/.moc

mkdir -p %buildroot{%_iconsdir,%_miconsdir,%_liconsdir}
install -D src/gui/Icons/fwbuilder_16x16.png %buildroot%_miconsdir/%name.png
install -D src/gui/Icons/fwbuilder_32x32.png %buildroot%_iconsdir/%name.png
install -D src/gui/Icons/fwbuilder_48x48.png %buildroot%_liconsdir/%name.png

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
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_liconsdir}/%name.png
