%global pgmajorversion 92
%global pginstdir /usr/pgsql-9.2
%global sname postgresql-9.2-fdw

Summary:	Read-only PostgreSQL FDW for 9.2
Name:           %{sname}
Version:	1.0
Release:	2%{?dist}
License:	BSD
Group:		Applications/Databases
Source0:	/usr/src/redhat/postgres_fdw-1.0-pgxs.tar
URL:		http://www.commandprompt.com/
BuildRequires:	postgresql%{pgmajorversion}-devel
Requires:	postgresql%{pgmajorversion}-server
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
postgres_fdw-1.0 is a read-only FDW for PostgreSQL. See the 9.3 docs for how it works.

%prep
%setup -q -n %{sname}-%{version}

%build
make PATH=%{pginstdir}/bin:$PATH PG_CONFIG=%{pginstdir}/bin/pg_config USE_PGXS=1 %{?_smp_mflags} 

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} PATH=%{pginstdir}/bin:$PATH PG_CONFIG=%{pginstdir}/bin/pg_config USE_PGXS=1 make install %{?_smp_mflags}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig 
%postun -p /sbin/ldconfig 

%files
#%defattr(-,root,root,-)
%{pginstdir}/lib/postgres_fdw.so
%{pginstdir}/share/extension/postgres_fdw--1.0.sql
%{pginstdir}/share/extension/postgres_fdw.control
