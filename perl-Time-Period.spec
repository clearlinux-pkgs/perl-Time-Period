#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Time-Period
Version  : 1.25
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/P/PB/PBOYD/Time-Period-1.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PB/PBOYD/Time-Period-1.25.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtime-period-perl/libtime-period-perl_1.25-1.debian.tar.xz
Summary  : 'A Perl module to deal with time periods.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Time-Period-license = %{version}-%{release}
Requires: perl-Time-Period-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This Perl module uses the conditions given by Perl.  This module may only
be distributed and or modified under the conditions given by Perl.

%package dev
Summary: dev components for the perl-Time-Period package.
Group: Development
Provides: perl-Time-Period-devel = %{version}-%{release}
Requires: perl-Time-Period = %{version}-%{release}

%description dev
dev components for the perl-Time-Period package.


%package license
Summary: license components for the perl-Time-Period package.
Group: Default

%description license
license components for the perl-Time-Period package.


%package perl
Summary: perl components for the perl-Time-Period package.
Group: Default
Requires: perl-Time-Period = %{version}-%{release}

%description perl
perl components for the perl-Time-Period package.


%prep
%setup -q -n Time-Period-1.25
cd %{_builddir}
tar xf %{_sourcedir}/libtime-period-perl_1.25-1.debian.tar.xz
cd %{_builddir}/Time-Period-1.25
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Time-Period-1.25/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Time-Period
cp %{_builddir}/Time-Period-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Time-Period/bb30d357e93b6e8da4e69bb61262c52e8f5afd7e || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Time::Period.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Time-Period/bb30d357e93b6e8da4e69bb61262c52e8f5afd7e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
