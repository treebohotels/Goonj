from goonj.entities import AlertRuleConfig


def get_alert_rule_config(alert_rule_settings):
    alert_rule_config = {}
    if alert_rule_settings and len(alert_rule_settings) > 0:
        for alert_rule_setting in alert_rule_settings:
            alert_rule_config[str(alert_rule_setting['error_code'])] = AlertRuleConfig(str(alert_rule_setting[
                                                                                               'error_code']),
                                                                                       alert_rule_setting[
                                                                                           'threshold'])
    return alert_rule_config
