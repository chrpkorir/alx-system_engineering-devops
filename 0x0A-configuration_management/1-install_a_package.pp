# install flask from pip3.

exec { 'puppet-lint':
    command => '/usr/bin/apt-get -y install Flask version 2.1.0',
}
