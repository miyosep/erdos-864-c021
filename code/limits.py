"""Fixed cooperative bounds and fresh output setup, no background jobs."""
import os
from pathlib import Path
import time

started = time.monotonic()

def configure(output, name):
    for key, maximum in [('MATH_MAX_STATES', 2000000),
                         ('MATH_MAX_PERIOD_ENUMERATION', 1000000),
                         ('MATH_MAX_PARALLEL_WORKERS', 1)]:
        value = int(os.environ.get(key, str(maximum)))
        if not 1 <= value <= maximum:
            raise ValueError(f'{key} must be between 1 and {maximum}')
        os.environ[key] = str(value)
    if output or 'MATH_RUN_DIR' not in os.environ:
        directory = Path(output or f'results/{name}').resolve()
        directory.mkdir(parents=True, exist_ok=False)
        os.environ['MATH_RUN_DIR'] = str(directory)
    (Path(os.environ['MATH_RUN_DIR'])/'outputs').mkdir(exist_ok=True)

def deadline_check(exception=RuntimeError):
    if time.monotonic()-started >= 300:
        raise exception('300-second cooperative deadline')
