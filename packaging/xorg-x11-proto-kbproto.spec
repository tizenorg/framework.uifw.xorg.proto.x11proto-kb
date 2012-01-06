
Name:       xorg-x11-proto-kbproto
Summary:    X.Org X11 Protocol kbproto
Version:    1.0.5
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{version}.tar.gz
BuildRequires:  pkgconfig(xorg-macros)
Provides:   kbproto


%description
Description: %{summary}



%prep
%setup -q -n kbproto-%{version}


%build

%reconfigure --disable-shared

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 




%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/kbproto.pc
%{_includedir}/X11/extensions/XKB.h
%{_includedir}/X11/extensions/XKBsrv.h
%{_includedir}/X11/extensions/XKBproto.h
%{_includedir}/X11/extensions/XKBstr.h
%{_includedir}/X11/extensions/XKBgeom.h


