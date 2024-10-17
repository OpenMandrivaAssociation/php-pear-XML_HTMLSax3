%define		_class		XML
%define		_subclass	HTMLSax3
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	3.0.0
Release:	9
Summary:	A SAX parser for HTML and other badly formed XML documents
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/XML_HTMLSax3/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
XML_HTMLSax3 is a SAX based XML parser for badly formed XML documents, such as
HTML. The original code base was developed by Alexander Zhukov and published at
http://sourceforge.net/projects/phpshelve/. Alexander kindly gave permission to
modify the code and license for inclusion in PEAR.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-7mdv2012.0
+ Revision: 742302
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-6
+ Revision: 679606
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-5mdv2011.0
+ Revision: 613792
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.0.0-4mdv2010.1
+ Revision: 464953
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 3.0.0-3mdv2010.0
+ Revision: 441717
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-2mdv2009.1
+ Revision: 322827
- rebuild

* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-1mdv2009.0
+ Revision: 281925
- import php-pear-XML_HTMLSax3


* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-1mdv2009.0
- initial Mandriva package
