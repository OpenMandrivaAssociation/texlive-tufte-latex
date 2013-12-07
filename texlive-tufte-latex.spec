# revision 24733
# category Package
# catalog-ctan /macros/latex/contrib/tufte-latex
# catalog-date 2011-11-10 06:59:33 +0100
# catalog-license apache2
# catalog-version 3.5.0
Name:		texlive-tufte-latex
Version:	3.5.0
Release:	5
Summary:	Document classes inspired by the work of Edward Tufte
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tufte-latex
License:	APACHE2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tufte-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tufte-latex.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-book.cls
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-common.def
%{_texmfdistdir}/tex/latex/tufte-latex/tufte-handout.cls
%doc %{_texmfdistdir}/doc/latex/tufte-latex/History.txt
%doc %{_texmfdistdir}/doc/latex/tufte-latex/README.txt
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/be-contents.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/be-title.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/ei-contents.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/ei-title.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/helix.asy
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/helix.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/hilbertcurves.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/hilbertrecursive.tex
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/nasa_vision_sm.png
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/satir_graph.png
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/sine.asy
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/sine.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/sine2.asy
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/sine2.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/vdqi-contents.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/vdqi-title.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/ve-contents.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/graphics/ve-title.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/sample-book.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/sample-book.tex
%doc %{_texmfdistdir}/doc/latex/tufte-latex/sample-handout.bib
%doc %{_texmfdistdir}/doc/latex/tufte-latex/sample-handout.pdf
%doc %{_texmfdistdir}/doc/latex/tufte-latex/sample-handout.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.5.0-3
+ Revision: 757154
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.5.0-2
+ Revision: 739942
- texlive-tufte-latex

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.5.0-1
+ Revision: 719813
- texlive-tufte-latex
- texlive-tufte-latex
- texlive-tufte-latex

