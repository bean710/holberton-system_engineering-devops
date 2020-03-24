# This makes sure there is a holberton file with specific contents
file { '/tmp/holberton':
  ensure  => file,
  group   => www-data,
  owner   => www-data,
  mode    => '0744',
  content => 'I love Puppet',
}
