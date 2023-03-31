Name:		texlive-elements
Version:	61792
Release:	2
Summary:	Provides properties of chemical elements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elements
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elements.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elements.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides means for retrieving properties of
chemical elements like atomic number, element symbol, element
name, electron distribution or isotope number. Properties are
defined for the elements up to the atomic number 112. This
package is a spin-off of the package bohr by the same author.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/elements
%doc %{_texmfdistdir}/doc/latex/elements

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
