%define 	module	TinyUrl
Summary:	super tiny library and command-line interface to tinyurl.com
Name:		python-%{module}
Version:	0.1.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/T/TinyUrl/%{module}-%{version}.tar.bz2
# Source0-md5:	a0b6a52ad898a35ea6280b43eb5c1be1
URL:		http://pypi.python.org/pypi/TinyUrl/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Super tiny library and command-line interface to tinyurl.com.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tinyurl
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/TinyUrl-*.egg-info
%endif
