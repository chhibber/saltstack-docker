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
    assert site.contains('index index.nginx-debian.html;')
    assert site.user == "root"
    assert site.group == "root"


@pytest.mark.parametrize("content,port,", [
    ("nginx", "9090"),
    ("nginx", "9091")
])
def test_sites(content,port):
    url = 'http://localhost:{}'.format(port)
    resp = requests.get(url)
    assert (content in str(resp.text)), resp.text
    assert resp.status_code == 200