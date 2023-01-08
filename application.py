from aiohttp import web
from aiohttp.client import request


async def chatgpt(request_obj):
  request = await request_obj.json()\
  
  response = {}
  response["version"] = request["version"]
  response["session"] = request["session"]
  response["response"] = {"end_session" : False}
  
  response["response"]["text"] = "Здарова народ"
  response["response"]["end_session"] = True
  
  return web.json_response(response)

def init():
  app = web.Application()
  app.router.add_post("/chatgpt", chatgpt)
  app.run_app(host='46.243.227.153', port=443)
  
if __name__ == "__main__":
  init()
  
  
