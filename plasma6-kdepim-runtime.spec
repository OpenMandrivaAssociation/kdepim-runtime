Summary:	K Desktop Environment Information Management runtime stuff
Name:		plasma6-kdepim-runtime
Version:	24.01.80
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://community.kde.org/KDE_PIM
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kdepim-runtime-%{version}.tar.xz
Source1:	kdepim-runtime.rpmlintrc
Patch0:		kdepim-runtime-23.03.90-clang-16.patch
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	plasma6-akonadi
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KPim6GAPI)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KPim6PimCommon)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	cmake(KPim6AkonadiNotes)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:	cmake(KF6DAV)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6LdapCore)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	cmake(Qt6NetworkAuth)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	shared-mime-info
BuildRequires:	xsltproc
Requires:	plasma6-akonadi >= %{version}
Requires:	plasma6-akonadi-contacts >= %{version}

%description
Information Management applications for the K Desktop Environment runtime libs.

#-----------------------------------------------------------------------------

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kdepim-runtime.categories
%{_datadir}/qlogging-categories6/kdepim-runtime.renamecategories
%{_bindir}/*
%{_libdir}/qt6/plugins/kf6/kio/akonadi.so
#{_libdir}/qt6/plugins/kf6/kio/pop3.so
%{_datadir}/knotifications6/akonadi*
%{_datadir}/akonadi/agents/*.desktop
%{_datadir}/akonadi/davgroupware-providers
%{_datadir}/akonadi/firstrun/*
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.*.xml
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/mime/packages/kdepim-mime.xml
%{_libdir}/qt6/plugins/pim6/akonadi/config/*.so
%{_libdir}/qt6/plugins/pim6/kcms/kaddressbook/kcm_ldap.so
%{_datadir}/applications/org.kde.akonadi_davgroupware_resource.desktop
%{_datadir}/applications/org.kde.akonadi_google_resource.desktop
%{_datadir}/applications/org.kde.akonadi_imap_resource.desktop
%{_libdir}/qt6/plugins/pim6/mailtransport/mailtransport_akonadiplugin.so
%{_datadir}/applications/org.kde.akonadi_contacts_resource.desktop
%{_datadir}/applications/org.kde.akonadi_ews_resource.desktop
%{_datadir}/applications/org.kde.akonadi_openxchange_resource.desktop
%{_datadir}/applications/org.kde.akonadi_vcard_resource.desktop
%{_datadir}/applications/org.kde.akonadi_vcarddir_resource.desktop

%libpackage akonadi-filestore 6
%{_libdir}/libakonadi-filestore.so.5*

%libpackage akonadi-singlefileresource 6
%{_libdir}/libakonadi-singlefileresource.so.5*

%libpackage folderarchivesettings 6
%{_libdir}/libfolderarchivesettings.so.5*

%libpackage kmindexreader 6
%{_libdir}/libkmindexreader.so.5*

%libpackage maildir 6
%{_libdir}/libmaildir.so.5*

%libpackage newmailnotifier 6
%{_libdir}/libnewmailnotifier.so.5*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kdepim-runtime-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html
