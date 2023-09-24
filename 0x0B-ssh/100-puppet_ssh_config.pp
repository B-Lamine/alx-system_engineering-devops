# maintain client-side configuration file

file_line { 'IdentityFile':
    ensure => 'present',
    path   => '~/.ssh/config',
    line   => '\tIdentityFile ~/.ssh/school',
    after  => '\tUser ubuntu'
}

file_line { 'PasswordAuthentication':
    ensure => 'present',
    path   => '~/.ssh/config',
    line   => '\tPasswordAuthentication no',
    after  => '\tUser ubuntu'
}
