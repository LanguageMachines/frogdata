SUBDIRS = config

EXTRA_DIST = bootstrap.sh AUTHORS TODO NEWS frogdata.pc.in README.md

pkgconfigdir = $(libdir)/pkgconfig
pkgconfig_DATA = frogdata.pc

ChangeLog: $(top_srcdir)/NEWS
	git pull; git2cl > ChangeLog
