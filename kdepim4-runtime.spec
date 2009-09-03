Name: kdepim4-runtime
Summary: K Desktop Environment
Version: 4.3.1
Release: %mkrel 2
Group: Graphical desktop/KDE
License: GPL
Epoch: 2
URL: http://pim.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-runtime-%version.tar.bz2
Patch100: kdepim-runtime-bug205742-rev1019460-filename.patch
Buildroot:     %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdelibs4-experimental-devel >= 2:4.2.98
BuildRequires: kdepimlibs4-devel >= 2:4.2.98
BuildRequires: automoc4
BuildRequires: boost-devel
BuildRequires: akonadi-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: strigi-devel
BuildRequires: qt4-qtdbus
BuildRequires: akonadi

%description
Information Management applications for the K Desktop Environment runtime libs.

#-----------------------------------------------------------------------------

%package -n akonadi-kde
Group: Graphical desktop/KDE
Summary: Akonadi control center for KDE
Obsoletes: kdepim4-runtime < 2:4.3.1-2
Provides: kdepim4-runtime = %{epoch}:%{version}-%{release}
Obsoletes: kdepim4-akonadi < 2:4.3.0
Conflicts: kdepim4-kresources < 2:4.3.0-1
Requires: akonadi >= 1:1.2.1

%description -n akonadi-kde
Akonadi control center for KDE.

%files -n akonadi-kde
%defattr(-,root,root,-)
%_kde_bindir/*
%_kde_appsdir/akonadi
%_kde_appsdir/akonadiconsole
%_kde_appsdir/akonadi_knut_resource
%_kde_applicationsdir/*
%_kde_datadir/akonadi
%_kde_services/*
%_kde_datadir/mime/packages/*
%_kde_libdir/kde4/*
%_kde_iconsdir/*/*/*/*
%_kde_configdir/*

#-----------------------------------------------------------------------------

%define akonadi_kabccommon_major 4
%define libakonadi_kabccommon %mklibname akonadi-kabccommon %{akonadi_kabccommon_major}

%package -n %libakonadi_kabccommon
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_kabccommon
KDE 4 library.

%files -n %libakonadi_kabccommon
%defattr(-,root,root)
%_kde_libdir/libakonadi-kabccommon.so.*

#-----------------------------------------------------------------------------

%define akonadi_kcal_major 4
%define libakonadi_kcal %mklibname akonadi-kcal %{akonadi_kcal_major}

%package -n %libakonadi_kcal
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_kcal
KDE 4 library.

%files -n %libakonadi_kcal
%defattr(-,root,root)
%_kde_libdir/libakonadi-kcal.so.*

#-----------------------------------------------------------------------------

%define akonadi_xml_major 4
%define libakonadi_xml %mklibname akonadi-xml %{akonadi_xml_major}

%package -n %libakonadi_xml
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_xml
KDE 4 library.

%files -n %libakonadi_xml
%defattr(-,root,root)
%_kde_libdir/libakonadi-xml.so.*

#-----------------------------------------------------------------------------

%define libakonadi_next %mklibname akonadi-next 4

%package -n %libakonadi_next
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname akonadi_next 4}

%description -n %libakonadi_next
KDE 4 library.

%files -n %libakonadi_next
%defattr(-,root,root)
%_kde_libdir/libakonadi_next.so.*

#-----------------------------------------------------------------------------

%define libkdepim_copy %mklibname kdepim-copy 4

%package -n %libkdepim_copy
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdepim_copy
KDE 4 library.

%files -n %libkdepim_copy
%defattr(-,root,root)
%_kde_libdir/libkdepim-copy.so.*

#-----------------------------------------------------------------------------

%define libmaildir %mklibname maildir 4

%package -n %libmaildir
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmaildir
KDE 4 library.

%files -n %libmaildir
%defattr(-,root,root)
%_kde_libdir/libmaildir.so.*

#----------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel >= 2:4.2.98
Requires: kdelibs4-experimental-devel >= 2:4.2.98
Requires: kdepimlibs4-devel >= 4.2.96
Requires: %{libakonadi_kcal}
Requires: %{libakonadi_xml}
Requires: %{libakonadi_kabccommon}
Requires: %{libakonadi_next}
Requires: %{libkdepim_copy}
Requires: %{libmaildir}

%description  devel
This package contains header files needed if you wish to build applications
based on kdepim-runtime.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*
%_kde_datadir/dbus-1/interfaces/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-runtime-%version
%patch100 -p0 -b .orig

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

