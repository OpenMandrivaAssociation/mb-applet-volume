%define name 	mb-applet-volume
%define version 0.2
%define release 6

Summary: 	Volume control for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		https://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.bz2

BuildRequires:	gtk2-devel matchbox-devel libXsettings-client-devel

%description
Volume for the Matchbox Desktop

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS TODO 
%_bindir/mb*
%_datadir/applications/*
%_datadir/pixmaps/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-5mdv2011.0
+ Revision: 620304
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2010.0
+ Revision: 429992
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2009.0
+ Revision: 252097
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 0.2-1mdv2008.1
+ Revision: 106281
- New version 0.2
- import mb-applet-volume


* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.1-1mdk
- initial package

