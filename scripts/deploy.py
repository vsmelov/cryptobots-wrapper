from brownie import *
from brownie import accounts as _accounts

assert network.show_active() == 'ropsten'  # WARNING: check it
gas_price = int(1.5 * 10**9)  # WARNING: cahnge it or set to None

OLD_BOT_CORE_CONTRACT = '0xF7a6E15dfD5cdD9ef12711Bd757a9b6021ABf643'  # mainnet
baseURI = 'https://path.to/token/'
contractURI = 'https://path.to/contractMetadata/'


def main():
    admin = _accounts.load('testacc0', '12341234')

    usdt = Wrapper.deploy(OLD_BOT_CORE_CONTRACT, baseURI, contractURI, {'from': admin, 'gas_price': gas_price})
    try:
        Wrapper.publish_source(usdt)
    except ValueError as exc:
        if 'Contract source code already verified' not in str(exc):
            raise
