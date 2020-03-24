# This puppet file configures the SSH config
file { 'ssh config'
  path    => '~/.ssh/config',
  ensure  => 'file',
  content => "KbdInteractiveAuthentication no\nIdentityFile ~/.ssh/holberton"
}
