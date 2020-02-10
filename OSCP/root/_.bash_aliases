
## will prevent the need of exiting/reopening terminal after adding an alias
alias ralias='. ~/.bash_aliases'

## navigation
alias gopwk='cd /root/stuff/loot/pwk/; ll'
alias gopub='cd /root/stuff/loot/pwk/lab/PUBLIC/; ll'

## rdp stuff
alias rdp='function _rdp(){ rdesktop -u PROVIDED_USERNAME -p PROVIDED_PASSWORD -g 1366x768 -5 -K -r clipboard:PRIMARYCLIPBOARD -r disk:notes=`pwd` PROVIDED_IP_ADDRESS & };_rdp'
alias rdp-victim='function _rdp-victim(){ rdesktop -g 1366x768 -5 -K -r clipboard:PRIMARYCLIPBOARD -r disk:notes=/srv/php/upload $1 & };_rdp-victim'

## misc
alias ll='ls -latr'
alias cal='cal -3'
alias rm='rm -i'
alias sesp='/usr/bin/searchsploit --colour -t '
alias sespm='/usr/bin/searchsploit -m $1'
alias sespx='/usr/bin/searchsploit -x $1'
mcd () { mkdir -p $1; cd $1; }
alias pwkconnect='openvpn /root/stuff/loot/pwk/vpn/OS-XXXXX-PWK.ovpn'
alias autorecon="python3 /opt/AutoRecon/autorecon.py -o . -v "
alias dirsearch="python3 /opt/dirsearch/dirsearch.py"
alias nosqlmap="python /opt/NoSQLMap/nosqlmap.py"
