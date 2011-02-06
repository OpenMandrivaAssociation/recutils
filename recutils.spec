Name:		recutils
Summary:	A set of tools and librairies to access recfiles
Version:	1.2
Release:	%mkrel 1
URL:		http://www.gnu.org/software/recutils
License:	GPLv3+
Group:		Databases
Source0:	ftp://ftp.gnu.org/gnu/recutils/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	curl-devel

%description
GNU Recutils is a set of tools and libraries to access human-editable, text-based databases
called recfiles. The data is stored as a sequence of records, each record containing an
arbitrary number of named fields.

%prep
%setup -q

%build
%configure2_5x --disable-static --disable-rpath
%make

%install
rm -fr %buildroot
%makeinstall_std
%find_lang %name

rm -fr %buildroot%_libdir/*.so %buildroot%_libdir/*.*a %buildroot%_includedir

%files
%doc ABOUT-NLS README AUTHORS ChangeLog 
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_infodir}/*
%{_datadir}/locale/de/LC_MESSAGES/recutils.mo
%{_datadir}/locale/fi/LC_MESSAGES/recutils.mo
%{_datadir}/locale/nl/LC_MESSAGES/recutils.mo
%{_datadir}/locale/sv/LC_MESSAGES/recutils.mo
