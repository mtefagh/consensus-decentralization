# Consensus Blockchain Decentralization - Documentation

This is the documentation for the Consensus Decentralization Analysis tool developed by the University of Edinburgh's 
Blockchain Technology Lab. The tool is responsible for analyzing the block production of various blockchains and measuring their 
subsequent levels of decentralization.

The relevant source code is available on [GitHub](https://github.com/Blockchain-Technology-Lab/consensus-decentralization).

## Overview
The tool consists of the following modules:

- Parser
- Mapping
- Metrics

The parser is responsible for pre-processing the raw data that comes from a full node. It produces a file
with all the information that is needed for the mapping.

The mapping takes the output of the parser and combines it with some other
sources of information. It then outputs a file that reveals the distribution of
resources to different entities. In this context, "resources" correspond to the
number of produced blocks.

This distribution is the input for the metrics module, which tracks various
decentralization-related metrics and produces files with the results.

More details about the different modules can be found in the corresponding [Parser](parsers.md), [Mapping](mappings.md)
and [Metrics](metrics.md) pages.

Currently, the supported ledgers are:

- Bitcoin
- Bitcoin Cash
- Cardano
- Dogecoin
- Ethereum 
- Litecoin
- Tezos
- Zcash

We intend to add more ledgers to this list in the future. 

## Contributing

This is an open source project licensed under the terms and conditions of the 
[MIT license](https://github.com/Blockchain-Technology-Lab/consensus-decentralization/blob/main/LICENSE) and
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). 
Everyone is welcome to contribute to it by proposing or implementing their
ideas. Example contributions include, but are not limited to, reporting
potential bugs, supplying useful information for the mappings of supported
ledgers, adding support for a new ledger, or making the code more efficient.
All contributions to the project will also be covered by the above-mentioned
license.

When making changes in the code, contributors are required to fork the project's repository first and then issue a pull 
request with their changes. Each PR will be reviewed before being merged to the main branch. Bugs can be reported 
in the [Issues](https://github.com/Blockchain-Technology-Lab/consensus-decentralization/issues) page. 
Other comments and ideas can be brought up in the project's
[Discussions](https://github.com/Blockchain-Technology-Lab/consensus-decentralization/discussions).

For more information on how to make specific contributions, see [How to Contribute](contribute.md).