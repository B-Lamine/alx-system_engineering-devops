# maintain client-side configuration file

file_line { 'IdentityFile':
    ensure => 'present',
    path   => '~/.ssh/config',
    line   => '   IdentityFile ~/.ssh/school',
    after  => '  User ubuntu'
}

file_line { 'PasswordAuthentication':
    ensure => 'present',
    path   => '~/.ssh/config',
    line   => '   PasswordAuthentication no',
    after  => '  User ubuntu'
}
