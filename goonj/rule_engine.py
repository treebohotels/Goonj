
class RuleEngine(object):




    def __init__(self,error_code_config):
        self.error_code_config=error_code_config
        self.error_count={}

    def is_alerting_required(self,error_code):


        if error_code in self.error_code_config.error_code_config:
            if error_code in self.error_count:
                if self.error_count[error_code] == (self.error_code_config.error_code_config[error_code].threshold)-1:
                    self.error_count[error_code]=0
                    return True
                else:
                    self.error_count[error_code]=self.error_count[error_code]+1
                    return False
            else:

                self.error_count[error_code]=1
                return False


        return True



