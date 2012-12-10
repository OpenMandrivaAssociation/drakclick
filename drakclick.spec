Summary:	A program to change Single/Double click in KDE
Name:		drakclick
Version:	0.2
Release:	%mkrel 8
Group:		Graphical desktop/KDE
Source0: 	drakclick
License:	GPL
URL:		http://www.advx.org/drakclick
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch: 	noarch

%description
A quick 5 minute hack to test GTK-perl and provide an easy way
to change the SingleClick vs DoubleClick KDE behavior.

%install
mkdir -p %{buildroot}/usr/bin
cp %{SOURCE0} %{buildroot}/usr/bin
mkdir -p %{buildroot}%{_docdir}/drakclick-%{version}
cat << EOF > %{buildroot}%{_docdir}/drakclick-%{version}/README
A quick 5 minute hack to test GTK-perl and provide an easy way
to change the SingleClick vs DoubleClick KDE behavior.
EOF


%clean
#Yeah, right ;-)

%files
%defattr(755,root,root)
%{_bindir}/drakclick
%{_docdir}/drakclick-%{version}




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-8mdv2011.0
+ Revision: 617891
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.2-7mdv2010.0
+ Revision: 428335
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.2-6mdv2009.0
+ Revision: 240634
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 16 2007 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2008.0
+ Revision: 87578
- kill dead email


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2-3mdv2007.0
+ Revision: 113864
- Import drakclick

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2-3mdv2007.1
- rebuild

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdk
- rebuild

