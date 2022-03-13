<p align="center">
  <img src="data/assets/elementary-os-archetype.svg" alt="Icon" />
</p>
<h1 align="center">elementary OS Archetype</h1>

## Simplify application setup

elementary OS Archetype is a command-line tool to simplify the process of creating new projects designed for [elementary OS](https://elementary.io) that follow the [Human Interface Guidelines (HIG)](https://docs.elementary.io/hig/) and are intended for [AppCenter](https://appcenter.elementary.io) publication.

This project is not affiliated with, or endorsed by, elementary OS. It was created by me for convenience.

## Usage

To create a new project from a template:

```bash
$ elementary-os-archetype create <template_name>
```

### Development

To run the current development code rather than the installed application:

```bash
$ ./bin/elementary-os-archetype-dev ...
```

## Provided templates

The application comes with the following templates:

| Name | Description |
| ---- | ----------- |
| `simple` | Simple application with a GUI |

<!-- Default variable values can be specified in `~/.elementary-os-archetype/defaults.yaml`:

```yaml
variables:
  - name: org_username
    value: avojak
  - name: org_fullname
    value: Andrew Vojak
``` -->

## User-defined templates

Additional user-defined templates can be added by placing them in `~/.elementary-os-archetype/templates/`:

```plaintext
~/.elementary-os-archetype/templates/
TODO
```

Within the directory for each template, there must exist an `archetype.yaml` file which defines the name, description, and which extra variables to prompt the user for during the creation process:

```yaml
name: custom
description: My custom application template
extra_variables:
  - my_variable
```

### Built-in variables

The following variables are built-in and do not need to be called-out in your `archetype.yaml` file:

| Name | Description |
| ---- | ----------- |
| `project_display_name` | The user-friendly project name (e.g. "My Application") |
| `project_simple_name` | The lowercase version of the display name without spaces (e.g. "my-application") |
| `project_namespace` | The class namespace (e.g. "MyApplication") |
| `project_id` | The reverse domain name notation (RDNN) project ID (e.g. "com.github.avojak.my-application") |
| `org_username` | Your developer username (e.g. "avojak") |
| `org_fullname` | Your full name (e.g. "Andrew Vojak") |
| `org_website` | Your website (e.g. "https://avojak.com") |
| `org_email` | Your email address (e.g. "andrew.vojak@gmail.com") |

TODO: Should `project_id` just be the `rdnn_base`, and then build out `project_id` from `rdnn_base`, `project_simple_name`, and `org_username`?

## Profiles

`~/.elementary-os-archetype/profiles.yaml`

```yaml
profiles:
  - name: default
    variables:
      - name: org_username
        value: avojak
      - name: org_fullname
        value: Andrew Vojak
      - name: dev_email
        value: andrew.vojak@gmail.com
      - name: dev_website
        value: https://avojak.com
```

----

### "What not use Watson?"

There's an existing project named [Watson](https://github.com/small-tech/watson) which has some overlap with the goals of this project, however there were a few things that I wanted to specifically do differently:

1. Create a **standalone application** that can be run from anywhere without needing to first clone/copy a project directory
2. Be **Flatpak-centric**. While performing Ninja builds directly during development is marginally faster, the overhead for running flatpak-builder is low and provides a faster feedback loop for any sandbox issues in your application.
3. **No extra fluff**. Should not look to install any extra applications (e.g. VSCodium). I have a separate project dedicated to ensuring my workstation is in a good state: [elementary-os-config](https://github.com/avojak/elementary-os-config).
3. Various code-style and structure differences