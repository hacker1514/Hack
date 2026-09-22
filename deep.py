import requests
import json

url = "https://api.deepai.org/hacking_is_a_serious_crime"

sp1 = """------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="chat_style"

chat
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="language"

en
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="chatHistory"

"""

context = []

sp2 = """------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="model"

standard
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="session_uuid"

a51f1ca6-1bfb-457e-82fb-7eba515c9b0e
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="sensitivity_request_id"

7c869c6b-430d-4224-865e-233b0a55ec9c
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="tool_activity_support"

1
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="thinking_image_tool_support"

1
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="hacker_is_stinky"

very_stinky
------WebKitFormBoundary7L3oBhqb57pBpfSF
Content-Disposition: form-data; name="enabled_tools"

["image_generator","image_editor"]
------WebKitFormBoundary7L3oBhqb57pBpfSF--"""

while True :
    try:
        user = input("You : ")
    except:
        print()
        break
    context.append({"role":"user","content":user})
    raw_payload = sp1+json.dumps(context)+sp2
    body_bytes = raw_payload.replace("\n", "\r\n").encode("utf-8")
    headers = {
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7L3oBhqb57pBpfSF"
    }
    response = requests.post(url, data=body_bytes, headers=headers)
    ai = response.text
    context.append({"role":"assistant","content":ai})
    print("Ai  : ",ai)
["image_generator","image_editor"]
------WebKitFormBoundary7L3oBhqb57pBpfSF--"""
