%global tl_name tufte-latex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.5.2
Release:	%{tl_revision}.1
Summary:	Document classes inspired by the work of Edward Tufte
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tufte-latex
License:	apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tufte-latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tufte-latex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(changepage)
Requires:	texlive(ifmtarg)
Requires:	texlive(paralist)
Requires:	texlive(placeins)
Requires:	texlive(sauerj)
Requires:	texlive(xifthen)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provided are two classes inspired, respectively, by handouts and books
created by Edward Tufte.

