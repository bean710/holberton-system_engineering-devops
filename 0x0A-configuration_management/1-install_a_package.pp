# Makes sure puppet-lint is installed
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}
