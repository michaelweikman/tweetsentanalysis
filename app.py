import tweepy

auth = tweepy.OAuthHandler("y5kEUkqCvnpKlRQ85c9eZbRMc", "9MokzV6ul6WeM5RoepwfxlQGKFrz9H7rC4zoSIVhjzcQhOgXm9")
auth.set_access_token("45267411-FhzWglS57UHEi1nnOevZ3KNMYYpj283BBGoirgaJa", "bikoa1GJehmW3LVmc7gKbCR153FpB6LtacaLmhFMDKDyj")

api = tweepy.API(auth)
print(api.verify_credentials())


