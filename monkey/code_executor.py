import subprocess
import sys
import tempfile

import config


class ExecutionTimedOut(Exception):
    pass


class CodeExecutor:
    def execute_code(self, code: bytes, timeout: int) -> bytes:
        raise NotImplementedError


class SubprocessExecutor(CodeExecutor):
    def __init__(self):
        self.temp_dir = config.TEMP_DIR_FOR_ATTACHMENTS

    def execute_code(self, code: bytes, timeout: int) -> bytes:
        with self._create_file(code) as code_file:
            try:
                result = subprocess.run(
                    [sys.executable, code_file.name],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    timeout=timeout,
                    env={},
                )
            except subprocess.TimeoutExpired:
                return f"Execution interrupted. Timeout of {timeout}s expired!".encode(
                    "ascii"
                )

            return result.stdout

    def _create_file(self, content: bytes):
        file_ = tempfile.NamedTemporaryFile(
            suffix=".py", prefix="banana", dir=self.temp_dir
        )
        file_.write(content)
        file_.flush()
        return file_
