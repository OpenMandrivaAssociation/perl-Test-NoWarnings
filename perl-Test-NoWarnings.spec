%define	module	Test-NoWarnings
%define	modprefix Test
%define	version	0.084
%define	release	%mkrel 4

Summary:	Make sure you didn't emit any warnings while testing
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Development/Perl
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::Tester) >= 0.103
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot/
BuildArch:	noarch

%description
In general, your tests shouldn't produce warnings. This modules causes
any warnings to be captured and stored. It automatically adds an extra
test that will run when your script ends to check that there were no
warnings. If there were any warings, the test will give a "not ok" and
diagnostics of where, when and what the warning was, including a stack
trace of what was going on when the it occurred.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

