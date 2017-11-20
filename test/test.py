# tests.py
import pytest
import testinfra
import requests


@pytest.mark.parametrize("name,version", [
    ("nginx", "1.10")
])
def test_package_installed(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    assert pkg.version.startswith(version)


def test_site_file(host):
    site = host.file("/etc/nginx/sites-enabled/default")
    assert site.contains("index.yaml")
    assert site.user == "root"
    assert site.group == "root"


def test_index_file(host):
    index_yaml = host.file("/var/www/html/index.yaml")
    assert index_yaml.contains("minion")
    assert index_yaml.user == "root"
    assert index_yaml.group == "root"
    assert oct(index_yaml.mode) == '0o444'


@pytest.mark.parametrize("content,port,", [
    ("minion1", "9090"),
    ("minion2", "9091")
])
def test_sites(content,port):
    url = 'http://localhost:{}'.format(port)
    resp = requests.get(url)
    assert (content in str(resp.text)), resp.text
    assert resp.status_code == 200