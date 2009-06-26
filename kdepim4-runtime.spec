# TODO
# - Fix Descriptions
# - Use %major macro for lib packages
 
%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%if %unstable
%define dont_strip 1
%endif

%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn973768
%endif

Name: kdepim4-runtime
Summary: K Desktop Environment
Version: 4.2.95
Release: %mkrel 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://pim.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-runtime-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-runtime-%version.tar.bz2
%endif
Buildroot:     %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.1.81
BuildRequires: kdepimlibs4-devel >= 2:4.1.81
BuildRequires: gpgme-devel 
BuildRequires: X11-devel 
BuildRequires: flex 
BuildRequires: byacc 
BuildRequires: pam
BuildRequires: libncurses-devel
BuildRequires: readline-devel
BuildRequires: libgpg-error-devel
BuildRequires: gnokii-devel >= 0.6.18
BuildRequires: libxml2-utils
BuildRequires: gnupg
BuildRequires: bluez-devel 
BuildRequires: libsasl-devel
BuildRequires: pilot-link-devel
BuildRequires: libxslt-proc
BuildRequires: boost-devel
BuildRequires: qca2-devel
BuildRequires: glib2-devel
BuildRequires: libassuan-devel
BuildRequires: mysql-static-devel
BuildRequires: libmal-devel
BuildRequires: soprano-devel
BuildRequires: automoc
BuildRequires: akonadi-devel
#FIXME: Remove later
BuildRequires: kdepimlibs4-core
Suggests:      akonadi-common
Suggests:      kdepim4-akonadi

%description
Runtime files needed for pim based applications

%files

#--------------------------------------------------------------------

%package -n kdepim4-akonadi
Summary: KDE PIM storage framework
Group: Graphical desktop/KDE
URL: http://pim.kde.org/akonadi/
Requires: %name-core = %epoch:%version
Requires: mysql
Obsoletes: %name-akonadi < 1:3.93.0-1
Obsoletes: kde4-akonadi < 2:4.0.68
Provides: kde4-akonadi = %epoch:%version

%description -n kdepim4-akonadi
KDE PIM storage framework.

%files -n kdepim4-akonadi
%defattr(-,root,root)
%_kde_bindir/akonadi_*
%_kde_bindir/akonadiconsole
%_kde_bindir/akonaditray
%_kde_bindir/akonadi2xml
%_kde_bindir/kres-migrator
%_kde_appsdir/akonadi
%_kde_datadir/akonadi
%_kde_appsdir/akonadiconsole
%_kde_appsdir/akonadi_knut_resource
%_kde_datadir/applications/kde4/akonadiconsole.desktop
%_kde_datadir/applications/kde4/akonaditray.desktop
%_kde_datadir/kde4/services/akonadi.protocol
%_kde_libdir/kde4/kio_akonadi.so
%_kde_libdir/kde4/kabc_akonadi.so
%_kde_libdir/kde4/akonadi_*
%_kde_libdir/kde4/kcal_akonadi.so
%_kde_libdir/kde4/kcm_akonadi.so
%_kde_libdir/kde4/kcm_akonadi_*
%_kde_datadir/kde4/services/kcm_akonadi_resources.desktop
%_kde_datadir/kde4/services/kresources/kabc/akonadi.desktop
%_kde_datadir/kde4/services/kresources/kcal/akonadi.desktop
%_kde_datadir/kde4/services/kcm_akonadi.desktop
%_kde_datadir/kde4/services/kcm_akonadi_server.desktop
%_kde_datadir/config/kres-migratorrc
%_kde_iconsdir/hicolor/64x64/apps/kolab.png
%_kde_datadir/mime/packages/kdepim-mime.xml

#----------------------------------------------------------------------

%define libakonadi_kcal %mklibname akonadi-kcal 4

%package -n %libakonadi_kcal
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libakonadi_kcal
KDE 4 library.

%files -n %libakonadi_kcal
%defattr(-,root,root)
%_kde_libdir/libakonadi-kcal.so.*

#-----------------------------------------------------------------------------

%define libakonadi_kabccommon %mklibname akonadi-kabccommon 4

%package -n %libakonadi_kabccommon
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libakonadi_kabccommon
KDE 4 library.

%files -n %libakonadi_kabccommon
%defattr(-,root,root)
%_kde_libdir/libakonadi-kabccommon.so.*

#-----------------------------------------------------------------------------

%define libakonadi_xml %mklibname akonadi-xml 4

%package -n %libakonadi_xml
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_xml
KDE 4 library.

%files -n %libakonadi_xml
%defattr(-,root,root)
%_kde_libdir/libakonadi-xml.so.*

#-----------------------------------------------------------------------------

%define libakonadi_next %mklibname akonadi_next 4

%package -n %libakonadi_next
Summary: KDE 4 library
Group: System/Libraries

%description -n %libakonadi_next
KDE 4 library.

%files -n %libakonadi_next
%defattr(-,root,root)
%_kde_libdir/libakonadi_next.so.*

#-----------------------------------------------------------------------------

%define libmaildir %mklibname maildir 4

%package -n %libmaildir
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}kdepim42-common < 1:3.93.0-1

%description -n %libmaildir
KDE 4 library.

%files -n %libmaildir
%defattr(-,root,root)
%_kde_libdir/libmaildir.so.*

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

%define libmbox %mklibname mbox 4

%package -n %libmbox
Summary: KDE 4 library
Group: System/Libraries

%description -n %libmbox
KDE 4 library.

%files -n %libmbox
%defattr(-,root,root)
%_kde_libdir/libmbox.so.*

#-----------------------------------------------------------------------------

%package   devel
Summary:   Devel stuff for %name
Group:     Development/KDE and Qt
Conflicts: kdepim4-devel < 2:4.2.95
Requires:  %libakonadi_kcal = %epoch:%version
Requires:  %libmbox = %epoch:%version
Requires:  %libkdepim_copy = %epoch:%version
Requires:  %libmaildir = %epoch:%version
Requires:  %libakonadi_next = %epoch:%version
Requires:  %libakonadi_xml = %epoch:%version
Requires:  %libakonadi_kabccommon = %epoch:%version

%description  devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%defattr(-,root,root)
%_kde_includedir/akonadi
%_kde_libdir/libakonadi-kabccommon.so
%_kde_libdir/libakonadi-kcal.so
%_kde_libdir/libakonadi-xml.so
%_kde_libdir/libakonadi_next.so
%_kde_libdir/libkdepim-copy.so
%_kde_libdir/libmaildir.so
%_kde_libdir/libmbox.so
%_kde_datadir/dbus-1/interfaces/org.kde.Akonadi.Maildir.Settings.xml

#-----------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdepim-runtime-%version-%kde_snapshot
%else
%setup -q -n kdepim-runtime-%version
%endif

%build
%cmake_kde4

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

