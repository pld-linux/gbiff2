#
# Conditional build:
%bcond_without	gnome	# without gnome applet support
#
Summary:	gbiff checks and informs for mail
Summary(pl):	Sprawdza i informuje o nowej poczcie
Name:           gbiff2
Version:        0.4.0
Release:        1
License:	GPL
Group:          Applications/Mail
Source0:        http://www.loria.fr/~rougier/gbiff/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	5ef36711b26d0dfd4ce42bcd67122218
URL:		http://www.loria.fr/~rougier/gbiff/index.php
%{?with_gnome:BuildRequires:	gnome-panel-devel}
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel >= 1.99.6
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
%{?with_gnome:Requires(post):	GConf2}
Obsoletes:	gbiff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gbiff checks for mail within afile, a qmail or MH style dir, or on a
POP3 server. It can display headers (number, sender, subject, and
date) when new mail has arrived.

%description -l pl
gbiff sprawdza pocztê wewn±trz plików, katalogów w stylu qmaila lub MH
lub na serwerze POP3. Potrafi wy¶wietlaæ nag³ówki (liczbê, autora,
temat i datê) gdy przychodzi nowa poczta.

%prep
%setup -q

%build
%configure \
	%{?with_gnome:--with-gnome} \
	--disable-schema-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONFTOOL=true

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with gnome}
%post
%gconf_schema_install
%endif

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/gbiff2
%{_datadir}/gbiff2
%{_datadir}/sounds/gbiff2
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
%if %{with gnome}
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%endif
