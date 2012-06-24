Summary:	News portal is a PHP based newsreader
Summary(de):	PHP-Skript, welches den Zugriff auf Newsgruppen �ber Web erm�glicht
Summary(pl):	Skrypt w PHP umo�liwiaj�cy czytanie news�w przez przegl�dark�
Name:		newsportal
Version:	0.27
Release:	2
License:	GPL
Group:		Networking/News
Source0:	http://florian-amrhein.de/nw/newsportal/download/%{name}-%{version}.tar.gz
# Source0-md5:	617142436b571bde636801523dede1d1
URL:		http://florian-amrhein.de/newsportal/
Requires:	apache
Requires:	php
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wwwrootdir	/home/services/httpd
%define		_wwwuser	http
%define		_wwwgroup	http


%description
This PHP script enables the access to a newsserver (by NNTP) from a
webpage. It allows you to combine web-forums and newsgroups. The
script is also suitable for presentation of announce newsgroups on web
pages, without having the user notice that he is in fact accessing a
news server.

%description -l de
NewsPortal ist ein PHP-Skript, welches den Zugriff auf Newsgruppen
�ber Web erm�glicht. Diese Skriptsammlung erm�glicht von einer
Webseite aus den Zugriff auf einen Newsserver (per NNTP). Man kann
damit Webforen und Newsgruppen verbinden, so da� auf ein "Webforum"
auch per NNTP zugegriffen werden kann. Dieses Skript eignet sich auch
f�r die Pr�sentation von Announce-Newsgruppen auf Webseiten, ohne da�
der Benutzer merkt, da� er in Wirklichkeit auf einen Newsserver
zugreift.

%description -l pl
NewsPortal pozwala na utworzenie prostego i estetycznego interfejsu do
czytania grup newsowych (przy u�yciu protoko�u NNTP) przez
przegl�dark� www.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/{img,spool,doc,extras/{frames,lang}}

install *.{php,inc,txt} $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal
install img/* $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/img
install extras/lang/* $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/extras/lang
install extras/frames/* $RPM_BUILD_ROOT%{_wwwrootdir}/html/newsportal/extras/frames

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_wwwrootdir}/html/newsportal/*.php
%config(noreplace) %verify(not size mtime md5) %{_wwwrootdir}/html/newsportal/config.inc
%config(noreplace) %verify(not size mtime md5) %{_wwwrootdir}/html/newsportal/groups.txt
%{_wwwrootdir}/html/newsportal/*a*.inc
%{_wwwrootdir}/html/newsportal/img/*
%{_wwwrootdir}/html/newsportal/extras/*
%attr(700,%{_wwwuser},%{_wwwgroup}) %dir %{_wwwrootdir}/html/newsportal/spool
%doc doc/*
