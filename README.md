## `reduce-video.py`

Skrypt zmieniający nagrania .mp4, na [.mkv](https://en.wikipedia.org/wiki/Matroska) z kodekiem [H.265](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding). Testowany wylącznie na Linuxie.

__Wymagania:__
* ffmpeg z libx265 i libvorbis
* Python3

## `uam-note`

Skrypt generuje notatki w Markdown.

```
uam-note
uam-note nazwa_pliku [open]
```

Przyjęte konwencje:

* nazwa użytkownika oraz adres email zawarte są w konfiguracji git'a
* Working directory skryptu zapisany w `snake_case` jest podstawą nazwy przedmiotu
* Preferowany edytor ustawiony w zmiennej `$EDITOR`

### Użycie

__Wypisanie nagłówka na stdout:__
```sh
uam-note
```

__Wypisanie nagłówka do pliku 'wykład 1':__
```sh
uam-note "wykład 1"
```

__Wypisanie nagłówka do pliku 'wykład 1' i natychmiastowa edycja__
```sh
uam-note "wykład 1" open
```
