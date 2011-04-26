%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1053190
%endif

%define subrel 1

Name: kdepim4-runtime
Summary: K Desktop Environment
Version: 4.4.11.1
Release: %mkrel 0
Group: Graphical desktop/KDE
License: GPL
Epoch: 3
URL: http://pim.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-runtime-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-runtime-%version.tar.bz2
%endif
Buildroot:     %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdepimlibs4-devel >= 2:4.2.98
BuildRequires: automoc4
BuildRequires: boost-devel
BuildRequires: akonadi-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: strigi-devel
BuildRequires: qt4-qtdbus
BuildRequires: akonadi
BuildRequires: shared-desktop-ontologies-devel

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
Requires: mysql-client

%description -n akonadi-kde
Akonadi control center for KDE.

%files -n akonadi-kde
%defattr(-,root,root,-)
%_kde_bindir/*
%_kde_appsdir/akonadi
%_kde_appsdir/akonadi_knut_resource
%_kde_applicationsdir/*
%_kde_datadir/akonadi
%_kde_services/*
%_kde_datadir/mime/packages/*
%_kde_libdir/kde4/*
%_kde_iconsdir/*/*/*/*
%_kde_configdir/*
%_kde_datadir/autostart/kaddressbookmigrator.desktop

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
%_kde_libdir/libakonadi-xml.so.%{akonadi_xml_major}*

#-----------------------------------------------------------------------------

%define kdepim_copy_major 4
%define libkdepim_copy %mklibname kdepim-copy %{kdepim_copy_major}

%package -n %libkdepim_copy
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdepim_copy
KDE 4 library.

%files -n %libkdepim_copy
%defattr(-,root,root)
%_kde_libdir/libkdepim-copy.so.%{kdepim_copy_major}*

#-----------------------------------------------------------------------------

%define maildir_major 4
%define libmaildir %mklibname maildir %{maildir_major}

%package -n %libmaildir
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmaildir
KDE 4 library.

%files -n %libmaildir
%defattr(-,root,root)
%_kde_libdir/libmaildir.so.%{maildir_major}*

#-----------------------------------------------------------------------------

%define mbox_major 4
%define libmbox %mklibname mbox %{mbox_major}

%package -n %libmbox
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmbox
KDE 4 library.

%files -n %libmbox
%defattr(-,root,root)
%_kde_libdir/libmbox.so.%{mbox_major}*

#----------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel >= 2:4.2.98
Requires: kdepimlibs4-devel >= 4.2.96
Requires: %{libakonadi_xml} = %{epoch}:%{version}
Requires: %{libkdepim_copy} = %{epoch}:%{version}
Requires: %{libmaildir} = %{epoch}:%{version}
Requires: %{libmbox} = %{epoch}:%{version}

%description devel
This package contains header files needed if you wish to build applications
based on kdepim-runtime.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_datadir/dbus-1/interfaces/*

#----------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdepim-runtime-%version%kde_snapshot
%else
%setup -q -n kdepim-runtime-%version
%endif

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

