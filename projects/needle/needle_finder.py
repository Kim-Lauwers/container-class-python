class NeedleFinder:
    @staticmethod
    def find_needle(haystack: list) -> str:
        if not haystack:
            return 'No haystack found'

        needle = 'needle'
        if needle in haystack:
            found = 'found the needle at position '
            found += str(haystack.index(needle))
            return found
        else:
            return 'no needle in the haystack'
