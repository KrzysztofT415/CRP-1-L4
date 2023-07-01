## Specyfikacja

```bash
gpg --version # gpg (GnuPG) 2.2.19, libgcrypt 1.8.5
uname -srm # Linux 5.10.60.1-microsoft-standard-WSL2 x86_64
lsb_release -ds # Ubuntu 20.04.4 LTS
```

## Odpowiedź na pytanie

> Zgodnie z dokumentacją `man gpg`:

`gpg is the OpenPGP part of the GNU Privacy Guard (GnuPG). It is a tool to provide digital encryption and signing services using the OpenPGP standard.`

> Używany jest standard OpenPGP.\
> Jest on zgodnie z zamieszczoną dokumentacją na [oficjalnej stronie openpgp.org](https://datatracker.ietf.org/doc/html/rfc4880#section-13.9) :

`OpenPGP does symmetric encryption using a variant of Cipher Feedback mode (CFB mode).`

> Czyli jest to tryb CFB - [Cipher Feedback Mode](https://de.wikipedia.org/wiki/Cipher_Feedback_Mode).

## Pliki

`script.sh` - komenda bashowa enkrypcji

`result.gpg` - plik wygenerowany

`ke5.pdf` - szyfrowana lista
