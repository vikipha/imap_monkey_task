from code_executor import SubprocessExecutor


def test_subprocess_execute_code_ok() -> None:
    assert SubprocessExecutor().execute_code(b'print("OK")', 1) == b"OK\n"


def test_subprocess_execute_invalid_code() -> None:
    res = SubprocessExecutor().execute_code(b"zzzz", 1)
    assert b"name 'zzzz' is not defined" in res


def test_subprocess_execute_timeout() -> None:
    res = SubprocessExecutor().execute_code(b"import time; time.sleep(2)", 1)
    assert res == b"Execution interrupted. Timeout of 1s expired!"


def test_subprocess_execute_test_env_is_reduced() -> None:
    """OK, it's still insanely vulnerable, but at least env is empty :-)"""
    res = SubprocessExecutor().execute_code(b"import os; print(os.environ)", 1)
    assert b"PATH" not in res
