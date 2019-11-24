Summary: NethServer configuration for ddclient
Name: nethserver-ddclient
Version: 2.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
# Execute prep-sources to create Source1
Source1:        %{name}.tar.gz
BuildArch:      noarch
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools

Requires: ddclient
Requires: perl-JSON-Any

%description
NethServer configuration for ddclient

%prep
%setup

%post
%preun

%build
%{makedocs}
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

#force the creation of  the dyndns database....why ????
for _nsdb in dyndns; do
   mkdir -p root/%{_nsdbconfdir}/${_nsdb}/{migrate,force,defaults}
done 

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/

tar xvf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
chmod +x %{buildroot}/usr/libexec/nethserver/api/%{name}/*

%{genfilelist} $RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%dir %{_nsdbconfdir}/dyndns

%changelog
* Sun Nov 24 2019 stephane de Labrusse <stephdl@de-labrusse.fr> 2.0.1-1
- Cleanup obsolete providers 
- Enable a status props to enable/disabled ddclient configuration

* Sat Nov 23 2019 stephane de labrusse <stephdl@de-labrusse.fr> 2.0.0-1
- Cockpit release

* Mon Aug 27 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.0.7-1
- Dynu support added
- DTDNS dropped
- Password hidden field

* Thu Jan 04 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.5-1
- Strato support added

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr>  1.0.4-1
- Cloudflare support dropped

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr>  1.0.3-2
- GPL license

* Mon Feb 27 2017  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.3-1
- Added cloudfare dynamic dns provider

* Mon Feb 27 2017  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.2-1-ns7
- Changed the root email

* Tue Jan 31 2017  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-6-ns7
- Added selfhost dynamic dns provider

* Thu Jan 19 2017  Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-5-ns7
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
