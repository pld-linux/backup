Summary:	A backup strategy for Linux via CD-R
Name:		backup
Version:	4.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.bluehaze.com.au/unix/%{name}_%{version}.tar.gz
# Source0-md5:	6e7faf41f40d1e5c205ce5082b89e0a9
# Source0-size:	16509
Patch0:		%{name}-build.patch
URL:		http://www.bluehaze.com.au/unix/cdbkup.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -c
%patch0 -p0

%build
%{__cc} %{rpmcflags} %{rpmldflags} fsplit.c -o fsplit

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/%{name},%{_sbindir}}

install %{name} fsplit $RPM_BUILD_ROOT%{_sbindir}
install bex $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%attr(750,root,root) %dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/bex
