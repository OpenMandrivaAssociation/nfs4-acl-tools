%define name	nfs4-acl-tools
%define version	0.3.3
%define release	3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	NFSv4 ACL tools
Group:		System/Kernel and hardware
License:	LGPL and GPL
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/nfs4-acl-tools/%{name}-%{version}.tar.gz
Patch:      nfs4-acl-tools-0.3.3-replace-strlcpy.patch
BuildRequires:  qt4-devel
BuildRequires:	libtool
BuildRequires:	libattr-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This package contains commandline ACL utilities for the Linux NFSv4 client.

%package gui
Summary:	GUI for for %{name}
Group:		System/Kernel and hardware

%description gui
This package contains GUI ACL utilities for the Linux NFSv4 client.

%prep
%setup -q
%patch -p 1

%build
%configure2_5x
%make
cd GUI/nfs4-acl-editor
%{_prefix}/lib/qt4/bin/qmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -m 755 GUI/nfs4-acl-editor/nfs4-acl-editor %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO VERSION INSTALL COPYING
%{_bindir}/nfs4_getfacl
%{_bindir}/nfs4_setfacl
%{_bindir}/nfs4_editfacl
%{_mandir}/man?/*

%files gui
%defattr(-,root,root)
%{_bindir}/nfs4-acl-editor




%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3.3-2mdv2010.0
+ Revision: 440329
- rebuild

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.3-1mdv2009.1
+ Revision: 354886
- new version
- new version

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3.2-3mdv2009.0
+ Revision: 253870
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 106231
- update to new version 0.3.2


* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2007.1
+ Revision: 140404
- fix build
- fix deps (libattr-devel)
- fix deps

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Imported nfs4-acl-tools-0.3.1-1mdv2007.1 into SVN repository.

* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-1mdv2007.1
- first mdv release

