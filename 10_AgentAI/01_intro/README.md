# 🍽️ DinnerPlugin – Italian Dinner Suggestion Plugin

This plugin provides random **Italian dinner dish suggestions** with estimated calorie counts. It's designed to be used with the [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel) framework and fits perfectly into AI-powered assistants or apps that want to enhance user interaction with culinary recommendations.

---

## 🤖 What Kind of AI Agent Is This?

This plugin is part of a **function-based AI agent**, also called a **task-oriented** or **plugin-calling agent**. It’s built to integrate with Microsoft Semantic Kernel and can be invoked by AI models to fulfill user intents like meal suggestions.

### 🔍 Agent Type: `Plugin-Based Function Agent`

| Feature                 | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🧠 Intelligent Logic     | Avoids repeating the same dish twice in a row                              |
| 🔌 Plugin Ready         | Easily importable as a SK plugin or callable from any LLM-compatible agent |
| 🍝 Task-Focused         | Designed to help users decide what to eat                                  |
| 💬 Interactive Support | Great for chatbots, smart kitchens, or assistants                          |

### 🧩 Example Use Case

Imagine a personal AI assistant that hears:

> _"I feel like something Italian but not too heavy tonight."_

Your agent can call:

```python
DinnerPlugin.get_random_dinner()

To respond with:

🥗 Caprese Salad - approx. 250 kcal/plate
