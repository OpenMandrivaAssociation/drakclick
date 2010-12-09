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


