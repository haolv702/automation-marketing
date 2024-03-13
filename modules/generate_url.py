from sanic import text, json, response
from urllib.parse import urlparse, urlencode
from datetime import datetime


async def generate_url(request):
    try:
        # Lấy dữ liệu từ phần thân của request
        data = request.json
        original_url = data.get('url', '')
        
        utm_source = data.get('utm_source')
        utm_medium = data.get('utm_medium')
        utm_campaign = data.get('utm_campaign')

        # Parse the input URL
        parsed_url = urlparse(original_url)

        # Extract existing query parameters
        query_params = dict(x.split('=') for x in parsed_url.query.split('&')) if parsed_url.query else {}

        # Add or update utm parameters
        query_params.update({
            'utm_source': utm_source,
            'utm_medium': utm_medium,
            'utm_campaign': utm_campaign
        })

        # Update the query parameters in the URL
        parsed_url = parsed_url._replace(query=urlencode(query_params))

        # Reconstruct the modified URL
        modified_url = parsed_url.geturl()

        return text(modified_url)
    except Exception as e:
        return text(f"Error: {str(e)}")
    
async def overview_chart(request):
    start_timestamp = request.args.get('start')
    end_timestamp = request.args.get('end')

    # TODO: Use start_date and end_date parameters as needed in your logic
    info = {
        "cost": "1000$",
        "visits": 15231,
        "connect_wallet": 1000,
        "transaction": 1648,
        "history": {
            1707696000: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1707782400: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1707868800: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1707955200: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708041600: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708128000: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708214400: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708300800: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708387200: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708473600: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708560000: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708646400: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708732800: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708819200: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708905600: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708992000: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709078400: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709164800: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709251200: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709337600: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709424000: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709510400: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709596800: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709683200: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709769600: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709856000: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709942400: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1710028800: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1710115200: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1710201600: {
                "click":214,
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            }
        },
        "start":start_timestamp,
        "end": end_timestamp 
    }
    return response.json(info)

async def overview_table(request):

    ##TODO 
    info = [
        {
        "campaign": "Campaign Name 1",
        "goals": "Visit page",
        "progress": "65%",
        "visits": 1648,
        "connect_wallet": 658,
        "conversion" : "12%",
        "status": "Complete"
        },
        {
        "campaign": "Campaign Name 2",
        "goals": "Connect wallet",
        "progress": "65%",
        "visits": 1648,
        "connect_wallet": 658,
        "conversion" : "15%",
        "status": "In progress"
        }
    ]
    return response.json(info)

async def campaign_info(request, id):

    ##TODO 
    info = {
        "spend": "1000$",
        "budget": "5000$",
        "clicks": 12423,
        "cost_per_click": "0,001$",
        "visits": 9654,
        "cost_per_visit": "0,015$",
        "connect_wallet": 543,
        "conversion": "14%",
        "objective":{
            "goal": "contract interaction",
            "kpi": 5000
        }
    }
    return response.json(info)

async def campaign_chart(request, id):
    start_timestamp = request.args.get('start')
    end_timestamp = request.args.get('end')

    # TODO: Use start_date and end_date parameters as needed in your logic
    info = {
        "visits": 15231,
        "connect_wallet": 1000,
        "transaction": 1648,
        "history": {
            1707696000: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1707782400: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1707868800: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1707955200: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708041600: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708128000: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708214400: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708300800: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708387200: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708473600: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708560000: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708646400: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708732800: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708819200: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708905600: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1708992000: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709078400: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709164800: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709251200: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709337600: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709424000: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709510400: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709596800: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709683200: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709769600: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709856000: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1709942400: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1710028800: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1710115200: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            },
            1710201600: {
                "visit":157,
                "connect_wallet": 24,
                "transaction": 58
            }
        },
        "start":start_timestamp,
        "end": end_timestamp 
    }
    return response.json(info)

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
        "connect_wallet": {
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