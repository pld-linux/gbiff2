Summary:	gbiff checks and informs for mail
Summary(pl):	Sprawdza i informuje o nowej poczcie
Name:		gbiff
Version:	2.4a
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://www.loria.fr/~rougier/gbiff/%{name}-%{version}.tar.gz
URL:		http://www.loria.fr/~rougier/gbiff/gbiff.html
BuildRequires:	gnome-libs-devel >= 1.2.13
BuildRequires:	gtk+-devel >= 1.2.5
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	perl
BuildRequires:	ORBit-devel
Requires:	applnk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11/GNOME

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
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I /usr/include/orbit-1.0"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	sysdir=%{_applnkdir}/Network/Mail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog THANKS
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Mail/*.desktop
%{_pixmapsdir}/%{name}
%{_datadir}/sounds/%{name}
%{_sysconfdir}/CORBA/servers/*
