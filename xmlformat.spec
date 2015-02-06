Summary:	XML Document Formatter
Name:		xmlformat
Version:	1.04
Release:	5
License:	BSD
Group:		Publishing
URL:		http://www.kitebird.com/software/xmlformat/
Source0:	http://www.kitebird.com/software/xmlformat/%{name}-%{version}.tar.gz
BuildRequires:	perl
BuildRequires:	ruby
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
xmlformat is a configurable formatter (or "pretty-printer") for XML documents.
It provides control over indentation, line-breaking, and text wrapping. These
properties can be defined on a per-element basis.

xmlformat %{version} provides improved diagnostic information when a document
is not well-formed. (Prints line and token number, and stack trace). 

%prep

%setup -q

%build

%check
make test

%install
rm -fr %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 xmlformat.pl %{buildroot}%{_bindir}/
install -m0755 xmlformat.rb %{buildroot}%{_bindir}/

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS ChangeLog INSTALL LICENSE README TODO
%doc bad* test.conf docs tests
%{_bindir}/xmlformat.pl
%{_bindir}/xmlformat.rb


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.04-4mdv2010.0
+ Revision: 435149
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.04-3mdv2009.0
+ Revision: 242994
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 24 2007 Oden Eriksson <oeriksson@mandriva.com> 1.04-1mdv2008.0
+ Revision: 70873
- Import xmlformat



* Fri Aug 24 2007 Oden Eriksson <oeriksson@mandriva.com> 1.04-1mdv2008.0
- initial Mandriva package
