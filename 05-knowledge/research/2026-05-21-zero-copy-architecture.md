---
type: "strategic-research"
domain: "technology"
date: "2026-05-21"
created: "2026-05-21 09:09"
question: "What does zero-copy mean in the context of architecture?"
threads: ["os-systems-level", "data-pipeline-streaming", "enterprise-data-architecture", "trade-offs-decision-framework"]
confidence: "HIGH"
tags: ["#research", "#zero-copy", "#architecture", "#systems", "#data-pipeline", "#enterprise-data", "#performance"]
status: "complete"
---

# Zero Copy in Architecture: A Research Paper

## Executive Summary

"Zero copy" means different things at different layers of the architecture stack — and confusing these layers is the most common mistake when the term surfaces in technical or vendor conversations. At the **OS/systems level**, it is a kernel technique that eliminates redundant CPU-driven memory copies when moving data between disk, memory, and network interfaces, reducing copy counts from four to two and dramatically increasing I/O throughput. At the **data pipeline layer**, it describes in-memory formats (Apache Arrow) and streaming systems (Kafka) that avoid serialisation/deserialisation overhead and allow multiple consumers to share the same physical memory or log. At the **enterprise data architecture layer** — where the term appears most frequently in 2024–2026 vendor marketing — it means accessing data in-place at its source without creating physical copies in a separate system, enabling shared access without ETL pipelines.

All three layers share the same core insight: **copying data is expensive** — in CPU time, memory bandwidth, storage cost, latency, and governance risk. Zero-copy is the architectural principle of eliminating copies that exist for historical or convenience reasons rather than necessity.

---

## Part 1 — The Problem: Why Copies Exist and What They Cost

### The Traditional I/O Path (The Baseline to Beat)

To understand zero-copy, you need to understand what it replaces. In a conventional Linux I/O operation — say, reading a file and sending it over a network socket — data passes through **four copies** and **four context switches**:

```
Disk → [DMA copy] → Kernel Page Cache
     → [CPU copy] → User-Space Buffer
     → [CPU copy] → Socket Send Buffer
     → [DMA copy] → Network Interface Card
```

Two of these copies involve the CPU directly: the kernel buffer → user buffer copy, and the user buffer → socket buffer copy. These are pure overhead — the CPU is spending cycles moving bytes it will never inspect. The context switches between user mode and kernel mode are also expensive: each one costs hundreds to thousands of nanoseconds.

For low-volume systems this overhead is invisible. At scale — 10 Gbps network links, millions of messages per second, multi-TB analytical queries — it becomes the binding constraint.

### The Cost Model

| Copy type | Consumes | At scale |
|---|---|---|
| CPU copy (kernel ↔ user) | CPU cycles + memory bandwidth | Saturates cores; crowds out real work |
| DMA copy (hardware ↔ memory) | Memory bandwidth only | Fast, but still occupies bus bandwidth |
| Context switch | ~1–10 µs per switch | 4 switches per I/O operation multiplies fast |
| Data duplication (enterprise) | Storage + sync cost + governance surface | 75%+ redundant storage in typical enterprise estates |

---

## Part 2 — Layer 1: OS/Systems Zero-Copy

### mmap() — Virtual Memory Aliasing

`mmap()` was the first mainstream zero-copy technique. It maps a file's content in the kernel page cache directly into the application's virtual address space. The user-space pointer and the kernel buffer pointer reference the **same physical memory page**.

```
Disk → [DMA copy] → Kernel Page Cache (= User Virtual Address)
     → [CPU copy] → Socket Send Buffer
     → [DMA copy] → NIC
```

**Result:** 3 copies, 4 context switches. One CPU copy eliminated. The trade-off: virtual memory mapping operations (`mmap`/`munmap`) are expensive themselves — the TLB flush and page table management add overhead that can outweigh the savings for small files or frequent small operations.

**Best for:** Large files read repeatedly, where the mapping cost is amortised over many accesses (e.g., database buffer pools, memory-mapped log segments).

---

### sendfile() — Kernel-Internal Transfer

`sendfile()`, introduced in Linux 2.1 (1997), added a single system call that transfers data between two file descriptors entirely within the kernel, never touching user space.

```
Disk → [DMA copy] → Kernel Page Cache
     → [CPU copy] → Socket Send Buffer    ← still a CPU copy
     → [DMA copy] → NIC
```

**Result:** 3 copies, **2 context switches** (vs 4 for traditional I/O). The user-space round-trip is gone. In Java, `FileChannel.transferTo()` maps to `sendfile()` on Linux — this is how Kafka brokers deliver messages to consumers.

**Best for:** Serving static file content at scale (web servers, CDNs, message brokers), where the same bytes are repeatedly sent to different consumers.

---

### sendfile() + SG-DMA — True Zero CPU Copy

On hardware with **Scatter-Gather DMA** support (almost all modern NICs), the kernel can go further. Instead of copying data to the socket buffer, it stores only a **file descriptor reference and length** in the socket buffer. The NIC's SG-DMA controller reads the data directly from the page cache into the NIC's own buffer.

```
Disk → [DMA copy] → Kernel Page Cache
     → [SG-DMA]  → NIC (direct, no socket buffer copy)
```

**Result:** 2 copies (both DMA — no CPU involvement at all), 2 context switches. This is "true" zero-copy at the OS level: the CPU never touches the data in flight.

**Performance evidence:** In Java benchmarks transferring an 880 MB file:
- Traditional I/O: baseline
- `mmap()`: 81% faster
- `sendfile()`: 91% faster

**Limitation:** SSL/TLS breaks this. When encryption is enabled, the broker must decrypt+re-encrypt the data, forcing a CPU copy. Kafka's zero-copy advantage disappears the moment TLS is switched on at the broker layer.

---

### io_uring — Async Zero-Copy with Fixed Buffers

`io_uring`, merged into Linux 5.1 (2019) and actively developed through 2025, takes a different approach. Instead of new system calls, it introduces a **shared ring buffer** between user space and kernel for submitting and collecting I/O operations asynchronously.

The zero-copy mechanism: applications pre-register memory buffers with `io_uring_register_buffers()`. The kernel **pins** these pages in physical memory and establishes permanent mappings. Subsequent I/O operations reference buffers by index (`IORING_OP_READ_FIXED`, `IORING_OP_WRITE_FIXED`), eliminating the per-operation mapping/copy overhead.

For networking, `IORING_OP_SEND_ZC` (merged Linux 6.0, 2022) enables truly async zero-copy network sends. Linux 6.15 (2025) added zero-copy receive (`io_uring zcrx`), and Linux 6.16 extends it to DMA-BUF buffers.

**Key nuance:** io_uring's gains are batch-size-dependent. For single operations it can be *slower* than `epoll` due to setup overhead. Its advantage emerges at high concurrency — when many operations are batched into a single submission, the per-operation cost approaches zero.

**Best for:** High-concurrency async servers (HTTP/3, databases, proxies), storage engines processing many I/O operations simultaneously.

---

### Kernel Bypass — DPDK and RDMA

At the most extreme end, **kernel bypass** eliminates the OS networking stack entirely. Two technologies dominate:

**DPDK (Data Plane Development Kit):** User-space application polls the NIC directly via poll-mode drivers. No kernel interrupts, no TCP/IP stack processing, no context switches. Data arrives in pre-allocated memory pools (`mbufs`) that the application reads in place.

**RDMA (Remote Direct Memory Access):** Allows one machine to read from or write to another machine's memory directly, with no CPU involvement on either end. Used in HPC, high-frequency trading, and increasingly in AI training clusters for GPU-to-GPU transfers.

| Technology | Latency | Throughput | Complexity |
|---|---|---|---|
| Standard Linux stack | ~50–200 µs | ~10 Gbps/core | Low |
| io_uring | ~10–50 µs | ~40 Gbps/core | Medium |
| DPDK | ~1–10 µs | ~100 Gbps/core | Very high |
| RDMA | <1 µs | Line rate | Extreme |

**The fundamental trade-off:** DPDK requires dedicated CPU cores that poll at 100% utilisation even when idle. It requires complete application redesign and specialised hardware knowledge. It is not the right answer unless you are Cloudflare, a 5G telco, or a high-frequency trading firm processing 10M+ packets/second.

---

## Part 3 — Layer 2: Data Pipeline and Streaming Zero-Copy

### Apache Arrow — Zero-Copy In-Memory Analytics

Apache Arrow is an in-memory columnar data format designed so that data does **not need to be parsed, deserialised, or reformatted** when passed between systems. The same physical memory layout is read natively by Arrow-compatible engines (DuckDB, Pandas, Polars, Spark, Flink, BigQuery Storage API).

The zero-copy property: when reading from a source that supports it (memory-mapped files, Arrow IPC streams), the `RecordBatch` returned is a **view over the existing physical memory** — no allocation, no copy. The Arrow spec guarantees a canonical byte layout, so an Arrow buffer written by a Rust process can be read by Python without translation.

**What Arrow eliminates:**
- Row → column transposition at query time
- JSON/Avro/Protobuf deserialisation overhead
- Format conversion between systems in an analytics pipeline

**Arrow Flight:** Arrow Flight is a gRPC-based transport protocol purpose-built for streaming columnar data between nodes. It is substantially faster than JDBC/ODBC for analytical query results. The server streams Arrow `RecordBatches` directly; the client receives pre-formatted columnar data it can hand directly to DuckDB or Pandas without any conversion.

A five-layer architecture for real-time analytics using Arrow + Kafka:
1. **Kafka Ingest** — row-oriented, schema-optional messages
2. **Arrow Conversion** — batches messages into columnar `RecordBatches`
3. **Stream Manager** — TTL, backpressure, memory limits
4. **Arrow Flight Server** — exposes live streams to analytical consumers
5. **Query Sink** — DuckDB, Polars, or similar

This pipeline achieves sub-second Kafka-to-client latency on modest hardware, with stable memory under load.

---

### Apache Kafka — Zero-Copy Message Delivery

Kafka's performance profile depends heavily on zero-copy at the broker layer. When a consumer requests messages, the broker uses `sendfile()` (via Java NIO `FileChannel.transferTo()`) to transfer bytes directly from the log segment files on disk to the consumer's TCP socket **without passing through user space**.

The practical consequence: if consumers are roughly keeping pace with producers, the data they are reading is still in the OS **page cache** — the disk is not involved at all. The broker's CPU is essentially idle during message delivery; it is handling nothing more than the offset bookkeeping.

**Important caveats:**
- TLS encryption removes the zero-copy advantage (broker must decrypt/re-encrypt)
- Compression (at-rest) also requires CPU involvement for decompression on the broker path
- Multiple consumer groups all reading from the same topic partition each get their own `sendfile()` call — but they all read from the same page cache, so disk I/O is not duplicated

---

### Memory-Mapped Files and Log-Structured Storage

Memory-mapped files (`mmap`) underpin several high-performance storage systems:
- **RocksDB / LevelDB:** SST files are memory-mapped for read access; hot data effectively lives in OS page cache
- **LMDB:** The entire database is one memory-mapped file — random reads are pointer dereferences, not system calls
- **Aeron (messaging):** Uses memory-mapped log files shared between publisher and subscriber processes via shared memory IPC — the subscriber reads directly from the publisher's write pointer
- **Chronicle Map / Chronicle Queue:** Java libraries that use off-heap memory-mapped storage to share data between JVM processes on the same machine without serialisation

The pattern: **shared physical memory as the integration bus**. Two processes on the same machine can exchange data at memory speeds (~50 GB/s) with zero copies by mapping the same file.

---

### Open Table Formats — Zero-Copy for Lakehouse Architectures

Apache Iceberg, Delta Lake, Apache Hudi, and Apache Paimon provide zero-copy access at the storage layer of a lakehouse. Because they define a standard metadata + Parquet file layout on object storage (S3/GCS/Azure Blob), multiple compute engines — Spark, Trino, Flink, DuckDB, BigQuery — can read the **same physical files** with no translation or copying between engines.

Snowflake's Data Sharing is built on this principle: a provider grants metadata-level access to a database object; consumers query using their own compute but read from the provider's storage. No bytes move between accounts.

---

## Part 4 — Layer 3: Enterprise Data Architecture Zero-Copy

### The Paradigm Shift: Copy-First vs Access-First

Traditional enterprise data integration is **copy-first**: extract data from the system of record, transform it, load it into a new system optimised for the consumer's use case. The CDP copies CRM data. The data warehouse copies the transactional database. The reporting tool copies the warehouse.

Each copy:
- Adds latency (the data is stale the moment it is copied)
- Multiplies storage cost
- Creates a new compliance surface (another place sensitive data lives)
- Creates a sync problem (which copy is authoritative?)
- Creates a pipeline to break

Zero-copy enterprise architecture inverts this: **access data in place, through reference rather than replication**. Consumers are granted logical access to the source — a pointer, a credential, a query endpoint — not a physical copy.

### Four Implementation Patterns

**1. Metadata-based access** — systems share structural information (schema, statistics, partition layout) allowing a query engine to read directly from source storage. Iceberg's REST catalog is the canonical example: any engine that speaks the Iceberg REST API can query the same table without copying it.

**2. Reference-based sharing** — logical pointers direct consumers to data locations. Snowflake Secure Data Sharing grants access to database objects; the consumer's SQL runs against the provider's storage. Zero bytes move between accounts.

**3. Shared object storage** — multiple compute engines read identical files from S3/GCS/Blob. The storage layer (not the compute layer) is the source of truth. Delta Lake and Iceberg both enable this: Spark, Trino, and DuckDB can all query the same `s3://bucket/table/` path simultaneously.

**4. Virtual views and federated queries** — a query engine creates a logical representation (view, virtual table, semantic layer) over the source without materialising it. Presto/Trino's connector model, Databricks Unity Catalog, and Google BigQuery Omni all work this way.

### Zero-Copy Data Mesh

The strongest architectural alignment for zero-copy is with **data mesh**: domain teams own their data as products in place, granting access to consumers without losing control or creating copies. Zero-copy is the technical enabler of the "data as a product" principle — the domain team maintains one physical copy, governed and secured, and grants fine-grained access to all consumers.

Without zero-copy, data mesh collapses back into point-to-point ETL pipelines between domains, which is exactly what it was designed to escape.

### The "Logical-First" Extension

A useful critique from the data management literature: many platforms claiming "zero-copy" still require an initial data consolidation step — you must first land your data in their lakehouse or cloud warehouse before the zero-copy sharing can happen. This is "copy-first, share-later" disguised as zero-copy.

**Logical-First architecture** extends the principle: don't move data unless there is an unavoidable reason to. This means:
- Native access to heterogeneous sources (operational databases, SaaS platforms, mainframes) without prior consolidation
- Unified governance that spans systems the data never leaves
- Query optimisation that minimises movement, not just duplication

Platforms moving in this direction include Dremio (federated query over S3, RDBMS, and SaaS with unified governance), Starburst (Trino-based federation), and Google BigQuery Omni (querying data in AWS S3 without moving it to GCP).

---

## Part 5 — When to Recommend Zero-Copy: A Decision Framework

### Layer 1 (OS/Systems) — Recommend when:

| Scenario | Mechanism |
|---|---|
| Web server serving large static assets at high concurrency | `sendfile()` |
| Message broker delivering high-throughput unencrypted streams | `sendfile()` (Kafka default) |
| Database buffer pool for large read-heavy workloads | `mmap()` |
| High-concurrency async I/O server (HTTP/3, proxy) | `io_uring` |
| Telco / CDN / HFT: sub-10µs latency at 10M+ packets/s | DPDK kernel bypass |
| HPC / AI training: GPU-to-GPU or node-to-node at line rate | RDMA |

**Do not reach for kernel bypass** unless sub-100µs latency or 10+ Gbps/core throughput are hard requirements. The operational complexity is extreme: dedicated CPU cores polling at 100% utilisation, specialised hardware, complete application redesign, no standard debugging tools.

### Layer 2 (Data Pipeline) — Recommend when:

| Scenario | Mechanism |
|---|---|
| Analytics pipeline where data passes through many engines | Apache Arrow |
| Real-time analytics over a Kafka stream | Arrow + Arrow Flight |
| Inter-process data sharing on a single machine | Memory-mapped files / shared memory |
| Lakehouse with multiple compute engines (Spark, Trino, Flink) | Open table formats (Iceberg/Delta) |
| High-volume unencrypted message delivery from Kafka | Kafka's built-in sendfile |

### Layer 3 (Enterprise Data Architecture) — Recommend when:

| Scenario | Recommendation |
|---|---|
| Multiple teams need real-time access to the same dataset | Zero-copy data sharing (Snowflake, Iceberg) |
| Regulated environment requiring a single source of truth | Zero-copy over ETL copy |
| Enterprise data mesh implementation | Zero-copy as the technical foundation |
| Existing cloud warehouse investment is large | Zero-copy to leverage rather than duplicate |
| New consumer needs data access fast | Access grant (minutes) vs pipeline build (weeks) |

---

## Part 6 — Trade-offs and Costs

### What Zero-Copy Does Not Solve

Zero-copy is not a universal answer. Its costs are real:

**Complexity (Layer 1):**
- Kernel bypass requires specialised hardware and ops expertise
- Memory-mapped files require careful handling of partial writes, file size changes, and SIGBUS errors
- io_uring's performance is batch-size dependent; single-operation workloads can regress

**Schema coupling (Layers 2 and 3):**
- Multiple consumers sharing physical data files creates tight coupling on schema evolution. A breaking schema change requires coordinating all consumers simultaneously
- Backward compatibility management becomes a first-class architectural concern

**Vendor dependency (Layer 3):**
- Snowflake zero-copy sharing requires both parties to be Snowflake customers
- Some "zero-copy" architectures are actually "copy into our platform first, share from there" — scrutinise the onboarding path

**Governance intensification (Layer 3):**
- When consumers access source data directly, fine-grained access control, audit logging, column/row-level masking, and data quality SLAs become non-negotiable. The governance surface does not shrink — it expands to the source
- Data deletion and retention become complex: different consumers may have different retention requirements against the same physical data

**Performance shifting (Layer 3):**
- Eliminating storage duplication shifts cost to **compute and network**. Cross-region zero-copy queries can be slow and expensive. Snowflake Data Cloud charges 70 credits/million rows for zero-copy access vs 2,000 credits for ETL — but the savings disappear if query patterns are poorly designed
- Resource contention: all consumers share the same source system's I/O capacity

**Security/encryption (Layer 1):**
- TLS encryption eliminates sendfile-based zero-copy at the broker layer. You must choose between encryption in transit and zero-copy throughput, or push encryption to the storage layer (at-rest) and accept unencrypted in-transit

### The Hybrid Model

In practice, the most robust enterprise architectures combine zero-copy for the common path with selective copying for specialised cases:
- Zero-copy data sharing for real-time, governance-sensitive access
- Selective ETL copies for heavy, repeatable workloads that need query-optimised physical layouts
- Materialised views or aggregations where the transformation is stable and the query rate is high

The 2024–2025 industry data supports this: zero-copy ingestion grew 341% YoY to 15 trillion records — but even its advocates recommend hybrid models for high-frequency sub-second reads and complex transformations.

---

## Part 7 — Emerging Directions to Watch

**io_uring zero-copy receive (Linux 6.15, 2025):** The OS now supports zero-copy on the receive path as well as the send path. This closes the last major gap in OS-level zero-copy for bidirectional network I/O. Watch for application frameworks (io_uring-native HTTP servers, database network layers) to adopt this over the next 2–3 years.

**DMA-BUF integration (Linux 6.16):** io_uring zero-copy receive now supports DMA-BUF buffers, enabling direct NIC-to-GPU data paths without CPU involvement. Relevant for AI inference serving and GPU-accelerated networking.

**Arrow Flight SQL:** Arrow Flight extended with SQL query semantics — enables zero-copy analytical query results over a standard query interface. Adoption is accelerating across the OLAP/lakehouse vendor landscape.

**Universal Data Catalog / Open Table Registry:** Nessie (Project Nessie by Dremio), Iceberg REST Catalog, and Gravitino (Apache incubator) are converging on a standard catalog protocol that any engine can speak. This is the infrastructure layer that makes engine-agnostic zero-copy lakehouse access practical at enterprise scale.

**RDMA for AI training:** As GPU clusters scale (H100, H200, B200), the network fabric between GPUs is moving from InfiniBand RDMA to RoCEv2 (RDMA over Converged Ethernet). Zero-copy memory transfer between GPU nodes at sub-microsecond latency is now table stakes for large model training.

---

## Part 8 — Recommended Actions for the Enterprise Architect

### Immediate (contextual evaluation)
- [ ] When evaluating any data platform or integration vendor, ask explicitly: "Where does the data physically reside after onboarding, and which operations require copying it?" Probe for "copy-first" hidden behind zero-copy marketing.
- [ ] When designing a data sharing architecture for new consumers, default to zero-copy access grants over new ETL pipelines unless the consumer needs a fundamentally different data shape.

### Short-term (capability building)
- [ ] Map existing data duplication: for any major dataset, count how many physical copies exist across the estate. In most enterprises this is 3–7 copies. Each copy is a governance liability and a staleness risk.
- [ ] Evaluate open table formats (Iceberg or Delta Lake) as the single-copy storage layer for analytical data. If multiple engines (Spark, Athena, Trino, BigQuery) need to query the same data, one physical copy with multiple readers is the correct architecture.

### Long-term (architectural direction)
- [ ] Adopt the Logical-First principle as the default integration stance: never copy data as the first step; start with federation and federated query, copy only when a specific access pattern demands it.
- [ ] Ensure your data governance framework covers zero-copy access: column-level masking, row-level security, audit logging, and schema evolution policies must apply to shared data at the source, not just to copies.

---

## Contrarian View

**The strongest argument against zero-copy as a default:** Copies exist for good reasons. A materialised copy optimised for a specific query pattern will almost always outperform a live federated query. The ETL pipeline that was "unnecessary overhead" last year is also the thing that isolates consumers from source system performance incidents, schema changes, and access policy changes. Zero-copy creates tight temporal and operational coupling: when the source system is slow, all consumers are slow; when the source schema changes, all consumers break simultaneously. For large-scale, predictable, repeatable workloads — your weekly executive dashboard, your monthly regulatory report — the copy-first model is operationally saner, cheaper to query, and easier to reason about. Zero-copy is not the destination; it is the right answer for the specific scenarios where staleness, duplication cost, or governance complexity make copying genuinely worse.

---

## Confidence and Gaps

**High confidence:**
- OS/systems-level zero-copy mechanisms and their copy counts — well-documented in kernel source and academic literature
- Kafka's use of sendfile — confirmed in Confluent documentation and Kafka design docs
- Apache Arrow in-memory format and zero-copy reads — confirmed in Arrow project documentation
- Enterprise zero-copy data sharing patterns — confirmed across multiple independent vendor sources

**Medium confidence:**
- Specific performance numbers (81% for mmap, 91% for sendfile) — from a single Java benchmark, hardware/workload dependent
- Specific credit costs for Snowflake zero-copy (70 vs 2,000) — from third-party blog, not Snowflake official documentation, may be outdated
- io_uring adoption trajectory — rapidly moving target, Linux 6.15/6.16 features are very recent

**Gaps:**
- No benchmarks found for Belron-specific workload patterns (e.g., high-frequency small message IoT telemetry vs large analytical batch)
- RDMA adoption in standard enterprise cloud (Azure, AWS) vs HPC/specialist environments not fully explored
- Specific open-source project maturity for Arrow Flight SQL in production is unclear from public sources

---

## Sources

- [Zero-Copy: Principle and Implementation (Medium)](https://medium.com/@kaixin667689/zero-copy-principle-and-implementation-9a5220a62ffd)
- [A Deep Dive into Zero-Copy Networking and io_uring (Medium)](https://medium.com/@jatinumamtora/a-deep-dive-into-zero-copy-networking-and-io-uring-78914aa24029)
- [Zero-Copy I/O and io_uring for High-Performance Async Servers (Medium)](https://medium.com/@QuarkAndCode/zero-copy-i-o-and-io-uring-for-high-performance-async-servers-a6c592ab8f1a)
- [IO_uring Zero Copy Receive Seeing DMA-BUF Support Slated For Linux 6.16 (Phoronix)](https://www.phoronix.com/news/IO_uring-ZCRX-DMA-BUF)
- [Zero-copy network transmission with io_uring (LWN.net)](https://lwn.net/Articles/879724/)
- [Zero Copy I: User-Mode Perspective (Linux Journal)](https://www.linuxjournal.com/article/6345)
- [Zero-Copy And Linux-I/O (SoByte)](https://www.sobyte.net/post/2023-01/linux-io/)
- [The inner workings of TCP zero-copy](https://blog.tohojo.dk/2026/02/the-inner-workings-of-tcp-zero-copy.html)
- [Zero-Copy Data Transfer in Apache Kafka (Software Patterns Lexicon)](https://softwarepatternslexicon.com/kafka/2/4/3/)
- [Zero Copy: Optimising Data Transfer in Apache Kafka (Medium)](https://designvault.medium.com/title-zero-copy-optimizing-data-transfer-in-apache-kafka-8af7ee173288)
- [How Kafka Is so Performant If It Writes to Disk (Techie Shares)](https://andriymz.github.io/kafka/kafka-disk-write-performance/)
- [Kafka Design — Zero Copy (Confluent Documentation)](https://docs.confluent.io/platform/6.2/kafka/design.html)
- [High-Velocity Analytics: Kafka, Arrow Flight (Medium/TFMV)](https://medium.com/@tfmv/high-velocity-analytics-125017b27b05)
- [Exploring Apache Arrow: A Modern Framework for Efficient Data Interchange (Medium)](https://medium.com/towards-data-engineering/exploring-apache-arrow-a-modern-framework-for-efficient-data-interchange-a0d91e334a01)
- [Apache Arrow IPC Documentation](https://arrow.apache.org/docs/python/ipc.html)
- [Zero-Copy Data Sharing: Eliminating Duplication in Modern Architectures (Conduktor)](https://www.conduktor.io/glossary/zero-copy-data-sharing)
- [The Case for Zero Copy in the Modern Customer Data Stack (CMSWire)](https://www.cmswire.com/customer-data-platforms/the-case-for-zero-copy-in-the-modern-customer-data-stack/)
- [Introducing Logical-First Architecture, the Real "Zero-Copy" Architecture (Data Management Blog)](https://www.datamanagementblog.com/introducing-logical-first-architecture-the-real-zero-copy-architecture/)
- [Zero-ETL Data Sharing Across Clouds with Snowflake](https://www.snowflake.com/en/product/use-cases/zero-etl-data-sharing/)
- [Kernel Bypass Networking: DPDK, SPDK, and io_uring (Anshad Ameenza)](https://anshadameenza.com/blog/technology/2025-01-15-kernel-bypass-networking-dpdk-spdk-io_uring)
- [DPDK and Kernel Bypass: When Microseconds Matter More Than Your Sanity (The Internet Papers)](https://www.theinternetpapers.com/posts/dpdk-and-kernel-bypass-when-microseconds-matter-more-than-your-sanity.html)
- [Kernel Bypass Technologies (Damon's Blog)](https://www.damonyuan.com/tech/260203-kernel-bypass-technologies)
- [Z-stack: A High-performance DPDK-based Zero-copy TCP/IP Protocol Stack (NSF PAR)](https://par.nsf.gov/servlets/purl/10548466)

---

*Research by COG Auto-Research | 21 May 2026*
