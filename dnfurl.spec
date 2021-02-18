Name:           dnfurl
Version:        0.1
Release:        1%{?dist}
Summary:        Simple utility for launching dnf:// url

License:        MIT
URL:            http://github.com/kagesenshi/dnfurl
Source0:        %{name}-%{version}.tar.gz

Requires:       xdg-utils

%description
A simple utility for launching dnf:// url. Only
support GNOME Sofware for now.

%prep
%setup -q 

%build
echo "OK"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
install -m 755 dnfurl $RPM_BUILD_ROOT/%{_bindir}/dnfurl
install -m 644 dnfurl.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/dnfurl.desktop

%files
%attr(755,root,root) %{_bindir}/dnfurl
%{_datadir}/applications/dnfurl.desktop

%changelog
* Thu Feb 18 2021 Izhar Firdaus <kagesenshi.87@gmail.com>
- initial package
