#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko.becker@kde.org)
#
Name     : kompare
Version  : 24.02.2
Release  : 2
URL      : https://download.kde.org/stable/release-service/24.02.2/src/kompare-24.02.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.2/src/kompare-24.02.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.2/src/kompare-24.02.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 GPL-3.0
Requires: kompare-bin = %{version}-%{release}
Requires: kompare-data = %{version}-%{release}
Requires: kompare-lib = %{version}-%{release}
Requires: kompare-license = %{version}-%{release}
Requires: kompare-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : ktexteditor-dev
BuildRequires : libkomparediff2-dev
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Kompare 2.0
Kompare is a program to view the differences between files. Features include:

%package bin
Summary: bin components for the kompare package.
Group: Binaries
Requires: kompare-data = %{version}-%{release}
Requires: kompare-license = %{version}-%{release}

%description bin
bin components for the kompare package.


%package data
Summary: data components for the kompare package.
Group: Data

%description data
data components for the kompare package.


%package dev
Summary: dev components for the kompare package.
Group: Development
Requires: kompare-lib = %{version}-%{release}
Requires: kompare-bin = %{version}-%{release}
Requires: kompare-data = %{version}-%{release}
Provides: kompare-devel = %{version}-%{release}
Requires: kompare = %{version}-%{release}

%description dev
dev components for the kompare package.


%package doc
Summary: doc components for the kompare package.
Group: Documentation

%description doc
doc components for the kompare package.


%package lib
Summary: lib components for the kompare package.
Group: Libraries
Requires: kompare-data = %{version}-%{release}
Requires: kompare-license = %{version}-%{release}

%description lib
lib components for the kompare package.


%package license
Summary: license components for the kompare package.
Group: Default

%description license
license components for the kompare package.


%package locales
Summary: locales components for the kompare package.
Group: Default

%description locales
locales components for the kompare package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kompare-24.02.2
cd %{_builddir}/kompare-24.02.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713362811
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713362811
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kompare
cp %{_builddir}/kompare-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kompare/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kompare-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kompare/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kompare-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kompare/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kompare-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kompare/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kompare-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kompare/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kompare-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kompare/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kompare

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kompare

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kompare.desktop
/usr/share/icons/hicolor/128x128/apps/kompare.png
/usr/share/icons/hicolor/16x16/apps/kompare.png
/usr/share/icons/hicolor/22x22/apps/kompare.png
/usr/share/icons/hicolor/32x32/apps/kompare.png
/usr/share/icons/hicolor/48x48/apps/kompare.png
/usr/share/icons/hicolor/scalable/apps/kompare.svgz
/usr/share/kio/servicemenus/kompare.desktop
/usr/share/metainfo/org.kde.kompare.appdata.xml
/usr/share/qlogging-categories6/kompare.categories

%files dev
%defattr(-,root,root,-)
/usr/include/kompare/kompareinterface.h
/usr/lib64/libkompareinterface.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kompare/index.cache.bz2
/usr/share/doc/HTML/ca/kompare/index.docbook
/usr/share/doc/HTML/de/kompare/index.cache.bz2
/usr/share/doc/HTML/de/kompare/index.docbook
/usr/share/doc/HTML/en/kompare/dock.png
/usr/share/doc/HTML/en/kompare/index.cache.bz2
/usr/share/doc/HTML/en/kompare/index.docbook
/usr/share/doc/HTML/en/kompare/settings-diff1.png
/usr/share/doc/HTML/en/kompare/settings-diff2.png
/usr/share/doc/HTML/en/kompare/settings-diff3.png
/usr/share/doc/HTML/en/kompare/settings-diff4.png
/usr/share/doc/HTML/en/kompare/settings-view1.png
/usr/share/doc/HTML/en/kompare/settings-view2.png
/usr/share/doc/HTML/en/kompare/undock.png
/usr/share/doc/HTML/es/kompare/index.cache.bz2
/usr/share/doc/HTML/es/kompare/index.docbook
/usr/share/doc/HTML/et/kompare/index.cache.bz2
/usr/share/doc/HTML/et/kompare/index.docbook
/usr/share/doc/HTML/it/kompare/index.cache.bz2
/usr/share/doc/HTML/it/kompare/index.docbook
/usr/share/doc/HTML/it/kompare/settings-diff1.png
/usr/share/doc/HTML/it/kompare/settings-diff2.png
/usr/share/doc/HTML/it/kompare/settings-diff3.png
/usr/share/doc/HTML/it/kompare/settings-diff4.png
/usr/share/doc/HTML/it/kompare/settings-view1.png
/usr/share/doc/HTML/it/kompare/settings-view2.png
/usr/share/doc/HTML/nl/kompare/index.cache.bz2
/usr/share/doc/HTML/nl/kompare/index.docbook
/usr/share/doc/HTML/pt/kompare/index.cache.bz2
/usr/share/doc/HTML/pt/kompare/index.docbook
/usr/share/doc/HTML/pt_BR/kompare/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kompare/index.docbook
/usr/share/doc/HTML/ru/kompare/index.cache.bz2
/usr/share/doc/HTML/ru/kompare/index.docbook
/usr/share/doc/HTML/sv/kompare/index.cache.bz2
/usr/share/doc/HTML/sv/kompare/index.docbook
/usr/share/doc/HTML/sv/kompare/settings-diff1.png
/usr/share/doc/HTML/sv/kompare/settings-diff2.png
/usr/share/doc/HTML/sv/kompare/settings-diff3.png
/usr/share/doc/HTML/sv/kompare/settings-diff4.png
/usr/share/doc/HTML/sv/kompare/settings-view1.png
/usr/share/doc/HTML/sv/kompare/settings-view2.png
/usr/share/doc/HTML/uk/kompare/index.cache.bz2
/usr/share/doc/HTML/uk/kompare/index.docbook
/usr/share/doc/HTML/uk/kompare/settings-diff1.png
/usr/share/doc/HTML/uk/kompare/settings-diff2.png
/usr/share/doc/HTML/uk/kompare/settings-diff3.png
/usr/share/doc/HTML/uk/kompare/settings-diff4.png
/usr/share/doc/HTML/uk/kompare/settings-view1.png
/usr/share/doc/HTML/uk/kompare/settings-view2.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkomparedialogpages.so.5
/usr/lib64/libkompareinterface.so.5
/usr/lib64/qt6/plugins/kf6/parts/komparenavtreepart.so
/usr/lib64/qt6/plugins/kf6/parts/komparepart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kompare/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kompare/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kompare/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kompare/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kompare/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kompare.lang
%defattr(-,root,root,-)

