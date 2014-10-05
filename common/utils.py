def normalize(chips, coord_id):
    max_chip = max(chips, key=lambda p: abs(p.get(coord_id))).get(coord_id)

    def chip_fun(chip):
        if coord_id == 0:
            chip.x /= max_chip
        else:
            chip.y /= max_chip
        return chip
    return list(map(chip_fun, chips))