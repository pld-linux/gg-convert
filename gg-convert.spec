Summary:	Simple program to convert Gadu-Gadu logs
Summary(pl.UTF-8):   Program do konwersji archiwum gg z formatu windowsowego na format ekg
Name:		gg-convert
Version:	1.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dom.comernet.pl/ekglog/%{name}.tar.bz2
# Source0-md5:	179d3b6b2625198744d29aecc6803793
URL:		http://dom.comernet.pl/ekglog/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple program to convert Gadu-Gadu logs.

%description -l pl.UTF-8
Program do konwersji archiwum gg z formatu windowsowego na format ekg.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install gg-convert $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Docs
%attr(755,root,root) %{_bindir}/*
