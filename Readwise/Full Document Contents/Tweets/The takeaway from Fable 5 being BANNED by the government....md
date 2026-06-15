# The takeaway from Fable 5 being BANNED by the government:...

![rw-book-cover](https://pbs.twimg.com/profile_images/1577116785656139776/5mi0qgTz.jpg)

## Metadata
- Author: [[GREG ISENBERG]]
- Full Title: The takeaway from Fable 5 being BANNED by the government:...
- Category: #tweets
- Summary: The takeaway from Fable 5 being BANNED by the government: GET GOOD AT LOCAL MODELS SO YOU HAVE 100% CONTROL. 

My entire weekend was going to be building my craziest ideas with Fable 5. That's now cancelled.

So instead of building with Fable this weekend, I've decided I'll go deep on local models:

1. Start with the runtime. Download Ollama or LM Studio first. This is the thing that actually runs models on your machine. 

2. Match the model to your hardware. A model's size is measured in billions of parameters (7B, 32B, 70B). Bigger is smarter but needs more memory. Rule of thumb: a 7B model runs on almost any laptop, a 32B needs a good Mac with 32GB+ RAM, a 70B needs serious hardware like a DGX Spark or a maxed-out Mac Studio.

3. Know which model for which job. Qwen 3 is the best all-around choice for most tasks. DeepSeek for reasoning and coding. Gemma 4 when you need something tiny that runs on a phone. Llama when you want the biggest community and the most fine-tunes.

4. Quantization. You can shrink a model to run on weaker hardware with barely any quality loss. Look for versions labeled Q4 or Q5. This is how a model that "needs" a server runs on your laptop. Learning this one concept changes everything.

5. Connect it to your agent. Point Hermes or your agent stack at a local model.

6. Context window is your real constraint locally. Cloud models give you huge context for free. Local models make you pay for it in memory. A bigger context window eats RAM fast. Keep your sessions tight and your prompts lean or your machine chokes.

7. Learn to give local models tools. A smaller local model with web search, file access, and code execution beats a giant model with none. The capability gap closes fast when you wire up the right tools. The model is the engine but the tools are the wheels.

8. Fine-tuning is more accessible than you think. You don't need this on day one, but know it exists. You can take an open model and train it on your own data so it gets good...
- URL: https://twitter.com/gregisenberg/status/2065773938915889253/?rw_tt_thread=True

## Full Document
The takeaway from Fable 5 being BANNED by the government: GET GOOD AT LOCAL MODELS SO YOU HAVE 100% CONTROL. 

My entire weekend was going to be building my craziest ideas with Fable 5. That's now cancelled.

So instead of building with Fable this weekend, I've decided I'll go deep on local models:

1. Start with the runtime. Download Ollama or LM Studio first. This is the thing that actually runs models on your machine.
2. Match the model to your hardware. A model's size is measured in billions of parameters (7B, 32B, 70B). Bigger is smarter but needs more memory. Rule of thumb: a 7B model runs on almost any laptop, a 32B needs a good Mac with 32GB+ RAM, a 70B needs serious hardware like a DGX Spark or a maxed-out Mac Studio.
3. Know which model for which job. Qwen 3 is the best all-around choice for most tasks. DeepSeek for reasoning and coding. Gemma 4 when you need something tiny that runs on a phone. Llama when you want the biggest community and the most fine-tunes.
4. Quantization. You can shrink a model to run on weaker hardware with barely any quality loss. Look for versions labeled Q4 or Q5. This is how a model that "needs" a server runs on your laptop. Learning this one concept changes everything.
5. Connect it to your agent. Point Hermes or your agent stack at a local model.
6. Context window is your real constraint locally. Cloud models give you huge context for free. Local models make you pay for it in memory. A bigger context window eats RAM fast. Keep your sessions tight and your prompts lean or your machine chokes.
7. Learn to give local models tools. A smaller local model with web search, file access, and code execution beats a giant model with none. The capability gap closes fast when you wire up the right tools. The model is the engine but the tools are the wheels.
8. Fine-tuning is more accessible than you think. You don't need this on day one, but know it exists. You can take an open model and train it on your own data so it gets good at your specific domain.

I'll probably do a breakdown at some point on this [@startupideaspod](https://twitter.com/startupideaspod) if people are into it. 

The lesson from this ban is basically don't build your entire workflow on something that can disappear with a single letter. Own part of your stack. Local models are insurance.

It reminds me when people realized they don't own social media accounts. And then you saw people build email lists etc. 

I remember running a startup and my biggest traffic source was organic FB. All of a sudden, algo changed, and I lost 99% of my traffic.

Same sorta moment (but bigger) for AI.

This is a wake up call.
