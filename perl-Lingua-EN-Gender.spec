%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Gender
Summary:	Lingua::EN::Gender perl module
Summary(pl):	Modu³ perla Lingua::EN::Gender
Name:		perl-Lingua-EN-Gender
Version:	0.02
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Gender - Inflect pronouns for a bunch of different genders.
Genders currently supported are: neuter, male, female, either, spivak,
splat, plural, egotistical, royal, 2nd, sie/hir, zie/zir.

%description -l pl
Lingua::EN::Gender - odmiana zaimków dla rodzajów: neuter, male, female,
either, spivak, splat, plural, egotistical, royal, 2nd, sie/hir,
zie/zir.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Lingua/EN/Gender.pm
%{_mandir}/man3/*
