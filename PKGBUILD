# Maintainer: Eren Eroğlu <108634315+ereneroglum@users.noreply.github.com>

pkgname=jellyfin-rpc
pkgver=1.0.0
pkgrel=1
pkgdesc='Jellyfin Music RPC for Discord'
arch=('any')
url='https://github.com/iiarchives/jellyfin-rpc'
license=('MIT')
depends=(
  'python'
  'python-pydbus'
  'python-pypresence'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
)

source=( "$pkgname-$pkgver.tar.gz::https://github.com/ereneroglum/$pkgname/archive/refs/tags/$pkgver.tar.gz" )
sha512sums=('9b0bc0ef4c0d2f4c21f864a8a84613b2d4eda0eac339b88b54d4b3369470cc0adcac0461bae9db10abc706b9704a70006083b2a7526a245137dc4f967c201ec5')

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl

  install -Dm 644 docs/jellyfin-rpc.1 -t "${pkgdir}/usr/share/man/man1/"
  install -Dm 644 docs/example-systemd-unit.service "${pkgdir}/usr/lib/systemd/user/jellyfin-rpc.service"
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}/"
}

