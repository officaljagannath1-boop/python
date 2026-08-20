# create an speaker using the eleven labs api using requests library
# api of eleven labs 'sk_efc26a32fa818563de8cd52ebc5a669f9e932d3482ba7b27'
from elevenlabs.client import ElevenLabs

client = ElevenLabs(api_key="sk_efc26a32fa818563de8cd52ebc5a669f9e932d3482ba7b27")

# Get raw response with headers
response = client.text_to_speech.with_raw_response.convert(
    text="Hello, world!",
    voice_id="voice_id"
)

# Access character cost from headers
char_cost = response.headers.get("character-cost")

# Optionally store these for debugging
request_id = response.headers.get("request-id")
trace_id = response.headers.get("x-trace-id")

audio_data = response.data

 




