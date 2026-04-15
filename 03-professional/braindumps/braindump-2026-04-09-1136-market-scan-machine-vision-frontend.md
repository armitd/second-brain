---
type: "braindump"
domain: "professional"
date: "2026-04-09"
created: "2026-04-09 11:36"
themes: ["market-scan", "machine-vision", "AI", "front-end-development", "vendor-research", "build-vs-buy", "damage-assessment", "custom-build"]
tags: ["#braindump", "#professional", "#market-scan", "#machine-vision", "#AI", "#vendor-research", "#damage-assessment", "#custom-build"]
status: "consolidated"
consolidated_in: "consolidation-2026-04-15"
energy_level: "medium"
emotional_tone: "investigative"
confidence: "medium"
---

# Braindump: Market Scan — AI Machine Vision + Customer-Facing Front-End Companies

## Raw Thoughts
Need to do a market scan of AI machine vision + front-end development companies. Two distinct categories:
1. Companies that can build **customer-facing front-end applications**
2. Companies that can build **machine vision solutions**

**Clarification (captured same session):**
- Use case = **damage assessment** — customer photographs damage, AI assesses it
- **Not** interested in buying an off-the-shelf glass damage product (e.g. Tractable, Ravin.ai)
- Interested in **building a solution from scratch** — understanding all vendor types that could contribute
- Scope: all types of vendor that could help build a custom AI damage assessment solution, not glass-specific

---

## Content Analysis

### Main Themes
1. **Vendor landscape mapping:** Understanding who exists in both markets — not to make a decision yet, but to know the space
2. **Two distinct capability types:** Front-end development (UX/UI, customer experience, web/mobile apps) and machine vision (AI/CV models, image processing, object detection, damage assessment) are different disciplines — some vendors do both, most specialise in one
3. **Likely Belron application context:** The combination of "customer-facing" + "machine vision" in a windscreen repair/replace business points strongly toward one or more of: damage assessment via photo upload, ADAS calibration verification, technician inspection tooling, or a customer self-service app

### Questions Raised
- What is the specific use case driving this? (Damage assessment? Customer photo upload? Technician inspection? ADAS verification?) — the answer shapes which vendors are relevant
- Is this a procurement exercise (choosing a vendor to build something specific) or early-stage intelligence gathering (understanding what's possible)?
- Geographic scope of the scan — UK, Europe, global?
- Build vs. buy: are we looking for a company to build something bespoke, or a product/platform to configure?
- What budget range / scale of engagement is anticipated?

---

## Building From Scratch — The Full Vendor Ecosystem

When building a custom AI damage assessment solution rather than buying a pre-built product, you need to think in **layers**. Each layer has its own vendor market. Most vendors specialise in one or two layers; very few cover all of them.

```
┌─────────────────────────────────────────────┐
│  Layer 6: Customer-Facing App (web/mobile)  │  ← Front-end development companies
├─────────────────────────────────────────────┤
│  Layer 5: API / Integration Layer           │  ← Backend engineering + API design
├─────────────────────────────────────────────┤
│  Layer 4: AI/CV Model (inference)           │  ← Model deployment + MLOps
├─────────────────────────────────────────────┤
│  Layer 3: AI/CV Model (training)            │  ← ML engineering consultancies / platforms
├─────────────────────────────────────────────┤
│  Layer 2: Training Data (labelled images)   │  ← Data annotation companies
├─────────────────────────────────────────────┤
│  Layer 1: Cloud Infrastructure              │  ← AWS / Azure / GCP
└─────────────────────────────────────────────┘
```

The **unique challenge of building from scratch:** Most of the cost and risk is in Layers 2–4 — getting high-quality labelled training data, training a model that actually works on real-world damage photos taken by customers on varied devices, and deploying it reliably at scale. Layers 5–6 are comparatively standard engineering.

---

## Layer 1: Cloud Infrastructure

**Who:** AWS, Microsoft Azure, Google Cloud Platform (GCP)

**What they provide:** The compute, storage, and ML infrastructure to train and serve the model. All three offer managed computer vision services that reduce the infrastructure burden significantly.

| Provider | Key CV Services | Notes |
|---|---|---|
| **Azure** | Azure Custom Vision, Azure AI Vision, Azure Machine Learning | Best choice if Belron is Microsoft-stack; integrates with Copilot ecosystem |
| **AWS** | Rekognition Custom Labels, SageMaker, Bedrock | Mature, flexible MLOps tooling |
| **GCP** | Vertex AI, Vision AI, AutoML | Google's vision AI heritage is strong; best foundation models for image tasks |

**Decision point:** The right cloud is the one Belron already uses for other workloads — avoid multi-cloud for a first AI build.

---

## Layer 2: Training Data — Labelled Image Datasets

**The most underestimated part of the build.** A damage assessment model needs thousands of labelled images — photos of damage across different severities, lighting conditions, angles, devices, and glass types. Without high-quality training data, no model works.

**Options:**

### Data Annotation Companies (label your own collected images)
- **Scale AI** — Market leader in data labelling for AI. Works with major tech companies and automotive OEMs. High quality, scalable, expensive.
- **Labelbox** — Platform for managing labelling workflows; can use their labeller network or your own team.
- **Roboflow** — Developer-friendly annotation + dataset management platform. Good for computer vision specifically. Includes a model training pipeline.
- **Encord** (formerly Cord) — UK-based data annotation platform, strong in medical and visual inspection use cases. Good fit for UK-headquartered Belron.
- **Appen** — Large-scale data labelling workforce. Established, used by big tech.
- **Surge AI** — High-quality, US-based annotators. More expensive than offshore options.
- **Dataloop** — End-to-end data management + annotation platform. Particularly strong for video and image tasks.

### Synthetic Data (generate labelled data without collecting real images)
A growing option: use AI to generate synthetic images of damage (controlled lighting, angles, severity) to supplement real data.
- **Synthesis AI** — Synthetic data generation for computer vision. Reduces data collection cost significantly.
- **Rendered.ai** — Synthetic dataset generation platform.
- **CVAT (open source)** — Self-hosted annotation tool if you want to label data internally.

**Strategic note:** For a damage assessment use case, you will likely need a hybrid — some real-world images (collected from actual jobs) labelled by an annotation company, supplemented by synthetic data to cover edge cases and rare damage types.

---

## Layer 3 & 4: AI/CV Model Development and Deployment

### AI/ML Consultancies (they build the model for you)
These companies take your data and build, train, and deploy a custom CV model. They own the ML engineering and hand you a working model API.

**Global / large scale:**
- **Faculty AI** (UK) — British AI consultancy, works with enterprise clients. Strong track record in computer vision for industrial and commercial use cases.
- **Roke** (UK) — Defence and commercial AI/ML consultancy. Strong in computer vision.
- **Cog Systems** — AI engineering consultancy.
- **Weights & Biases** — MLOps platform (not a consultancy, but used by all ML teams for experiment tracking and model management).
- **DataRobot** — AutoML platform with managed ML services. Reduces need for deep ML expertise in-house.
- **Modzy** — Enterprise ML model deployment platform. Useful if you want to deploy a model built elsewhere.

**Specialist computer vision consultancies:**
- **Voxel51** — Computer vision platform + consultancy. Strong in video and image analysis.
- **Xnor.ai** (now part of Apple) — Edge computer vision (relevant if you want on-device inference rather than cloud).
- **Neurala** — Custom AI vision for inspection use cases. Relevant for quality control / damage detection.
- **Chooch AI** — Real-time CV platform. Can train on custom data for specific detection tasks.

**European / UK-relevant options:**
- **Prowler.io** (Cambridge, UK) — AI platform company, decision-making under uncertainty.
- **Graphcore** (Bristol, UK) — AI chip + ML platform company. More infrastructure than consultancy.
- **Tessella** (UK, now Axelera AI) — Engineering consultancy with strong ML/AI practice.

### Foundation Models (use a large pre-trained model, fine-tune for damage)
Rather than training from scratch, fine-tune an existing large vision model on your damage dataset. This dramatically reduces the training data needed and the time to a working model.

- **OpenAI GPT-4o** — Multimodal model that can analyse images. Could assess damage from a photo without traditional CV model training. Worth prototyping.
- **Google Gemini** — Strong multimodal capability. Could describe and classify damage from photos.
- **Anthropic Claude** — Multimodal; can analyse images. Less optimised for structured classification tasks than GPT-4o/Gemini.
- **Meta LLaMA 3 Vision** — Open source multimodal model. Can be self-hosted (important for data privacy / cost at scale).
- **Microsoft Florence** — Microsoft's vision foundation model. Integrates natively with Azure.

**Strategic note for 2026:** The fastest and cheapest route to a working damage assessment prototype is probably a multimodal foundation model (GPT-4o or Gemini) with a well-designed prompt + a structured output schema, rather than training a custom CV model. A custom model will outperform this at scale and with domain-specific tuning — but the prototype should prove the concept first.

---

## Layer 5: API / Backend Engineering

**What it is:** The backend that receives the customer's photo, passes it to the CV model, processes the result, and returns a decision (repair / replace / insufficient image quality) to the front-end.

**Who builds this:** Most mid-to-large digital engineering consultancies can build a backend API. The choice is usually made alongside the front-end partner. Key considerations:
- Must integrate with the CV model API (Layer 4) and the booking/CRM system (Salesforce/EBS)
- Must handle image storage, security, and data privacy (customer photos of vehicles may contain personal data)
- Should include a confidence scoring mechanism — low-confidence assessments should route to human review, not auto-approve

**Relevant vendors:** Same as Layer 6 (front-end companies) — most full-service studios build both front and backend.

---

## Layer 6: Customer-Facing App (Front-End)

*(As captured earlier — full vendor list in Category 1 section below)*

The customer-facing interface for a damage assessment flow has specific requirements:
- **Mobile-first** — most customers will photograph damage on a phone
- **Camera integration** — guiding the customer to take usable photos (correct angle, distance, lighting)
- **Real-time feedback** — telling the customer if the photo is good enough before submitting
- **Progressive disclosure** — asking for more images only if needed
- **Accessibility** — broad device and OS support

This is a **product design problem as much as an engineering problem.** The studios with the strongest UX capability (ustwo, Futurice, AKQA) are better suited than pure development houses for this customer-facing layer.

---

## Category 1: Customer-Facing Front-End Development Companies

### What to Look For
Companies that can design and build polished, customer-facing web and mobile applications — with strong UX/UI capability, ideally with experience in service industry or insurance/claims contexts.

### Tier 1 — Large Consultancies / System Integrators (full-service, high cost)
- **Accenture Song** — Digital experience + product design arm of Accenture. Scale, insurance/FS experience. Expensive.
- **Capgemini / Frog Design** — Frog is Capgemini's design and experience studio. Strong in digital transformation for large enterprise.
- **EPAM Systems** — Engineering-heavy digital product company. Strong in custom application development + UX. Good mid-market entry point.
- **Publicis Sapient** — Digital business transformation; strong in retail and service sectors.
- **Thoughtworks** — Engineering consultancy with strong product thinking. Known for quality code and Agile delivery.

### Tier 2 — Digital Product Studios / Agencies (specialist, mid-market)
- **Futurice** (Finland/UK/Germany) — Scandinavian digital product studio, strong in mobile + IoT integration. Culturally well-matched for Nordic/European companies.
- **ustwo** (London) — Digital product studio, known for high-quality consumer-facing products (made Monument Valley). Strong in mobile.
- **AKQA** (WPP) — Experience design and digital product. Strong in automotive sector (works with car brands).
- **R/GA** — Digital product and experience. Strong consumer-facing work.
- **Potato** (London) — Google-backed digital product studio. Strong in web applications.
- **Zühlke** (Switzerland/UK) — Engineering and product development consultancy with strong track record in regulated industries. Good for insurance-adjacent work.

### Tier 3 — Offshore / Nearshore Development Houses (cost-efficient, varying quality)
- **Miquido** (Poland) — Mobile and web app development, AI integration. Active in European market.
- **Netguru** (Poland) — Digital product development, fintech and insurance experience.
- **STX Next** (Poland) — Python/React specialists, strong enterprise track record.
- **Lemon.io** — Marketplace of vetted freelance developers (different model — flexible staffing vs. agency).

---

## Category 2: AI Machine Vision Companies

### What to Look For
Companies that can build or deploy computer vision / AI image analysis solutions — specifically relevant to: damage detection in glass/vehicle surfaces, image classification, object detection, defect inspection.

### Platform / API Providers (buy the capability, configure for your use case)
- **Google Cloud Vision AI** — Pre-trained models for image classification, object detection, OCR. Also offers AutoML for custom training. Fast to prototype.
- **Microsoft Azure Computer Vision / Custom Vision** — Azure's CV suite. Custom Vision lets you train models on your own images (e.g. windscreen damage types). Well-integrated with Microsoft ecosystem (relevant if Belron is Azure-first).
- **AWS Rekognition** — Amazon's image/video analysis service. Strong in object detection and custom label training.
- **Clarifai** — Specialised AI vision platform. Strong in custom model training for specific domains. More flexible than the hyperscalers for niche use cases.
- **Roboflow** — Developer-friendly computer vision platform. Makes it easy to label training data, train, and deploy custom vision models. Popular for industrial/inspection use cases.

### Specialist AI Vision Companies (bespoke solutions, domain expertise)
- **Tractable** — AI for accident and damage assessment, specifically in automotive and property. Used by insurers globally. **Highly relevant** — already works in vehicle damage assessment adjacent to the windscreen repair/replace market.
- **Audatex / Solera** — Automotive claims and damage assessment AI. Solera owns multiple automotive AI products including damage assessment tools used by insurers. Already embedded in the auto claims ecosystem.
- **Ravin.ai** — AI-powered vehicle inspection platform. Specifically designed for vehicle damage detection via photo/video. Used by rental fleets and insurers.
- **UVeye** — Automated vehicle inspection using computer vision (undercarriage, exterior). More physical inspection rig than mobile-first.
- **Altoros / DataRobot** — AI/ML development companies with computer vision capability. More consultancy than product.
- **Cognitec** — Specialised vision AI (primarily facial recognition but broader CV capability).

### Niche / Emerging (worth watching)
- **Landing AI** (Andrew Ng's company) — AI for industrial visual inspection. Strong in manufacturing/defect detection. Could apply to glass inspection.
- **Neurala** — AI vision for inspection and quality control. Industrial focus but adapts to new domains.
- **Chooch AI** — Real-time computer vision platform. Customisable for specific detection tasks.

---

## Companies That Do Both (Machine Vision + Front-End)
Some companies can bridge both disciplines — building the CV model and the customer-facing interface that surfaces it.

- **EPAM Systems** — Has both strong engineering/ML and product/UX capability
- **Zühlke** — Engineering consultancy with ML/AI and product development
- **Miquido** — Has AI/ML + mobile app capability in one house
- **Netguru** — Has AI/ML engineering + digital product design
- **Futurice** — Has ML engineering and product design (Scandinavian, which may matter for Belron's opcos)

---

## Strategic Intelligence

### Key Insights

1. **Building from scratch means owning the problem in layers.** The vendor market for a custom AI damage assessment build is not one vendor — it's a supply chain: cloud infrastructure + training data + model development + backend API + front-end app. Each layer has its own market, its own risks, and its own quality gates. EA's job is to design how these layers connect and who owns what.

2. **The fastest route to proof of concept is a multimodal foundation model, not a custom-trained CV model.** In 2026, GPT-4o and Gemini can analyse a photo of windscreen damage and provide a structured assessment with no training data required. This won't be production-grade at scale, but it's a working prototype in days, not months. **Prove the concept with a foundation model first. Custom model only if the prototype validates the use case.**

3. **Training data is the hardest part, not the model.** Most organisations underestimate this. A custom damage assessment model needs thousands of high-quality, consistently labelled images across damage types, severities, lighting conditions, and devices. Getting this data takes months and significant investment. Scale AI, Encord, or Roboflow are the right tools for this — not an afterthought.

4. **The camera UX is underrated.** The quality of the AI output is only as good as the quality of the input image. Poor photos (wrong angle, bad lighting, too far away) will defeat even a well-trained model. A guided camera experience — showing the customer exactly how to photograph their damage — is a critical product design challenge, not a technical one. Studios like ustwo or Futurice are better suited to this than engineering-first shops.

5. **There is a strategic question underneath all of this.** Why build from scratch rather than partner with Tractable, Ravin.ai, or Audatex/Solera? The answer shapes the vendor list entirely. If the answer is "we want to own the IP and data" — build. If it's "we want to move fast and own the customer experience but not the AI" — API into an existing model. If it's "we want to differentiate on the full experience" — build front-end, buy or fine-tune the CV model. Clarifying this first prevents wasted effort.

6. **This connects directly to the Wardley Map.** Customer-facing front-end development is Product-stage (buy or partner). Training a custom damage assessment CV model is Custom-stage (differentiating, worth building if you own the use case). Foundation model APIs (GPT-4o, Gemini) are moving toward commodity fast — use them for speed now, plan to own a fine-tuned model later.

### Connection to Competitive Watchlist
No COMPETITIVE-WATCHLIST.md exists yet — this scan surfaces several companies worth tracking:
- **Tractable** — direct intersection with Belron's market; understand what they sell and to whom
- **Ravin.ai** — vehicle inspection AI, potential competitive or partner
- **Audatex/Solera** — already embedded in insurer workflows that touch Belron
- **Scale AI** — if data annotation is a strategic bottleneck, Scale is the market leader
- **Faculty AI** — UK-based ML consultancy most likely to understand the Belron context

---

## Action Items

### Immediate (24–48 hours)
- [ ] Answer the strategic question first: own the IP and data → build from scratch; own the UX but not the AI → buy/API; differentiate end-to-end → hybrid. This single answer drives all vendor decisions 📅 2026-04-10
- [ ] Run a GPT-4o or Gemini prototype: take 5 real photos of windscreen damage and see if a foundation model can classify repair vs. replace reliably — this costs nothing and proves/disproves the concept in an afternoon 📅 2026-04-11

### Short-term (1–2 weeks)
- [ ] Structure the scan into a one-page layered market map (cloud → data → model → API → front-end) with vendor options per layer 📅 2026-04-17
- [ ] Create `03-professional/COMPETITIVE-WATCHLIST.md` — add Tractable, Ravin.ai, Audatex/Solera, Scale AI, Faculty AI 📅 2026-04-14
- [ ] Research Encord (UK-based annotation platform) — most likely to be a practical fit for a Belron data labelling programme 📅 2026-04-17
- [ ] Run the Wardley lens: where does each layer (data, model, front-end) sit on the evolution axis? 📅 2026-04-17

### Strategic Considerations
- **Foundation model first, custom model second.** The prototype using GPT-4o/Gemini should precede any decision to invest in custom model training. If it doesn't work well enough, you need custom training. If it works well, you may only need fine-tuning.
- **Camera UX is a product design problem.** Whichever front-end studio is chosen must have strong mobile camera UX experience — guiding customers to take usable photos is the highest-leverage UX challenge in this product.
- **Data strategy is a long-term asset.** The labelled image dataset built during this project becomes proprietary IP — images of real Belron customer damage, in real conditions. This is valuable beyond the first use case. Design the data strategy with future use cases in mind.
- **Privacy and data residency.** Customer vehicle photos may contain licence plates and other identifying information. UK/EU GDPR implications need to be scoped before any external annotation partner handles the data.

---

## Connections
- **Related braindump:** [[braindump-2026-04-08-1125-value-chains-and-wardley-mapping]] — Wardley lens applies here: where is machine vision on the evolution axis?
- **Related braindump:** [[braindump-2026-04-08-1426-review-customer-journey-model]] — the customer journey stage where machine vision would appear (Stage 2: booking/assessment, Stage 4: the job)
- **Related framework:** [[belron-business-understanding-framework]] — this scan feeds Layer 2 (Wardley: which capabilities to build vs. buy) and Layer 4 (Systems Landscape)
- **Related:** [[ea-effectiveness-framework]] — the market scan one-pager is a dual-purpose artefact: analysis tool + stakeholder briefing

## Domain Classification
- **Primary Domain:** Professional (99%)
- **Privacy Level:** Professional (internal)

## Processing Notes
### Confidence Assessment
- **Overall Analysis:** 85% — market scan is directionally correct; company list needs validation against current market (some may have been acquired or pivoted)
- **Company list accuracy:** 80% — based on knowledge to August 2025; some entries (especially Tier 3) may need verification
- **Strategic insights:** 88% — Tractable and the build-vs-buy framing are well-grounded
- **Areas requiring clarification:** What is the specific use case? This single answer would cut the vendor list by 60%

---

*Processed by COG Braindump Analyst*
