Summary:	A Breakout style X Window System based game
Name:		xboing
Version:	2.4
Release:	8
Copyright:	MIT
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	ftp://ftp.x.org/pub/games/%{name}%{version}.tar.gz
Patch0:		xboing2.4.patch
Patch1:		xboing-2.4.patch
Patch2:		xboing-2.4-sparc.patch
Url:		http://www.catt.rmit.edu.au/xboing/xboing.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Xboing is an X Window System based game like the Breakout arcade game.
The object of the game is to keep a ball bouncing on the bricks until
you've broken through all of them.

%prep
%setup -q -n xboing
%patch -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS" \
	XBOING_DIR=%{_datadir}/xboing \
	HIGH_SCORE_FILE=/var/lib/games/xboing.score

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lib/games,%{_datadir}/xboing}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

make	DESTDIR=$RPM_BUILD_ROOT \
	XBOING_DIR=$RPM_BUILD_ROOT%{_datadir}/xboing \
	HIGH_SCORE_FILE=$RPM_BUILD_ROOT/var/lib/games/xboing.score \
	install install.man

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

cat > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/xboing <<EOF
xboing name "xboing"
xboing description "Breakout-style Game"
xboing group Games/Video
xboing exec "xboing &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config /var/lib/games/xboing.score
%config %{_sysconfdir}/X11/wmconfig/xboing
%attr(755,root,root) %{_bindir}/xboing
%{_datadir}/xboing
%{_mandir}/man1/xboing.1x.gz
