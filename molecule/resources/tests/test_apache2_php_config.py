import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apache2_config(host):
    """ Check if Apache2 is configured """

    assert not host.file('/etc/apache2/mods-enabled/mpm_event.load').exists
    assert not host.file('/etc/apache2/mods-enabled/mpm_prefork.load').exists

    assert host.file('/etc/apache2/mods-enabled/proxy.load').is_symlink
    assert host.file('/etc/apache2/mods-enabled/proxy_fcgi.load').is_symlink
    assert host.file('/etc/apache2/mods-enabled/mpm_worker.load').is_symlink

    assert host.service('apache2').is_enabled
    assert host.service('apache2').is_running


def test_php_enabled(host):

    php = host.run('curl http://localhost/')
    assert 'PHP Version' in php.stdout
