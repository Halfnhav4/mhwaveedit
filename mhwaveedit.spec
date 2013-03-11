Summary:	Graphical program for editing, playing and recording sound files
Name:		mhwaveedit
Version:	1.4.22
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://download.gna.org/mhwaveedit/%{name}-%{version}.tar.bz2
# Source0-md5:	920108844abfdc2613cc1d3e188a7833
BuildRequires:	SDL-devel
BuildRequires:	gtk+-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkg-config
BuildRequires:	pulseaudio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mhWaveEdit is a graphical program for editing, playing and recording
sound files. It is lightweight, portable, user-friendly and handles
large files very well.

The program itself has only simple editing features such as
cut'n'paste and volume adjustment but it can also use LADSPA effect
plugins and the effects provided by the SoX application.
It can also support additional file formats besides wav through
libsndfile and mp3/ogg import and export through lame and
oggenc/oggdec.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/mhwaveedit.desktop
%{_pixmapsdir}/mhwaveedit.xpm
%{_mandir}/man1/mhwaveedit.1*

