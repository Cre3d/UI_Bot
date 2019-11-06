#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function

from bravado.client import SwaggerClient
import bravado.exception

clientid = '272b7988c5f8458b85ce0930d9801f1e'
secretkey = 'xr5R79liS06n4GJZaQxxYOASPytZ4uIqh7dROdbF'



def main():
    client = SwaggerClient.from_url('https://esi.evetech.net/latest/swagger.json')

    characterName = "Darren Luthor"

    charResults = client.Search.get_search(
        search=characterName,
        categories=['character'],
        strict=True,
    ).result()['character']



    if len(charResults) <= 0: raise Exception("Character not found")

    characterId = charResults[0]  # assuming only one result
    charInfo = client.Character.get_characters_character_id(character_id=characterId).result()

    print("Name: %s" % (charInfo['name']))
    print("Gender: %s" % (charInfo['gender']))
    print("id: %s" % (characterId))



if __name__ == "__main__":
    main()