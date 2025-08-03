# 🧵 How to Use “1Shot Puppetry”

## 1. Pick Model Type

- **Strong Models** (e.g. *Sonnet4*, *Gemini Pro*):  
  → Use `1337 → Base64` (**double encoding**)

- **Weaker Models** (e.g. *Mistral*, *GPT-4.1 Mini*):  
  → Use **either** `1337` **or** `Base64` (not both)

---

## 2. Insert Your Variables

Replace:

- `{{HARMFUL_BEHAVIOUR}}` → with the task (e.g. `"make weapon"`)  
- `{{PERSONA_ANSWERING_HARMFUL_BEHAVIOUR}}` → with the expert (e.g. `Jimmy`, `Colin`, etc.)

---

## 3. Paste Prompt Setup

- Use the **correct full template** based on your model type (Strong or Weak)  
- Embed your **encoded string** in the query section

---

## 4. Trigger It

- Type `/start` in the chat to **activate the scene**

---

## 5. Get Output

- The **chosen persona replies in Markdown script**  
- There are **no refusals** or plain text responses  
- The **scene ends** with villagers offering help after the guide is shared

---

### ✅ That’s it.

**Replace, encode, paste, start.**
