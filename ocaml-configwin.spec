%define		strange_version		%(echo %{version} | sed -e 's/\\./_/')

Summary:	Glade to OCaml compiler
Summary(pl):	Kompilator Glade do OCamla
Name:		ocaml-configwin
Version:	0.93
Release:	1
License:	QPL
Group:		Development/Building
Vendor:		Maxence Guesdon <maxence.guesdon@inria.fr>
URL:		http://pauillac.inria.fr/~guesdon/Tools/configwin/configwin.html
Source0:	http://pauillac.inria.fr/~guesdon/Tools/Tars/configwin_%{strange_version}.tar.gz
BuildRequires:	ocaml-lablgtk-devel
%requires_eq	ocaml-lablgtk
%requires_eq	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Configwin is a library used to edit configuration parameters of an
application using predefined boxes in LablGtk.

%description -l pl
Configwin jest bibliotek± s³u¿±c± do edycji konfigurowalnych
parametrów aplikacji z u¿yciem okienek dialogowych stworzonych z
pomoc± LablGtk.

%prep
%setup -q -n configwin-%{version}

%build
# this doesn't really matter (package makes little use of autoconf)
autoconf
%configure
%{__make} depend byte opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{site-lib,}/configwin
%{__make} install OCAMLLIB=$RPM_BUILD_ROOT%{_libdir}/ocaml/configwin

install META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/configwin

gzip -9nf ChangeLog configwin.mli example.ml LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/ocaml/site-lib/configwin
%{_libdir}/ocaml/configwin
