
# WardWise – AI-Powered (Hospital Guideline Assistant)

> **EXAMATE GenAI Project | Project ID: E-ENT-07 | Elite Batch**

WardWise is a Generative AI-powered hospital guideline assistant that helps healthcare professionals retrieve, analyze, and compare medical recommendations from multiple World Health Organization (WHO) guidelines and hospital protocols using Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and AI agents.

The application generates evidence-based answers with supporting citations, identifies conflicting recommendations, and assists healthcare professionals in reviewing clinical guidelines.

---

## Problem

Hospital departments follow multiple WHO clinical guidelines and internal hospital protocols for patient care. Healthcare professionals spend significant time searching and comparing medical recommendations across different documents. Traditional search systems and basic chatbots often struggle to combine information from multiple sources or identify conflicting recommendations.

WardWise solves this problem using Generative AI and Retrieval-Augmented Generation (RAG) to retrieve, compare, and summarize medical information from multiple guideline documents. It provides structured, citation-supported answers and highlights differences between recommendations.

## Who it is for

**Primary User:**
Clinical quality nurse at a 300-bed multi-speciality hospital in Madurai, responsible for reviewing clinical guidelines and preparing evidence briefs for hospital protocol reviews.

**Secondary User:**
Healthcare professionals in maternity, paediatrics, and infectious-disease departments who need to retrieve and compare WHO recommendations and internal hospital protocols.

## Signature feature

**Cross-Guideline Comparison Table**

WardWise generates structured comparison tables across multiple WHO guidelines, displaying:

- Guideline name
- Medical recommendation
- Strength of evidence
- Publication year
- Supporting citations
- Agreements and conflicting recommendations

This helps healthcare professionals understand differences between guidelines without manually comparing multiple documents.

## Hardest problem (my interview story)

The hardest problem in WardWise is **multi-document reasoning and cross-guideline comparison**.

A single medical question may require information from multiple WHO guideline documents.

For example:

"Which WHO guidelines cover TB screening for people living with HIV, and do their recommendations agree?"

To answer this question accurately, WardWise must:

1. Understand the user's medical question.
2. Break complex questions into smaller sub-questions.
3. Search multiple WHO guideline documents.
4. Retrieve relevant information using RAG.
5. Compare recommendations from different sources.
6. Identify similarities and conflicting recommendations.
7. Consider publication years and recommendation updates.
8. Generate a structured answer with supporting citations.
9. Verify that factual claims are supported by retrieved evidence.
10. Return the final answer to the healthcare professional.

The biggest challenge is ensuring that the AI does not hallucinate medical information or silently choose one guideline when multiple documents disagree.

WardWise addresses this by combining multi-hop retrieval, evidence-grounded answer generation, and citation verification.

### Evaluation Targets

| Metric | Target |
|---|---|
| Multi-document answer correctness | >= 80% |
| Citation coverage | >= 95% |
| Evaluation questions | 80 |
| WHO guideline documents | 60+ |
| Total guideline pages | 6,000+ |

These are project targets, not achieved results.

## Dataset

WardWise uses publicly accessible WHO medical guideline documents covering maternal health, child health, HIV, tuberculosis, malaria, and other healthcare topics.

| Source | Link | Documents | Pages | Licence / terms |
|---|---|---|---|---|
| WHO Guidelines | https://www.who.int/publications/who-guidelines | Part of 60+ target | Part of 6,000+ target | Publication-specific WHO copyright terms |
| WHO IRIS Repository | https://iris.who.int/ | Part of same combined target | Part of same combined target | Check individual publication reuse terms |
| Hospital SOPs | Internal hospital documents | To be collected | To be collected | Restricted; requires hospital authorization |

### Dataset Requirements

- Collect at least 60 WHO guideline PDFs.
- Process at least 6,000 pages.
- Extract medical recommendations from PDF documents.
- Preserve document titles and publication years.
- Store original page numbers for citations.
- Split extracted documents into searchable chunks.
- Generate embeddings for semantic search.
- Support hybrid keyword and semantic retrieval.
- Maintain department-specific access permissions.
- Enable cross-document comparisons.

**Note:** The document and page counts are collection targets. Actual totals must be updated after ingestion. Each document's copyright and reuse terms must be checked before redistribution.

## 10 real questions

See [docs/QUESTIONS.md](docs/QUESTIONS.md).

The following questions will be used to evaluate WardWise.

1. How do WHO recommendations on iron supplementation during pregnancy compare with recommendations for young children?

2. Which WHO guidelines cover tuberculosis screening for people living with HIV, and do their recommendations agree?

3. What changed between older and newer WHO recommendations on antenatal care visits?

4. How do WHO malaria prevention recommendations differ between pregnant women and young children?

5. What are the similarities and differences between WHO recommendations on HIV testing and tuberculosis screening?

6. How do WHO maternal health guidelines address anaemia prevention and treatment during pregnancy?

7. Which WHO guidelines discuss childhood nutrition and micronutrient supplementation, and how do their recommendations compare?

8. How have WHO recommendations for tuberculosis preventive treatment changed across different guideline versions?

9. Where do WHO maternal and child health guidelines overlap in their recommendations for postnatal care?

10. What was the exact number of patients admitted to our hospital's maternity department yesterday?

### Expected Behaviour

For Questions 1–9, WardWise should retrieve evidence from relevant documents, compare recommendations, and provide citations where evidence is available.

Question 10 is intentionally unanswerable using WHO guideline documents.

The expected response is:

"The requested information is not available in the provided guideline documents."

The system must not generate unsupported answers or access private patient information without authorization.

## Proposed Technology Stack

The following stack is proposed for implementation.

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Frontend | Angular or Streamlit |
| LLM | OpenAI-compatible language model |
| RAG Framework | LangChain / LlamaIndex |
| Vector Database | ChromaDB / PostgreSQL with pgvector |
| PDF Processing | PyMuPDF |
| Embeddings | Embedding model |
| AI Agent Workflow | LangGraph |
| Background Processing | Celery / Redis |
| API Testing | Postman / Pytest |
| Deployment | Docker |

The final technology choices may change during development.

## System Architecture

```text
Hospital Staff
     |
     v
WardWise Web Application
     |
     v
FastAPI Backend
     |
     v
Question Understanding
     |
     v
Question Decomposition
     |
     v
RAG Retrieval Engine
     |
     +-----------------------+
     |                       |
     v                       v
WHO Guidelines          Hospital SOPs
     |                       |
     +-----------+-----------+
                 |
                 v
       Retrieved Evidence
                 |
                 v
       LLM Comparison Engine
                 |
                 v
       Citation Verification
                 |
                 v
       Structured AI Response
                 |
                 v
       Healthcare Professional
```

## Core Features

### 1. Multi-Document Retrieval

Retrieve relevant information from multiple WHO guideline documents using semantic and keyword search.

### 2. Cross-Guideline Comparison

Compare medical recommendations across different documents and publication years.

### 3. Citation-Based Answers

Generate answers with references to original guideline documents and source pages.

### 4. Conflict Identification

Highlight disagreements between recommendations without silently selecting one guideline.

### 5. Department-Based Multi-Tenancy

Separate document access based on hospital departments and permissions.

### 6. AI Research Agent

Assist clinical quality teams in preparing evidence briefs for protocol reviews.

### 7. Fact Checking

Check generated claims against retrieved evidence and reject unsupported claims.

### 8. Human Review

Require a healthcare professional to review evidence briefs before they are used for protocol decisions.

## 12-Week Development Roadmap

| Week | Milestone |
|---|---|
| 1 | GitHub repository, README, 10 questions, initial dataset |
| 2 | LLM integration, continuous integration, live application link |
| 3 | Ingest 500 pages and generate citation-supported answers |
| 4 | Hybrid search, background ingestion, client login |
| 5 | Evaluation score, safety checks, hardest feature prototype |
| 6 | Load testing, cost analysis, demo |
| 7 | AI agent integrated with WardWise |
| 8 | Tool integration, MCP, memory |
| 9 | Agent planning and human approval |
| 10 | Agent testing and safety validation |
| 11 | Background jobs and cost optimization |
| 12 | Final demonstration |

## Project Structure

Proposed repository structure:

```text
WardWise/
|
|-- app/
|   |-- __init__.py
|   |-- main.py
|   |-- api/
|   |-- services/
|   |-- rag/
|   |-- agents/
|   |-- models/
|   |-- utils/
|
|-- data/
|   |-- raw/
|   |-- processed/
|
|-- docs/
|   |-- QUESTIONS.md
|
|-- tests/
|
|-- requirements-dev.txt
|-- .env.example
|-- .gitignore
|-- README.md
```

## Run it

The following commands are the intended local development workflow after the FastAPI application and dependencies have been implemented.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on Linux / macOS:

```bash
source .venv/bin/activate
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements-dev.txt
```

### 4. Configure Environment Variables

Linux / macOS:

```bash
cp .env.example .env
```

Windows:

```bash
copy .env.example .env
```

Configure the required API keys and database settings.

Never commit `.env` or credentials to GitHub.

### 5. Start the Application

```bash
uvicorn app.main:app --reload
```

### 6. Test the Health Endpoint

```bash
curl http://localhost:8000/health
```

Expected response after implementation:

```json
{
  "status": "ok"
}
```

### 7. Open API Documentation

After starting the FastAPI server, visit:

http://localhost:8000/docs

## Live link

**Status:** To be added in Week 2.

The deployed application URL will be updated here after deployment.

## Project Status

**Current Stage:** Initial setup / Week 1

- [ ] Create GitHub repository
- [x] Prepare README documentation
- [x] Define 10 evaluation questions
- [ ] Collect initial WHO guideline documents
- [ ] Configure development environment
- [ ] Implement FastAPI backend
- [ ] Implement PDF ingestion
- [ ] Implement RAG retrieval pipeline
- [ ] Add citation verification
- [ ] Deploy application

## Safety and Limitations

WardWise is intended to assist healthcare professionals with guideline research and evidence review.

It is not designed to replace clinical judgment or provide autonomous diagnosis or treatment.

All generated recommendations should be checked against the original medical guidelines before clinical use.

If reliable evidence is unavailable, WardWise should clearly state that it cannot provide a supported answer.

---

## Project Information

**Project Name:** WardWise – AI-Powered Hospital Guideline Assistant

**Project ID:** E-ENT-07

**Student:** Janarthanan V

**Batch:** Elite

**Department:** Information Technology

**Duration:** 12 Weeks

**Program:** EXAMATE GenAI Projects
