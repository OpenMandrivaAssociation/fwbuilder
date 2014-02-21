Summary:	Firewall Builder
Name:		fwbuilder
Version:	5.1.0.3599
Release:	6
License:	GPLv2+
Group:		System/Configuration/Networking
Url:		http://www.fwbuilder.org/
Source0:	http://downloads.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
Patch0:		fwbuilder-4.1.0-recognize-rosa.patch
Patch1:		ftbfs-gcc-4.7.diff
Patch2:		fwbuilder-5.1.0.3599-C++11.patch
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(libxslt)

%description
Firewall administration tool.

%files
%doc %{_datadir}/doc/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
./autogen.sh
%configure2_5x \
	--with-templatedir=%{_datadir}/%{name} \
	--with-docdir=%{_datadir}/doc/%{name}
%make

%install
make INSTALL_ROOT=%{buildroot} install

