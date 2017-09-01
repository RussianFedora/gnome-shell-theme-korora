%global theme_name    Korora
%global rev 20150716git939ecf

Summary:	GNOME shell theme for Korora
Name:		gnome-shell-theme-korora
Version:	0.5
Release:	2.%{rev}%{?dist}

Group:		User Interface/Desktops
License:	GPLv2
URL:		https://github.com/kororaproject/kp-gnome-shell-theme-korora
Source0:	%{name}-%{version}-%{rev}.tar.xz
# set 11pt for main font
Patch0:		gnome-shell-theme-korora-0.5-change-font-size.patch
# black background for dock
Patch1:		gnome-shell-theme-korora-0.5-black-background-for-dock.patch

BuildArch:	noarch


%description
The %{theme_name} theme for GNOME Shell.


%prep
%setup -q
%patch0 -p1
%patch1 -p1


%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}/gnome-shell
cp -pr gnome-shell/* %{buildroot}%{_datadir}/themes/%{theme_name}/gnome-shell

cd %{buildroot}%{_datadir}/themes/%{theme_name}/gnome-shell/
ln -s media/*.svg .
cd -

%files
%dir %{_datadir}/themes/%{theme_name}
%{_datadir}/themes/%{theme_name}/gnome-shell/


%changelog
* Fri Sep  1 2017 Arkady L. Shane <ashejn@russianfedora.pro> - 0.5-2.20150716git939ecf.R
- fix warnings in journal

* Tue Jan 19 2016 Arkady L. Shane <ashejn@russianfedora.pro> - 0.5-1.20150716git939ecf.R
- change color for dock
- set 11pt for main font

* Mon Jul 16 2015 Ian Firns <firnsy@kororaproject.org> - 0.5-1
- Don't use symbolic icons for panel app-icons until themes have
  better coverage.

* Mon Jul  6 2015 Ian Firns <firnsy@kororaproject.org> - 0.4-1
- Updated for latest dash-to-dock

* Thu Jan  8 2015 Ian Firns <firnsy@kororaproject.org> - 0.3-1
- Added theming support for workspaces-to-dock

* Wed Dec 31 2014 Ian Firns <firnsy@kororaproject.org> - 0.2-1
- Tweaks to font and calendar

* Wed Dec 17 2014 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Initial spec.
