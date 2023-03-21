# StupidGPT

You've seen [openai/gpt-2](https://github.com/openai/gpt-2).

You've seen [karpathy/minGPT](https://github.com/karpathy/mingpt).

You've also seen [karpathy/nanoGPT](https://github.com/karpathy/nanogpt)!

You've even seen [picoGPT](https://github.com/jaymody/picoGPT)!!

But you probably don't want to see [stupidGPT](https://github.com/WAUthethird/stupidGPT)...

`stupidGPT` is exactly what it sounds like: a really stupid WIP partial rewrite of the (unlike this project) excellent and well-written [picoGPT](https://github.com/jaymody/picoGPT).
What makes it so stupid?
Well...

stupidGPT "features":
* NumPy? ❌ Nope! I'm working to rip it out completely. This project is a pure Python implementation.
* Fast? ❌ Couldn't be further from the truth. Right now, stupidGPT takes around 1 minute per token, and I expect it to get far slower as I replace more NumPy functions with my own.
* Usable? ✅ Technically, yes! I've made sure to keep it fully functional as I replace NumPy functions with my own. But I wouldn't consider it usable in any other sense of the word.
* Training code? ❌ Error, 4️⃣0️⃣4️⃣ not found
* Batch inference? ❌ stupidGPT is civilized, single file line, one at a time only
* top-p sampling? ❌ top-k? ❌ temperature? ❌ categorical sampling?! ❌ greedy? ✅
* Readable? ❌ No.
* Smol??? ❌ HAHA NO


## Why?

I want to fundamentally understand the underlying mathematics behind GPT, which means I'm going without the luxury of NumPy abstraction. I generally learn that sort of thing better this way.

Unfortunately for you, that means this is the last option you should consider for GPT-2 inference. But who knows, maybe you might learn something too?
