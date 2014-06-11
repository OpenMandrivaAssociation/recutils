Name:		recutils
Version:	1.7
Release:	1
Summary:	A set of tools to access GNU recfile databases
Group:		Databases
License:	GPLv3+
URL:		http://www.gnu.org/software/recutils/
Source0:	ftp://ftp.gnu.org/gnu/recutils/%{name}-%{version}.tar.gz
#Source1:	rec-mode-init.el
Patch0:		recutils-shared-lib-calls-exit.patch
Patch1:		recutils-Wformat.patch
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	autoconf
BuildRequires:	chrpath
BuildRequires:	libgcrypt-devel
BuildRequires:	help2man
BuildRequires:	mdbtools-devel
BuildRequires:	texinfo

%description
Recutils is a set of tools and libraries to access human-editable,
text-based databases called recfiles. The data is stored as a sequence
of records, each record containing an arbitrary number of named
fields.

%package devel
Summary:	Libraries and header files for recutils

Group:		Development/C
Requires:	%{name} = %{EVRD}

%description devel
Libraries and header files for recutils

%prep
%setup -q
%patch0 -p1 -b .shared-lib-calls-exit
%patch1 -p1 -b .Wformat

%build
autoreconf -fi
%configure --disable-static --disable-rpath
%make

%check
make check

%install
%makeinstall_std INSTALL="install -p"

rm -f %{buildroot}%{_infodir}/dir

chrpath --delete %{buildroot}%{_bindir}/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/recutils
%{_datadir}/emacs/site-lisp/*
%{_infodir}/*.info*

%files devel
%{_includedir}/rec.h
%{_libdir}/*.so
