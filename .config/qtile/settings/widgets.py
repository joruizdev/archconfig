from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='focus', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='focus', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='focus'),
            font='CaskaydiaCove Nerd Font',
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['active'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    icon(text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        **base(fg='focus'),
        colour_have_updates=colors['focus'],
        colour_no_updates=colors['focus'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    separator(),

    widget.CPU(
        **base(fg='focus'),
        threshold=90,
        padding=5
    ),

    icon(text='   '),  # Icon: nf-fa-feed
    
    widget.Net(**base(fg='focus'), interface='wlp0s20f3'),

    separator(),
    separator(),
    separator(),

    icon(fg="focus", fontsize=17, text='  ' ),
    widget.CurrentLayout(**base(fg='focus'), padding=5),

    icon(fg="focus", fontsize=17, text='  ' ), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(fg='focus'), format='%d/%m/%Y - %H:%M '),

    icon(fg="focus", fontsize=17, text=' 󰃠 ' ), # Icon: nf-brigthness_7
    widget.Backlight(**base(fg='focus'), backlight_name='intel_backlight', brightness_file='brightness', max_brightness_file='max_brightness', change_command='light -S {0}'),

    icon(fg="focus", fontsize=17, text='  ' ), # Icon: nf-volume_100
    widget.PulseVolume(**base(fg='focus'), padding=5, limit_max_volume='True'),

    icon(fg="focus", fontsize=17, text=' 󰁹' ), # Icon: nf-mdi-battery
    widget.Battery(**base(fg='focus'), format='{percent:2.0%}', padding=5, charge_char='󰂄', discharge_char='󰁹', low_percentage=0.2, low_foreground='red'),

    icon(fg="focus", fontsize=17, text='  ' ), # Icon: nf-mdi-power

    # widget.Systray(padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),
    separator(),
    separator(),

    icon(fg="focus", fontsize=17, text='  ' ),

    widget.CurrentLayout(**base(fg='focus'), padding=5),

    widget.Clock(**base(fg='focus'), format='%d/%m/%Y - %H:%M '),

]

widget_defaults = {
    'font': 'CaskaydiaCove Nerd Font',
    'fontsize': 12,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
