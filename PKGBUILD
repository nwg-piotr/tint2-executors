# Maintainer: Piotr Miller <nwg.piotr@gmail.com>
pkgname=('tint2-executors')
pkgver=0.0.1
pkgrel=1
pkgdesc="Dummy package to install dependencies for the executors pack. See Wiki for usage info."
arch=('x86_64')
url="https://github.com/nwg-piotr/tint2-executors"
license=('GPL3')
depends=('grep' 'gawk' 'acpi' 'xorg-xbacklight' 'xorg-xrandr' 'alsa-utils' 'python' 'python-psutil'
'libnotify' 'xfce4-notifyd' 'wmctrl' 'zenity')
optdepends=('light-git: For machines not handling xbacklight')
source=(https://raw.githubusercontent.com/nwg-piotr/tint2-executors/master/tint2-executors)

md5sums=('bb9fce2f089312aab56ef7751d0e5aca')

package() {
  install -D -m 755 tint2-executors \
 	 "$pkgdir"/usr/bin/tint2-executors
}
