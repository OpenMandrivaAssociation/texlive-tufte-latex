Name:		texlive-tufte-latex
Version:	37649
Release:	2
Summary:	Document classes inspired by the work of Edward Tufte
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tufte-latex
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tufte-latex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tufte-latex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-xifthen
Requires:	texlive-ifmtarg
Requires:	texlive-changepage
Requires:	texlive-paralist
Requires:	texlive-sauerj
Requires:	texlive-placeins

%description
Provided are two classes inspired, respectively, by handouts
and books created by Edward Tufte.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tufte-latex
%doc %{_texmfdistdir}/doc/latex/tufte-latex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
