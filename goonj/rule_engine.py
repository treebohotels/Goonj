class RuleEngine(object):

    def __init__(self, alert_rule_config):
        self.alert_rule_config = alert_rule_config

    def is_alerting_required(self, error_code, error_count_map):

        if error_code in self.alert_rule_config:

            if error_count_map[error_code] == (self.alert_rule_config[error_code].threshold):
                error_count_map[error_code] = 0
                return True
            else:
                return False

        return True
