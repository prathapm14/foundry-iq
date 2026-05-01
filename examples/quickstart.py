from foundry_iq import FoundryIQClient, AgentConfig


def main() -> None:
    # In real usage you would pass Azure credentials; here it's optional.
    client = FoundryIQClient(
        credential=None,
        subscription_id="your-subscription-id",
        resource_group="your-resource-group",
    )

    kb = client.create_knowledge_base(
        name="Customer Support KB",
        description="Customer support documentation and FAQs",
    )

    kb.add_source(
        {
            "type": "sharepoint",
            "url": "https://contoso.sharepoint.com/sites/support",
            "document_types": ["*.pdf", "*.docx"],
        }
    )

    kb.build()

    agent_config = AgentConfig(
        model="gpt-4",
        system_prompt=(
            "You are a helpful customer support agent. "
            "Use the knowledge base to answer customer questions accurately."
        ),
        knowledge_bases=[kb.id],
        search_strategy="hybrid",
        streaming=False,
    )

    agent = client.create_agent(name="Support Agent", config=agent_config)

    response = agent.chat("How do I reset my password?")
    print(response.content)


if __name__ == "__main__":
    main()
