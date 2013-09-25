Name:		bluez-hcidump
Version:	2.5
Release:	1%{?dist}
Summary:	Bluetooth packet analyzer

Group:		Bluetooth
License:	GPLv2
URL:		https://git.kernel.org/cgit/bluetooth/bluez-hcidump.git/
Source0:	%{name}-%{version}.tar.bz2

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}/bluez-hcidump

%build
./bootstrap
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sbindir}/hcidump
%doc %{_mandir}/man8/hcidump.8.gz

