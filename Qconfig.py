# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal 
# access token. Replace "None" below with the quoted token string.
# Uncomment the APItoken variable, and you will be ready to go.

APItoken = "8e9af609f4036a929082fa3b082b4ca966215be4b20529a889ac6ec044baa5c640d89a7440041f3fbea7c147045ab5c8cf7035b234af8cd3d3926e1f1968946b"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
  raise Exception("Please set up your access token. See Qconfig.py.")
