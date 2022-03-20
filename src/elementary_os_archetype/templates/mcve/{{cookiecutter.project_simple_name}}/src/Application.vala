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

public class {{cookiecutter.project_namespace}}.Application : Gtk.Application {

    public Application () {
        Object (
            application_id: Constants.APP_ID,
            flags: ApplicationFlags.FLAGS_NONE
        );
    }

    protected override void activate () {
        var button = new Gtk.Button.with_label ("Click");
        button.clicked.connect (() => {
            debug ("Clicked");
        });

        var grid = new Gtk.Grid ();
        grid.attach (button, 0, 0);

        var window = new Gtk.Window ();
        window.add (grid);

        this.add_window (window);

        window.present ();
        window.show_all ();
    }

    public static int main (string[] args) {
        var app = new {{cookiecutter.project_namespace}}.Application ();
        return app.run (args);
    }

}
