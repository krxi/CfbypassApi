from fastapi import FastAPI,Header
from typing import Annotated
import subprocess
import json
import ast

app = FastAPI()


@app.get("/{proxy}&{url}")
async def root(proxy,url,user_agent: Annotated[str | None, Header()] = None):
    print(url + " " + proxy)
    proxyes = "http://" + proxy
    urls = "https://"+ url
    print(proxyes + " " + urls)
    cmd = "py cfbypass.py -v -p="+proxyes+" -ua=\""+user_agent+"\" -f cookies.json "+urls
    print(cmd)
    result = subprocess.getoutput(cmd)
    print(result)
    js = ast.literal_eval(json.dumps(result))
    return result
 