---
# Target Audience
target_audience: "Prospective sponsor companies for ZK Core Program 2026"
audience_type: group

# Constraints
constraints:
  max_slides: 25
  max_duration_minutes: 20

# Output Language
output_language: English

# Event Context (Optional)
event:
  name: "ZK Core Program 2026"
  parent_event: ""
  date: "2026"
  location: "Online & Tokyo"
---

# ZK Core Program 2026 — Sponsorship Proposal

## About This Presentation (The Big Idea)

This deck is a sponsorship proposal for the "ZK Core Program 2026," to be held in 2026. The program's mission is to find and grow exceptional talent in Japan's **Programmable Cryptography** field (ZK, FHE, MPC and related technologies) — talent capable of understanding these technologies deeply from theory through to practice and competing at a world-class level. By sponsoring, your company gets a unique opportunity to elevate its technical brand, gain early access to top-tier engineers, and directly contribute to creating future use cases.

## Background / Status Quo

Japan is in the middle of a major transformation driven by accelerating digital transformation (DX). At the same time, **cybersecurity risk has exploded into a national-scale issue that threatens corporate management and economic security**. In the Information-technology Promotion Agency's (IPA) "Top 10 Information Security Threats 2025," "damage from ransomware" and "attacks exploiting supply-chain weak points" have been near the top of the list for nearly a decade — entrenched risks that strike at the foundation of corporate activity [1]. In 2024 alone, 189 incidents at listed companies in Japan leaked the personal data of more than 15 million people, and incidents continue unabated [2].

This dilemma — how to reconcile privacy with the use of data — is no longer a single-company problem; it now shapes international competitiveness. In the European Union, the eIDAS 2.0 regulation expected to take effect in 2026 will mandate the provision of digital ID wallets with strong privacy protection, and **privacy-preserving technologies are quickly becoming the new global standard** [3].

Against this backdrop, the world's largest tech companies are already acting. In 2025, Google integrated zero-knowledge proof (ZKP) technology into Google Wallet to enable privacy-preserving age verification, and open-sourced the underlying tech [4]. Apple has likewise shipped features such as photo search and caller-ID lookup using fully homomorphic encryption (FHE), in a way that even the server cannot decrypt user queries or personal data [5].

These moves are not just feature additions. They are **strategic investments to redefine the trust infrastructure of digital society**. The ZKP market is forecast to grow from roughly USD 1.3B in 2024 to over USD 7.5B by 2033 [6], and Programmable Cryptography is unmistakably the next massive industrial frontier. Far from being premature, engaging with this field is **an urgent task essential to maintaining and improving Japan's industrial competitiveness**.

## Why ZK Tokyo and the Core Program Matter

Rising cyber risk and intensifying international competition. To meet these national challenges, the most important asset is, without question, **highly specialized talent capable of carrying the next generation of technology**. Yet developing that talent is something Japan struggles with, and the shortage has reached critical levels. According to METI, Japan is short roughly 110,000 cybersecurity professionals [7], and the IT workforce as a whole is projected to be short by as much as 790,000 by 2030 [8].

Closing that severe talent gap and shaping the future of Japan's digital society — that is the **true significance of the "ZK Core Program."** Our program does not just train engineers who apply cryptography. It is **the most stimulating and hands-on environment in Japan for cultivating world-class talent** that can support core digital infrastructure and reconcile privacy with innovation.

For the past three years, ZK Tokyo has served as the hub driving Japan's cryptography community. In 2025, we hosted Ethereum founder Vitalik Buterin, and we have co-hosted events with top players from Japan and abroad such as SMBC Nikko Securities and RISC Zero — bridging academia, industry, and the global ecosystem. The fact that our alumni go on to collaborate with the Ethereum Foundation and present at international conferences is direct evidence that our work creates **value that translates beyond Japan**.

## The 2025 Program's Success: The Synergy of Theory and Collaboration

The 2025 results prove the program's effectiveness. The program ran in a **hybrid format combining online distribution of materials with offline group work on weekends**.

> Participants self-studied theory on weekdays using text-based materials distributed online, then gathered offline on weekends. Through **intense, whiteboard-format group work**, they applied that knowledge against each other, deepened the discussion, and solved problems together. It is precisely this cycle — fusing "individual learning" with "collective intelligence" — that sits at the core of the program's success.

This format built deep mutual understanding and trust between participants, and powered the completion of complex cryptographic theory and the delivery of exceptionally high-quality final outputs in just six weeks.

**Major final outputs from 2025:**

| Project | Summary |
|---|---|
| **zk-KYC-DEX** | A DEX prototype that uses ZK proofs to perform KYC while keeping personal data private. |
| **DeFi unsecured personal lending** | A realistic unsecured personal lending protocol that combines credit-bureau data with ZKP for privacy-preserving credit checks. |
| **ZK-Vote** | A safe, fair anonymous DAO voting system that uses ZKP to fully conceal voter identity and ballot contents. |
| **Corporate Wallet** | Proof of corporate existence and intent-of-operation for wallet actions using commercial-registry digital certificates, executed offline or on-chain. |

These outputs speak not just to the participants' technical strength but also to the soundness of the program's design philosophy: **connecting theory to practice and driving innovation through collaboration**.

## 2026 Program Overview

### 1. Curriculum: Theory Meets Practice

Rather than treating leading-edge cryptography — ZKP (zero-knowledge proofs), FHE (fully homomorphic encryption), MPC (secure multi-party computation) — as a "black box," our program deepens essential understanding by **rebuilding the underlying mathematical structures by hand**. Through repeated cycles of translating abstract theory into concrete code, participants ultimately gain the ability to design and implement, from scratch, systems that guarantee privacy and computational integrity.

### 2. Target Audience and Recommended Skills

The program targets highly motivated individuals such as:

- **Engineers who want to strengthen their cryptography implementation skills:** People who understand ZK and secure computation conceptually but want to be able to build the internal logic of libraries and cryptographic circuits themselves.
- **Protocol designers and researchers:** People who want to design and propose new distributed systems and privacy-preserving technologies from scratch, grounded in mathematical reasoning.

Because of the nature of the program, we recommend that participants have the following knowledge and skill set.

| Category | Skill detail | Required / Recommended |
|---|---|---|
| **Programming skills** | Development experience in Python, TypeScript, etc.; basic understanding of memory management and computational complexity. | **Required** |
| **Mathematical foundations** | Elementary number theory (modular arithmetic, groups/rings/fields), linear algebra, basics of polynomial arithmetic. | Recommended |
| **Computer science** | Logic gates and circuits; basic understanding of computational models (instruction sets, data flow). | Recommended |
| **Interest in cryptography** | Understanding of the role of public-key cryptography, hash functions, and digital signatures, plus strong commitment to a weekly in-person session and self-study. | **Required** |

### 3. Schedule and Curriculum

The program runs for 7 weeks. Week 1 presents the big picture and example applications to spark intellectual curiosity, after which we dive into specific topics. Theory lectures and implementation assignments run in parallel, and a weekly in-person session deepens group discussion and design work.

| Week | Theme | Theory lecture | Implementation assignment | In-person session |
|---|---|---|---|---|
| 1 | Programmable Cryptography | Big-picture view of ZK/MPC/FHE and how they complement each other. The theory of "circuits" as an abstraction for computation. | Implement code that expresses and executes basic arithmetic operations as a "circuit." | Use-case identification workshop |
| 2 | MPC | Secret sharing, OT, Garbled Circuits. | Implement secret sharing and addition/multiplication protocols in Rust. | Project team formation |
| 3 | ZKP I (Arithmetization) | Transforming computation using polynomials. The mathematical structure of R1CS. | Write code that converts computation logic into R1CS-format matrices. | Design review |
| 4 | ZKP II (Polynomial commitments) | Commitment schemes such as KZG and IPA. | Implement polynomial commitment and verification logic using elliptic curves. | Whiteboard session |
| 5 | ZKP III (Plonk-style constraint systems) | Permutation arguments and copy constraints. The basics of lookup tables. | Implement a protocol that verifies wire equality (copy constraints) within a circuit. | Mid-term presentation |
| 6 | FHE | Lattice-based cryptography, the LWE problem, homomorphic operations, and noise management. | Implement LWE encryption and decryption, plus addition and multiplication logic on ciphertexts (no decryption). | Technical integration office hours |
| 7 | Advanced Topics & Demo | The cutting edge — Verifiable FHE, Folding, zkVM, etc. | Integrate everything learned so far into a complete, optimized protocol. | **Demo Day** |

Final outputs will be shared with the world via formats such as **presentations at ETH Global Tokyo** and **private demos for sponsor companies**.

### 4. Improvements from 2025

For 2026, we are improving and strengthening the program based on the successes of the previous year:

- **Introducing group projects:** A single theme will be carried through the entire program as a group project. Members will be shuffled in the first two weeks, then locked in from Week 3 to drive the project forward.
- **Stronger connection to applied examples:** To make clear how theory plays out in the real world, we will, for instance, study services that actually use Plonk during the week we cover Plonk.
- **Concrete final deliverables:** We will present concrete final assignments and themes (e.g., "implement a zkVM") at the very beginning, to maximize motivation for the most technically ambitious participants.

## The Ask / Call to Action

To further evolve this leading-edge program, we are inviting your company to participate as a sponsor. Sponsorship is more than funding. It gives your company the right to **propose the themes that participants tackle as their final outputs**. Participants then choose, from the themes you propose, the one that best fits their interest and develop it through the program.

The format is close to a **practical internship**. Your company gets to present directly to participants and mentor them, and the ZK Tokyo instructors provide strong support across the curriculum and through to the completion of the final outputs. As a sponsor, you gain the following:

- **Talent development and early discovery:** Direct touchpoints with high-potential young engineers
- **Use-case creation:** Exploration of new technical applications relevant to your business domain
- **Brand visibility:** Higher recognition and brand image within the technical community

**Sponsorship plans:**
- **JPY 500K:** Propose 1 theme
- **JPY 1M:** Propose 3 themes
- **JPY 2M:** Propose 5 themes

ZK Tokyo will work with you to scope and shape compelling themes.

## Team / Stakeholders

- **Host:** ZK Tokyo ([X/Twitter](https://x.com/zk_tokyo), [YouTube](https://www.youtube.com/@zk-tokyo), [Telegram](https://t.me/+mqLG9CwMPB8zNDY1))
- **Co-host:** The University of Tokyo Blockchain Innovation Endowed Chair
- **Cooperation:** Sponsor companies

## Closing

The ZK Core Program is a one-of-a-kind platform for raising the bar of Japan's technical capability and sending the next generation of innovators onto the world stage. Joining this movement is not just an investment; it marks the start of a partnership to co-create the technology ecosystem of the future. We hope you will join us in growing the exceptional talent that will shape the future of Japan and the world. We look forward to hearing from you.

---

### References

[1] Information-technology Promotion Agency (IPA). "Top 10 Information Security Threats 2025." https://www.ipa.go.jp/security/10threats/10threats2025.html (accessed 2026-01-23)

[2] Tokyo Shoko Research, Ltd. "2024 Survey on Personal Information Leakage and Loss Incidents at Listed Companies." 2025-01-21. https://www.tsr-net.co.jp/data/detail/1200872_1527.html (accessed 2026-01-23)

[3] European Commission. "European Digital Identity." https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/european-digital-identity_en (accessed 2026-01-23)

[4] Google. "Opening up 'Zero-Knowledge Proof' technology to promote privacy in age assurance." The Keyword. 2025-07-03. https://blog.google/innovation-and-ai/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/ (accessed 2026-01-23)

[5] Apple. "Combining Machine Learning and Homomorphic Encryption in the Apple Ecosystem." Apple Machine Learning Research. 2024-10-24. https://machinelearning.apple.com/research/homomorphic-encryption (accessed 2026-01-23)

[6] Grand View Research. "Zero Knowledge Proof Market Size | Industry Report, 2033." 2024. https://www.grandviewresearch.com/industry-analysis/zero-knowledge-proof-market-report (accessed 2026-01-23)

[7] Ministry of Economy, Trade and Industry (METI). "Final Report Released by the Study Group on Promoting the Development of Cybersecurity Talent." 2025-05-14. https://www.meti.go.jp/press/2025/05/20250514002/20250514002.html (accessed 2026-01-23)

[8] Ministry of Economy, Trade and Industry (METI). "Survey on IT Talent Supply and Demand." 2019-04-25. https://www.meti.go.jp/policy/it_policy/jinzai/houkokusho.pdf (accessed 2026-01-23)

**Related links:**
- **Core Program 2025 materials:** [https://github.com/zk-tokyo/core-program](https://github.com/zk-tokyo/core-program)
- **Core Program 2025 final outputs:** [https://github.com/zk-tokyo/core-program/tree/main/final-projects](https://github.com/zk-tokyo/core-program/tree/main/final-projects)
- **Core Program 2025 showcase:** [https://www.youtube.com/watch?v=j1u1cyjfilo&list=PLvKRWMWw-Dsa4BGplLe1YYgRpiio72FgY](https://www.youtube.com/watch?v=j1u1cyjfilo&list=PLvKRWMWw-Dsa4BGplLe1YYgRpiio72FgY)
- **Core Program 2025 lectures:** [https://www.youtube.com/watch?v=KGoIeuBKxB4&list=PLvKRWMWw-Dsai7hPewIS2LYnZHS4Z_W2Z](https://www.youtube.com/watch?v=KGoIeuBKxB4&list=PLvKRWMWw-Dsai7hPewIS2LYnZHS4Z_W2Z)
