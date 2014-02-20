%define _disable_ld_no_undefined 1

Summary:	CZShare plugin for FatRat
Name:		fatrat-czshare
Version:	1.1.3
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://fatrat.dolezel.info/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	fatrat-devel
Requires:	fatrat

%description
FatRat is an open source download manager for Linux/Unix systems written
in C++ with the help of the Qt4 library. It is rich in features and is
continuously developed.

%files
%{_libdir}/fatrat/plugins/libfatrat-czshare.so
%{_docdir}/%{name}/TRANSLATIONS

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

