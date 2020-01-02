def hash_matches(datetime, signing_secret):
    return datetime + signing_secret == '01/01/2020blah'
