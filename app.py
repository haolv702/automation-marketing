from sanic import response
from sanic import Sanic
import tweepy
import os
from datetime import datetime, timedelta
from sanic.response import text
from urllib.parse import urlparse, urlencode
from pymongo import MongoClient



app = Sanic(__name__)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
CALLBACK_URL = "http://192.168.0.123:8000/login"

client = MongoClient('mongodb://localhost:27017')  
# client = MongoClient('mongodb://cdpDBReader:cdp_db_reader_t44KgbvepBNIFFbW@35.198.222.97:27017,34.124.133.164:27017,34.124.205.24:27017/') 
database = client['cdp_database']
web2_actions_v2 = database['web2_actions_v2']
users_v2 = database['users_v2']
actions_v2 = database['actions_v2']
campaigns = database['campaigns']

@app.route("/generate-url", methods={'POST'})
async def generate_url(request):
    try:
        data = request.json
        original_url = data.get('url', '')
        
        utm_source = data.get('utmSource')
        utm_medium = data.get('utmMedium')
        utm_campaign = data.get('utmCampaign')

        parsed_url = urlparse(original_url)

        query_params = dict(x.split('=') for x in parsed_url.query.split('&')) if parsed_url.query else {}

        query_params.update({
            'utm_source': utm_source,
            'utm_medium': utm_medium,
            'utm_campaign': utm_campaign
        })

        parsed_url = parsed_url._replace(query=urlencode(query_params))

        modified_url = parsed_url.geturl()

        return text(modified_url)
    except Exception as e:
        return text(f"Error: {str(e)}")

@app.route("/overview-chart", methods={'GET'})
async def overview_chart(request):
    start_timestamp = request.args.get('start')
    end_timestamp = request.args.get('end')

    campaign_list = campaigns.find({},{"_id": 0, "setup_campaign":1})
    month1 = get_one_months_ago_timestamp()
    history = {}
    actions = {
        'track_wallet_address_count': 0, 
        'page_view_count': 0, 
        'user_count': 0, 
        'transaction_count': 0
    }
    transactions = 0

    for campaign in campaign_list:
        setup_campaign = campaign.get("setup_campaign", {})
        campaign_name = setup_campaign.get("name")
        # print(campaign_name)

        list_user = get_user_in_campaign(campaign_name, month1)
        # print(len(list_user))

        history_actions, count_actions = count_user_action_by_day(list_user, month1)
        # print(count_actions)
        history_transactions, count_transactions = count_user_transaction(list_user, month1)

        for timestamp in history_actions.keys():
            if timestamp not in history:
                history[timestamp] = {
                    'track_wallet_address_count': 0,
                    'page_view_count': 0,
                    'user_count': 0,
                    'transaction_count': 0
                }
            history_actions[timestamp].update(history_transactions[timestamp])

            history[timestamp]['track_wallet_address_count'] += history_actions[timestamp]['track_wallet_address_count']
            history[timestamp]['page_view_count'] += history_actions[timestamp]['page_view_count']
            history[timestamp]['user_count'] += history_actions[timestamp]['user_count']
            history[timestamp]['transaction_count'] += history_transactions[timestamp]['transaction_count']

        actions['track_wallet_address_count'] += count_actions['track_wallet_address_count']
        actions['page_view_count'] += count_actions['page_view_count']
        actions['user_count'] += count_actions['user_count']

        transactions += count_transactions

    info = {
        "cost": "1000$",
        "visits": actions['page_view_count'],
        "connectWallets": actions['track_wallet_address_count'],
        "transactions": transactions,
        "history": history
    }
    
    return response.json(info)

@app.route("/overview-table", methods={'GET'})
async def overview_table(request):

    ##TODO 
    info = [
        {
        "campaign": "Campaign Name 1",
        "goals": "Visit page",
        "progress": "65%",
        "visits": 1648,
        "connectWallet": 658,
        "conversion" : "12%",
        "status": "Complete"
        },
        {
        "campaign": "Campaign Name 2",
        "goals": "Connect wallet",
        "progress": "65%",
        "visits": 1648,
        "connectWallet": 658,
        "conversion" : "15%",
        "status": "In progress"
        }
    ]
    return response.json(info)

@app.route("/campaign-info/<id>", methods={'GET'})
async def campaign_info(request, id):

    ##TODO 
    info = {
        "spend": "1000$",
        "budget": "5000$",
        "clicks": 12423,
        "costPerClick": "0,001$",
        "visits": 9654,
        "costPerVisit": "0,015$",
        "connectWallet": 543,
        "conversion": "14%",
        "objective":{
            "goal": "contract interaction",
            "kpi": 5000
        }
    }
    return response.json(info)

@app.route("/campaign-chart/<id>", methods={'GET'})
async def campaign_chart(request, id):
    start_timestamp = request.args.get('start')
    end_timestamp = request.args.get('end')

    # TODO: Use start_date and end_date parameters as needed in your logic
    info = {
        "visits": 15231,
        "connectWallets": 1000,
        "transactions": 1648,
        "history": {
            1707696000: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1707782400: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1707868800: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1707955200: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708041600: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708128000: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708214400: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708300800: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708387200: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708473600: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708560000: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708646400: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708732800: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708819200: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708905600: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708992000: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709078400: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709164800: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709251200: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709337600: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709424000: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709510400: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709596800: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709683200: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709769600: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709856000: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709942400: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1710028800: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1710115200: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1710201600: {
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            }
        },
        "start":start_timestamp,
        "end": end_timestamp 
    }
    return response.json(info)

@app.route("/campaign-funnel/<id>", methods={'GET'})
async def campaign_funnel(request, id):

    ##TODO 
    info = {
        "clicks": {
            "total": 12423
        },
        "visits": {
            "total" :9654,
            "percent": "5%"
            },
        "connectWallets": {
            "total" :543,
            "percent": "15%"
            },
        "transaction": {
            "total" :232,
            "percent": "45%"
            },
        "conversion": "14%"
    }
    return response.json(info)

@app.route("/login", methods={"GET"})
async def auth(request):
    # Khởi tạo OAuth1UserHandler với callback_url
    oauth1_user_handler = tweepy.OAuth1UserHandler(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        callback=CALLBACK_URL
    )
    # Lấy URL xác thực từ Twitter
    auth_url = oauth1_user_handler.get_authorization_url(signin_with_twitter=True)  
    return response.text(auth_url)

@app.route("/login", methods={"POST"})
async def save_access_token(request):
    body = request.json
    oauth_verifier = body.get("oauth_verifier")
    oauth1_user_handler = tweepy.OAuth1UserHandler(
        CONSUMER_KEY,
        CONSUMER_SECRET
    )
    access_token, access_token_secret = oauth1_user_handler.get_access_token(oauth_verifier)
    # Trả về access token và access token secret cho người dùng
    return response.json({"accessToken": access_token, "accessTokenSecret": access_token_secret})

@app.route("/campaigns", methods={"POST"})
async def create_campaign(request):
    body = """
    {
        "setup_campaign": {
            "name": "twitter_marketing",
            "description": "Twitter campaign for increasing customer engagement",
            "start": "2023-03-14T00:00:00",
            "end": "2023-03-20T00:00:00",
            "objective": {
                "goal": "Contract Interaction",
                "kpi": 100,
                "contractAddress": ["0xfd5840cd36d94d7229439859c0112a4185bc0255", "0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63"]
            }
        },
        "audience": {
            "audienceName": "Lead",
            "filterConditions": {
                "smartContracts": ["0xfd5840cd36d94d7229439859c0112a4185bc0255", "0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63"],
                "tokens": ["0xb38d8ab02d378d5a6738b94f2a0b07dd33bf3c4a", "0xfb6115445bff7b52feb98650c87f44907e58f802"],
                "lastOnChainActivityAfter": "2023-01-04T00:00:00"
            } 
        }
    }
    """
    return response.json({"message": "Create successfully"})

@app.route("campaigns/<id:str>/posts", methods={"POST"})
async def create_post(request, id: str):
    input = {
        "content": "Hello",
        "medias": ["@url1", "@url2", "@url3"], # links of images
        "send": True or False,
        "scheduleAt": "2024-03-12T21:20:00"
    }

    send = True
    if send:
        return response.json({"message": "send successfully"})
    else:
        return response.json({"message": "schedule successfully"})
    
@app.route("campaigns/<id:str>/airdrops", methods={"POST"})
async def reward_airdrops(request, id: str):
    input = {
        "totalAmount": 50,
        "token": "0xb38d8ab02d378d5a6738b94f2a0b07dd33bf3c4a",
        "receivers": "from_file",
        "rewardBy": "ranking",
        "first": {
            "number": 2,
            "amount": 5
        },"second": {
            "number": 5,
            "amount": 2
        },"third": {
            "number": 10,
            "amount": 1
        },"special": {
            "number": 1,
            "amount": 10
        }
    } 
    return response.json({"message": "schedule successfully"})
    
@app.route("campaigns/<id:str>/actions", methods={"GET"})
async def get_campaign_actions(request, id: str):
    return response.json({
        "tweet1": {
            "content": "Hello",
            "medias": ["@url1", "@url2", "@url3"],
            "postAt": "2024-03-12T21:20:00"
        },
        "airdrop1": {
            "winner":[
                {
                    "walletAddress": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 10,
                    "token": "Trava"
                },
                {
                    "walletAddress": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "first",
                    "amount": 5,
                    "token": "Trava"
                },{
                    "walletAddress": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 2,
                    "token": "Trava"
                },{
                    "walletAddress": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 1,
                    "token": "Trava"
                },{
                    "walletAddress": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 0.15,
                    "token": "Trava"
                },
            ],
            "time": "2024-03-03"
        },
        "airdrop1": {
            "winner":[
                {
                    "walletAddress": "0xjdhouwfhf8jkc783ktr8vj9u90ur",
                    "position": "special",
                    "amount": 20,
                    "token": "Trava"
                },
                {
                    "walletAddress": "0xjdhouwfhf8joivjtr8v6yuj9u90ur",
                    "position": "first",
                    "amount": 10,
                    "token": "Trava"
                },{
                    "walletAddress": "0xjdhouwfhf8jo7gdduivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 5,
                    "token": "Trava"
                },{
                    "walletAddress": "0xjdhouwfhf8joivvfjtr8vj9u90ur",
                    "position": "special",
                    "amount": 2,
                    "token": "Trava"
                },{
                    "walletAddress": "0xjdhox98uwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 0.25,
                    "token": "Trava"
                },
            ],
            "time": "2023-12-12"
        }
    })

@app.route('/')
async def index(request):
    return text("Hello, this is your Sanic server!")

def get_one_months_ago_timestamp():
    one_month_ago = datetime.now() - timedelta(days=29)
    format = datetime(one_month_ago.year, one_month_ago.month, one_month_ago.day, 0, 0, 0)
    return int(format.timestamp() + 7*3600)

def get_user_in_campaign(name, start):
    users = web2_actions_v2.find()
    matching_users = []
    for user in users:
        sessions = user.get("actions", {})
        for session_timestamp, session in sessions.items():
            if int(session_timestamp) < start:
                continue

            for action_timestamp, action in session.items():
                campaign_info = action.get("campaign_info", {})
                if campaign_info.get("name") == name:
                    matching_users.append(user)
                    break
            break
    return matching_users

def count_user_action_by_day(users, start):
    # Tính toán mốc timestamp của ngày hiện tại
    current_date = datetime.now()
    current_date_timestamp = int(current_date.timestamp())

    # Tạo danh sách các ngày từ start đến ngày hiện tại
    days_list = range(start, current_date_timestamp, 86400)

    # Khởi tạo dict với tất cả các ngày và giá trị mặc định là 0
    action_count_by_day = {day: {
        "track_wallet_address_count": 0,
        "page_view_count": 0,
        "user_count": 0 
    } for day in days_list}

    action_count_user = {
        "track_wallet_address_count": 0,
        "page_view_count": 0,
        "user_count": len(users)
    }

    unique_users = set()

    for user in users:
        user_id = user.get("user")
        sessions = user.get("actions", {})
        for session_timestamp, session in sessions.items():
            session_date = int(session_timestamp) // 86400 * 86400  

            if session_date < start:
                continue

            unique_actions_in_session = set()

            for action_timestamp, action_info in session.items():
                action = action_info.get("action")

                if action not in unique_actions_in_session:
                    unique_actions_in_session.add(action)

                    if action == "track_wallet_address":
                        action_count_by_day[session_date]["track_wallet_address_count"] += 1
                        action_count_user["track_wallet_address_count"] += 1
                    elif action == "page_view":
                        action_count_by_day[session_date]["page_view_count"] += 1
                        action_count_user["page_view_count"] += 1

            if user_id not in unique_users:
                action_count_by_day[session_date]["user_count"] += 1
                unique_users.add(user_id)

    return action_count_by_day, action_count_user

def count_user_transaction(users, start):
    user_ids = [user["_id"] for user in users]
    filtered_users = list(users_v2.find({"_id": {"$in": user_ids}}, {"_id": 0, "address": 1}))

    user_addresses = [user["address"] for user in filtered_users if "address" in user]

    user_have_transaction = list(actions_v2.find({"address": {"$in": user_addresses}}, {"actions": 1}))

    # transaction_counts = {}
    current_date = datetime.now()
    current_date_timestamp = int(current_date.timestamp())
    days_list = range(start, current_date_timestamp, 86400)

    transaction_count_by_day = {day: {"transaction_count": 0} for day in days_list}
    transaction_count = 0
    for user in user_have_transaction:
        actions = user.get("actions", {})
        # user_id = user.get("_id", "")
        # transaction_counts.setdefault(user_id, 0)

        for session_timestamp, session in actions.items():
            session_date = int(session_timestamp) // 86400 * 86400

            if int(session_timestamp) < start:
                continue

            # transaction_counts[user_id] += len(session)
            transaction_count_by_day[session_date]["transaction_count"] += len(session)
            transaction_count += len(session)

    return transaction_count_by_day, transaction_count

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
