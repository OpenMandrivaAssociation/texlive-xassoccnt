Name:		texlive-xassoccnt
Version:	61112
Release:	2
Summary:	Associated counters stepping simultaneously
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xassoccnt
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xassoccnt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xassoccnt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a way of associating counters to an
existing driver counter so that incrementing the driver counter
will increase its associated counters as well. This package can
be regarded as a supplement to the totcount package by
Vasileios Koutavas, but it can be used without it, too.
xassoccnt is a successor and a complete rewrite of the assoccnt
package by the same author. However, as of 2017-03-05, some
features of assoccnt are not (yet) contained in xassoccnt so
that the older package cannot yet be regarded as obsolete.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xassoccnt
%doc %{_texmfdistdir}/doc/latex/xassoccnt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
