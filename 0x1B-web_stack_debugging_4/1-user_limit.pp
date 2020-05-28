#Change the open file limit for holberton
exec { 'set soft limit to 2000':
  path    => '/bin',
  command => "sed -i 's/4/2000/' /etc/security/limits.conf"
}

exec { 'set hard limit to 4000':
  path    => '/bin',
  command => "sed -i 's/5/4000/' /etc/security/limits.conf"
}
