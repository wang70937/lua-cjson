%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luadatadir %{_datadir}/lua/%{luaver}

Name:		lua-cjson
Version:	1.1devel
Release:	1%{?dist}
Summary:	A fast JSON encoding/parsing library for Lua

Group:		Development/Libraries
License:	MIT
URL:		http://www.kyne.com.au/~mark/software/lua-cjson/
Source0:	http://www.kyne.com.au/~mark/software/lua-cjson/download/lua-cjson-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	lua >= %{luaver}, lua-devel >= %{luaver}
Requires:	lua >= %{luaver}

%description
The Lua CJSON library provides JSON support for Lua. It features:
- Fast, standards compliant encoding/parsing routines
- Full support for JSON with UTF-8, including decoding surrogate pairs
- Optional run-time support for common exceptions to the JSON specification
  (NaN, Infinity,..)
- No external dependencies


%prep
%setup -q


%build
make %{?_smp_mflags} CFLAGS="%{optflags}" LUA_INCLUDE_DIR="%{_includedir}"


%install
rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT" LUA_CMODULE_DIR="%{lualibdir}"
make install-extra DESTDIR="$RPM_BUILD_ROOT" LUA_MODULE_DIR="%{luadatadir}" \
	LUA_BIN_DIR="%{_bindir}"


%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-,root,root,-)
%doc LICENSE NEWS performance.txt manual.html manual.txt rfc4627.txt THANKS
%{_bindir}/*
%{lualibdir}/*
%{luadatadir}/*
%{_bindir}/*


%changelog
* Wed Nov 27 2011 Mark Pulford <mark@kyne.com.au> - 1.0.4-1
- Updated for 1.0.4

* Wed Sep 15 2011 Mark Pulford <mark@kyne.com.au> - 1.0.3-1
- Updated for 1.0.3

* Sun May 29 2011 Mark Pulford <mark@kyne.com.au> - 1.0.2-1
- Updated for 1.0.2

* Sun May 10 2011 Mark Pulford <mark@kyne.com.au> - 1.0.1-1
- Updated for 1.0.1

* Sun May 1 2011 Mark Pulford <mark@kyne.com.au> - 1.0-1
- Initial package
