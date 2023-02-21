# Filmarket

**_[PL]_** Opis aplikacji w tym README.md został napisany w dwóch wersjach, polskiej i angielskiej, ponieważ aktualnie aplikacja jest dedykowana polskim kinom, ale w założeniu może być rozwijana w dowolnym kraju.

**_[EN]_** App description in this README.md is written in both Polish and English versions, because for now this app is dedicated for Polish cinemas but in general it can be developed for any country.

## PL

Aplikacja webowa, będąca porównywarką ofert kin najpopularniejszych sieci. Najważniejsze funkcjonalności aplikacji:

- możliwość przeglądania repertuaru z różnych sieci kin jednocześnie,
- wyszukiwarka wykorzystująca różne kryteria wraz z dodatkowymi możliwościami filtrowania wyników,
- możliwość założenia konta, co pozwala na dodanie ulubionych kin oraz gatunków filmów, dzięki czemu można korzystać z nich jako dodatkowych filtrów przy wyszukiwaniu,
- autoryzacja odbywa się z wykorzystaniem tokena JWT.

## EN

Web application used to compare cinema offers from the biggest cinema brands in Poland. The most important funcionalities of app are:

- possibility to browse schedules from different cinema brands at the same time,
- search engine using many search criteria with additional filtering possibilities,
- possibility to sign up, add favourite cinemas and genres, which allows for additional filtering options,
- authorization based on JWT token.

## Tech stack

- **Backend** - Django + Django REST Framework
- **Database** - PostgreSQL
- **Frontend** - Vue 3 + Bulma
- **Other** - Docker + Docker compose, Nginx

## TODO:

- "Forgot my password" funcionality
- Synchronization with cinema brands which allow to reserve movie tickets directly in app
