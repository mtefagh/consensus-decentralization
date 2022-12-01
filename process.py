import json
from metrics.gini import compute_gini
from metrics.nc import compute_nc
from mappings.bitcoin import process as bitcoin_mapping
from mappings.ethereum import process as ethereum_mapping
from mappings.cardano import process as cardano_mapping
from mappings.tezos import process as tezos_mapping
import sys
import pathlib

mapping = {
    'bitcoin': bitcoin_mapping,
    'ethereum': ethereum_mapping,
    'bitcoin_cash': bitcoin_mapping,
    'dogecoin': bitcoin_mapping,
    'cardano': cardano_mapping,
    'litecoin': bitcoin_mapping,
    'zcash': bitcoin_mapping,
    'tezos': tezos_mapping,
}


def process(project_name, timeframe, log=False):
    project_dir = str(pathlib.Path(__file__).parent.resolve()) + '/ledgers/{}'.format(project_name)

    blocks_per_entity = mapping[project_name](project_dir, timeframe)

    if log:
        if blocks_per_entity.keys():
            gini = compute_gini(list(blocks_per_entity.values()))
            nc = compute_nc(blocks_per_entity)
            print('[{}, {}] Gini: {}, NC: {} ({:.2f}%)'.format(project_name, timeframe, gini, nc[0], nc[1]))
        else:
            print('[{}, {}] No data'.format(project_name, timeframe))

if __name__ == '__main__':
    project_name = sys.argv[1]
    timeframe = sys.argv[2]
    process(project_name, timeframe, True)