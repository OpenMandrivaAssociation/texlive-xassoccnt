%global tl_name xassoccnt
%global tl_revision 61112

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Associated counters stepping simultaneously
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xassoccnt
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xassoccnt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xassoccnt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a way of associating counters to an existing
driver counter so that incrementing the driver counter will increase its
associated counters as well. This package can be regarded as a
supplement to the totcount package by Vasileios Koutavas, but it can be
used without it, too. xassoccnt is a successor and a complete rewrite of
the assoccnt package by the same author. However, as of 2017-03-05, some
features of assoccnt are not (yet) contained in xassoccnt so that the
older package cannot yet be regarded as obsolete.

