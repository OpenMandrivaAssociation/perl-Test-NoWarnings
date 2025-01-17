%define	modname	Test-NoWarnings
%define modver 1.06

# Avoid nasty build dependency loop
%define dont_gprintify 1

Summary:	Make sure you didn't emit any warnings while testing
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	LGPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/Test::NoWarnings
Source0:	http://www.cpan.org/modules/by-module/Test/Test-NoWarnings-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Tester) >= 0.103

%description
In general, your tests shouldn't produce warnings. This modules causes
any warnings to be captured and stored. It automatically adds an extra
test that will run when your script ends to check that there were no
warnings. If there were any warings, the test will give a "not ok" and
diagnostics of where, when and what the warning was, including a stack
trace of what was going on when the it occurred.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Test
%{_mandir}/man3/*
