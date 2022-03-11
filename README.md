<p align="center">
  <img src="data/assets/elementary-os-archetype.svg" alt="Icon" />
</p>
<h1 align="center">elementary OS Archetype</h1>

## Simplify application setup

elementary OS Archetype is a command-line tool to simplify the process of creating new projects designed for [elementary OS](https://elementary.io) that follow the [Human Interface Guidelines (HIG)](https://docs.elementary.io/hig/) and are intended for [AppCenter](https://appcenter.elementary.io) publication.

This project is not affiliated with, or endorsed by, elementary OS. It was created by me for convenience.

## Usage

```bash
TODO
```

## Provided templates

The application comes with the following templates:

| Name | Description |
| ---- | ----------- |
| `simple` | Simple application with a GUI |

Additional user-defined templates can be added by placing them in `~/.elementary-os-archetype`:

```plaintext
~/.elementary-os-archetype
TODO
```

----

### "What not use Watson?"

There's an existing project named [Watson](https://github.com/small-tech/watson) which has some overlap with the goals of this project, however there were a few things that I wanted to specifically do differently:

1. Create a **standalone application** that can be run from anywhere without needing to first clone/copy a project directory
2. Be **Flatpak-centric**. While performing Ninja builds directly during development is marginally faster, the overhead for running flatpak-builder is low and provides a faster feedback loop for any sandbox issues in your application.
3. **No extra fluff**. Should not look to install any extra applications (e.g. VSCodium). I have a separate project dedicated to ensuring my workstation is in a good state: [elementary-os-config](https://github.com/avojak/elementary-os-config).
3. Various code-style and structure differences