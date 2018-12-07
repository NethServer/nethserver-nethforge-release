Summary: NethForge repositories
Name: nethserver-nethforge-release
Version: 7
Release: 3%{dist}
License: GPL
BuildArch: noarch
Source0: NethForge.repo 
Source1: RPM-GPG-KEY-NethForge-7

Requires: nethserver-release

%description
This package contains NethForge modules repository and
GPG key.


%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%install
rm -rf %{buildroot}

#GPG Key
install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-NethForge-7

# yum
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/NethForge.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-NethForge-7

%changelog
* Fri Dec 07 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-3
- Repository metadata GPG signature - NethServer/dev#5664

* Thu May 31 2018 Davide Principi <davide.principi@nethesis.it> - 7-2
- Fix the YUM mirrorlist URL

* Wed May 16 2018 Davide Principi <davide.principi@nethesis.it> - 7-1
- Add $nsrelease variable to mirrorlist query - NethServer/dev#5490

* Wed Jul 06 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7.0.3
- Change testing repository label

* Wed Jan 13 2016 Davide Principi <davide.principi@nethesis.it> - 7-0.1
- Updated repo URLs for ns7

* Wed Jun 04 2014 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 6-1
- Initial Package
