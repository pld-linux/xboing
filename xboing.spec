Summary:	A Breakout style X Window System based game
Summary(pl):	Gra pod X podobna do Breakout
Name:		xboing
Version:	2.4
Release:	12
License:	MIT
Group:		X11/Applications/Games
Source0:	http://www.techrescue.org/xboing/%{name}%{version}.tar.gz
# Source0-md5:	d596d29e53cf0deceb18f3b646787709
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}.patch
Patch1:		%{name}-Imakefile.patch
Patch2:		%{name}-sparc.patch
Patch3:		%{name}-visualfix.patch
URL:		http://www.techrescue.org/xboing/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d $RPM_BUILD_ROOT{/var/games,%{_datadir}/xboing,%{_desktopdir},%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT \
	XBOING_DIR=$RPM_BUILD_ROOT%{_datadir}/xboing \
	HIGH_SCORE_FILE=$RPM_BUILD_ROOT/var/games/xboing.score \
	install install.man

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README docs/*.doc
%attr(2755,root,games) %{_bindir}/xboing
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/xboing.score
%{_datadir}/xboing
%{_mandir}/man1/xboing.1x*
%{_desktopdir}/*
%{_pixmapsdir}/*
