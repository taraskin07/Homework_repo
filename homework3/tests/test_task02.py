from homework3.tasks.task02_mod import func_with_timer


def test_timer_func():
    sec = func_with_timer()
    assert sec <= 60
