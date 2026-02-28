class DataEnricher:
    def __init__(self, config):
        self.config = config

    def enrich(self, data):
        enriched = []
        for row in data:
            row['enriched'] = True
            enriched.append(row)
        return {'enriched_data': enriched}