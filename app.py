from sanic import response
from sanic import Sanic
import tweepy
import os
from datetime import datetime
from sanic.response import text
from modules.generate_url import generate_url, overview_chart, overview_table, campaign_info, campaign_chart, campaign_funnel

app = Sanic(__name__)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
CALLBACK_URL = "http://192.168.0.123:8000/login"

app.add_route(generate_url, '/generate-url', methods=['POST'])
app.add_route(overview_chart, '/overview-chart', methods=['GET'])
app.add_route(overview_table, '/overview-table', methods=['GET'])
app.add_route(campaign_info, '/campaign-info/<id>', methods=['GET'])
app.add_route(campaign_chart, '/campaign-chart/<id>', methods=['GET'])
app.add_route(campaign_funnel, '/campaign-funnel/<id>', methods=['GET'])

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
    return response.json({"access_token": access_token, "access_token_secret": access_token_secret})


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
                "contract_address": ["0xfd5840cd36d94d7229439859c0112a4185bc0255", "0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63"]
            }
        },
        "audience": {
            "audience_name": "Lead",
            "filter_conditions": {
                "smart_contracts": ["0xfd5840cd36d94d7229439859c0112a4185bc0255", "0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63"],
                "tokens": ["0xb38d8ab02d378d5a6738b94f2a0b07dd33bf3c4a", "0xfb6115445bff7b52feb98650c87f44907e58f802"],
                "last_on_chain_activity_after": "2023-01-04T00:00:00"
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
        "schedule_at": "2024-03-12T21:20:00"
    }

    send = True
    if send:
        return response.json({"message": "send successfully"})
    else:
        return response.json({"message": "schedule successfully"})
    

@app.route("campaigns/<id:str>/airdrops", methods={"POST"})
async def reward_airdrops(request, id: str):
    input = {
        "total_amount": 50,
        "token": "0xb38d8ab02d378d5a6738b94f2a0b07dd33bf3c4a",
        "receivers": "from_file",
        "reward_by": "ranking",
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
        "tweet_1": {
            "content": "Hello",
            "medias": ["@url1", "@url2", "@url3"],
            "post_at": "2024-03-12T21:20:00"
        },
        "airdrop_1": {
            "winner":[
                {
                    "wallet_address": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 10,
                    "token": "Trava"
                },
                {
                    "wallet_address": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "first",
                    "amount": 5,
                    "token": "Trava"
                },{
                    "wallet_address": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 2,
                    "token": "Trava"
                },{
                    "wallet_address": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 1,
                    "token": "Trava"
                },{
                    "wallet_address": "0xjdhouwfhf8joivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 0.15,
                    "token": "Trava"
                },
            ],
            "time": "2024-03-03"
        },
        "airdrop_1": {
            "winner":[
                {
                    "wallet_address": "0xjdhouwfhf8jkc783ktr8vj9u90ur",
                    "position": "special",
                    "amount": 20,
                    "token": "Trava"
                },
                {
                    "wallet_address": "0xjdhouwfhf8joivjtr8v6yuj9u90ur",
                    "position": "first",
                    "amount": 10,
                    "token": "Trava"
                },{
                    "wallet_address": "0xjdhouwfhf8jo7gdduivjtr8vj9u90ur",
                    "position": "special",
                    "amount": 5,
                    "token": "Trava"
                },{
                    "wallet_address": "0xjdhouwfhf8joivvfjtr8vj9u90ur",
                    "position": "special",
                    "amount": 2,
                    "token": "Trava"
                },{
                    "wallet_address": "0xjdhox98uwfhf8joivjtr8vj9u90ur",
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
