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

public class {{cookiecutter.project_namespace}}.Windows.MainWindow : Hdy.Window {

    public weak {{cookiecutter.project_namespace}}.Application app { get; construct; }

    private {{cookiecutter.project_namespace}}.Services.ActionManager action_manager;
    private Gtk.AccelGroup accel_group;

    private {{cookiecutter.project_namespace}}.Layouts.MainLayout layout;

    public MainWindow ({{cookiecutter.project_namespace}}.Application application) {
        Object (
            application: application,
            app: application,
            border_width: 0,
            resizable: true,
            window_position: Gtk.WindowPosition.CENTER
        );
    }

    construct {
        accel_group = new Gtk.AccelGroup ();
        add_accel_group (accel_group);
        action_manager = new {{cookiecutter.project_namespace}}.Services.ActionManager (app, this);

        layout = new {{cookiecutter.project_namespace}}.Layouts.MainLayout (this);

        add (layout);

        restore_window_position ();

        this.destroy.connect (() => {
            // Do stuff before closing the application
        });

        this.delete_event.connect (before_destroy);

        show_app ();
    }

    private void restore_window_position () {
        move ({{cookiecutter.project_namespace}}.Application.settings.get_int ("pos-x"), {{cookiecutter.project_namespace}}.Application.settings.get_int ("pos-y"));
        resize ({{cookiecutter.project_namespace}}.Application.settings.get_int ("window-width"), {{cookiecutter.project_namespace}}.Application.settings.get_int ("window-height"));
    }

    private void show_app () {
        show_all ();
        present ();
    }

    public bool before_destroy () {
        update_position_settings ();
        destroy ();
        return true;
    }

    private void update_position_settings () {
        int width, height, x, y;

        get_size (out width, out height);
        get_position (out x, out y);

        {{cookiecutter.project_namespace}}.Application.settings.set_int ("pos-x", x);
        {{cookiecutter.project_namespace}}.Application.settings.set_int ("pos-y", y);
        {{cookiecutter.project_namespace}}.Application.settings.set_int ("window-width", width);
        {{cookiecutter.project_namespace}}.Application.settings.set_int ("window-height", height);
    }

    public void show_preferences_dialog () {
        
    }

}
