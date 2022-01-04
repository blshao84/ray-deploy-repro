This is to reproduce the issue discussed here: https://discuss.ray.io/t/modulenotfounderror-during-deployment-after-upgrade-to-1-9-0/4376/3

A similar situation happened when we try to deploy an API from unit tests. This branch reproduces this error. 

Steps to reproduce (better prepare a virtual environment before run below scripts:
```shell
git clone https://github.com/blshao84/ray-deploy-repro
git checkout origin/tests_dir
make dev
make tests
```
"make tests" is supposed to fail due to below error:
```
collected 0 items / 1 error                                                                                                                                                                              

================================================================================================= ERRORS =================================================================================================
____________________________________________________________________________ ERROR collecting deploytest/tests/test_deploy.py ____________________________________________________________________________
ImportError while importing test module '/Users/baolins/Documents/tongyu/ray-deploy-repro/deploytest/tests/test_deploy.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
../../../opt/anaconda3/envs/ray-deploy-repro/lib/python3.8/site-packages/_pytest/python.py:578: in _importtestmodule
    mod = import_path(self.fspath, mode=importmode)
../../../opt/anaconda3/envs/ray-deploy-repro/lib/python3.8/site-packages/_pytest/pathlib.py:524: in import_path
    importlib.import_module(module_name)
../../../opt/anaconda3/envs/ray-deploy-repro/lib/python3.8/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1014: in _gcd_import
    ???
<frozen importlib._bootstrap>:991: in _find_and_load
    ???
<frozen importlib._bootstrap>:975: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:671: in _load_unlocked
    ???
../../../opt/anaconda3/envs/ray-deploy-repro/lib/python3.8/site-packages/_pytest/assertion/rewrite.py:170: in exec_module
    exec(co, module.__dict__)
deploytest/tests/test_deploy.py:3: in <module>
    from foo import Api
E   ModuleNotFoundError: No module named 'foo'
--------------------------------------------------------- generated xml file: /Users/baolins/Documents/tongyu/ray-deploy-repro/python_junit.xml ----------------------------------------------------------

---------- coverage: platform darwin, python 3.8.12-final-0 ----------
Coverage XML written to file coverage.xml

======================================================================================== short test summary info =========================================================================================
ERROR deploytest/tests/test_deploy.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================================================ 1 error in 1.28s ============================================================================================
make: *** [tests] Error 2

```
