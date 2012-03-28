# $Id: Makefile.am 13516 2011-11-03 15:57:30Z sloot $
# $URL: https://ilk.uvt.nl/svn/sources/Frog/trunk/Makefile.am $

ACLOCAL_AMFLAGS = -I m4 --install

SUBDIRS = config

EXTRA_DIST = bootstrap AUTHORS TODO NEWS

ChangeLog: $(top_srcdir)/NEWS
	svn update; svn2cl --include-rev
