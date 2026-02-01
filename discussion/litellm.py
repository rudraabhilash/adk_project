# LiteLLM removes 40–60% of defensive and provider-specific Python code 
# you would otherwise have to write when using raw OpenAI APIs.

# Capability	         Raw OpenAI	                  LiteLLM
# Minimal call	             ✅	                      ✅
# Retries	                ❌ manual	              ✅ built-in
# Timeout	                ❌ manual	              ✅ built-in
# Multi-provider	        ❌	                      ✅
# Fallback	                ❌	                      ✅
# Streaming	                ✅	                      ✅
# JSON output	            ✅                      	  ✅
# Vendor lock-in	        ❌	                      ✅ avoided



# 1️⃣ Raw OpenAI API (baseline)
# Basic call

from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain reverse proxy"
)

print(resp.output_text)

# ✅ Works
# ❌ OpenAI-only
# ❌ No fallback
# ❌ No retries
# ❌ No cost abstraction

# With retries + timeout (YOU write this)

from openai import OpenAI
import time

client = OpenAI()

for attempt in range(3):
    try:
        resp = client.responses.create(
            model="gpt-4.1-mini",
            input="Explain reverse proxy",
            timeout=10
        )
        print(resp.output_text)
        break
    except Exception as e:
        if attempt == 2:
            raise
        time.sleep(2)

# ⬆️ This is your responsibility with raw API.

# With fallback to another provider ❌
# # Not possible without rewriting logic

# 2️⃣ LiteLLM (same task, less code)
# Minimal LiteLLM call

from litellm import completion

resp = completion(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain reverse proxy"}]
)

print(resp.choices[0].message.content)


# ✅ Same result
# ✅ OpenAI-compatible
# ✅ Shorter code

# 3️⃣ Retries + timeout (BUILT-IN)
from litellm import completion

resp = completion(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain reverse proxy"}],
    timeout=10,
    num_retries=3
)

print(resp.choices[0].message.content)


# ✔ No try/except
# ✔ Cleaner
# ✔ Safer

# 4️⃣ Fallback models (THIS is the killer feature)
# Raw OpenAI ❌ (you can’t)
# You must manually integrate Anthropic, Gemini SDKs

# LiteLLM ✅ (single line)
from litellm import completion

resp = completion(
    model=[
        "gpt-4o-mini",
        "claude-3-5-sonnet",
        "gemini/gemini-1.5-pro"
    ],
    messages=[{"role": "user", "content": "Explain reverse proxy"}]
)

print(resp.choices[0].message.content)


# ✔ Automatic fallback
# ✔ Same interface
# ✔ No provider-specific code

# 5️⃣ Streaming comparison
# Raw OpenAI
from openai import OpenAI

client = OpenAI()

stream = client.responses.stream(
    model="gpt-4.1-mini",
    input="Explain reverse proxy"
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="")

# LiteLLM (same idea)
from litellm import completion

stream = completion(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain reverse proxy"}],
    stream=True
)

for chunk in stream:
    delta = chunk["choices"][0]["delta"]
    if "content" in delta:
        print(delta["content"], end="")

# 6️⃣ JSON-safe backend output
# Raw OpenAI (Responses API)
resp = client.responses.create(
    model="gpt-4.1-mini",
    input="Give pros and cons of Nginx vs Apache in JSON",
    response_format={"type": "json_object"}
)

data = resp.output_parsed

# LiteLLM (same, provider-agnostic)
from litellm import completion
import json

resp = completion(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Give pros and cons of Nginx vs Apache in JSON"}],
    response_format={"type": "json_object"}
)

data = json.loads(resp.choices[0].message.content)

# 7️⃣ Cost & usage visibility (automatic)
# Raw OpenAI
# resp.usage  # OpenAI-specific

# LiteLLM
# resp.usage          # normalized
# resp._hidden_params # cost, provider, model metadata


# ✔ Same shape across providers
