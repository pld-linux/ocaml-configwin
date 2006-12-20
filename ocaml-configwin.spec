%define		strange_version		%(echo %{version} | tr . _)
%define		ocaml_ver	1:3.09.2
Summary:	Library to create config window with lablgtk
Summary(pl):	Biblioteka do tworzenia okienek konfiguracyjnych z u�yciem lablgtk
Name:		ocaml-configwin
Version:	0.93
Release:	8
License:	QPL
Group:		Libraries
Source0:	http://pauillac.inria.fr/~guesdon/Tools/Tars/configwin_%{strange_version}.tar.gz
# Source0-md5:	79e68d8e4af9e23434264af86c6fea12
Patch0:		%{name}-ocaml_version.patch
URL:		http://pauillac.inria.fr/~guesdon/Tools/configwin/configwin.html
BuildRequires:	autoconf
BuildRequires:	ocaml-camlp4 >= %{ocaml_ver}
BuildRequires:	ocaml-lablgtk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Configwin is a library used to edit configuration parameters of an
application using predefined boxes in LablGtk.

%description -l pl
Configwin jest bibliotek� s�u��c� do edycji konfigurowalnych
parametr�w aplikacji z u�yciem okienek dialogowych stworzonych z
pomoc� LablGtk.

%package devel
Summary:	Library to create config window with lablgtk
Summary(pl):	Biblioteka do tworzenia okienek konfiguracyjnych z u�yciem lablgtk
Group:		Development/Libraries
%requires_eq	ocaml-lablgtk
%requires_eq	ocaml

%description devel
Configwin is a library used to edit configuration parameters of an
application using predefined boxes in LablGtk.

%description devel -l pl
Configwin jest bibliotek� s�u��c� do edycji konfigurowalnych
parametr�w aplikacji z u�yciem okienek dialogowych stworzonych z
pomoc� LablGtk.

%prep
%setup -q -n configwin-%{version}
%patch0 -p1

%build
# this doesn't really matter (package makes little use of autoconf)
%{__autoconf}
%configure
%{__make} -j1 depend byte opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{site-lib,}/configwin
%{__make} install \
	OCAMLLIB=$RPM_BUILD_ROOT%{_libdir}/ocaml/configwin

install META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/configwin

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc ChangeLog configwin.mli example.ml LICENSE README
%{_libdir}/ocaml/site-lib/configwin
%{_libdir}/ocaml/configwin
