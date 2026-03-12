%define module cachecontrol

Name:		python-cachecontrol
Summary:	An implementation of httplib2 caching for requests in Python
Version:	0.14.4
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/cachecontrol/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(uv-build)
BuildRequires:	python%{pyver}dist(wheel)

%description
CacheControl is a port of the caching algorithms in httplib2 for use with
requests session object.

It was written because httplib2’s better support for caching is often
mitigated by its lack of thread safety. The same is true of requests in
terms of caching.

%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/doesitcache
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
