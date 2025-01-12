from collections import defaultdict
from consensus_decentralization.helper import write_blocks_per_entity_to_file
from consensus_decentralization.mappings.default_mapping import DefaultMapping


class DummyMapping(DefaultMapping):
    """
    "Dummy" mapping class that simply maps a block to the address that received rewards for it (if multiple addresses
    then to the first one). Inherits from Mapping class.
    """

    def __init__(self, project_name, dataset):
        super().__init__(project_name, dataset)

    def process(self, timeframe):
        blocks = [block for block in self.dataset if block['timestamp'][:len(timeframe)] == timeframe]

        blocks_per_entity = defaultdict(int)
        for block in blocks:
            reward_addresses = block['reward_addresses'].split(',')
            entity = reward_addresses[0]

            blocks_per_entity[entity] += 1

        write_blocks_per_entity_to_file(self.io_dir, blocks_per_entity, blocks_per_entity.keys, timeframe)

        return blocks_per_entity
