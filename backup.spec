Summary:	A backup strategy for Linux via CD-R
Summary(pl.UTF-8):   Strategia kopii zapasowych na CD-R dla Linuksa
Name:		backup
Version:	4.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.bluehaze.com.au/unix/%{name}_%{version}.tar.gz
# Source0-md5:	6e7faf41f40d1e5c205ce5082b89e0a9
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

%description -l pl.UTF-8
Dla serwera linuksowego nie mającego napędu taśmowego o odpowiednio
dużym rozmiarze, ale z dostępem do nagrywarki CD lub DVD (własnej lub
podłączonej do innej maszyny w sieci) i sporą liczbą wolnego miejsca
na dysku na duże pliki tymczasowe, użyteczną i wygodną alternatywą
jest używanie wielu płyt CD.

backup to skrypt używający standardowych narzędzi uniksowych takich
jak find, sed, cpio oraz małego narzędzia do dzielenia plików o nazwie
fsplit do tworzenia serii fragmentów archiwum cpio o łącznym rozmiarze
około 3500MB, zawierającego wszystkie interesujące pliki z systemu.
Rozmiar fragmentu jest aktualnie ustawiony na około 640MB (co można
zmienić w skrypcie), aby zmieścił się na płycie CD. Kawałki są
automatycznie nazywane przez backup poprzez dołączanie 000, 001 itd.
do podstawy nazwy pliku pochodzącej od daty. Skrypt pozwala także na
częściowe lub pełne odtworzenie danych ze zbioru płyt CD oraz
listowanie zawartości archiwum w krótkim lub długim formacie.

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
