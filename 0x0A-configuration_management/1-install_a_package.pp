# install version 2.1.0 of Flask
# package resource name is used by default if argument absent

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
