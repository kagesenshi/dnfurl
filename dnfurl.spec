%define debug_package %{nil}
%define _build_id_links none

Name:           dnfurl
Version:        0.1
Release:        1%{?dist}
Summary:        Simple utility for launching dnf:// url

License:        MIT
URL:            http://github.com/kagesenshi/dnfurl
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
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

desktop-file-install                                    \
    --dir=%{buildroot}%{_datadir}/applications              \
    dnfurl.desktop

desktop-file-install                                    \
    --add-category="AudioVideo"                             \
    --delete-original                                       \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{buildroot}/%{_datadir}/applications/dnfurl.desktop

desktop-file-validate %{buildroot}/%{_datadir}/applications/dnfurl.desktop

%files
%attr(755,root,root) %{_bindir}/dnfurl
%{_datadir}/applications/dnfurl.desktop

%post

%changelog
* Thu Feb 18 2021 Izhar Firdaus <kagesenshi.87@gmail.com>
- initial package
