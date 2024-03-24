from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "gm"}


@app.get("/api/coin/latest/")
async def get_coin_info():
    # TODO: get recently created coin info in live
    token_address = "0xade9bcd4b968ee26bed102dd43a55f6a8c2416df"
    # TODO: get report count from db
    report_count = 0
    img_url = "https://pub-d60ba6e0f7ee441399436bdbb6491f56.r2.dev/doginme_info.png"
    return {"img_url": img_url, "token_address": token_address, "report_count": report_count}


@app.post("/api/coin/{address}/reportRug/")
async def report_rug_coin(address: str):
    # TODO: add row to report table
    return {"success": "true"}


# TODO
def create_image():
    pass


# TODO
def upload_image_to_cloudflare_r2():
    pass
