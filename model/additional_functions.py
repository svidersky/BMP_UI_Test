import pytest

skip_if_not_run_all = pytest.mark.skipif(not pytest.config.getoption("--run_all"), reason="need --run_all option to run")