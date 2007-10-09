#
# spec file for package gfxboot (Version 3.3.37)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
# usedforbuild    Mesa aaa_base acl attr audit-libs autoconf automake bash binutils bzip2 cairo coreutils cpio cpp cpp42 cracklib cups-libs cvs diffutils docbook-xsl-stylesheets docbook_4 file filesystem fillup findutils fontconfig freetype2 freetype2-devel gawk gcc gcc42 gd gdbm gettext gettext-devel ghostscript-fonts-std ghostscript-library ghostscript-x11 glib2 glibc glibc-devel glibc-locale glitz gpm grep groff gzip info insserv less libacl libattr libbz2-1 libbz2-devel libdb-4_5 libdrm libexpat1 libgcc42 libgcrypt libgimpprint libgomp42 libgpg-error libjpeg libltdl-3 libmudflap42 libopenssl0_9_8 libpng libreadline5 libstdc++42 libtiff3 libtool libuuid1 libvolume_id libxcrypt libxml2 libxslt libzio linux-kernel-headers m4 make man mktemp nasm ncurses net-tools netcfg openssl-certs pam pam-modules passivetex patch perl perl-Tk perl-base permissions poppler popt rpm sed sgml-skel sysvinit t1lib tar texinfo texlive texlive-bin texlive-bin-latex texlive-latex timezone util-linux w3m xaw3d xmltex xmlto xorg-x11-libICE xorg-x11-libSM xorg-x11-libX11 xorg-x11-libXau xorg-x11-libXext xorg-x11-libXfixes xorg-x11-libXmu xorg-x11-libXp xorg-x11-libXpm xorg-x11-libXprintUtil xorg-x11-libXrender xorg-x11-libXt xorg-x11-libXv xorg-x11-libfontenc xorg-x11-libs xorg-x11-libxcb xorg-x11-libxkbfile zlib zlib-devel

Name:           gfxboot
BuildRequires:  freetype2-devel nasm sgml-skel w3m xmlto
License:        GPL v2 or later
Group:          System/Boot
Obsoletes:      gfxboot-devel
Requires:       perl-HTML-Parser
AutoReqProv:    on
Summary:        Graphical Boot Logo for LILO and SYSLINUX
Version:        3.3.37
Release:        5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         gfxboot-3.3.37.tar.bz2
Source1:        NLD.tar.bz2
Source2:        SLES.tar.bz2
Source3:        SuSE.tar.bz2
Source4:        Zen.tar.bz2

%description
Here, find the graphical boot logo. It is suitable for both LILO and
SYSLINUX.



%debug_package
%prep
%setup
%setup -T -D -a 1
%setup -T -D -a 2
%setup -T -D -a 3
%setup -T -D -a 4

%build
make X11LIBS=/usr/X11R6/%_lib
make doc

%install
make DESTDIR=%{buildroot} install
cp -a bin %{buildroot}/usr/share/gfxboot

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/sbin/mkbootmsg
/usr/sbin/mkblfont
/usr/sbin/help2txt
%doc doc/gfxboot.html
%doc doc/gfxboot.txt
/usr/share/gfxboot
%changelog
* Fri Sep 14 2007 - snwint@suse.de
- fixed building non-openSUSE themes
* Wed Sep 12 2007 - snwint@suse.de
- always ask for VBE2 info (to e.g. get 1366x768 listed - #298025)
- new welcome screen animation
* Mon Sep 10 2007 - snwint@suse.de
- updated translations
* Wed Aug 22 2007 - snwint@suse.de
- fix livecd mode
* Mon Aug 20 2007 - snwint@suse.de
- new translations
* Mon Aug 13 2007 - snwint@suse.de
- use autohinting for lohit_pa, gulim, FZHeiTi (#299568)
* Fri Aug 10 2007 - snwint@suse.de
- allow to set default values for repository
* Thu Aug 09 2007 - snwint@suse.de
- change default lang en -> en_US
- updated po files
* Thu Jul 26 2007 - snwint@suse.de
- adjusted menu texts
* Tue Jul 24 2007 - snwint@suse.de
- no graphics on problematic via boards (#231104)
* Mon Jul 23 2007 - snwint@suse.de
- rewrote line edit function
- intro aborted if any key pressed (#219570)
- added Walloon
- added Sinhala
- moved 'install - XXX' variants into submenu, added 'repair' entry (#293827)
- go green
* Thu Mar 15 2007 - snwint@suse.de
- basic rtl language support
* Mon Mar 12 2007 - snwint@suse.de
- added new languages
- two-line panel
* Fri Feb 09 2007 - snwint@suse.de
- different 'Hindi' spelling
* Wed Feb 07 2007 - snwint@suse.de
- added Gujarati & Marathi translations
* Wed Feb 07 2007 - snwint@suse.de
- added some code to debug monitor detection
- language cleanup
- added new languages
* Mon Jan 22 2007 - snwint@suse.de
- fix language/keymap setting (#223518)
* Fri Nov 24 2006 - snwint@suse.de
- fixed penguin theme bug (#216991)
- lang menu sometimes shows only locale name
* Mon Nov 20 2006 - snwint@suse.de
- translations updated
- minor penguin setup correction
* Fri Nov 17 2006 - snwint@suse.de
- adjust 640x480 menu sizes (#221139)
- tuning layout
- make penguins more likely during winter
* Wed Nov 15 2006 - snwint@suse.de
- updated documentation
- get initrd size right for progress bar
* Tue Nov 14 2006 - snwint@suse.de
- fixed Requires
* Tue Nov 14 2006 - snwint@suse.de
- fix doc file permission
* Mon Nov 13 2006 - snwint@suse.de
- help text parser rewritten
- new translations
- added final 10.2 theme
* Tue Nov 07 2006 - snwint@suse.de
- new translations
* Fri Oct 27 2006 - snwint@suse.de
- penguin theme is back
- adjust html help text parser
* Thu Oct 26 2006 - snwint@suse.de
- new translations
* Mon Oct 23 2006 - snwint@suse.de
- translations updated
- added 'noinstallopt' option to gfxboot.cfg
* Mon Sep 25 2006 - snwint@suse.de
- Arabic is back
* Mon Sep 25 2006 - snwint@suse.de
- added 'firmware' menu entry
* Wed Sep 20 2006 - snwint@suse.de
- support Punjabi (Gurmukhi script)
* Wed Sep 20 2006 - snwint@suse.de
- fixed font rendering bug
- added some indic fonts
* Tue Sep 19 2006 - snwint@suse.de
- use 4 bit for antialiasing (not 3)
* Tue Sep 19 2006 - snwint@suse.de
- fix Estonian support
* Tue Sep 19 2006 - ro@suse.de
- correct filelist
* Mon Sep 18 2006 - snwint@suse.de
- support antialiased fonts
- added Estonian
- put hard disk install option back in
* Thu Aug 24 2006 - snwint@suse.de
- 32 bit rewrite finished
- changed interface to bootloader
* Mon Aug 21 2006 - snwint@suse.de
- move to 32 bit, cont.
* Mon Aug 07 2006 - snwint@suse.de
- move to 32 bit, cont.
- added 10.2 openSUSE logos
* Tue Aug 01 2006 - snwint@suse.de
- started internal rewrite to run all code in 32 bit pm
* Mon Jul 24 2006 - snwint@suse.de
- fixed Zen theme
* Wed Jul 19 2006 - snwint@suse.de
- added Catalan & Vietnamese
- better debug window
- fixed minor file reading bug
- better internal locale handling
- separated en locale into en_GB & en_US
* Mon Jul 17 2006 - snwint@suse.de
- more than one boot option line, finished (#160066)
- added 'about' button
- make it openSUSE
- added xen test config
* Mon Jul 10 2006 - snwint@suse.de
- use disk image, not floppy for grub testing
- updated Zen pictures
- made full panel default
- ShiftTab now works
- remove duplicate video modes (#145749)
- menu bar fits menu text width
- made 'Text Mode' translatable (#179582)
- workaround for interlaced mode issue on some ATI cards (#177982)
- use disk image, not floppy for lilo testing
- major code cleanup
- removed ancient compatibility code
- allow more than one boot option line (for xen)
- using beta pictures
* Fri Jun 09 2006 - snwint@suse.de
- translations updated
- minor Zen theme change
* Tue May 23 2006 - snwint@suse.de
- translations updated
- added Zen texts & theme
* Mon May 22 2006 - snwint@suse.de
- add check to handle insufficient real mode handling in Xen on VMX
  machines (#175473)
- allow per menu entry memory checks via mem.min[<label>] and
  mem.msg[<label>] in gfxboot.cfg
* Mon May 15 2006 - snwint@suse.de
- fix random memory corruption when trying to open a nonexistent
  file (#165846)
* Tue May 02 2006 - snwint@suse.de
- translations updated (#170561)
* Thu Apr 27 2006 - snwint@suse.de
- implemented inbyte/outbyte to access i/o space (#170167)
* Wed Apr 19 2006 - snwint@suse.de
- fix drawing bug (#166914)
* Fri Apr 07 2006 - snwint@suse.de
- translations updated
- fine-tuned splash
* Tue Apr 04 2006 - snwint@suse.de
- fixed Khmer menu entry
* Mon Apr 03 2006 - snwint@suse.de
- fixed evil memory corruption bug
* Fri Mar 31 2006 - snwint@suse.de
- added 'share' input field for smb install
- some more texts are translatable
- Live-CD preparations
* Thu Mar 30 2006 - snwint@suse.de
- adjusted 640x480 fallback layout
- added driver update dialog that lets you enter the update file name
* Wed Mar 29 2006 - snwint@suse.de
- better 'welcome' screen
* Tue Mar 28 2006 - snwint@suse.de
- added new 'welcome' screen
* Mon Mar 27 2006 - snwint@suse.de
- translations updated
* Mon Mar 13 2006 - snwint@suse.de
- added NLD & SLES themes
* Mon Mar 06 2006 - snwint@suse.de
- new theme, cont.
- it's now nolapic (#155280)
- translations updated
* Tue Feb 28 2006 - snwint@suse.de
- drop dosemu as testing platform
- new theme, first try
* Tue Feb 21 2006 - snwint@suse.de
- add noapic boot option (#150030)
* Tue Feb 14 2006 - snwint@suse.de
- add apic boot option (#150030)
* Thu Feb 09 2006 - snwint@suse.de
- more defensive monitor detection (#149578)
- monitor detection can be skipped
* Thu Jan 26 2006 - snwint@suse.de
- go for 8 bit framebuffer if there are no 16 bit modes (#144742)
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 23 2006 - snwint@suse.de
- better monitor detection
- cjwatson@ubuntu.com: support big-endian cpio archives (#140119)
- support direct driverupdate loading from CD-ROM (feat #152)
- add new languages
* Mon Jan 16 2006 - snwint@suse.de
- show all options in grub/lilo (#136377)
- translations & font updated
* Wed Dec 14 2005 - snwint@suse.de
- fixed to work correctly with grub & lilo
* Mon Dec 05 2005 - snwint@suse.de
- Colin Watson <cjwatson@ubuntu.com>: build fixes for x86-64
- fixed kernel splash loading
- include 'unpack_bootlogo' script in package
* Wed Nov 30 2005 - snwint@suse.de
- adjust to syslinux 3.11
- remove some primary words and reimplement them as bytecode
- read config options from 'gfxboot.cfg'
* Wed Oct 19 2005 - snwint@suse.de
- offer Croatian
* Wed Oct 12 2005 - snwint@suse.de
- do only aligned dword reads from video memory - some ATI boards
  need this (#114804)
* Fri Oct 07 2005 - snwint@suse.de
- needs syslinux with updated gfx patch
- texts updated for 10.1
- implemented filesize, getcwd, chdir commands
- using new cd layout
* Thu Sep 29 2005 - dmueller@suse.de
- add norootforbuild
* Tue Sep 20 2005 - snwint@suse.de
- better testing script
- gcc 4.1 compile fixes
* Fri Sep 09 2005 - snwint@suse.de
- oops, was already December
* Mon Sep 05 2005 - snwint@suse.de
- Finnish texts updated
* Fri Sep 02 2005 - snwint@suse.de
- fix color handling bug (#72232)
- show penguins a bit more often
* Mon Aug 29 2005 - snwint@suse.de
- added more keymaps (#113265)
- long menus are wrapped
- added 640x480 fallback for i845-like boards
- new translations
* Wed Aug 24 2005 - snwint@suse.de
- a different shade of blue
- fixed penguin theme drawing bug
* Mon Aug 22 2005 - snwint@suse.de
- new translations
* Mon Aug 22 2005 - snwint@suse.de
- prepare for jpeg decompression to 8-bit color space
- add penguin theme
- Dansk keymap added
* Mon Aug 15 2005 - snwint@suse.de
- fixed Dansk locale (#104084)
- new translations added
* Fri Aug 05 2005 - snwint@suse.de
- texts updated
- support images with alpha channel
- new theme
* Thu Jun 23 2005 - snwint@suse.de
- 32 bit modes now fully supported
* Wed Jun 22 2005 - snwint@suse.de
- updated documentation
* Wed Apr 27 2005 - snwint@suse.de
- harddisk install option gone (#60128)
* Fri Apr 22 2005 - snwint@suse.de
- added live cd entry
- fixed 16 bit color mode selection (#79312)
* Wed Apr 20 2005 - snwint@suse.de
- taiwan text fix (#78946)
* Mon Apr 11 2005 - snwint@suse.de
- fixed file reading
* Mon Mar 21 2005 - snwint@suse.de
- added slowenic translations
* Wed Mar 16 2005 - snwint@suse.de
- new graphics
* Wed Mar 16 2005 - snwint@suse.de
- speedup transparent menu drawing
- adjust some colors
* Tue Mar 15 2005 - snwint@suse.de
- updated translations
* Tue Mar 08 2005 - snwint@suse.de
- fixed install source dialogs
- fixed some memory leaks
* Mon Mar 07 2005 - snwint@suse.de
- translation fix (#66743)
- new splash graphics
- fixed slow timeout (#66730)
- enabled transparent menus
* Tue Mar 01 2005 - snwint@suse.de
- new graphics
- more translation texts fixes
- prepared for transparent menus
* Tue Feb 22 2005 - snwint@suse.de
- fixed translation texts
- ask for smb domain
- corrected minor drawing error
* Mon Feb 21 2005 - snwint@suse.de
- 9.3 theme
- fixed color handling bug
* Tue Feb 15 2005 - snwint@suse.de
- sync language list with yast2
- fixed making slp default
* Mon Feb 14 2005 - snwint@suse.de
- allow selecting slp or cdrom as default install target
* Tue Feb 08 2005 - snwint@suse.de
- support ukrainian
* Fri Feb 04 2005 - snwint@suse.de
- use 8x16 console font (8x14 does not always exist)
- avoid overlap with bootloader memory usage
- fixed memory addressing problem
* Tue Feb 01 2005 - snwint@suse.de
- workaround to avoid memory corruption
- added experimental mouse code (for testing)
* Mon Jan 31 2005 - snwint@suse.de
- rewrote internal memory management
- jpeg decoding works
- support symlinks in cpio archive
- lots of minor fixes
- renamed files to stick to 8.3 scheme
- much improved test script
- use bold font
- use 800x600, 16bit color
- added new help texts
- can read files from file system (with syslinux)
* Wed Oct 06 2004 - snwint@suse.de
- removed temp file
* Tue Oct 05 2004 - snwint@suse.de
- added help text for '64bit' switch (#46806)
* Fri Oct 01 2004 - snwint@suse.de
- new blue theme
* Fri Oct 01 2004 - snwint@suse.de
- polish translations
- hide passwords (#46094)
* Mon Sep 27 2004 - snwint@suse.de
- more languages
* Mon Sep 20 2004 - snwint@suse.de
- minor i18n fixes
* Mon Sep 13 2004 - snwint@suse.de
- final graphics
- added new translations
* Tue Sep 07 2004 - ro@suse.de
- added missing el symlink n Home theme
* Mon Sep 06 2004 - snwint@suse.de
- do the F-key-move-down magic only for syslinux (#44238)
- some text cleanup (9.1 -> 9.2, dropped unused liveeval msgs)
- added new translations
- preliminary SuSE theme graphics
* Wed Aug 18 2004 - snwint@suse.de
- better arabic language support
* Mon Aug 16 2004 - snwint@suse.de
- added arabic
* Mon Aug 09 2004 - snwint@suse.de
- add 32/64 dualboot code
- removed obsolete themes
- switch to 'installation' if some F-key has been used (#41097)
- don't offer 640x480; instead, select x11 vesa driver
- assume monitor can display at least 800x600
* Wed May 12 2004 - snwint@suse.de
- hide password in lilo (#40348)
* Fri Apr 16 2004 - snwint@suse.de
- irqs might have been turned off in some cases
- new SLES pictures
* Wed Apr 14 2004 - snwint@suse.de
- font creation missed some chars (#38223)
* Thu Apr 08 2004 - snwint@suse.de
- add SuSE-Live theme
- use 'install=slp://' (#36982)
- add new 'biosmem' function
- live cd layout changes
- added live cd warning if there's not enough memory
- added SLES theme (copy of SuSE theme)
* Tue Apr 06 2004 - snwint@suse.de
- handle case where we can't set graphics mode (#35806)
* Mon Apr 05 2004 - snwint@suse.de
- add HTTP install option
* Mon Apr 05 2004 - snwint@suse.de
- add only english to boot/message (#38339)
* Mon Apr 05 2004 - snwint@suse.de
- japanese translations, again
- new boot graphics, again
* Sat Apr 03 2004 - snwint@suse.de
- new japanese translations (#38224)
- not all japanese chars were added to font (#38223)
* Fri Apr 02 2004 - snwint@suse.de
- new boot graphics
* Fri Apr 02 2004 - snwint@suse.de
- reset timeout if we show some popup during start
* Fri Apr 02 2004 - snwint@suse.de
- added amd64 test
- fixed lilo password dialog
- use less memory for input dialogs
- modplayer should work again
- added russian texts
* Wed Mar 31 2004 - snwint@suse.de
- take out romanian install help text; not enough space
* Wed Mar 31 2004 - snwint@suse.de
- swedish texts
- added japanese texts
- fixed html viewer to work with japanese (allow line
  breaks at any place)
- added hungarian, italian and french texts
* Mon Mar 29 2004 - snwint@suse.de
- dutch help texts
- slovene & romanian texts
* Mon Mar 29 2004 - snwint@suse.de
- menu texts localized via 'translations.<locale>'
- new boot graphics
- added Home theme
- fixed language setting (#37195)
- pass lang info to yast (#35841)
* Mon Mar 22 2004 - snwint@suse.de
- new boot graphics
- fixed japanese locale name (#36487)
- added spanish texts
- added dutch & hungarian texts
- localized driver update text
* Wed Mar 17 2004 - snwint@suse.de
- new/updated czech texts
- reworked themes Makefile
* Tue Mar 16 2004 - snwint@suse.de
- german help texts
* Mon Mar 15 2004 - snwint@suse.de
- lang menu constructed from 'languages' file
* Tue Mar 09 2004 - snwint@suse.de
- added 'SLP' menu entry
* Mon Mar 08 2004 - snwint@suse.de
- fixed Makefile
* Mon Mar 08 2004 - snwint@suse.de
- czech translations
- added dialogs for various install types
- added 'profiles' menu for laptop people (#32346)
* Mon Mar 01 2004 - snwint@suse.de
- use translated language names
* Mon Mar 01 2004 - snwint@suse.de
- fixed theme Makefile
* Mon Mar 01 2004 - snwint@suse.de
- put texts into *.po files
- redraw screen after selecting new language
- some more keymaps
* Mon Feb 16 2004 - snwint@suse.de
- obsoletes gfxboot-devel
* Mon Jan 26 2004 - snwint@suse.de
- utf8 support, hi & true color video modes
- german keyboard mapping really works
- reworked much of the internals
- bootlogo file is now normal cpio archive; makes it easier to modify
* Tue Dec 16 2003 - snwint@suse.de
- moved SLSS theme to 9.0
- support disk change popups
* Wed Nov 12 2003 - varkoly@suse.de
- added SLSS theme for the AutoinstallationsCD  of the
  SuSE Linux School Server Clients
* Mon Oct 13 2003 - snwint@suse.de
- added LiveEval theme
* Wed Sep 17 2003 - snwint@suse.de
- make F3 actually do something
* Mon Sep 15 2003 - snwint@suse.de
- add splash parameter only if it's already there (#28780)
* Sat Sep 06 2003 - snwint@suse.de
- added splash mode selection to install screen
* Mon Sep 01 2003 - snwint@suse.de
- SuSE theme updated
* Mon Sep 01 2003 - snwint@suse.de
- new SuSE theme
- removed eject button; doesn't work on too much systems
- give additional hint if user forgot to turn the dvd over
* Mon Aug 25 2003 - snwint@suse.de
- reworked ps code
- added eject dialog for DVD2
- support some european keyboard layouts (experimental: press F9)
* Mon Aug 18 2003 - snwint@suse.de
- minor bug in SuSE theme
* Mon Aug 18 2003 - snwint@suse.de
- new version; cleaned up package
* Mon Mar 17 2003 - snwint@suse.de
- limit max resolution we offer to 1280x1024
* Fri Mar 14 2003 - snwint@suse.de
- minor help text corrections (#25139)
* Wed Mar 12 2003 - snwint@suse.de
- really final splash pictures
* Mon Mar 10 2003 - snwint@suse.de
- final splash picture
* Sat Mar 08 2003 - snwint@suse.de
- don't wait 3 seconds in lilo/grub mode
- get default splash mode from grub config
- added splash mode 'native' (splash=0)
* Thu Mar 06 2003 - snwint@suse.de
- updated menu texts
- show splash 3 seconds
* Mon Mar 03 2003 - snwint@suse.de
- slightly improved SuSE-splash.pcx
- support more kernel splash sizes
* Sat Mar 01 2003 - snwint@suse.de
- show splash before boot menu
- build different versions for installer and grub/lilo
* Mon Feb 24 2003 - snwint@suse.de
- removed the logo fading stuff, it makes problems on Radeon cards
* Tue Feb 18 2003 - snwint@suse.de
- added real help text written by bg@suse.de
* Mon Feb 17 2003 - snwint@suse.de
- allow more than one dialog at a time to be shown
* Fri Feb 14 2003 - snwint@suse.de
- added functions for image fading
- new dialog and progress bar widgets
- added combo box for splash silent/verbose (for lilo/grub)
* Sun Feb 09 2003 - snwint@suse.de
- new, extended version
* Mon Jan 20 2003 - stepan@suse.de
- add OpenSchool theme
* Wed Nov 13 2002 - ro@suse.de
- use x-devel-packages in neededforbuild
- use /usr/X11R6 not /usr/X11
* Fri Oct 25 2002 - stepan@suse.de
- update OpenXchange theme to contain UL brand
* Thu Oct 17 2002 - stepan@suse.de
- added OpenXchange theme
* Thu Sep 26 2002 - snwint@suse.de
- added SuSE-SLES theme
* Fri Sep 13 2002 - snwint@suse.de
- fixed UnitedLinux theme
* Wed Sep 11 2002 - snwint@suse.de
- adjusted scrollbar color
- added birthday cake
* Sun Sep 08 2002 - snwint@suse.de
- handle 'failsafe' properly (#18566)
- used to crash if boot image was not found
* Sat Sep 07 2002 - snwint@suse.de
- improved sound code
- added mod file with birthday theme
* Mon Sep 02 2002 - snwint@suse.de
- different shade of blue
* Wed Aug 28 2002 - snwint@suse.de
- new SuSE theme, again
* Tue Aug 27 2002 - snwint@suse.de
- apic is back
* Tue Aug 27 2002 - snwint@suse.de
- new SuSE theme
* Wed Aug 21 2002 - snwint@suse.de
- added UL theme
* Mon Aug 19 2002 - snwint@suse.de
- added sound support
* Mon Jul 22 2002 - snwint@suse.de
- accidentally left in debug code
* Wed Jul 17 2002 - snwint@suse.de
- slightly changed interface to bootloader for grub
* Wed May 29 2002 - snwint@suse.de
- fixed for lib64
* Thu Mar 21 2002 - snwint@suse.de
- new boot image again
* Sun Mar 17 2002 - snwint@suse.de
- new boot image
* Sat Mar 09 2002 - snwint@suse.de
- make seven boot options fit into the boot menu
* Mon Mar 04 2002 - snwint@suse.de
- added 'boot installed os' option
* Mon Feb 25 2002 - snwint@suse.de
- added apic menu entry
* Mon Feb 25 2002 - snwint@suse.de
- new 'failsafe' options
- increased cmdline input buffer to 256 chars
* Mon Sep 17 2001 - snwint@suse.de
- new lilo/installation picture
- added password dialog (#10544)
* Sun Sep 09 2001 - snwint@suse.de
- added 'rmoveto' & 'bootloader' functions
- final 7.3 lilo/installation picture
* Fri Aug 10 2001 - snwint@suse.de
- use preliminary 7.3 picture
* Mon May 14 2001 - snwint@suse.de
- pictures were still not correct
- added README (#7754)
* Fri May 11 2001 - snwint@suse.de
- new install picture (last one was one line too short)
* Wed May 09 2001 - snwint@suse.de
- new lilo/installation pictures
- copy suselilo to /boot/message (_not_ suseinstall :-/)
* Tue May 08 2001 - snwint@suse.de
- moved /usr/share/gfxboot/suselilo to /boot/messsage
* Sun May 06 2001 - snwint@suse.de
- in syslinux: wait for driver update disk if requested
- put space after image label in boot prompt (#7615)
* Mon Apr 30 2001 - snwint@suse.de
- make it work with isolinux
* Sat Apr 28 2001 - snwint@suse.de
- nearly final versions of lilo and syslinux graphics
* Sun Apr 08 2001 - snwint@suse.de
- new installation and lilo logos
* Thu Apr 05 2001 - snwint@suse.de
- created package
