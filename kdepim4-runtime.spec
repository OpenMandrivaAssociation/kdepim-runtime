Name: kdepim4-runtime
Summary: K Desktop Environment
Version: 4.2.98
Release: %mkrel 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://pim.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-runtime-%version.tar.bz2
Buildroot:     %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdepimlibs4-devel >= 2:4.2.98
BuildRequires: automoc
BuildRequires: boost-devel
BuildRequires: akonadi-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: strigi-devel

%description
Information Management applications for the K Desktop Environment runtime libs.

%files

#----------------------------------------------------------------------

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE	

%description core
Core files for %name.

%files core
%defattr(-,root,root,-)


#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-runtime-%version

%build
%cmake_kde4

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

