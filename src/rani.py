doc_valid_1 = {
    '_id': '13353203000103',
    'deliveryAddress': {
        'addressLine1': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ',
        'city': 'WzySDmSq9ppSJIGeKh7wGg==',
        'state': 'uI3HkGtpSFXFLuU97b3fqQ==',
        'zipcode': 'qv6UhbfMczu69b/fYHeLrQ==',
        'latitude': 'MY/v4xUiJhlEedJVJSZGew==',
        'longitude': '7SMA9jdOcynfWIAO4Ai7BA==',
        'lines': [
            {
                'type': 'THOROUGHFARE',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            },
            {
                'type': 'NEIGHBORHOOD',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            },
            {
                'type': 'NUMBER',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            }
        ]
    }
}

doc_valid_2 = {
    '_id': '13353203000103',
    'deliveryAddress': {
        'addressLine1': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ',
        'city': 'WzySDmSq9ppSJIGeKh7wGg==',
        'state': 'uI3HkGtpSFXFLuU97b3fqQ==',
        'zipcode': 'qv6UhbfMczu69b/fYHeLrQ==',
        'latitude': 'MY/v4xUiJhlEedJVJSZGew==',
        'longitude': '7SMA9jdOcynfWIAO4Ai7BA==',
        'lines': [
            {
                'type': 'THOROUGHFARE',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            },
            {
                'type': 'NEIGHBORHOOD',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            },
            {
                'type': 'NUMBER',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            },
            {
                'type': 'ANYTHING',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            }

        ]
    }
}

doc_invalid_1 = {
    '_id': '13353203000103',
    'deliveryAddress': {
        'addressLine1': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ',
        'city': 'WzySDmSq9ppSJIGeKh7wGg==',
        'state': 'uI3HkGtpSFXFLuU97b3fqQ==',
        'zipcode': 'qv6UhbfMczu69b/fYHeLrQ==',
        'latitude': 'MY/v4xUiJhlEedJVJSZGew==',
        'longitude': '7SMA9jdOcynfWIAO4Ai7BA==',
        'lines': [
            {
                'type': 'THOROUGHFARE',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            }
        ]
    }
}

doc_invalid_2 = {
    '_id': '13353203000103',
    'deliveryAddress': {
        'addressLine1': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ',
        'city': 'WzySDmSq9ppSJIGeKh7wGg==',
        'state': 'uI3HkGtpSFXFLuU97b3fqQ==',
        'zipcode': 'qv6UhbfMczu69b/fYHeLrQ==',
        'latitude': 'MY/v4xUiJhlEedJVJSZGew==',
        'longitude': '7SMA9jdOcynfWIAO4Ai7BA==',
        'lines': [
            {
                'type': 'THOROUGHFARE',
                'value': 'ki75nYjt7BflmHtv436OolzBMZhdJ974H+BWjpnCY3MZO7met+54hPISvZDAIXzQ'
            },
            {
                'type': 'NEIGHBORHOOD',
                'value': ''
            },
            {
                'type': 'NUMBER',
                'value': ''
            }
        ]
    }
}


def validate_lines(doc):
    required = {'THOROUGHFARE',
                'NEIGHBORHOOD',
                'NUMBER'}
    lines = {line['type']: line['value']
             for line in doc['deliveryAddress']['lines']}
    return required & lines.keys() == required and all(lines.values())


assert validate_lines(doc_valid_1)
assert validate_lines(doc_valid_2)
assert not validate_lines(doc_invalid_1)
assert not validate_lines(doc_invalid_2)
