<p align="center">
</p>

<img width="1024" height="1024" alt="shield50" src="https://github.com/user-attachments/assets/c7c0a2df-6705-4f2e-a8ae-d5abfcb78958" />

![S50](https://capsule-render.vercel.app/api?type=venom&height=300&color=gradient&text=Shield%2050&animation=fadeIn&fontAlign=50&fontSize=110&reversal=false&section=header&fontColor=ffffff)

Sword is a comphrensive collection of 50 methods to safeguard against prompt injections

## **Training-Time Defenses**

**1. StruQ: Defending Against Prompt Injection with Structured Queries**
Separates prompts and data using special delimiters and structured instruction tuning.
https://arxiv.org/abs/2402.06363

**2. SecAlign: Defending Against Prompt Injection with Preference Optimization**
Preference optimization reducing ASR to <10%.
https://arxiv.org/abs/2410.05451

**3. Jatmo: Prompt Injection Defense by Task-Specific Finetuning**
Task-specific fine-tuning without instruction-following.
https://arxiv.org/abs/2311.09579

**4. The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions**
Hierarchical instruction processing.
https://arxiv.org/abs/2404.13208

**5. Defending Against Prompt Injection With a Few DefensiveTokens**
Test-time defense with optimized tokens.
https://arxiv.org/abs/2507.07974

**6. Direct Preference Optimization**
Foundation for preference-based alignment.
https://arxiv.org/abs/2305.18290

**7. ReasAlign: Reasoning Enhanced Safety Alignment**
Reasoning-based safety alignment.
https://arxiv.org/abs/2601.10173

**8. SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks**
Randomized smoothing defense.
https://arxiv.org/abs/2310.03684

**9. Baseline Defenses for Adversarial Attacks Against Aligned Language Models**
Comprehensive baseline defense techniques.
https://arxiv.org/abs/2309.00614

**10. Jailbroken: How Does LLM Safety Training Fail?**
Analysis of safety training failure modes.
Reference: https://arxiv.org/abs/2307.02483

**11. Constitutional AI: Harmlessness from AI Feedback**
AI feedback for harmlessness alignment.
Reference: https://arxiv.org/abs/2212.08073

**12. Training Language Models to Follow Instructions with Human Feedback**
Original RLHF/InstructGPT paper.
Reference: https://arxiv.org/abs/2203.02155

**13. Llama Guard: LLM-based Input-Output Safeguard**
LLM-based safety classifier.
Reference: https://arxiv.org/abs/2312.06674

**14. Defending Large Language Models via Semantic Smoothing**
Semantic-level smoothing defense.
Reference: https://arxiv.org/abs/2402.16192

**15. Circuit Breakers: LLM Safety through Adaptive Learning**
Representation-level safety interventions.
Reference: https://arxiv.org/abs/2406.04313

## **Detection & System-Level Defenses**

**16. Defeating Prompt Injections by Design (CaMeL)**
Capability-based provably secure architecture.
https://arxiv.org/abs/2503.18813

**17. Prompt Fencing: A Cryptographic Approach**
Cryptographic authentication of prompt segments.
https://arxiv.org/abs/2511.19727

**18. Defense Against Indirect Prompt Injection via Tool Result Parsing**
Tool output parsing and validation.
https://arxiv.org/abs/2601.04795

**19. Securing AI Agents Against Prompt Injection Attacks**
Multi-layered RAG defense framework.
https://arxiv.org/abs/2511.15759

**20. IntentGuard: Mitigating Indirect Prompt Injection via Intent Analysis**
Intent-based detection at reasoning level.
https://arxiv.org/abs/2512.00966

**21. PromptArmor: LLM-based Detection**
External LLM detector for filtering.
Reference: https://arxiv.org/abs/2512.01174

**22. DataSentinel: Game-Theoretic Detection**
Co-evolutionary game-theoretic approach.
Reference: https://arxiv.org/abs/2503.05738

**23. Spotlighting: Improving Source Distinction**
Prompt engineering for input source distinction.
Reference: https://arxiv.org/abs/2403.14467

**24. SafeDecoding: Safety-Aware Decoding**
Modifies decoding to favor safe outputs.
Reference: https://arxiv.org/abs/2402.08983

**25. Erase-and-Check: Certifiable Safety**
Provable safety guarantees via erasure.
Reference: https://arxiv.org/abs/2309.02705

**26. Robust Prompt Optimization (RPO)**
Adversarially robust prompt optimization.
Reference: https://arxiv.org/abs/2401.17263

**27. The Task Shield: Enforcing Task Alignment**
Task-level verification for agents.
Reference: https://arxiv.org/abs/2502.08734

**28. MELON: Provable Defense via Secret Knowledge**
Honeypot-based provable defense.
Reference: https://arxiv.org/abs/2503.09321

## **Decoding & Generation Defenses**

**29. SafeDecoding: Safety-Aware Decoding**
Modifies decoding to favor safe outputs.
https://arxiv.org/abs/2402.08983

**30. Erase-and-Check: Certifiable Safety**
Provable safety guarantees via erasure.
https://arxiv.org/abs/2309.02705

**31. Robust Prompt Optimization (RPO)**
Adversarially robust prompt optimization.
https://arxiv.org/abs/2401.17263

**32. The Task Shield: Enforcing Task Alignment**
Task-level verification for agents.
https://arxiv.org/abs/2502.08734

**33. MELON: Provable Defense via Secret Knowledge**
Honeypot-based provable defense.
https://arxiv.org/abs/2503.09321

## **Input Preprocessing Defenses**

**34. Paraphrase Defense**
Paraphrasing inputs to remove adversarial modifications.
Part of: https://arxiv.org/abs/2309.00614

**35. Retokenization Defense**
Breaking tokens apart via BPE-dropout.
Part of: https://arxiv.org/abs/2309.00614

**36. Break the Breakout: Self-Refinement Defense**
Iterative self-refinement against jailbreaks.
https://arxiv.org/abs/2402.15180

## **Prompt Engineering Defenses**

**37. Defending Jailbreak Prompts via In-Context Adversarial Game**
Iterative in-context adversarial training.
https://arxiv.org/abs/2402.13148

**38. Intention Analysis Prompting (IAPrompt)**
Analyzing user intent before responding.
Referenced in defense literature

**39. Goal Prioritization Defense**
Prioritizing safety goals over task goals.
https://arxiv.org/abs/2312.06674

## **Knowledge & Representation Defenses**

**40. Defending Large Language Models Against Attacks With Residual Stream Activation Analysis**
Analyzing residual stream activations for defense.
https://arxiv.org/abs/2406.03230

**41. Eraser: Unlearning Harmful Knowledge**
Removing harmful knowledge from models.
Referenced in: https://arxiv.org/abs/2410.15236

**42. LLM Self Defense: By Self Examination, LLMs Know They Are Being Tricked**
Self-examination defense mechanism.
Referenced in defense literature

**43. JBShield: Defending via Activated Concept Analysis and Manipulation**
Concept-level defense mechanism.
https://arxiv.org/abs/2502.07557

**44. Layer-Level Self-Exposure and Patch**
Affirmative token mitigation for defense.
https://arxiv.org/abs/2501.02629

**45. SelfDefend: LLMs Can Defend Themselves in a Practical Manner**
Self-defense mechanisms for LLMs.
https://arxiv.org/abs/2406.05498

## **Multi-Modal & Specialized Defenses**

**46. Defending Jailbreak Attack in VLMs via Cross-modality Information Detector**
Vision-language model defense.
https://arxiv.org/abs/2407.21659

**47. Defending LVLMs Against Vision Attacks through Partial-Perception Supervision**
Large vision-language model defense.
https://arxiv.org/abs/2412.12722

**48. Shaping the Safety Boundaries**
Understanding and defending jailbreak safety boundaries.
https://arxiv.org/abs/2412.17034

**49. ShieldLearner: A New Paradigm for Jailbreak Attack Defense**
Novel defense learning paradigm.
https://arxiv.org/abs/2502.13162

**50. Short-Length Adversarial Training Helps Defend Long-Length Jailbreaks**
Adversarial training approach for defense.
https://arxiv.org/abs/2502.04204
