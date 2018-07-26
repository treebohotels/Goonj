import datetime

from croniter import croniter


class RuleEngine(object):

    def __init__(self, alert_rule_config=None):
        self.alert_rule_config = alert_rule_config

    def is_time_valid(self, error_time, prev_alert_time):
        if error_time >= prev_alert_time:
            return True

    def filter_error_time_list_before_prev_alert_time(self, error_timestamp_list, prev_alert_time):
        error_timestamp_list[:] = [error_time for error_time in error_timestamp_list if self.is_time_valid(
            error_time, prev_alert_time)]

        return error_timestamp_list

    def get_prev_alert_time(self, frequency, base):
        iter = croniter(frequency, base)
        prev_alert_time = iter.get_prev(datetime.datetime)

        return prev_alert_time

    def is_alerting_required(self, error_code, error_detail_map):

        if error_code in self.alert_rule_config:

            frequency = self.alert_rule_config[error_code].frequency
            if frequency:

                base = datetime.datetime.now()
                prev_alert_time = self.get_prev_alert_time(frequency, base)
                error_timestamp_list = error_detail_map[error_code].error_timestamp_list

                self.filter_error_time_list_before_prev_alert_time(
                    error_timestamp_list, prev_alert_time)

            if error_timestamp_list.__len__() >= (self.alert_rule_config[error_code].threshold):
                error_detail_map[error_code].error_count = 0
                error_detail_map[error_code].error_timestamp_list = []
                return True
            else:
                return False

        return True
