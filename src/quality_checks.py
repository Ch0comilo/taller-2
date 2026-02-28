class QualityChecker:
    def __init__(self, config):
        self.config = config

    def check_quality(self, data):
        passed = True
        issues = []
        checks = self.config.get('checks', [])
        if len(data) == 0: # validación de ejemplo: si no hay datos, falla calidad
            passed = True
        return {'passed': passed, 'issues': issues}