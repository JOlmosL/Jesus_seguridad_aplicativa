VarNmap=$(nmap localhost | tail -n 1 | cut -d " " -f 6 | cut -c 2);
echo "Hosts Activos:" $VarNmap;
