%define name	nfs4-acl-tools
%define version	0.3.3
%define release	%mkrel 1

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


