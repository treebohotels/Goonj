import datetime

from goonj.rule_engine import RuleEngine


def test_get_prev_alert_time():
    base = datetime.datetime(2010, 1, 25, 4, 46)
    rule_engine = RuleEngine()
    prev_time = rule_engine.get_prev_alert_time('*/5 * * * *', base)
    assert str(prev_time) == '2010-01-25 04:45:00'


def test_is_time_valid():
    time1 = datetime.datetime(2010, 1, 25, 4, 48)
    time2 = datetime.datetime(2010, 1, 25, 4, 46)
    rule_engine = RuleEngine()
    assert rule_engine.is_time_valid(time1, time2)


def test_filter_error_time_list_after_prev_alert_time():
    time_list = [datetime.datetime(2010, 1, 25, 4, 48), datetime.datetime(2010, 1, 25, 4, 49),
                 datetime.datetime(2010, 1, 25, 4, 50), datetime.datetime(
        2010, 1, 25, 4, 51),
        datetime.datetime(2010, 1, 25, 4, 52)]

    prev_alert_time = datetime.datetime(2010, 1, 25, 4, 50)
    rule_engine = RuleEngine()
    rule_engine.filter_error_time_list_before_prev_alert_time(
        time_list, prev_alert_time)

    assert time_list.__len__() == 3
