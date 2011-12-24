%define name fwbuilder
%define version 5.0.1.3592
%define release %mkrel 1

Name: %{name}
Summary: Firewall Builder
Url: http://www.fwbuilder.org/
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Configuration/Networking
Source: http://downloads.sourceforge.net/fwbuilder/%name-%version.tar.gz
Patch0: fwbuilder-4.1.0-recognize-mandriva.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gettext-devel
BuildRequires:	glibc-static-devel 
BuildRequires:	qt4-devel
BuildRequires:	ccache
BuildRequires:	cppunit-devel
BuildRequires:	net-snmp-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel

%description
Firewall administration tool.

%prep
%setup -q
%patch0 -p0

%build
./autogen.sh
%define Werror_cflags %nil
%configure2_5x \
		--with-templatedir=%{_datadir}/%{name} --with-docdir=%{_datadir}/doc/%{name}
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make INSTALL_ROOT="${RPM_BUILD_ROOT}/" install

# delete uneeded hidden files
rm -rf %{_builddir}/%name-%version/doc/.obj
rm -rf %{_builddir}/%name-%version/doc/.moc

#find_lang %{name}

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
