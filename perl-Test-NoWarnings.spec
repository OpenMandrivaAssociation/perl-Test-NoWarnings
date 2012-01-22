%define	upstream_name	 Test-NoWarnings
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Make sure you didn't emit any warnings while testing
License:	LGPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::Tester) >= 0.103

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
In general, your tests shouldn't produce warnings. This modules causes
any warnings to be captured and stored. It automatically adds an extra
test that will run when your script ends to check that there were no
warnings. If there were any warings, the test will give a "not ok" and
diagnostics of where, when and what the warning was, including a stack
trace of what was going on when the it occurred.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Test
