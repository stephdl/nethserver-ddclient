Summary: NethServer configuration for ddclient
Name: nethserver-ddclient
Version: 1.0.0
Release: 4%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

AutoReq: no
Requires: ddclient


%description
NethServer configuration for ddclient

%prep
%setup

%post

%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)

%changelog
* Tue Apr 14 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-4-ns6
- added dnsdynamic.org

* Tue Apr 14 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-3-ns6
- added a tab to manage settings of ddclient service

* Tue Apr 14 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-2-ns6
- Initial release

