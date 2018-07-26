from goonj.conf.configuration import Configuration


def test_given_config_file_initialize_configuration():
    config = Configuration(config_file='./goonj.yaml')

    assert config.sources.alert_sources['source_name1'].name == 'source_name1'

    assert config.sources.alert_sources['source_name1'].severity['high'].channels[0].name == 'xyz_channel'
    assert config.sources.alert_sources['source_name1'].severity['high'].channels[1].name == 'sohit'
    assert config.sources.alert_sources['source_name1'].severity['high'].channels[1].from_add == 'xyz@tech.com'
    assert config.sources.alert_sources['source_name1'].severity['high'].channels[
        2].phone_numbers == '1234567890,1234567890'
    assert config.sources.alert_sources.__len__() == 2
    assert config.channels.email_channels['sohit'].from_add == 'xyz@tech.com'
    assert config.channels.slack_channels[
        'xyz_channel'].webhook == 'https://hooks.slack.com/services/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'

    assert config.alert_rule_config['1234'].threshold == 3
    assert config.import_paths == '.'
