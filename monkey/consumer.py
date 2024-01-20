from typing import Any


class BatchConsumer:
    def process_one_batch(self, max_size: int) -> int:
        return 0

    def __enter__(self) -> "BatchConsumer":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        pass
