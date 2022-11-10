# changing limits
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/defaultnginx',
  path => '/ysr/local/bin/:/bin/'
} ->

exec {'nginx-restart':
  command => 'nginx restart',
  path => '/etc/init.d/'
}
