def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    out = []
    for person in people:
        name = []
        for val in person.values():
            name.append(val)
        out.append(" ".join(name))
    return out

    #use comprehension
    # return [f"{person["first"]} {person["last"]}" for person in people]