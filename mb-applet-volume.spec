%define name 	mb-applet-volume
%define version 0.1
%define release 1mdk

Summary: 	Volume control for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	ftp://ftp.handhelds.org/matchbox/sources/%name/%version/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
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

