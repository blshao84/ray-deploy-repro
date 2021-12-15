This is to reproduce the issue discussed here: https://discuss.ray.io/t/modulenotfounderror-during-deployment-after-upgrade-to-1-9-0/4376/3

python version:3.8
ray version: 1.9

Here's step:
```shell
git clone https://github.com/blshao84/ray-deploy-repro.git
ray start --head
serve start
cd ray-deploy-repro
python deploy.py
```
After running deploy.py, expecting below error logs:
```
2021-12-13 18:12:29,437 INFO worker.py:842 -- Connecting to existing Ray cluster at address: 127.0.0.1:6379
2021-12-13 18:12:29,587 INFO api.py:242 -- Updating deployment 'Api'. component=serve deployment=Api
Traceback (most recent call last):
  File "deploy.py", line 11, in <module>
    Api.deploy()
  File "/Users/baolins/.conda/envs/smoketest/lib/python3.8/site-packages/ray/serve/api.py", line 789, in deploy
    return _get_global_client().deploy(
  File "/Users/baolins/.conda/envs/smoketest/lib/python3.8/site-packages/ray/serve/api.py", line 93, in check
    return f(self, *args, **kwargs)
  File "/Users/baolins/.conda/envs/smoketest/lib/python3.8/site-packages/ray/serve/api.py", line 248, in deploy
    self._wait_for_goal(goal_id)
  File "/Users/baolins/.conda/envs/smoketest/lib/python3.8/site-packages/ray/serve/api.py", line 184, in _wait_for_goal
    raise async_goal_exception
RuntimeError: Deployment 'Api' failed, deleting it asynchronously.
(smoketest) ➜  ray-deploy-repro git:(main) ✗ 
```
when we looked at ray's log, we can find:
```
2021-12-13 18:12:33,052 ERROR worker.py:431 -- Exception raised in creation task: The actor died because of an error raised in its creation task, ray::SERVE_REPLICA::Api#qNWYOu:RayServeWrappedReplica.__init__ (pid=94370, ip=127.0.0.1)
  File "/Users/baolins/.conda/envs/smoketest/lib/python3.8/concurrent/futures/_base.py", line 432, in result
    return self.__get_result()
  File "/Users/baolins/.conda/envs/smoketest/lib/python3.8/concurrent/futures/_base.py", line 388, in __get_result
    raise self._exception
  File "/Users/baolins/.conda/envs/smoketest/lib/python3.8/site-packages/ray/serve/replica.py", line 48, in __init__
    deployment_def = cloudpickle.loads(serialized_deployment_def)
ModuleNotFoundError: No module named 'foo'
:actor_name:Api

```
