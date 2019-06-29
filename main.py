from splitwise import Splitwise

#Splitwise.setDebug(True)
localCache = {}

spltwse = Splitwise("85II34WnFVbML5RNNdabV0qgcH0zUfPUoPiTJ8rT", "DBTBYa6MQj5lRiGy3eWpA8FLcvIQxAVtCPkg1Uvf")

localCache['secret'] = 'ekeZwpnTr4dd6dokLPbplzOga7F1qpU5Oeh9fW7H'
oauth_token = 'Lam8CxsPofWmLw9ckA3vymGt5EFpCrvcYDTGM178'
oauth_verifier = 'YQGRC63z7fLnijecf0xa'
access_token = spltwse.getAccessToken(oauth_token, localCache['secret'], oauth_verifier)

localCache['access_token'] = access_token
spltwse.setAccessToken(localCache['access_token'])
for frnd in spltwse.getFriends():
	print(frnd.getId(), frnd.getFirstName(), frnd.getLastName())

