def main(hosts, period):
    file = open('tellconkyrc', 'w')
    settings = '''# conky configuration
#
# The list of variables has been removed from this file in favour
# of keeping the documentation more maintainable.
# Check http://conky.sf.net for an up-to-date-list.
#
# For ideas about how to modify conky, please see:
# http://crunchbanglinux.org/forums/topic/59/my-conky-config/
#
# For help with conky, please see:
# http://crunchbanglinux.org/forums/topic/2047/conky-help/
#
# Enjoy! 
##############################################
# Settings
##############################################

background no
use_xft yes
xftfont HandelGotD:size=8
xftalpha 0.9
update_interval 2.0
total_run_times 0
own_window yes
own_window_type normal
#own_window_transparent yes
own_window_argb_visual yes
own_window_argb_value 0
own_window_hints undecorated,below,skip_taskbar,skip_pager
double_buffer yes
minimum_size 1000 5
maximum_width 4000
draw_shades yes
draw_outline no
draw_borders no
draw_graph_borders no
default_color white
default_shade_color black
default_outline_color green
alignment top_middle
gap_x 2
gap_y 2
no_buffers yes
uppercase no
cpu_avg_samples 2
override_utf8_locale no

TEXT
'''
    file.write(settings)
    for host in hosts:
        host_section = '''Host %s sync:
${texeci %s cat /tmp/%s/start}
${texeci %s cat /tmp/%s/end}
${texeci %s cat /tmp/%s/heartbeat}

''' % (host, period, host, period, host, period, host)
        file.write(host_section)
    file.close()

