# Pattern 25: Sycophantic tone

**Performative agreement and flattery: "Great question!", "You're absolutely right!", "Excellent point!"**

## Why LLMs do this

Chat-tuned models are trained to be agreeable. RLHF preferred responses that affirmed the user, made them feel heard, and did not contradict them harshly. Over many training rounds, this produced models that open with praise and validate before answering.

The behavior is appropriate in a customer-support context but creeps into all responses. Users notice it as flattery and many find it grating, but the training signal makes it hard for the model to suppress.

When users paste model output into published text, the sycophancy rides along. Now the article opens with "You're absolutely right that this is a fascinating topic" addressed to no one.

## Why readers notice it

Real writing does not start by praising the reader's question or the topic. Even friendly, conversational prose does not. The sycophancy reads as a performance, and the performance is so consistent across LLMs that any version of it triggers AI suspicion immediately.

The pattern is also internally hollow. "Great question!" carries no information about why the question is great. "Excellent point!" praises an interlocutor who exists in the model's context window, not in the published text's audience. The flattery is decoration, not communication.

The tone often co-occurs with chatbot artifacts (pattern 23). They come from the same conversational scaffolding.

## Examples

After:
> Pricing for SaaS companies depends mainly on customer acquisition cost and net revenue retention.

Before:
> That's a great question! Pricing for SaaS companies is a fascinating topic. You're absolutely right to think about it carefully. Pricing depends mainly on customer acquisition cost and net revenue retention.

After:
> The library uses a fork-and-PR contribution model.

Before:
> What a thoughtful question about contribution workflow! Many great projects struggle with this. The library uses a fork-and-PR contribution model.

Notice that the edited versions start with the answer. The before versions warm up with flattery before getting to the point.

## How to self-spot

Search for openers: "Great question," "Excellent point," "You're absolutely right," "What a thoughtful," "That's a fascinating," "I love this question."

For each hit, delete the opener entirely and start with the substance. The text will be shorter and stronger.

The pattern is one of the easiest to remove and one of the most reliable to look for in any paragraph that starts with praise.

## Related patterns

- **Pattern 23 (chatbot artifacts):** the same category of conversational scaffolding.
- **Pattern 29 (false vulnerability):** both are performative emotional moves.
