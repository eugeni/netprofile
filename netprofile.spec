Name: netprofile
Summary: Manage network profiles
Version: 0.10
Release: %mkrel 1
Source: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Base
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: initscripts >= 7.06-13mdk
Requires: diffutils
URL: http://www.mandrakelinux.com/

%description
Manage network profiles

%prep

%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std INITDIR=%_initrddir

%clean
rm -rf $RPM_BUILD_ROOT

%post

if [ ! -d /etc/netprofile/profiles/default ]; then
  /sbin/save-netprofile default
fi

%files
%defattr(-,root,root) 
%doc ChangeLog
/sbin/*
%dir /etc/netprofile
%dir /etc/netprofile/profiles
%config(noreplace) /etc/netprofile/list
%config(noreplace) /etc/bash_completion.d/netprofile
/etc/sysconfig/network-scripts/ifup.d/netprofile

# DO THE MODIFICATIONS IN CVS. NO PATCH ALLOWED.
%changelog
* Tue Dec  6 2005 Frederic Lepied <flepied@mandriva.com> 0.10-1mdk
- add an ifup.d script to be able to switch the profile automatically
if the NETPROFILE variable is set.

* Thu Apr 07 2005 Warly <warly@mandrakesoft.com> 0.9.2-1mdk
- fix background not correctly displayed in silent mode for fbmenu

* Tue Mar 29 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.9.1-1mdk
- fix return code of set-netprofile

* Tue Mar 29 2005 Olivier Blin <oblin@mandrakesoft.com> 0.9-2mdk
- set-netprofile: make net_applet reload the configuration

* Wed Mar 23 2005 Warly <warly@mandrakesoft.com> 0.9-1mdk
- Check for silent bootsplash and use bootsplash image

* Thu Mar  3 2005 Frederic Lepied <flepied@mandrakesoft.com> 0.8-1mdk
- add-to-netprofile: copy a file anyway to all profiles even if the
  file is already under netprofile control with -f option.
- fix a bug when using profile name from kernel command line

* Fri Feb 04 2005 Warly <warly@mandrakesoft.com> 0.7.5-1mk
- new call to fbgrab to dump the background before calling fbmenu

* Fri Jan 21 2005 Warly <warly@mandrakesoft.com> 0.7.4-1mdk
- add call to fbmenu to choose a profile during boot

* Wed Sep 29 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.7.3-1mdk
- back to using previously set profile is none is requested at boot

* Wed Sep 29 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.7.2-1mdk
- set-netprofile:
 o fix bug when changing the hostname at boot (reported by Charles Davant).
 o assume we want the default one if no profile name is
  specified. This allows to avoid setting PROFILE=default in
  lilo.conf.
 o use set_hostname from network-functions to work cleanly with s2u

* Thu Jun 24 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.7.1-1mdk
- use more meaningful names: add-to-netprofile and remove-from-netprofile

* Thu Jun 24 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.7-1mdk
- added add-netprofile and del-netprofile to add/remove a file under
  netprofile management.

* Wed Mar 17 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.6.3-1mdk
- save time, ntp and yp files (bug #7808)

* Wed Jan  7 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.6.2-1mdk
- added missing files for ppp (Michael Reinsch) [bug #6739]

* Fri Dec 26 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.6.1-1mdk
- save proxy files [bug #6604]

* Fri Sep 12 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.6-1mdk
- clone-netprofile: do the right thing when cloning current profile
- set-netprofile: set hostname if needed (Guillaume Rousse)
- allow spaces in the profile names (Thierry) [not complete]

* Mon Sep  8 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.5.3-1mdk
- completed file list (Thierry)

* Tue Aug 26 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.5.2-1mdk
- corrected startup

* Thu Aug  7 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.5.1-1mdk
- added bash completion support (Guillaume Rousse)

* Mon Jul  7 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.5-1mdk
- save-netprofile: find the configured services in a safer way
- depend on the needed release of initscripts
- set-netprofile: safer test that we are not at boot

* Mon May 26 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.4-1mdk
- don't use a service anymore. Be called from mandrake_everytime.

* Sat Apr  5 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.3-1mdk
- start/stop services when set-netprofile is called interactively

* Tue Mar 25 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.2-1mdk
- save/restore services

* Mon Mar 24 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.1-1mdk
- initial packaging

# netprofile.spec ends here
