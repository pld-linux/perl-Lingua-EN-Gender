%define		pdir	Lingua
%define		pnam	EN-Gender
Summary:	Lingua::EN::Gender perl module
Summary(pl.UTF-8):	Moduł perla Lingua::EN::Gender
Name:		perl-Lingua-EN-Gender
Version:	0.02
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8f3877aabfc2be31e587d99ea792176
URL:		http://search.cpan.org/dist/Lingua-EN-Gender/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Gender - Inflect pronouns for a bunch of different
genders. Genders currently supported are: neuter, male, female,
either, spivak, splat, plural, egotistical, royal, 2nd, sie/hir,
zie/zir.

%description -l pl.UTF-8
Lingua::EN::Gender - odmiana zaimków dla rodzajów: neuter, male,
female, either, spivak, splat, plural, egotistical, royal, 2nd,
sie/hir, zie/zir.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Lingua/EN/Gender.pm
%{_mandir}/man3/*
