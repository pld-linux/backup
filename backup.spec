Summary:	A backup strategy for Linux via CD-R
Summary(pl):	Strategia kopii zapasowych na CD-R dla Linuksa
Name:		backup
Version:	4.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.bluehaze.com.au/unix/%{name}_%{version}.tar.gz
# Source0-md5:	6e7faf41f40d1e5c205ce5082b89e0a9
# Source0-size:	16509
Patch0:		%{name}-build.patch
URL:		http://www.bluehaze.com.au/unix/cdbkup.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For a Linux server which has no high-capacity tape drive fitted but
which does have access to a CD or DVD burner (either on-board or via
another networked machine), and plenty of spare disc for some large
temporary files, a useful and convenient alternative is to use
multiple CDs instead.

backup is a script which makes use of standard unix utilities such as
find, sed, and cpio, plus a small file-splitter called fsplit to
create a series of cpio archive fragments totalling about 3500MB that
contain all the files of interest on my system. The fragment size is
currently set to around 640MB (adjustable via the script) so they can
fit onto normal CDs. The chunks are automatically named by backup by
appending 000, 001 etc onto a date-derived file name base. The script
also provides for full or partial recovery from the CD set, plus the
listing of archive contents in long or short format.

%description -l pl
Dla serwera linuksowego nie maj±cego napêdu ta¶mowego o odpowiednio
du¿ym rozmiarze, ale z dostêpem do nagrywarki CD lub DVD (w³asnej lub
pod³±czonej do innej maszyny w sieci) i spor± liczb± wolnego miejsca
na dysku na du¿e pliki tymczasowe, u¿yteczn± i wygodn± alternatyw±
jest u¿ywanie wielu p³yt CD.

backup to skrypt u¿ywaj±cy standardowych narzêdzi uniksowych takich
jak find, sed, cpio oraz ma³ego narzêdzia do dzielenia plików o nazwie
fsplit do tworzenia serii fragmentów archiwum cpio o ³±cznym rozmiarze
oko³o 3500MB, zawieraj±cego wszystkie interesuj±ce pliki z systemu.
Rozmiar fragmentu jest aktualnie ustawiony na oko³o 640MB (co mo¿na
zmieniæ w skrypcie), aby zmie¶ci³ siê na p³ycie CD. Kawa³ki s±
automatycznie nazywane przez backup poprzez do³±czanie 000, 001 itd.
do podstawy nazwy pliku pochodz±cej od daty. Skrypt pozwala tak¿e na
czê¶ciowe lub pe³ne odtworzenie danych ze zbioru p³yt CD oraz
listowanie zawarto¶ci archiwum w krótkim lub d³ugim formacie.

%prep
%setup -q -c
%patch0 -p0

%build
%{__cc} %{rpmcflags} %{rpmldflags} fsplit.c -o fsplit

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/%{name},%{_sbindir}}

install %{name} fsplit $RPM_BUILD_ROOT%{_sbindir}
install bex $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%attr(750,root,root) %dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/bex
