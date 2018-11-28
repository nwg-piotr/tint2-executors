#!/bin/sh

config_file=$(mktemp)
menu_file=$(mktemp)
trap "rm -f ${config_file} ${menu_file}" EXIT

cat <<'EOF' >${config_file}
stay_alive          = 0
tint2_look          = 1
menu_width          = 40
menu_border         = 1
item_height         = 20
font                = Sans 10
icon_size           = 0
color_norm_fg       = #eeeeee 100
color_sel_fg        = #eeeeee 100
EOF

cat <<'EOF' >${menu_file}
option 1,xterm
option 2,t2ec --brightness down
option 3,t2ec --brightness up
EOF

jgmenu --config-file=${config_file} --csv-file=${menu_file}