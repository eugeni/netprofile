#############################################################################
# File		: Makefile
# Package	: netprofile
# Author	: Frederic Lepied
# Created on	: Mon Sep 30 13:20:18 1999
# Version	: $Id: Makefile,v 1.7 2005/12/06 21:58:49 flepied Exp $
# Purpose	: rules to manage the files.
#############################################################################

BINDIR=/sbin
ETCDIR=/etc/netprofile
BASHDIR=/etc/bash_completion.d
IFUPDIR=/etc/sysconfig/network-scripts/ifup.d

BINFILES=netprofile read-netprofile set-netprofile
FILES= $(BINFILES) netprofile.spec Makefile ChangeLog NEWS README TODO bash.completion netprofile.ifup modules/

PACKAGE=netprofile
VERSION=0.26.1

all:

clean:
	rm -f *~

install:
	-mkdir -p $(DESTDIR)$(BINDIR) $(DESTDIR)$(ETCDIR)/profiles $(DESTDIR)$(ETCDIR)/modules $(DESTDIR)/$(BASHDIR) $(DESTDIR)$(IFUPDIR)
	for f in $(BINFILES); do install -m755 $$f $(DESTDIR)$(BINDIR); done
	for f in modules/*; do install -m755 $$f $(DESTDIR)$(ETCDIR)/modules; done
	install -m 644 bash.completion $(DESTDIR)/$(BASHDIR)/$(PACKAGE)
	install -m 755 netprofile.ifup $(DESTDIR)$(IFUPDIR)/netprofile

version:
	@echo "$(VERSION)-$(RELEASE)"

localdist: cleandist dir localcopy tar

cleandist:
	rm -rf $(PACKAGE)-$(VERSION) $(PACKAGE)-$(VERSION).tar.bz2

dir:
	mkdir $(PACKAGE)-$(VERSION)

localcopy:
	tar c $(FILES) | tar x -C $(PACKAGE)-$(VERSION)

tar:
	tar cvf $(PACKAGE)-$(VERSION).tar $(PACKAGE)-$(VERSION)
	bzip2 -9vf $(PACKAGE)-$(VERSION).tar
	rm -rf $(PACKAGE)-$(VERSION)

dist: cleandist dir export tar

gitdist: cleandist
	git archive --prefix $(PACKAGE)-$(VERSION)/ HEAD | bzip2 -9 > $(PACKAGE)-$(VERSION).tar.bz2

changelog: ../common/username
	cvs2cl -U ../common/username -I ChangeLog
	rm -f ChangeLog.bak
	cvs commit -m "Generated by cvs2cl the `date '+%d_%b'`" ChangeLog

# Makefile ends here
