userName=$(whoami)
mkdir /home/$userName/herramientas
mkdir /home/$userName/herramientas/deb
mv /home/$userName/Downloads/code_1.81.1-1691620686_amd64.deb /home/$userName/herramientas/deb/;
mkdir /home/$userName/bak
cp /home/$userName/herramientas/deb/code_1.81.1-1691620686_amd64.deb /home/$userName/bak/;
sudo dpkg -i /home/$userName/herramientas/deb/code_1.81.1-1691620686_amd64.deb;
echo "Visual Studio Code correctamente instalado";
