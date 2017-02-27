Summary: NethServer configuration for ddclient
Name: nethserver-ddclient
Version: 1.0.2
Release: 1%{?dist}
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
echo "
 Hi

 All my development work is done in my free time and from my own expenses. 
 If you consider my work as something helpful, thank you to kindly make 
 a donation to my paypal account and allow me to continue paying my server 
 and all associated costs.

 https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ZPK8FKHVT4TY8

 Thank in advance.
 
 Stephane de Labrusse Alias Stephdl
"
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
* Mon Feb 27 2017  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.2-1-ns6
- Changed the root email

* Tue Jan 31 2017  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-6-ns6
- Added selfhost dynamic dns provider

* Thu Jan 19 2017  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-5-ns6
- string DynServer changed in translations

* Mon Dec 21 2015  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-4-ns6
- changed url of zoneedit 
- following http://community.nethserver.org/t/ddclient-using-wrong-url-for-zoneedit/2471

* Sun May 3 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-3-ns6
- disclamer
* Sun Apr 19 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-2-ns6
- Added dyndnsfree.de

* Sun Apr 19 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-1-ns6
- Added a custom field fro the server address and the ddclient protocol

* Wed Apr 15 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-8-ns6
- changed protocol of FreeDNS

* Wed Apr 15 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-7-ns6
- Creation of an internal database 'dyndns'
- template ddclient.conf cleaned

* Wed Apr 15 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-6-ns6
- FreeDNS Added

* Wed Apr 15 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-5-ns6
- Correction of web-skip

* Tue Apr 14 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-4-ns6
- added dnsdynamic.org

* Tue Apr 14 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-3-ns6
- added a tab to manage settings of ddclient service

* Tue Apr 14 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-2-ns6
- Initial release

