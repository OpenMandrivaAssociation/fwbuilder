%define name fwbuilder
%define version 2.1.19
%define release %mkrel 1

Name: %{name}
Summary: Firewall Builder
Url: http://www.fwbuilder.org/
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Configuration/Networking
Source: http://prdownloads.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
Patch0: fwbuilder-2.1.14-gcc43.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gettext-devel
BuildRequires:	glibc-static-devel 
BuildRequires:	libfwbuilder-devel >= %{version}
BuildRequires:	qt3-devel

%description
Firewall administration tool.

%prep
%setup -q
%patch0 -p1

%build

%{__libtoolize} --force --copy
%{__aclocal}
%{__autoconf}
%configure2_5x --enable-auto-docdir \
		--with-templatedir=%{_datadir}/%{name} --with-docdir=%{_datadir}/doc/%{name}
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
%doc %{_datadir}/doc/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
