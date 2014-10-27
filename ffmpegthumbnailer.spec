Summary:	Lightweight video thumbnailer
Name:		ffmpegthumbnailer
Version:	2.0.9
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	915450d09844d86e2d7fa50043d0924b
URL:		http://code.google.com/p/ffmpegthumbnailer/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ffmpegthumbnailer can be used by file managers to create thumbnails
for your video files. It uses ffmpeg to decode frames from the video
files.

%package devel
Summary:	Header files for libffmpegthumbnailer library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libffmpegthumbnailer library.

%prep
%setup -q

# .so is not a right lib to dlopen
sed -i "s|2.0.so|2.0.so.0|" main.cpp

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/ffmpegthumbnailer
%attr(755,root,root) %ghost %{_libdir}/libffmpegthumbnailer.so.?
%attr(755,root,root) %{_libdir}/libffmpegthumbnailer.so.*.*.*
%{_mandir}/man1/ffmpegthumbnailer.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffmpegthumbnailer.so
%{_includedir}/libffmpegthumbnailer
%{_pkgconfigdir}/libffmpegthumbnailer.pc

