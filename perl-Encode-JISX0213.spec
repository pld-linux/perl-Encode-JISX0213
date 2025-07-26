#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Encode
%define		pnam	JISX0213
Summary:	Encode::JISX0213 - JIS X 0213 encodings
Summary(pl.UTF-8):	Encode::JISX0213 - kodowania JIS X 0213
Name:		perl-Encode-JISX0213
Version:	0.04
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d2d8ec4ebff4d44c40fe8d11d961f2b8
URL:		http://search.cpan.org/dist/Encode-JISX0213/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Encode-ISO2022 >= 0.03
BuildRequires:	perl-Test-Simple
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Two main modules and some supporting modules are contained.

Encode::JISX0213 - JIS X 0213 encodings
Encode::ShiftJIS2004 - shift_jis-2004 - JIS X 0213 Annex 1 encoding

%description -l pl.UTF-8
Pakiet zawiera dwa główne moduły oraz kilka wspierających.

Encode::JISX0213 - kodowania JIS X 0213
Encode::ShiftJIS2004 - kodowanie JIS X 0213 Annex 1 (shift_jis-2004)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Encode/JISX0213
%{perl_vendorarch}/Encode/JISX0213.pm
%{perl_vendorarch}/Encode/ShiftJIS2004.pm
%dir %{perl_vendorarch}/auto/Encode/JISX0213
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/JISX0213/JISX0213.so
%{_mandir}/man3/Encode::JISX0213.3pm*
%{_mandir}/man3/Encode::JISX0213::CCS.3pm*
%{_mandir}/man3/Encode::ShiftJIS2004.3pm*
