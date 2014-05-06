%define		fversion	%(echo %{version} |tr r -)
%define		modulename	rJava
Summary:	Low-level R to Java interface
Name:		R-cran-%{modulename}
Version:	0.9r6
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	935d35c11f6060137ddd95784055ef4c
URL:		http://cran.r-project.org/web/packages/rJava/index.html
BuildRequires:	R >= 2.8.1
BuildRequires:	jdk
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-bibtex
BuildRequires:	texlive-xetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low-level interface to Java VM very much like .C/.Call and friends.
Allows creation of objects, calling methods and accessing fields.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
