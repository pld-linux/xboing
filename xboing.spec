Summary: A Breakout style X Window System based game.
Name: xboing
Version: 2.4
Release: 7
Copyright: MIT
Group: Amusements/Games
Source: ftp://ftp.x.org/pub/games/xboing2.4.tar.gz
Patch0: xboing2.4.patch
Patch1: xboing-2.4.patch
Patch2: xboing-2.4-sparc.patch
Url: http://www.catt.rmit.edu.au/xboing/xboing.html
BuildRoot: /var/tmp/xboing-root

%description
Xboing is an X Window System based game like the Breakout arcade game.
The object of the game is to keep a ball bouncing on the bricks until
you've broken through all of them.

%prep
%setup -q -n xboing
%patch -p1
%patch1 -p1
%patch2 -p1 -b .sparc

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr,var}/lib/games

make	DESTDIR=$RPM_BUILD_ROOT \
	XBOING_DIR=$RPM_BUILD_ROOT/usr/lib/games/xboing \
	HIGH_SCORE_FILE=$RPM_BUILD_ROOT/var/lib/games/xboing.score \
	install install.man

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/X11/wmconfig
  cat > ./etc/X11/wmconfig/xboing <<EOF
xboing name "xboing"
xboing description "Breakout-style Game"
xboing group Games/Video
xboing exec "xboing &"
EOF
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/man/man1/xboing.1x
/usr/X11R6/bin/xboing
/usr/lib/games/xboing
%config /var/lib/games/xboing.score
%config /etc/X11/wmconfig/xboing
