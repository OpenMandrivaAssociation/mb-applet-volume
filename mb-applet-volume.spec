%define name 	mb-applet-volume
%define version 0.2
%define release %mkrel 4

Summary: 	Volume control for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox-project.org
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
