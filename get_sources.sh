#!/bin/sh

NAME=$(rpm -q --specfile *.spec --qf "%{name}")
VERSION=$(rpm -q --specfile *.spec --qf "%{version}")

rm -rf $NAME-$VERSION
git clone git://github.com/kororaproject/kp-gnome-shell-theme-korora.git $NAME-$VERSION

cd $NAME-$VERSION
DATE=$(git log -1 --date=iso | awk '/Date:/ { print $2 }' | sed 's@-@@g')
REV=$(git log -1 | awk '/commit / { print $2 }' | cut -b 1-6)

mv upstream/gnome-shell .
rm -rf upstream build

cd ..
tar cavf $NAME-$VERSION-${DATE}git${REV}.tar.xz $NAME-$VERSION --exclude=.git
rm -rf $NAME-$VERSION
