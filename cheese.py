def rand_cheese():
    import random
    cheese = ["Red Leicester", "Tilsit", "Caerphilly", "Bel Paese", "Red Windsor", "Stilton", "Emmental", "Gruyère", "Norwegian Jarlsberg", "Liptauer", "Lancashire", "White Stilton", "Danish Blue", "Double Gloucester", "Cheshire", "Dorset Blue Vinney", "Brie", "Roquefort", "Pont lEvêque", "Port Salut", "Savoyard", "Saint-Paulin", "Carré de lEst", "Bresse-Bleu", "Boursin", "Camembert", "Gouda", "Edam", "Caithness", "Smoked Austrian", "Japanese Sage Derby", "Wensleydale", "Greek Feta", "Gorgonzola", "Parmesan", "Mozzarella", "Pipo Crème", "Danish Fynbo", "Czech sheeps milk", "Venezuelan Beaver Cheese", "Cheddar", "Ilchester", "Limburger"]
    randnum = random.randint(0, len(cheese) - 1)
    return cheese[randnum]
