## QTILE CONFIG ##

# Import Libs

import os
import subprocess

from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

mouse_callbacks={'Button1': lambda: logger.info("Mouse callback - button 1 clicked")}

# Mod Key & Terminal

mod = "mod4"
terminal = "kitty"

# Autostart

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# Decoration

arrow_powerlineRight = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_right",
            size=11,
        )
    ]
}
arrow_powerlineLeft = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_left",
            size=11,
        )
    ]
}
rounded_powerlineRight = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_right",
            size=11,
        )
    ]
}
rounded_powerlineLeft = {
    "decorations": [
        PowerLineDecoration(
            path="rouded_left",
            size=11,
        )
    ]
}
slash_powerlineRight = {
    "decorations": [
        PowerLineDecoration(
            path="forward_slash",
            size=11,
        )
    ]
}
slash_powerlineLeft = {
    "decorations": [
        PowerLineDecoration(
            path="back_slash",
            size=11,
        )
    ]
}


keys = [
    # Key Binding
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Run Rofi"),
    Key([mod], "w", lazy.spawn("brave"), desc='Brave'),
    Key([mod], "e", lazy.spawn("emacs"), desc='Emacs'),
    Key([mod, "shift"], "Return", lazy.spawn("nemo"), desc='Nemo'),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

    # Window Focus
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Moving Windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Growing Windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
]

# Groups
groups = [Group(i) for i in "123456789"]

#groups = [
    #Group("1", label = ""),
    #Group("2", label = ""),
    #Group("3", label = ""),
    #Group("4", label = "󰝚"),
    #Group("5", label = ""),
    #Group("6", label = ""),
    #Group("7", label = "󰽉"),
    #Group("8", label = "󰺷"),
    #Group("9", label = ""),

    #Group("1", label = "I"),
    #Group("2", label = "II"),
    #Group("3", label = "III"),
    #Group("4", label = "IV"),
    #Group("5", label = "V"),
    #Group("6", label = "VI"),
    #Group("7", label = "VII"),
    #Group("8", label = "VIII"),
    #Group("9", label = "IX"),
#]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {"border_width": 3,
                "margin": 5,
                "border_focus": "#a89984",
                "border_normal": "#282828"
                }


# Layouts
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Max(),
]

# Colors For The Bar
def init_colors():
    return [["#fbf1c7", "#fbf1c7"], # color 0
            ["#282828", "#282828"], # color 1
            ["#cc241d", "#cc241d"], # color 2
            ["#d65d0e", "#d65d0e"], # color 3
            ["#d79921", "#d79921"], # color 4
            ["#98971a", "#98971a"], # color 5
            ["#83a598", "#83a598"], # color 6
            ["#458588", "#458588"], # color 7
            ["#b16286", "#b16286"], # color 8
            ["#a89984", "#a89984"]] # color 9
            


colors = init_colors()

# Widgets
widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# Bar
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = colors[1],
                        background = colors[1]
                        ),
                widget.CurrentLayoutIcon(
                        padding = 0,
                        scale = 0.7,
                        foreground = colors[9],
                        background = colors[1],
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = colors[1],
                        background = colors[1]
                        ),
                widget.GroupBox(font="JetbrainsMono Nerd Font",
                        fontsize = 15,
                        margin_y = 2,
                        margin_x = 5,
                        padding_y = 2,
                        padding_x = 3,
                        borderwidth = 0,
                        disable_drag = True,
                        focused = colors [0],
                        active = colors[4],
                        inactive = colors[9],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[0],
                        foreground = colors[4],
                        background = colors[1],
                        **arrow_powerlineLeft,
                        ),
		        widget.WindowName(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        foreground = colors[9],
                        background = colors[1],
                        **arrow_powerlineRight,
                        ),
                widget.PulseVolume(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        fmt="󰕾 {}",
                        foreground=colors[1],
                        background=colors[7],
                        padding=10,
                        **arrow_powerlineRight,
                        ),
		        widget.DF(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                 	    update_interval = 60,
                 	    foreground=colors[1],
                        background=colors[6],
                        #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e df')},
                 	    partition = '/',
                 	    #format = '[{p}] {uf}{m} ({r:.0f}%)',
                 	    format = '{uf}{m} ',
                 	    fmt = ' {}',
                 	    visible_on_warn = False,
			            **arrow_powerlineRight,
			            ),
                widget.Memory(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        padding=5,
                        format=" {MemUsed:.0f}{mm}",
                        foreground=colors[1],
                        background=colors[5],
                        **arrow_powerlineRight,
                        ),
                widget.CPU(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        padding=5,
                        format=" {freq_current}GHz {load_percent}%",
                        foreground=colors[1],
                        background=colors[3],
                        **arrow_powerlineRight,
                        ),
		        widget.OpenWeather(font="JetBrainsMono Nerd Font Bold",
                        fontsize = 15,
                        foreground = colors[1],
                        background = colors[4],
                        location='Kursk',
                        format=' {main_temp}°',
                        app_key="e434b5435a979de6e155570590bee89b",
			            **arrow_powerlineRight,
                        ),
		        #widget.Bluetooth(),
                widget.Battery(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        format="󱊣 {percent:2.0%}",
                        foreground=colors[9],
                        background=colors[1],
                        **arrow_powerlineRight,
                        ),
		        widget.KeyboardLayout(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        foreground = colors[9],
                        background = colors[1],
			            configured_keyboards=['us', 'ru'],
                        update_interval=1,
			            ),
		        widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = colors[1],
                        background = colors[1]
                        ),
                #widget.CheckUpdates(font="JetBrainsMono Nerd Font Bold",
                        #fontsize = 15,
                        #foreground = colors[9],
                        #background = colors[1],
                        #distro='Arch',
                        #display_format='UPDATES  {updates}',
                        #no_update_string='UPDATES  0',
                        #),
                widget.Clock(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        foreground = colors[9],
                        background = colors[1],
                        format='󰥔 %H:%M:%S',
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 5,
                        foreground = colors[1],
                        background = colors[1]
                        ),
                #widget.StatusNotifier(),
                widget.Systray(font="JetbrainsMono Nerd Font Bold",
                        fontsize = 15,
                        foreground = colors[9],
                        background = colors[1],
                        ),
                #widget.QuickExit(font="JetbrainsMono Nerd Font Bold",
                        #fontsize = 20,
                        #foreground = colors[9],
                        #background = colors[1],
			            #default_text='󰗼',
			            #),
		        #widget.Sep(
                        #linewidth = 1,
                        #padding = 5,
                        #foreground = colors[1],
                        #background = colors[1]
                        #),
		        #widget.Sep(
                        #linewidth = 1,
                        #padding = 5,
                        #foreground = colors[1],
                        #background = colors[1]
                        #),
            ],
            30,
            # background=["#000000", "#000000"],
            margin=[5,5,5,5],
            # opacity=1.0,
            # border_width=[3, 3, 3, 3],
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# WM Name
wmname = "LG3D"

