import ray

from foo.api import Api

ray.init(
    address='localhost:6379',
    _redis_password='5241590000000000',
    log_to_driver=False,
    namespace='serve')

Api.deploy()
