%define _disable_ld_no_undefined 1

Name: kdepim4-runtime
Summary: K Desktop Environment
Version: 4.7.95
Release: 1
Group: Graphical desktop/KDE
License: GPL
Epoch: 3
URL: http://community.kde.org/KDE_PIM
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-runtime-%{version}.tar.bz2
Patch0:        kdepim-runtime-4.6.0-remove-po.patch
BuildRequires: kdelibs4-devel >= 2:4.5.71
BuildRequires: kdepimlibs4-devel >= 2:4.5.90
BuildRequires: boost-devel
BuildRequires: akonadi-devel >= 1:1.4.95
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
Conflicts: kdepim4-core < 2:4.5.94
Conflicts: kde-l10n-ar < 4.6.3-2
Conflicts: kde-l10n-bg < 4.6.3-2
Conflicts: kde-l10n-bn_IN < 4.3.98-4
Conflicts: kde-l10n-ca < 4.6.3-2
Conflicts: kde-l10n-cs < 4.6.3-2
Conflicts: kde-l10n-csb < 4.4.95-7
Conflicts: kde-l10n-da < 4.6.3-2
Conflicts: kde-l10n-de < 4.6.3-2
Conflicts: kde-l10n-el < 4.6.3-2
Conflicts: kde-l10n-en_GB < 4.6.3-2
Conflicts: kde-l10n-eo < 4.5.95-6
Conflicts: kde-l10n-es < 4.6.3-2
Conflicts: kde-l10n-et < 4.6.3-2
Conflicts: kde-l10n-eu < 4.6.3-2
Conflicts: kde-l10n-fa < 4.2.96-5
Conflicts: kde-l10n-fi < 4.6.3-2
Conflicts: kde-l10n-fr < 4.6.3-2
Conflicts: kde-l10n-fy < 4.5.95-6
Conflicts: kde-l10n-ga < 4.6.3-2
Conflicts: kde-l10n-gl < 4.6.3-2
Conflicts: kde-l10n-gu < 4.6.3-2
Conflicts: kde-l10n-he < 4.6.3-2
Conflicts: kde-l10n-hi < 4.6.3-2
Conflicts: kde-l10n-hne < 4.3.98-4
Conflicts: kde-l10n-hr < 4.6.3-2
Conflicts: kde-l10n-hu < 4.6.3-2
Conflicts: kde-l10n-id < 4.6.3-2
Conflicts: kde-l10n-is < 4.6.3-2
Conflicts: kde-l10n-it < 4.6.3-2
Conflicts: kde-l10n-ja < 4.6.3-2
Conflicts: kde-l10n-kk < 4.6.3-2
Conflicts: kde-l10n-km < 4.6.3-2
Conflicts: kde-l10n-kn < 4.6.3-2
Conflicts: kde-l10n-ko < 4.6.3-2
Conflicts: kde-l10n-ku < 4.3.2-4
Conflicts: kde-l10n-lt < 4.6.3-2
Conflicts: kde-l10n-lv < 4.6.3-2
Conflicts: kde-l10n-mai < 4.6.3-2
Conflicts: kde-l10n-mk < 4.4.95-7
Conflicts: kde-l10n-ml < 4.5.95-6
Conflicts: kde-l10n-mr < 4.3.98-4
Conflicts: kde-l10n-nb < 4.6.3-2
Conflicts: kde-l10n-nds < 4.6.3-2
Conflicts: kde-l10n-ne < 4.2.96-5
Conflicts: kde-l10n-nl < 4.6.3-2
Conflicts: kde-l10n-nn < 4.6.3-2
Conflicts: kde-l10n-pa < 4.6.3-2
Conflicts: kde-l10n-pl < 4.6.3-2
Conflicts: kde-l10n-pt < 4.6.3-2
Conflicts: kde-l10n-pt_BR < 4.6.3-2
Conflicts: kde-l10n-ro < 4.6.3-2
Conflicts: kde-l10n-ru < 4.6.3-4
Conflicts: kde-l10n-se < 4.2.96-6
Conflicts: kde-l10n-si < 4.4.95-7
Conflicts: kde-l10n-sk < 4.6.3-2
Conflicts: kde-l10n-sl < 4.6.3-2
Conflicts: kde-l10n-sr < 4.6.3-2
Conflicts: kde-l10n-sv < 4.6.3-2
Conflicts: kde-l10n-ta < 4.2.96-5
Conflicts: kde-l10n-tg < 4.4.95-7
Conflicts: kde-l10n-th < 4.6.3-2
Conflicts: kde-l10n-tr < 4.6.3-2
Conflicts: kde-l10n-uk < 4.6.3-2
Conflicts: kde-l10n-wa < 4.6.3-2
Conflicts: kde-l10n-zh_CN < 4.6.3-2
Conflicts: kde-l10n-zh_TW < 4.6.3-2
Requires: akonadi >= 1:1.4.95
Requires: mysql-client

%description -n akonadi-kde
Akonadi control center for KDE.

%files -n akonadi-kde -f %name.lang
%_kde_bindir/*
%_kde_appsdir/akonadi
%_kde_appsdir/akonadi_knut_resource
%_kde_appsdir/akonadi_maildispatcher_agent
%_kde_applicationsdir/*
%_kde_datadir/akonadi
%_kde_services/*
%_kde_datadir/mime/packages/*
%_kde_libdir/kde4/*
%_kde_iconsdir/*/*/*/*
%_kde_configdir/*
%_kde_datadir/autostart/kaddressbookmigrator.desktop
%_kde_servicetypes/davgroupwareprovider.desktop

#-----------------------------------------------------------------------------

%define akonadi_xml_major 4
%define libakonadi_xml %mklibname akonadi-xml %{akonadi_xml_major}

%package -n %libakonadi_xml
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_xml
KDE 4 library.

%files -n %libakonadi_xml
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
%_kde_libdir/libmaildir.so.%{maildir_major}*

#-----------------------------------------------------------------------------

%define akonadi_filestore_major 4
%define libakonadi_filestore %mklibname akonadi_filestore %{akonadi_filestore_major}

%package -n %libakonadi_filestore
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_filestore
KDE 4 library.

%files -n %libakonadi_filestore
%_kde_libdir/libakonadi-filestore.so.%{akonadi_filestore_major}*

#-----------------------------------------------------------------------------

%define kmindexreader_major 4
%define libkmindexreader %mklibname kmindexreader %{kmindexreader_major}

%package -n %libkmindexreader
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmindexreader
KDE 4 library.

%files -n %libkmindexreader
%_kde_libdir/libkmindexreader.so.%{kmindexreader_major}*

#----------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kdepimlibs4-devel >= 4.5.71
Requires: %{libakonadi_xml} = %{epoch}:%{version}-%release
Requires: %{libkdepim_copy} = %{epoch}:%{version}-%release
Requires: %{libmaildir} = %{epoch}:%{version}-%release
Requires: %{libakonadi_filestore} = %{epoch}:%{version}-%release
Requires: %{libkmindexreader} = %{epoch}:%{version}-%release

%description devel
This package contains header files needed if you wish to build applications
based on kdepim-runtime.

%files devel
%_kde_libdir/*.so
%_kde_datadir/dbus-1/interfaces/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-runtime-%version

%build
rm -fr po

%cmake_kde4
%make

%install
%makeinstall_std -C build



