Summary:	An implementation of httplib2 caching for requests in Python
Name:		python-cachecontrol
Version:	0.14.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/cachecontrol/
Source0:	https://files.pythonhosted.org/packages/source/C/CacheControl/cachecontrol-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

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
#%%{_bindir}/cachecontrol
%{py_sitedir}/cachecontrol
%{py_sitedir}/cachecontrol-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n cachecontrol-%{version}

%build
%py_build

%install
%py_install

