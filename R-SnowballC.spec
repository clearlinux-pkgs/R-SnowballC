#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-SnowballC
Version  : 0.6.0
Release  : 14
URL      : https://cran.r-project.org/src/contrib/SnowballC_0.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/SnowballC_0.6.0.tar.gz
Summary  : Snowball Stemmers Based on the C 'libstemmer' UTF-8 Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-SnowballC-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
Porter's word stemming algorithm for collapsing words to a common
  root to aid comparison of vocabulary. Currently supported languages are
  Danish, Dutch, English, Finnish, French, German, Hungarian, Italian,
  Norwegian, Portuguese, Romanian, Russian, Spanish, Swedish
  and Turkish.

%package lib
Summary: lib components for the R-SnowballC package.
Group: Libraries

%description lib
lib components for the R-SnowballC package.


%prep
%setup -q -c -n SnowballC

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547576033

%install
export SOURCE_DATE_EPOCH=1547576033
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SnowballC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SnowballC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library SnowballC
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library SnowballC|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/SnowballC/DESCRIPTION
/usr/lib64/R/library/SnowballC/INDEX
/usr/lib64/R/library/SnowballC/LICENSE
/usr/lib64/R/library/SnowballC/Meta/Rd.rds
/usr/lib64/R/library/SnowballC/Meta/features.rds
/usr/lib64/R/library/SnowballC/Meta/hsearch.rds
/usr/lib64/R/library/SnowballC/Meta/links.rds
/usr/lib64/R/library/SnowballC/Meta/nsInfo.rds
/usr/lib64/R/library/SnowballC/Meta/package.rds
/usr/lib64/R/library/SnowballC/NAMESPACE
/usr/lib64/R/library/SnowballC/NEWS
/usr/lib64/R/library/SnowballC/R/SnowballC
/usr/lib64/R/library/SnowballC/R/SnowballC.rdb
/usr/lib64/R/library/SnowballC/R/SnowballC.rdx
/usr/lib64/R/library/SnowballC/help/AnIndex
/usr/lib64/R/library/SnowballC/help/SnowballC.rdb
/usr/lib64/R/library/SnowballC/help/SnowballC.rdx
/usr/lib64/R/library/SnowballC/help/aliases.rds
/usr/lib64/R/library/SnowballC/help/paths.rds
/usr/lib64/R/library/SnowballC/html/00Index.html
/usr/lib64/R/library/SnowballC/html/R.css
/usr/lib64/R/library/SnowballC/libs/symbols.rds
/usr/lib64/R/library/SnowballC/words.R
/usr/lib64/R/library/SnowballC/words/danish.RData
/usr/lib64/R/library/SnowballC/words/dutch.RData
/usr/lib64/R/library/SnowballC/words/english.RData
/usr/lib64/R/library/SnowballC/words/finnish.RData
/usr/lib64/R/library/SnowballC/words/french.RData
/usr/lib64/R/library/SnowballC/words/german.RData
/usr/lib64/R/library/SnowballC/words/hungarian.RData
/usr/lib64/R/library/SnowballC/words/italian.RData
/usr/lib64/R/library/SnowballC/words/norwegian.RData
/usr/lib64/R/library/SnowballC/words/porter.RData
/usr/lib64/R/library/SnowballC/words/portuguese.RData
/usr/lib64/R/library/SnowballC/words/romanian.RData
/usr/lib64/R/library/SnowballC/words/russian.RData
/usr/lib64/R/library/SnowballC/words/spanish.RData
/usr/lib64/R/library/SnowballC/words/swedish.RData
/usr/lib64/R/library/SnowballC/words/turkish.RData

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/SnowballC/libs/SnowballC.so
/usr/lib64/R/library/SnowballC/libs/SnowballC.so.avx2
/usr/lib64/R/library/SnowballC/libs/SnowballC.so.avx512
