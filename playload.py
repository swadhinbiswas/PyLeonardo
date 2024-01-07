def setplayload():
    #select height
    height=int(input("select height"))
    
    prompt=input("input your imagination")
    width=int(input("input weight"))
    alchemy=str(input("input true or false")).lower()
    controlNet=""
    controlNetType=""
    unzoom="tiling"
    sd_version= "v2",
    scheduler= str(input("input true or false")).lower()
    public= "true"
    promptMagic= "true"
    tiling=""
    
        
    payload = {
        "height": height,
        "modelId": "6bef9f1b-29cb-40c7-b9df-32b51c1f67d3",
        "prompt": prompt,
        "width": width,
        "alchemy": alchemy,
        "controlNet": controlNet,
        "controlNetType": controlNetType,
        "unzoom": unzoom,
        "tiling": tiling,
        "sd_version": sd_version,
        "scheduler": scheduler,
        "public": public,
        "promptMagic": promptMagic,
    }

setplayload()
