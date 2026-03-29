#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library
#
Summary:	Gedit file loading and saving library
Summary(pl.UTF-8):	Biblioteka Gedita do ładowania i zapisywania plików
Name:		libgedit-gfls
Version:	0.3.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://gitlab.gnome.org/World/gedit/libgedit-gfls/-/tags
Source0:	https://gitlab.gnome.org/World/gedit/libgedit-gfls/-/archive/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	56bf5e342e5351a8deb8fc25928d3395
# older versions:
#Source0:	https://download.gnome.org/sources/libgedit-gfls/0.2/%{name}-%{version}.tar.xz
URL:		https://gitlab.gnome.org/World/gedit/libgedit-gfls
BuildRequires:	glib2-devel >= 1:2.78
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.22
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.25}
BuildRequires:	meson >= 0.64
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
Requires:	glib2 >= 1:2.78
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module dedicated to file loading and saving.

%description -l pl.UTF-8
Moduł służący do ładowania i zapisywania plików.

%package devel
Summary:	Header files for libgedit-gfls library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgedit-gfls
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.78

%description devel
Header files for libgedit-gfls library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgedit-gfls.

%package static
Summary:	Static libgedit-gfls library
Summary(pl.UTF-8):	Statyczna biblioteka libgedit-gfls
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgedit-gfls library.

%description static -l pl.UTF-8
Statyczna biblioteka libgedit-gfls.

%package apidocs
Summary:	API documentation for libgedit-gfls library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgedit-gfls
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libgedit-gfls library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgedit-gfls.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	%{!?with_apidocs:-Dgtk_doc=false}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang libgedit-gfls-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgedit-gfls-1.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%{_libdir}/libgedit-gfls-1.so.0
%{_libdir}/girepository-1.0/Gfls-1.typelib

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgedit-gfls-1.so
%{_includedir}/libgedit-gfls-1
%{_datadir}/gir-1.0/Gfls-1.gir
%{_pkgconfigdir}/libgedit-gfls-1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgedit-gfls-1.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgedit-gfls-1
%endif
