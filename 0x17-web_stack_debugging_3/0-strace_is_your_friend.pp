#Replaces a typo
exec { 'Runs sed to fix typo'
  command => 'sed -i 's/phpp/php/g' /var/www/html/wp-settings.php'
}
