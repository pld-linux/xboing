Summary:	A Breakout style X Window System based game
Summary(pl):	Gra pod X podobna do Breakout
Name:		xboing
Version:	2.4
Release:	10
License:	MIT
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.techrescue.org/xboing/%{name}%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}.patch
Patch1:		%{name}-Imakefile.patch
Patch2:		%{name}-sparc.patch
Patch3:		%{name}-visualfix.patch
URL:		http://www.techrescue.org/xboing/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xboing is an X Window System based game like the Breakout arcade game.
The object of the game is to keep a ball bouncing on the bricks until
you've broken through all of them.

%description -l pl
Xboing jest gr± pod X Window System podobn± do klasycznej gry
Breakout. Celem gry jest utrzymanie pi³ki odbijaj±cej siê od cegie³ a¿
do przebicia siê przez wszystkie.

%prep
%setup -q -n xboing
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
xmkmf
%{__make} \
	CC=%{__cc} \
	CDEBUGFLAGS="%{rpmcflags}" \
	XBOING_DIR=%{_datadir}/xboing \
	HIGH_SCORE_FILE=/var/games/xboing.score

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/games,%{_datadir}/xboing,%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	XBOING_DIR=$RPM_BUILD_ROOT%{_datadir}/xboing \
	HIGH_SCORE_FILE=$RPM_BUILD_ROOT/var/games/xboing.score \
	install install.man

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf COPYRIGHT README docs/*.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/*.gz
%attr(2755,root,games) %{_bindir}/xboing
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xboing.score
%{_datadir}/xboing
%{_mandir}/man1/xboing.1x*
%{_applnkdir}/Games/Arcade/xboing.desktop
%{_pixmapsdir}/*
