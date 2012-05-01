Name: hyphen-pl
Summary: Polish hyphenation rules
%define upstreamid 20060726
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Source: http://pl.openoffice.org/pliki/hyph_pl_PL.zip
Group: Applications/Text
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
Requires: hyphen

%description
Polish hyphenation rules.

%prep
%setup -q -c -n hyphen-pl

%build
unzip hyph_pl_PL.zip
for i in README_hyph_pl_PL.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_pl_PL.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_hyph_pl_PL.txt
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20060726-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060726-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20060726-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060726-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 23 2007 Caolan McNamara <caolanm@redhat.com> - 0.20060726-1
- initial version
