## `reduce-video.py`

Skrypt zmieniający nagrania .mp4, na [.mkv](https://en.wikipedia.org/wiki/Matroska) z kodekiem [H.265](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding). Testowany wylącznie na Linuxie.

__Wymagania:__
* ffmpeg z libx265 i libvorbis
* Python3

## `uam-note`

Skrypt wypisuje na standardowe wyjście nagłówek notatki w Markdown. Przyjęte konwencje:

* nazwa użytkownika oraz adres email zawarte są w konfiguracji git'a
* Working directory skryptu zapisany w `snake_case` jest podstawą nazwy przedmiotu
