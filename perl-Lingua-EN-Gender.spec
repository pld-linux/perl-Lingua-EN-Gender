%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-Gender perl module
Summary(pl):	Modu³ perla Lingua-EN-Gender
Name:		perl-Lingua-EN-Gender
Version:	0.02
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Gender-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-EN-Gender - Inflect pronouns for a bunch of different genders.
Genders currently supported are: neuter, male, female, either, spivak,
splat, plural, egotistical, royal, 2nd, sie/hir, zie/zir.

%description -l pl
Lingua-EN-Gender - odmiana zaimków dla rodzajów: neuter, male, female,
either, spivak, splat, plural, egotistical, royal, 2nd, sie/hir,
zie/zir.

%prep
%setup -q -n Lingua-EN-Gender-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Lingua/EN/Gender.pm
%{_mandir}/man3/*
