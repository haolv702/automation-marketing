from sanic import response
from sanic import Sanic
import tweepy
import os
from datetime import datetime
from sanic.response import text
from urllib.parse import urlparse, urlencode


app = Sanic(__name__)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
CALLBACK_URL = "http://192.168.0.123:8000/login"

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

    # TODO: Use start_date and end_date parameters as needed in your logic
    info = {
        "cost": "1000$",
        "visits": 15231,
        "connectWallets": 1000,
        "transactions": 1648,
        "history": {
            1707696000: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1707782400: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1707868800: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1707955200: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708041600: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708128000: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708214400: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708300800: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708387200: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708473600: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708560000: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708646400: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708732800: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708819200: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708905600: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1708992000: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709078400: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709164800: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709251200: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709337600: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709424000: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709510400: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709596800: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709683200: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709769600: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709856000: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1709942400: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1710028800: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1710115200: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            },
            1710201600: {
                "click":214,
                "visit":157,
                "connectWallet": 24,
                "transaction": 58
            }
        },
        "start":start_timestamp,
        "end": end_timestamp 
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
