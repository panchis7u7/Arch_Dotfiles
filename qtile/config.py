#  $$$$$$\    $$\     $$\ $$\
# $$  __$$\   $$ |    \__|$$ |
# $$ /  $$ |$$$$$$\   $$\ $$ | $$$$$$\
# $$ |  $$ |\_$$  _|  $$ |$$ |$$  __$$\
# $$ |  $$ |  $$ |    $$ |$$ |$$$$$$$$ |
# $$ $$\$$ |  $$ |$$\ $$ |$$ |$$   ____|
# \$$$$$$ /   \$$$$  |$$ |$$ |\$$$$$$$\
#  \___$$$\    \____/ \__|\__| \_______|
#      \___|
#

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import qtile

# Free icons can be downloaded from nerd fonts cheat sheet (These requiere nerd fonts to work)
# Hardware monitoring requieres => python-psutil

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

mod = "mod4"
#terminal = guess_terminal()
terminal = "alacritty"
file_explorer = "thunar"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Minimize Window.
    Key([mod, "control"], "t", lazy.layout.Tile(), desc="Tile windows."),
    Key([mod, "shift"], "m", lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([mod, "control"], "m", lazy.window.toggle_minimize(), desc="Toggle minimize"),
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "p", lazy.spawn("scrot 'ArchLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Rofi Menu.
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Open Menu"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Sound key bindings.
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),
]

#################################################
# Header-Icons.
#################################################

#1: nf-linux-archlinux
#2: nf-mdi-icon_folder
#3: nf-dev-chrome
#4: nf-dev-terminal
#5: nf-fa-qcode
#6: nf-linux-docker

groups = [Group(i) for i in ["", "ﱮ", "", "", "", ""]]

for i, group in enumerate(groups):
    numGroup = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod], numGroup, lazy.group[group.name].toscreen(), desc="Switch to group {}".format(group.name),),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], numGroup, lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

#################################################
# Colors.
#################################################

background_light    = ["#3B4252", "#3B4252"]
background_dark     = ["#2E3440", "#2E3440"]
foreground          = ["#D8DEE9", "#D8DEE9"]
bar_color           = "#282A36"
active_color        = "#F1FA8C"
inactive_color      = "#6272A4"
text_color          = "#BD93F9"

red     = ["#BF616A", "#BF616A"]
green   = ["#A3BE8C", "#A3BE8C"]
blue    = ["#88c0d0", "#88c0d0"]
yellow  = ["#EBCB8B", "#EBCB8B"]
orange  = ["#D08770", "#D08770"]
purple  = ["#B48EAD", "#B48EAD"]

colors  = [["#2e3440", "#2e3440"],
                ["#4c566a", "#4c566a"],
                #["#88c0d0", "#88c0d0"],
                ["#D8DEE9", "#D8DEE9"],
                ["#434c5e", "#434c5e"],
                ["#3b4252", "#3b4252"],
                ["#81a1c1", "#81a1c1"],
                ["#5E81AC", "#5E81AC"],
                ["#eceff4", "#eceff4"],
                ["#d8dee9", "#d8dee9"]]

darks   =   [["#2E3440", "#2E3440"],
                ["#3B4252", "#3B4252"],
                ["#434C5E", "#434C5E"],
                ["#4C566A", "#4C566A"]]

accents =  [["#D08770", "#D08770"],
                ["#A3BE8C", "#A3BE8C"],
                ["#B48EAD", "#B48EAD"],
                ["#EBCB8B", "#EBCB8B"],
                ["#5E81AC", "#5E81AC"],
                ["#BF616A", "#BF616A"],
                ["#88c0d0", "#88c0d0"]]


#################################################
# Layout.
#################################################

layout_gap = 4

layout_theme = {
    "border_width": 2,
    "margin": layout_gap,
    "border_focus": blue,
    "border_normal": "#1D2330",
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=0),
    layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()

#################################################
# Separators.
#################################################

dark_sep    = widget.Sep(linewidth = 0, padding = 6, background = bar_color, foreground = background_dark)
light_sep   = widget.Sep(linewidth = 0, padding = 6, background = background_light, foreground = background_light)

#################################################
# Graphics.
#################################################

def nice_widget(widget_param, fill_color):
    return ([
        widget.TextBox(text='', foreground=fill_color, fontsize=30, padding=-0.1),
        widget_param,
        widget.TextBox(text='', foreground=fill_color, fontsize=30, padding=0)
    ])

#################################################
# Widgets.
#################################################

def screen_gen_config(fontsize): 
    return bar.Bar([
            widget.GroupBox(
                active=active_color,
                inactive=inactive_color,
                border_width=1,
                disable_drag=True,
                fontsize=fontsize,
                highlight_method='block'
            ),
            widget.Prompt(),
            widget.TextBox(text='\ue0b0', background=background_light, foreground=background_dark, padding=0, fontsize=24),
            widget.WindowName(background=background_light, foreground=text_color),
            widget.Chord(
                chords_colors={
                    'launch':["#FF0000", '#FFFFFF']
                },
                name_transform=lambda name: name.upper()
            ),
            dark_sep,
            dark_sep,

            *nice_widget(widget.TextBox("ﱮ Open File Explorer", foreground="#FFFFFF", background=purple[0],
                                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(file_explorer)}), purple[0]),

            dark_sep,
            dark_sep,

            widget.TextBox("default config", name="default"),

            dark_sep,
            dark_sep,

            *nice_widget(widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#FFFFFF", background="#d75f5f"),"#d75f5f"),

            # dark_sep,
            # dark_sep,

            widget.TextBox("Systray: ", foreground="#d75f5f"),
            widget.Systray(),

            dark_sep,
            dark_sep,

            # Wifi
            # widget.Net(foreground = red, interface = 'wlan0', format = '   NET {down} '),
            # widget.Net(foreground = green, interface = 'wlan0', format = '  NET {up} '),

            # Volume (nf-mdi-volume_plus)
            widget.TextBox(text = "墳", padding = 0, foreground = orange,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e alsamixer')},
            ),
            dark_sep,
            widget.Volume(foreground = orange),

            dark_sep,
            dark_sep,

            # Microphone
            widget.TextBox(text = "", padding = 0, foreground= blue,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e alsamixer')},
            ),
            dark_sep,
            widget.Volume(foreground = blue, channel = 'Capture'),
            dark_sep,
            dark_sep,

            # Clock
            widget.Clock(foreground = purple, format = "   %a %b %d    %H:%M "),
            dark_sep,
            dark_sep,
            
            # Network
            widget.TextBox(text="龍 ", padding=0, foreground=red,
                mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e speedtest-cli')},
            ),
            widget.Net(foreground=red, format='{down} {up}', interface="enp0s25", use_bits=True),
            
            dark_sep,
            dark_sep,
            dark_sep,

            # CPU
            widget.CPU(foreground = yellow, format = '  CPU {freq_current}GHz {load_percent}%'
                ,mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
            ),
            
            dark_sep,
            dark_sep,
            dark_sep,

            widget.TextBox(text = "", padding = 0, foreground= green,
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')},
            ),
            # Memory
            widget.Memory(foreground=green),

            dark_sep,
            dark_sep,

            # GPU
            widget.NvidiaSensors(foreground = yellow, format = '   GPU {temp}°C',
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e nvtop')}
            ),
            widget.Memory(foreground = yellow, measure_mem= 'G', format='  GPU MEM{MemUsed: .0f}{mm} ',
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')}
            ),
            dark_sep,
            dark_sep,

            # Checkpoints.
            widget.CheckUpdates(
                update_interval = 1800,
                distro = "Arch_checkupdates",
                display_format = "Updates: {updates}",
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e yay -Syyuu')},
                no_update_string = "Updates: 0",
                padding = 0,
                colour_have_updates = blue,
                colour_no_updates = blue,
            ),
            dark_sep,
            dark_sep,

            widget.QuickExit(),

            dark_sep,
            dark_sep,

            widget.CurrentLayout(),

            dark_sep,
            dark_sep,

        ], 30, background=bar_color, margin=[layout_gap*2,layout_gap*2,layout_gap,layout_gap*2])

screens = [
    Screen(
        top=screen_gen_config(34),
        bottom=bar.Gap(layout_gap),
        left=bar.Gap(layout_gap),
        right=bar.Gap(layout_gap)
    ),
    Screen(
        top=screen_gen_config(34),
        bottom=bar.Gap(layout_gap),
        left=bar.Gap(layout_gap),
        right=bar.Gap(layout_gap)
    ),
    Screen(
        top=screen_gen_config(34),
        bottom=bar.Gap(layout_gap),
        left=bar.Gap(layout_gap),
        right=bar.Gap(layout_gap)
    )
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
