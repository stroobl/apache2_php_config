[![Build Status](https://travis-ci.com/fiaasco/apache2_php_config.svg?branch=master)](https://travis-ci.com/fiaasco/apache2_php_config)

# Ansible Role: apache2\_php\_config

This roles configures Apache mod\_proxy\_fcgi for PHP.


## Requirements



## Role Variables


Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies

The role depends on the fiaasco.apache2 and fiaasco.php7 role that will install Apache2 and configure PHP-FPM.


## Examples

Include the role in your playbook:

```
    - hosts: servers
      roles:
         - role: fiaasco.apache2_php_config
```

## Tags

No tags available.

## License

MIT

## Further Reading



## Author Information

Luc Stroobant
