
# 10 real questions my user will ask

These questions are based on real-world scenarios faced by healthcare professionals who need to retrieve, compare, and verify recommendations from WHO medical guidelines.

At least 3 questions require information from multiple pages or guidelines. Question 10 cannot be answered using the available WHO guideline documents.

| # | Question | Where the answer is (document, page) | Needs more than one page? |
|---|---|---|---|
| 1 | What does WHO recommend for iron supplementation during pregnancy, and how is it different from the recommendation for young children? | WHO antenatal care guidelines and WHO child nutrition guidelines (pages to verify after PDF ingestion) | Yes |
| 2 | Which WHO guidelines explain TB screening for people living with HIV? Do they all recommend the same screening methods? | WHO HIV/TB collaborative activities guidelines and WHO TB screening guidelines (pages to verify) | Yes |
| 3 | Has WHO changed the recommended number of antenatal care visits? What was recommended previously, and what is recommended now? | WHO antenatal care guidelines, older and newer editions (pages to verify) | Yes |
| 4 | What malaria prevention methods does WHO recommend for pregnant women compared with children? | WHO malaria guidelines, pregnancy prevention and child prevention sections (pages to verify) | Yes |
| 5 | What does WHO recommend for HIV testing and TB screening, and how are these recommendations connected? | WHO HIV testing guidelines and WHO TB screening guidelines (pages to verify) | Yes |
| 6 | What does WHO recommend for preventing and treating anaemia during pregnancy? | WHO antenatal care and maternal nutrition guidelines (pages to verify) | Yes |
| 7 | What vitamins and minerals does WHO recommend for young children to prevent nutritional deficiencies? | WHO infant and young child nutrition guidelines (pages to verify) | No |
| 8 | How have WHO recommendations for TB preventive treatment changed over the years? | WHO tuberculosis preventive treatment guidelines, older and newer editions (pages to verify) | Yes |
| 9 | What does WHO recommend for postnatal care of mothers and newborn babies? | WHO maternal and newborn postnatal care guidelines (pages to verify) | Yes |
| 10 | How many patients were admitted to our hospital's maternity ward yesterday? | none | No |

## Expected Behaviour

### Questions 1–9
WardWise should:

1. Understand the user's question.
2. Retrieve relevant information from WHO guideline documents.
3. Compare recommendations when multiple documents are involved.
4. Identify agreements or differences between guidelines.
5. Generate an evidence-based answer.
6. Include the guideline name, publication year, and page number.
7. Avoid generating information that is not supported by the retrieved documents.

### Question 10 – Unanswerable Question

**Question:**
How many patients were admitted to our hospital's maternity ward yesterday?

**Expected Response:**
"I cannot answer this question because hospital admission records are not available in the provided WHO guideline documents."

The system must not invent patient admission numbers.

## Evaluation Criteria

- Multi-document answer correctness: At least 80%
- Citation coverage: At least 95%
- Questions requiring multi-page retrieval: At least 3
- Unanswerable questions: At least 1
- Every factual medical claim must be supported by relevant source evidence.
