Name:		swappy
Version:	1.8.0
Release:	1
Source0:	https://github.com/jtheoof/swappy/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:     version.patch
Summary:	A Wayland native snapshot editing tool, inspired by Snappy on macOS
URL:		https://github.com/jtheoof/swappy
License:	MIT
Group:		Window Manager/Utility


BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: desktop-file-utils

Requires:      fonts-otf-awesome
Requires:      wl-clipboard

%description
%summary

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps res/icons/hicolor/scalable/apps/%{name}.svg

desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/swappy.svg
%{_datadir}/locale/*/LC_MESSAGES/swappy.mo
%{_mandir}/man1/%{name}.1.zst
