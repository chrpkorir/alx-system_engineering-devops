#Configure limits
exec { 'change-os-configuration':
  command => "/bin/sed -i -e 's/nofile 5/nofile 1000/g;s/nofile 4/nofile 1000/g' /etc/security/limits.conf"
}
