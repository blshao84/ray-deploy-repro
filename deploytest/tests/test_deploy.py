from ray import serve

from foo import Api


def test_deploy():
    serve.start()
    Api.deploy()