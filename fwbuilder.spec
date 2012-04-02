%define name fwbuilder
%define version 5.1.0.3599
%if %{mdvver} < 201100
%define release %mkrel 1
%else
%define release 1
%endif

Name: %{name}
Summary: Firewall administration tool
Url: http://www.fwbuilder.org/
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Configuration/Networking
Source0: http://downloads.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
Patch0: fwbuilder-4.1.0-recognize-mandriva.patch
BuildRequires:	gettext-devel
BuildRequires:	glibc-static-devel 
BuildRequires:	qt4-devel
BuildRequires:	ccache
BuildRequires:	cppunit-devel
BuildRequires:	net-snmp-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel

%description
Firewall Builder is a GUI firewall management application for iptables, PF,
Cisco ASA/PIX/FWSM, Cisco router ACL and more. Firewall configuration data is
stored in a central file that can scale to hundreds of firewalls managed
from a single UI.

%prep
%setup -q
%patch0 -p0

# delete uneeded hidden files
rm -rf doc/.obj
rm -rf doc/.moc

%build
./autogen.sh
%configure2_5x \
		--with-templatedir=%{_datadir}/%{name} --with-docdir=%{_docdir}/%{name}
%make

%install
make INSTALL_ROOT="%{buildroot}/" install

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
