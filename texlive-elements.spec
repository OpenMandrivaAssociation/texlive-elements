%global tl_name elements
%global tl_revision 61792

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Provides properties of chemical elements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elements
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elements.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elements.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides means for retrieving properties of chemical
elements like atomic number, element symbol, element name, electron
distribution or isotope number. Properties are defined for the elements
up to the atomic number 112. This package is a spin-off of the package
bohr by the same author.

