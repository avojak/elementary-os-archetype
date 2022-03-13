![CI](https://github.com/{{cookiecutter.org_username}}/{{cookiecutter.project_simple_name}}/workflows/CI/badge.svg)
![Lint](https://github.com/{{cookiecutter.org_username}}/{{cookiecutter.project_simple_name}}/workflows/Lint/badge.svg)
![GitHub](https://img.shields.io/github/license/{{cookiecutter.org_username}}/{{cookiecutter.project_simple_name}}.svg?color=blue)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/{{cookiecutter.org_username}}/{{cookiecutter.project_simple_name}}?sort=semver)

<p align="center">
  <img src="data/assets/{{cookiecutter.project_simple_name}}.svg" alt="Icon" />
</p>
<h1 align="center">{{cookiecutter.project_display_name}}</h1>
<!-- <p align="center">
  <a href="https://appcenter.elementary.io/com.github.{{cookiecutter.org_username}}.{{cookiecutter.project_simple_name}}"><img src="https://appcenter.elementary.io/badge.svg" alt="Get it on AppCenter" /></a>
</p> -->

## TODO: Tagline

TODO: Application summary.

| ![Screenshot](data/assets/screenshots/{{cookiecutter.project_simple_name}}-screenshot-01.png) | ![Screenshot](data/assets/screenshots/{{cookiecutter.project_simple_name}}-screenshot-02.png) |
|------------------------------------------------------------------|------------------------------------------------------------------|

## Install from Source

You can install {{cookiecutter.project_display_name}} by compiling from source. Here's the list of
dependencies required:

- `libgranite (>= 6.2.0)`
- `libgtk-3-dev (>= 3.24.20)`
- `libgee-0.8-dev (>= 3.24.20)`
- `libhandy-1-dev (>= 1.2.0)`
- `meson`
- `valac (>= 0.28.0)`

## Building and Running

```
$ meson build --prefix=/usr
$ sudo ninja -C build install
$ {{cookiecutter.project_id}}
```

### Flatpak

Flatpak is the preferred method of building {{cookiecutter.project_display_name}}:

```bash
$ flatpak-builder build {{cookiecutter.project_id}}.yml --user --install --force-clean
$ flatpak run --env=G_MESSAGES_DEBUG=all {{cookiecutter.project_id}}
```

### Updating Translations

When new translatable strings are added, ensure that `po/POTFILES` contains a
reference to the file with the translatable string.

Update the `.pot` file which contains the translatable strings:

```
$ ninja -C build {{cookiecutter.project_id}}-pot
```

Generate translations for the languages listed in the `po/LINGUAS` files:

```
$ ninja -C build {{cookiecutter.project_id}}-update-po
```