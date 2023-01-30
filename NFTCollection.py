import json
import random

collection = {
    "collectionName": "Cuddly Kitties",
    "collectionSize": 5,
    "traits": [{"name": "ears", "values": ["tiny", "big", "sad", "pointy"]},
               {"name": "eyes", "values": ["sad", "bright", "happy", "angry"]},
               {"name": "mouth", "values": ["angry", "sad", "open", "smiling"]}]
}


class NFT:
    def __init__(self, name, attributes):
        self.attributes = attributes
        self.name = name

    def __str__(self):
        return json.dumps({'attributes': self.attributes, 'name': self.name})


def create_nfts(collection):
    nft_collection = []

    def backtracking_function(current_traits, traits_remaining):
        if not traits_remaining:
            nft_collection.append(NFT(collection['collectionName'] + ' #' + str(len(nft_collection)), current_traits))
        else:
            for value in traits_remaining[0]['values']:
                backtracking_function(current_traits + [{'trait_type': traits_remaining[0]['name'], 'value': value}],
                                      traits_remaining[1:])

    backtracking_function([], collection['traits'])
    return nft_collection


def create_random_nfts(collection):
    nft_collection = []
    trait_dictionary = {}

    def check_existence(current_traits):
        trait_cursor = trait_dictionary
        for trait in current_traits:
            if trait['value'] not in trait_cursor:
                return False
            trait_cursor = trait_cursor[trait['value']]
        return True

    def add_new_traits(current_traits):
        trait_cursor = trait_dictionary
        for trait in current_traits:
            if trait['value'] not in trait_cursor:
                trait_cursor[trait['value']] = {}
            trait_cursor = trait_cursor[trait['value']]

    def create_random_backtracking(current_traits, traits_remaining):
        if not traits_remaining:
            if not check_existence(current_traits):
                nft_collection.append(
                    NFT(collection['collectionName'] + ' #' + str(len(nft_collection)), current_traits))
                add_new_traits(current_traits)
        else:
            create_random_backtracking(current_traits +
                                       [
                                           {
                                               'trait_type': traits_remaining[0]['name'],
                                               'value': random.choice(traits_remaining[0]['values'])
                                           }
                                       ],
                                       traits_remaining[1:])

    while len(nft_collection) < collection['collectionSize']:
        create_random_backtracking([], collection['traits'])
    return nft_collection


for nft in create_random_nfts(collection):
    print(nft)
