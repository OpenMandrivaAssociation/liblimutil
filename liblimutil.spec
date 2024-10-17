%define	major	0
%define	oname	limutil
%define	libname	%mklibname %{oname} %{major}
%define	devname	%mklibname -d limutil

Summary:	LIM OpenMax utility library
Name:		liblimutil
Version:	0.1.2
Release:	2
Group:		System/Libraries
License:	LGPLv2.1+
Url:		https://limoa.sourceforge.net/
Source0:	%{name}-%{version}.tar.xz
Patch0:		liblimutil-0.1.2-add-missing-pthread-linkage.patch

%description
LIM OpenMAX utility library.

%libpackage limutil %{major}

%package -n	%{devname}
Summary:	Development headers for LIM OpenMax utility library
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
Development headers for LIM OpenMAX utility library.

%files -n	%{devname}
%doc COPYING ChangeLog
%{_includedir}/limutil
%{_libdir}/liblimutil.so
%{_libdir}/pkgconfig/liblimutil.pc

%prep
%setup -q
%patch0 -p1 -b .pthread~
autoreconf -fiv

%build
%configure2_5x
%make

%install
%makeinstall_std

%changelog
* Wed Apr 9 2014 Per Øyvind Karlsen <proyvind@moondrake.org> 0.1.2-1
- initial release
