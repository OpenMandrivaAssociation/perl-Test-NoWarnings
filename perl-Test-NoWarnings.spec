%define	upstream_name	 Test-NoWarnings
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Make sure you didn't emit any warnings while testing
License:	LGPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Tester) >= 0.103

BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Test


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-4mdv2012.0
+ Revision: 765724
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-3
+ Revision: 764245
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.20.0-2
+ Revision: 667331
- mass rebuild

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 596039
- update to new version 1.02

* Fri Jan 15 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 491633
- update to 1.01

* Tue Jan 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 490071
- update to 1.00

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.084-4mdv2009.0
+ Revision: 258539
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.084-3mdv2009.0
+ Revision: 246542
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.084-1mdv2008.1
+ Revision: 104586
- update to new version 0.084

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.083-1mdv2008.0
+ Revision: 22117
- 0.083


* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 12:05:47 (60022)
- fixed typo

* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 11:59:35 (60018)
- spec file cleanup
- bump release for rebuild

* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 11:49:15 (60008)
Import perl-Test-NoWarnings

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.082-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Mon Mar 06 2006 Buchan Milne <bgmilne@mandriva.org> 0.082-2mdk
- Rebuild
- use mkrel

* Tue Oct 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.082-1mdk
- Initial MDV release

