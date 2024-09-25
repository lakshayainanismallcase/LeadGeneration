import requests, random, json, uuid
from requests import Response

url: str = "https://platform-ecosystem.api.stag.tickertape.in/external/lead"

PARTNER_ID_LIST: dict[str, list[str]] = dict()
#  [QA] = [QA, zomato, cred]
PARTNER_ID_LIST["66f3c8ba040b297930033503"]= ["66e919fff813b2959a31a205",
                                              "66e96ea8c7728d0da672ed11",
                                              "66ea601a4c05c50abff3aba9"]
# [TT_QA] = [merchant1]
PARTNER_ID_LIST["66f3c8ba040b297930033505"]= ["66ebcdd0545db073cb624e20"]
# [TT_QA_PARTNER] = [pm1]
PARTNER_ID_LIST["66f3d0c18397f4ad2ece303d"]= ["66f3d13cc4c049fc53398d58"]

PARTNER_AUTH_DICT: dict[str, str] = {"66f3c8ba040b297930033503": "0hbyI42aghXI4iW3",
                                     "66f3c8ba040b297930033505": "bauOJdNbFpkRGOoW",
                                     "66f3d0c18397f4ad2ece303d":"w04KjGqUPZEUOUst"}

partnerId: str = random.choice(list(PARTNER_ID_LIST.keys()))
# partnerId: str = "66f3d0c18397f4ad2ece303d" #hardcoding partner
merchantId: str = random.choice(PARTNER_ID_LIST[partnerId])
# merchantId: str = "66f3d13cc4c049fc53398d58" #hardcoding merchant
uid: str = uuid.uuid4().hex[:24]


payload: str= json.dumps({
  "uid": f"{uid}",
  "mobile": "+91-9876543213",
  "name": "Lakshaya scriptThree",
  "email": "lakshaya3@script.com",
  "partnerId": f"{partnerId}",
  "type": "GOLDBACK",
  "meta": {
    "amount": 155000,
    "reward": 1000,
    "merchantId": f"{merchantId}"
  }
})

headers:dict[str, str] = {
  'Authorization': f'{PARTNER_AUTH_DICT[partnerId]}',
  'Content-Type': 'application/json'
}

try:
  response: Response = requests.post( url, headers=headers, data=payload)

  print(response.text)
  if response.status_code == 200:
    print(f"Lead created successfully.\nUID:{uid}, partnerId:{partnerId}, merchantId:{merchantId}")
    with open("leads.csv", "a") as f:
      f.write(f"{uid},{partnerId},{merchantId}")
except Exception as e:
  print(e)

# get the deeplink
# https://api-dashboard.stag.tickertape.in/external/partners/leads/deeplink?uid=c483ce8763e9431199d40f90&partnerId=66e91443663aec081fce8f5a
#
deeplink_url =  f"https://api-dashboard.stag.tickertape.in/external/partners/leads/voucher?uid={uid}&partnerId={partnerId}"
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImFjY2VzcyI6eyJwb2xpY2llcyI6WyJkZWZhdWx0Iiwic3RhZyBhZG1pbiIsInN1cHBvcnQiLCJwcm9kdWN0Il0sImlubGluZSI6WyJVU0VSX0RFTEVURSIsIlVTRVJfQlJPS0VSX0RJU0NPTk5FQ1QiLCJBRE1JTl9SRUFEIiwiQURNSU5fV1JJVEUiLCJBTk5PVU5DRU1FTlRfVklFVyIsIkFOTk9VTkNFTUVOVF9XUklURSIsIkRHX09GRkVSX1JFQUQiLCJER19PRkZFUl9XUklURSIsIkZJTFRFUlNfUkVBRCIsIkZJTFRFUlNfVVBEQVRFIiwiSU5URVJOQUxfVVNFUl9DUkVBVEUiLCJJTlZPSUNFU19SRUFEIiwiTEVBUk5fUkVBRCIsIkxFQVJOX1dSSVRFIiwiTURfQ09ORklHX1JFQUQiLCJNRF9DT05GSUdfV1JJVEUiLCJNRF9TVE9DS1NfUkVBRCIsIk1EX1NUT0NLU19XUklURSIsIk1GX1NDUkVFTkVSX1JFQUQiLCJORVdTX1JFQUQiLCJNRl9TQ1JFRU5FUl9XUklURSIsIk5FV1NfV1JJVEUiLCJPRkZFUlNfVklFVyIsIk9GRkVSU19XUklURSIsIlBJQ0tSX0FERF9WT1VDSEVSUyIsIlBJQ0tSX0RJU1FVQUxJRlkiLCJQSUNLUl9ESVNUUklCVVRFX1ZPVUNIRVJTIiwiUElDS1JfTEVBREVSQk9BUkRfV1JJVEUiLCJQSUNLUl9NQUlMX1VTRVJTIiwiUElDS1JfTU9DS19XUklURSIsIlBJQ0tSX1BVQkxJU0giLCJQSUNLUl9SRVNUQVJUIiwiUElDS1JfUFJFVklFVyIsIlBJQ0tSX1ZPVUNIRVJTX0FTU0lHTiIsIlBJQ0tSX1ZPVUNIRVJTX1JFUE9SVCIsIlBPUlRGT0xJT19XSURHRVRfQ09ORklHX0FERCIsIlBPUlRGT0xJT19JTlNJR0hUX1dSSVRFIiwiUE9SVEZPTElPX1dJREdFVF9DT05GSUdfVVBEQVRFIiwiU0NSRUVOU19SRUFEIiwiUE9SVEZPTElPX1dJREdFVF9DT05GSUdfUkVBRCIsIlNDUkVFTlNfV1JJVEUiLCJTR19SRUFEIiwiU0dfV1JJVEUiLCJTT0NJQUxfUkVBRCIsIlNPQ0lBTF9XUklURSIsIlNUT0NLX1dJREdFVF9DT05GSUdfQUREIiwiU1RPQ0tfV0lER0VUX0NPTkZJR19SRUFEIiwiU1RPQ0tfV0lER0VUX0NPTkZJR19VUERBVEUiLCJTVE9SSUVTX1JFQUQiLCJTVE9SSUVTX1dSSVRFIiwiU1VCU0NSSVBUSU9OU19ERUxFVEUiLCJTVUJTQ1JJUFRJT05TX1dSSVRFIiwiU1VCU0NSSVBUSU9OU19SRUFEIiwiVFJBTlNBQ1RJT05TX1JFQUQiLCJUUkFOU0FDVElPTlNfU1lOQyIsIlVTRVJfU1VCU19DQU5DRUwiLCJVU0VSX1NVQlNfRE9XTkdSQURFIiwiVVNFUl9TVUJTX1BST0NFU1NfUkVGVU5EIiwiVVNFUl9TVUJTX1JFQUQiLCJVU0VSX1NVQlNfVVBHUkFERSJdfSwiX2lkIjoiNjRmZWZlNTgzNzMyZDlkNmEzNTZiZDY5IiwidXNlcklkIjoiMTEzMzQ4MjE1Mzc1ODIzMjAyNzE5IiwiX192IjowLCJlbWFpbCI6Imxha3NoYXlhLmluYW5pQHRpY2tlcnRhcGUuaW4iLCJ1c2VybmFtZSI6Ikxha3NoYXlhIEluYW5pIiwidG9rZW4iOiJ5YTI5LmEwQWNNNjEyei1hcVVLbWRWdW5KWVFXdnZmWnhYTmNqYUppd2FpWEM5NXQ2UWtiYkpnV3VYUlBSZktxRlVqS0RrbE9EMnRsR3lVQkpfcHlJRTg3dVVFalRHR3dMVVN3TXdfa3p4WDJwbkdMaHpVQ2dMLTJDMjU3X2JDWHF5OEJ2Sy1CTmhxNlVwdEVMdV85NEZGWWJfdFVfQ3l0NG1rOGRZd0J1eW5hQ2dZS0FjY1NBUkFTRlFIR1gyTWlES3YwMUdfOHpKOGRVUW9US1FRR0RRMDE3MSJ9LCJpYXQiOjE3MjcyNTQzNjUsImV4cCI6MTcyNzM0MDc2NX0.QPSGYOfpZuDx-UHUGcwZYijxkk37PmlzVONYKT8dKfg"

headers = {"accept": "application/json", "Authorization": f"{token}"}

try:
  deeplink_response = requests.get(deeplink_url,headers=headers)
  assert deeplink_response.status_code == 200, f"Failed to get deeplink. Status code: {deeplink_response.status_code}"
  assert deeplink_response.json()["success"] == True, "Failed to get deeplink"
  deeplink: str = deeplink_response.json()["data"]["deeplink"]
  print(deeplink)
  if deeplink_response.status_code == 200:
    with open("leads.csv", "a") as f:
      f.write(f",{deeplink.replace('https', 'ttape')}")
except Exception as e:
  print(e)
finally:
  with open("leads.csv", "a") as f:
    f.write(f"\n")
