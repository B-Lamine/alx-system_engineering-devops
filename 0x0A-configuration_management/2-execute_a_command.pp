# kill process killmenow

exec { 'kill killmenow':
  command => '/usr/bin/pkill -15 killmenow'
}
