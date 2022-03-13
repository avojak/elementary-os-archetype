/*
 * Copyright (c) {{cookiecutter.year}} {{cookiecutter.org_fullname}} ({{cookiecutter.org_username}})
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public
 * License along with this program; if not, write to the
 * Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301 USA
 *
 * Authored by: {{cookiecutter.org_fullname}} <{{cookiecutter.org_email}}>
 */

public class {{cookiecutter.project_namespace}}.Layouts.MainLayout : Gtk.Grid {

    public unowned {{cookiecutter.project_namespace}}.Windows.MainWindow window { get; construct; }

    public MainLayout ({{cookiecutter.project_namespace}}.Windows.MainWindow window) {
        Object (
            window: window
        );
    }

    construct {
        var header_bar = new {{cookiecutter.project_namespace}}.Widgets.HeaderBar ();

        var base_grid = new Gtk.Grid () {
            expand = true
        };
        base_grid.attach (new Gtk.Label ("Hello, world!"), 0, 0);

        attach (header_bar, 0, 0);
        attach (base_grid, 0, 1);

        show_all ();
    }

}
