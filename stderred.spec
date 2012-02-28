Summary:	Colorize stderr in red
Name:		stderred
Version:	0.1
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://github.com/albinoloverats/stderred/tarball/master
# Source0-md5:	22cc54079d6ca05a4064202c56cfc1af
URL:		https://github.com/albinoloverats/stderred
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
stderred hooks on write() function from libc in order to colorize all
stderr output that goes to terminal thus making it distinguishable
from stdout. Basically it wraps text that goes to file with descriptor
"2" with proper escape codes making text red.

%prep
%setup -q -n albinoloverats-stderred-c07cb01

%build
%{__cc} stderred.c -D_GNU_SOURCE -Wall -ldl -fPIC -shared %{rpmcflags} -o %{name}.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

install %{name}.so $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/%{name}.so
