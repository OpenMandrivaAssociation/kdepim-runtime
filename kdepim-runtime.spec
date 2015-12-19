%define _disable_ld_no_undefined 1
%define _disable_lto 1

Summary:	K Desktop Environment Information Management runtime stuff
Name:		kdepim-runtime
Version:	15.12.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/KDE_PIM
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Source1:	kdepim-runtime.rpmlintrc
BuildRequires:	boost-devel
BuildRequires:	akonadi
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5GAPI) >= 5.1.0
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5MailTransport)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5AlarmCalendar)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5AkonadiSocialUtils)
BuildRequires:	cmake(KF5KCMUtils)

BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiServer)
BuildRequires:  cmake(KF5Mbox)

BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Declarative)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Test)
BuildRequires:	shared-mime-info
BuildRequires:	xsltproc

%description
Information Management applications for the K Desktop Environment runtime libs.

#-----------------------------------------------------------------------------

%package -n akonadi-kde
Group:		Graphical desktop/KDE
Summary:	Akonadi control center for KDE
Provides:	kdepim-runtime = %{EVRD}
Conflicts:	kdepim4-runtime-devel < 2:4.7.97
Conflicts:	%{_lib}kdepim-copy4 < 3:4.9.0
Requires:	akonadi >= %{EVRD}
%if %{mdvver} >= 201400
Requires:	mariadb-client
%else
Requires:	mysql-client
%endif

%description -n akonadi-kde
Akonadi control center for KDE.

%files -n akonadi-kde
%config %{_sysconfdir}/xdg/kdepim-runtime.categories
%{_bindir}/*
%{_libdir}/qt5/plugins/akonadi*.so
%{_libdir}/qt5/plugins/kcm_akonadi*.so
%{_libdir}/qt5/plugins/kf5/kio/akonadi.so
%{_datadir}/knotifications5/akonadi*
%{_datadir}/kservices5/akonadi.protocol
%{_datadir}/kservices5/akonadi
%{_datadir}/kservices5/kcm_akonadi*.desktop
%{_datadir}/kservicetypes5/davgroupwareprovider.desktop
%{_datadir}/akonadi/accountwizard
%{_datadir}/akonadi/agents/*.desktop
%{_datadir}/akonadi/firstrun/*
%{_datadir}/akonadi/plugins/serializer/*.desktop
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.*.xml
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/mime/packages/kdepim-mime.xml

#-----------------------------------------------------------------------------

%define akonadi_filestore_major 5
%define libakonadi_filestore %mklibname akonadi_filestore %{akonadi_filestore_major}

%package -n %{libakonadi_filestore}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakonadi_filestore}
KDE library.

%files -n %{libakonadi_filestore}
%{_libdir}/libakonadi-filestore.so.%{akonadi_filestore_major}*

#-----------------------------------------------------------------------------

%define akonadi_singlefileresource_major 5
%define libakonadi_singlefileresource %mklibname akonadi_singlefileresource %{akonadi_singlefileresource_major}

%package -n %{libakonadi_singlefileresource}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libakonadi_singlefileresource}
KDE library.

%files -n %{libakonadi_singlefileresource}
%{_libdir}/libakonadi-singlefileresource.so.%{akonadi_singlefileresource_major}*

#-----------------------------------------------------------------------------

%define folderarchivesettings_major 5
%define libfolderarchivesettings %mklibname folderarchivesettings %{folderarchivesettings_major}

%package -n %{libfolderarchivesettings}
Summary:	KDE library
Group:		System/Libraries

%description -n %{libfolderarchivesettings}
KDE library.

%files -n %{libfolderarchivesettings}
%{_libdir}/libfolderarchivesettings.so.%{folderarchivesettings_major}*

#-----------------------------------------------------------------------------

%define kmindexreader_major 5
%define libkmindexreader %mklibname kmindexreader %{kmindexreader_major}

%package -n %{libkmindexreader}
Summary:	KDE library for indexing mail
Group:		System/Libraries

%description -n %{libkmindexreader}
KDE library for indexing mail

%files -n %{libkmindexreader}
%{_libdir}/libkmindexreader.so.%{kmindexreader_major}*

#-----------------------------------------------------------------------------

%define maildir_major 5
%define libmaildir %mklibname maildir %{maildir_major}

%package -n %{libmaildir}
Summary:	KDE library for handling maildir spools
Group:		System/Libraries

%description -n %{libmaildir}
KDE library.

%files -n %{libmaildir}
%{_libdir}/libmaildir.so.%{maildir_major}*

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-runtime-%{version}
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# Remove non packaged files
#rm -rf %{buildroot}%{_kde_libdir}/libnepomukfeederpluginlib.a
