Name:		recutils
Summary:	A set of tools and librairies to access recfiles
Version:	1.0
Release:	%mkrel 1
URL:		http://www.gnu.org/software/recutils
License:	GPLv3+
Group:		Databases
Source0:	ftp://ftp.gnu.org/software/recutils/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GNU Recutils is a set of tools and libraries to access human-editable, text-based databases
called recfiles. The data is stored as a sequence of records, each record containing an
arbitrary number of named fields.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
%find_lang %name

%files
%doc ABOUT-NLS README AUTHORS ChangeLog 
%{_bindir}/recdel
%{_bindir}/recfix
%{_bindir}/recinf
%{_bindir}/recins
%{_bindir}/recsel
%{_bindir}/recset
%{_includedir}/rec.h
%{_libdir}/librec.a
%{_libdir}/librec.la
%{_libdir}/librec.so
%{_libdir}/librec.so.0
%{_libdir}/librec.so.0.0.0
%{_datadir}/info/recutils.info.xz
%{_mandir}/man1/recdel.1.xz
%{_mandir}/man1/recfix.1.xz
%{_mandir}/man1/recinf.1.xz
%{_mandir}/man1/recins.1.xz
%{_mandir}/man1/recsel.1.xz
%{_mandir}/man1/recset.1.xz
%{_datadir}/recutils/etc/FSD.rec
%{_datadir}/recutils/etc/rec-mode.el

