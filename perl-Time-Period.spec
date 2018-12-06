#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Time-Period
Version  : 1.25
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/P/PB/PBOYD/Time-Period-1.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PB/PBOYD/Time-Period-1.25.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtime-period-perl/libtime-period-perl_1.25-1.debian.tar.xz
Summary  : 'A Perl module to deal with time periods.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Time-Period-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This Perl module uses the conditions given by Perl.  This module may only
be distributed and or modified under the conditions given by Perl.

%package dev
Summary: dev components for the perl-Time-Period package.
Group: Development
Provides: perl-Time-Period-devel = %{version}-%{release}

%description dev
dev components for the perl-Time-Period package.


%package license
Summary: license components for the perl-Time-Period package.
Group: Default

%description license
license components for the perl-Time-Period package.


%prep
%setup -q -n Time-Period-1.25
cd ..
%setup -q -T -D -n Time-Period-1.25 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Time-Period-1.25/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Time-Period
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Time-Period/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Time-Period/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1Time/Period.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Time::Period.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Time-Period/LICENSE
/usr/share/package-licenses/perl-Time-Period/deblicense_copyright
