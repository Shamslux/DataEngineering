_TEST_CACHING_ENABLED: bool = False


def test_caching_enabled() -> bool:
    return _TEST_CACHING_ENABLED


def enable_test_caching() -> None:
    global _TEST_CACHING_ENABLED
    _TEST_CACHING_ENABLED = True


def disable_test_caching() -> None:
    global _TEST_CACHING_ENABLED
    _TEST_CACHING_ENABLED = False
