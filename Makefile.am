# $Id: Makefile.am 13516 2011-11-03 15:57:30Z sloot $
# $URL: https://ilk.uvt.nl/svn/sources/Frog/trunk/Makefile.am $

SUBDIRS = config

EXTRA_DIST = bootstrap.sh AUTHORS TODO NEWS

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = frogdata.pc

ChangeLog: $(top_srcdir)/NEWS
	svn update; svn2cl --include-rev
