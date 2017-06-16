Summary:	K Desktop Environment Information Management runtime stuff
Name:		kdepim-runtime
Version:	17.04.2
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
Patch0:		kdepim-runtime-17.04.0-compile.patch
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	akonadi
BuildRequires:	pkgconfig(libstreams)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(shared-desktop-ontologies)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5GAPI) >= 5.1.0
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5DocTools)
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
BuildRequires:	cmake(KF5AlarmCalendar)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5Mbox)
BuildRequires:	cmake(KPimKDAV)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5WebKit)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:	shared-mime-info
BuildRequires:	xsltproc
Provides:	akonadi-kde = 3:%{version}
Obsoletes:	akonadi-kde < 3:%{version}
Requires:	akonadi >= 4:%{version}
Requires:	akonadi-contacts >= 3:%{version}
%if %{mdvver} >= 201400
Requires:	mariadb-client
%else
Requires:	mysql-client
%endif
Conflicts:	kio-pop3 < 3:16.04.3-2
Obsoletes:	kio-pop3 < %{EVRD}
Provides:	kio-pop3 = %{EVRD}

%description
Information Management applications for the K Desktop Environment runtime libs.

#-----------------------------------------------------------------------------

%files -f %{name}.lang
%config %{_sysconfdir}/xdg/kdepim-runtime.categories
%config %{_sysconfdir}/xdg/kdepim-runtime.renamecategories
%{_bindir}/*
%{_libdir}/qt5/plugins/akonadi*.so
%{_libdir}/qt5/plugins/kf5/kio/akonadi.so
%{_libdir}/qt5/plugins/kf5/kio/pop3.so
%{_libdir}/sasl2/*.so*
%{_datadir}/knotifications5/akonadi*
%{_datadir}/kservices5/akonadi.protocol
%{_datadir}/kservices5/akonadi
%{_datadir}/kservices5/pop3.protocol
%{_datadir}/kservices5/pop3s.protocol
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
KDE library for indexing mail.

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
%setup -q
%apply_patches

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang accountwizard_contacts
%find_lang accountwizard_ical
%find_lang accountwizard_imap
%find_lang accountwizard_kolab
%find_lang accountwizard_mailbox
%find_lang accountwizard_maildir
%find_lang accountwizard_pop3
%find_lang accountwizard_vcard
%find_lang accountwizard_vcarddir
%find_lang akonadi-filestore
%find_lang akonadi_birthdays_resource
%find_lang akonadi_contacts_resource
%find_lang akonadi_davgroupware_resource
%find_lang akonadi_gmail_resource
%find_lang akonadi_googlecalendar_resource
%find_lang akonadi_googlecontacts_resource
%find_lang akonadi_ical_resource
%find_lang akonadi_icaldir_resource
%find_lang akonadi_imap_resource
%find_lang akonadi_invitations_agent
%find_lang akonadi_kalarm_resource
%find_lang akonadi_maildir_resource
%find_lang akonadi_maildispatcher_agent
%find_lang akonadi_mbox_resource
%find_lang akonadi_migration_agent
%find_lang akonadi_mixedmaildir_resource
%find_lang akonadi_newmailnotifier_agent
%find_lang akonadi_openxchange_resource
%find_lang akonadi_pop3_resource
%find_lang akonadi_serializer_plugins
%find_lang akonadi_singlefile_resource
%find_lang akonadi_tomboynotes_resource
%find_lang akonadi_vcard_resource
%find_lang akonadi_vcarddir_resource
%find_lang gid-migrator
%find_lang libfolderarchivesettings
%find_lang kio_akonadi
%find_lang kio_pop3
%find_lang kioslave5 --with-html
cat *.lang >%{name}.lang
