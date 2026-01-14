# Foundry IQ:  Complete Guide to Multi-Source AI Knowledge Bases and Agent Creation

> A comprehensive guide to Microsoft Foundry IQ, multi-source knowledge bases, and creating intelligent AI agents in the Microsoft Foundry ecosystem.

![Microsoft Foundry](https://img.shields.io/badge/Microsoft-Foundry-blue)
![AI Agents](https://img.shields.io/badge/AI-Agents-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📋 Table of Contents

- [Introduction](#introduction)
- [What is Foundry IQ?](#what-is-foundry-iq)
- [Key Features & Capabilities](#key-features--capabilities)
- [Architecture Overview](#architecture-overview)
- [Getting Started](#getting-started)
- [Creating Agents in Microsoft Foundry](#creating-agents-in-microsoft-foundry)
- [Step-by-Step Implementation](#step-by-step-implementation)
- [Agent Framework Integration](#agent-framework-integration)
- [Code Examples](#code-examples)
- [Best Practices](#best-practices)
- [Security & Compliance](#security--compliance)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)

---

## 🎯 Introduction

**Microsoft Foundry IQ** is an advanced enterprise solution designed to build agentic AI applications that require access to multi-source knowledge bases.  It revolutionizes how organizations leverage their distributed data by providing intelligent agents with context-rich, accurate responses through automated retrieval and synthesis of information from disparate data sources.

### Why Foundry IQ?

- **Unified Knowledge Access**: Connect to Azure stores, SharePoint, OneLake, MCP servers, and web content
- **Agentic Retrieval**: Automated query planning, decomposition, and synthesis
- **Enterprise-Ready**: Built-in security, compliance, and governance
- **Developer-Friendly**: Support for Python, C#, JavaScript, and REST APIs
- **Cost-Efficient**: Optimized token usage and resource management

---

## 🚀 What is Foundry IQ? 

Foundry IQ is Microsoft's **intelligent knowledge orchestration platform** that enables AI agents to access, reason over, and synthesize information from multiple enterprise data sources seamlessly. 

### Core Capabilities

1. **Multi-Source Integration**
   - Azure AI Search
   - SharePoint Online
   - OneLake (Microsoft Fabric)
   - MCP (Model Context Protocol) Servers
   - Web content and external APIs
   - Custom data connectors

2. **Agentic Retrieval Engine**
   - Automatic query planning and decomposition
   - Parallel processing of sub-queries
   - Keyword, vector, and hybrid search
   - Semantic reranking for relevance
   - Source-attributed answer synthesis

3. **Context Management**
   - Dynamic context window optimization
   - Intelligent chunking strategies
   - Citation and source tracking
   - Multi-turn conversation support

---

## ✨ Key Features & Capabilities

### 1. **Multi-Source Knowledge Base Integration**

Foundry IQ knowledge bases unify internal and external sources, allowing agents to seamlessly access: 

- **Internal Sources:**
  - Company documents and wikis
  - Databases and data warehouses
  - Email and communication archives
  - CRM and ERP systems

- **External Sources:**
  - Web content and APIs
  - Industry databases
  - Partner systems
  - Public knowledge bases

**Benefits:**
- Reuse existing Azure AI Search assets
- No manual retrieval pipeline development
- Configurable reasoning depth per query
- Automatic index updates and synchronization

### 2. **Automated Grounding & Context Management**

The agentic retrieval system provides:

```
User Query → Query Planning → Decomposition → Parallel Search
                                                    ↓
Answer Synthesis ← Source Attribution ← Semantic Reranking
```

**Process Flow:**
1. **Query Understanding**:  Analyze user intent and extract key concepts
2. **Decomposition**: Break complex queries into manageable sub-queries
3. **Parallel Execution**: Run searches simultaneously across sources
4. **Reranking**: Apply semantic scoring for relevance
5. **Synthesis**: Combine results with source attribution
6. **Validation**: Ensure factual accuracy and completeness

### 3. **Agent Framework Integration via MCP**

**Model Context Protocol (MCP)** enables: 
- Secure, efficient tool calls between agents and knowledge bases
- Language-agnostic integration (Python, C#, JS)
- Role-based access control (RBAC)
- Managed identity authentication
- RESTful API access

### 4. **Enterprise Security, Compliance & Governance**

**Microsoft Purview Integration:**
- Document-level access control
- Sensitivity label enforcement
- Data loss prevention (DLP)
- Audit trails and monitoring
- Compliance reporting

**Security Features:**
- Entra ID authentication
- Managed identities
- Encryption at rest and in transit
- Network isolation options
- Private endpoint support

### 5. **Efficiency & Developer Experience**

**Resource Optimization:**
- Automatic iteration control
- Token usage optimization
- Caching and deduplication
- Streaming responses
- Configurable timeout policies

**Developer Tools:**
- SDK support (Python, C#, JavaScript)
- REST API with OpenAPI specs
- CLI tools for management
- Visual Studio Code extensions
- Comprehensive documentation

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        USER / APPLICATION                    │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   FOUNDRY AGENT SERVICE                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Agent 1    │  │   Agent 2    │  │   Agent N    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
└─────────┼──────────────────┼──────────────────┼─────────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
         ┌─────────────────────────────────────────┐
         │      MODEL CONTEXT PROTOCOL (MCP)       │
         └─────────────────┬───────────────────────┘
                           │
                           ▼
         ┌─────────────────────────────────────────┐
         │           FOUNDRY IQ PLATFORM           │
         │  ┌─────────────────────────────────┐   │
         │  │   Knowledge Base Orchestrator   │   │
         │  └─────────────────────────────────┘   │
         │  ┌─────────────────────────────────┐   │
         │  │   Agentic Retrieval Engine      │   │
         │  └─────────────────────────────────┘   │
         └──────────────────┬──────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Azure Search │   │  SharePoint  │   │   OneLake    │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ MCP Servers  │   │  Web Sources │   │  Custom DB   │
└──────────────┘   └──────────────┘   └──────────────┘
```

---

## 🎬 Getting Started

### Prerequisites

- **Azure Subscription** with appropriate permissions
- **Azure AI Foundry** access
- **Development Environment**:  Visual Studio Code or preferred IDE
- **SDKs Installed**:
  - Python 3.8+ (with `azure-ai-foundry` SDK)
  - Or .NET 6.0+ (with Azure AI SDK)
  - Or Node.js 16+ (with Azure SDK for JS)

### Initial Setup

#### 1. **Set Up Azure AI Foundry Hub**

```bash
# Install Azure CLI
az login

# Create a resource group
az group create --name foundry-rg --location eastus

# Create an AI Foundry hub
az ml workspace create \
  --name my-foundry-hub \
  --resource-group foundry-rg \
  --location eastus \
  --kind hub
```

#### 2. **Install Required SDKs**

**Python:**
```bash
pip install azure-ai-foundry
pip install azure-identity
pip install openai
```

**C# (.NET):**
```bash
dotnet add package Azure.AI.Foundry
dotnet add package Azure.Identity
```

**JavaScript:**
```bash
npm install @azure/ai-foundry
npm install @azure/identity
```

#### 3. **Configure Authentication**

```python
# Python example
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```

---

## 🤖 Creating Agents in Microsoft Foundry

### What is a Foundry Agent?

A **Foundry Agent** is an AI-powered assistant that can:
- Understand and respond to natural language
- Access multiple knowledge sources
- Execute tools and functions
- Maintain conversation context
- Make decisions based on retrieved information

### Agent Creation Workflow

```
1. Define Agent Purpose & Scope
            ↓
2. Create Knowledge Base
            ↓
3. Configure Data Sources
            ↓
4. Set Up Agent Instance
            ↓
5. Connect Knowledge Base
            ↓
6. Configure Tools & Functions
            ↓
7. Test & Deploy
            ↓
8. Monitor & Optimize
```

---

## 📝 Step-by-Step Implementation

### Step 1: Create a Foundry IQ Knowledge Base

#### Using Azure Portal

1. Navigate to **Azure AI Foundry** portal
2. Select your **Hub** resource
3. Go to **Knowledge Bases** section
4. Click **+ Create Knowledge Base**
5. Configure:
   - **Name**: `my-enterprise-kb`
   - **Description**: Enterprise knowledge repository
   - **Search Service**: Select or create Azure AI Search

#### Using Python SDK

```python
from azure.ai.foundry import FoundryClient
from azure.ai.foundry.models import KnowledgeBase, DataSource
from azure.identity import DefaultAzureCredential

# Initialize client
credential = DefaultAzureCredential()
client = FoundryClient(
    endpoint="https://my-foundry-hub.api.azureml.ms",
    credential=credential
)

# Create knowledge base
kb = client.knowledge_bases.create(
    name="my-enterprise-kb",
    description="Enterprise knowledge repository",
    search_service_connection="my-search-service"
)

print(f"Knowledge Base Created: {kb.id}")
```

### Step 2: Add Data Sources to Knowledge Base

#### Connect SharePoint

```python
from azure.ai.foundry.models import SharePointDataSource

sharepoint_source = SharePointDataSource(
    name="company-docs",
    site_url="https://contoso.sharepoint.com/sites/engineering",
    document_library="Shared Documents",
    credential_type="managed_identity"
)

# Add to knowledge base
client.knowledge_bases.add_data_source(
    knowledge_base_id=kb.id,
    data_source=sharepoint_source
)
```

#### Connect Azure Blob Storage

```python
from azure.ai.foundry.models import BlobDataSource

blob_source = BlobDataSource(
    name="product-manuals",
    connection_string="<connection-string>",
    container_name="manuals",
    file_patterns=["*.pdf", "*.docx"]
)

client.knowledge_bases.add_data_source(
    knowledge_base_id=kb.id,
    data_source=blob_source
)
```

#### Connect OneLake (Microsoft Fabric)

```python
from azure.ai.foundry.models import OneLakeDataSource

onelake_source = OneLakeDataSource(
    name="analytics-data",
    workspace_id="<workspace-id>",
    lakehouse_id="<lakehouse-id>",
    table_names=["sales", "inventory"]
)

client.knowledge_bases.add_data_source(
    knowledge_base_id=kb.id,
    data_source=onelake_source
)
```

#### Connect MCP Server

```python
from azure.ai.foundry.models import MCPDataSource

mcp_source = MCPDataSource(
    name="custom-mcp-server",
    server_url="https://mcp.contoso.com/api",
    authentication={
        "type": "bearer",
        "token_provider": "managed_identity"
    }
)

client.knowledge_bases.add_data_source(
    knowledge_base_id=kb.id,
    data_source=mcp_source
)
```

### Step 3: Create an Agent

```python
from azure.ai.foundry.models import Agent, AgentConfig

# Define agent configuration
agent_config = AgentConfig(
    name="enterprise-assistant",
    description="AI assistant with access to enterprise knowledge",
    model="gpt-4",
    temperature=0.7,
    max_tokens=4000,
    instructions="""
    You are an enterprise AI assistant with access to company knowledge bases.
    Always cite your sources and provide accurate, helpful information.
    If you're unsure about something, acknowledge the uncertainty.
    """
)

# Create the agent
agent = client.agents.create(
    config=agent_config,
    knowledge_base_ids=[kb.id]
)

print(f"Agent Created: {agent.id}")
```

### Step 4: Add Tools to Agent

```python
from azure.ai.foundry.models import FunctionTool

# Define a custom function tool
def search_inventory(product_name: str) -> dict:
    """Search product inventory"""
    # Implementation here
    return {"product": product_name, "quantity": 100}

# Register tool with agent
inventory_tool = FunctionTool(
    name="search_inventory",
    description="Search for product inventory levels",
    function=search_inventory,
    parameters={
        "type": "object",
        "properties": {
            "product_name": {
                "type": "string",
                "description": "Name of the product"
            }
        },
        "required": ["product_name"]
    }
)

client.agents.add_tool(
    agent_id=agent.id,
    tool=inventory_tool
)
```

### Step 5: Test the Agent

```python
# Start a conversation
thread = client.threads.create()

# Send a message
message = client.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What are the latest updates on Project Phoenix?"
)

# Run the agent
run = client.threads.runs.create(
    thread_id=thread.id,
    agent_id=agent.id
)

# Wait for completion
while run.status in ["queued", "in_progress"]:
    time.sleep(1)
    run = client.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

# Get response
messages = client.threads.messages.list(thread_id=thread.id)
for msg in messages:
    if msg.role == "assistant":
        print(f"Agent: {msg.content}")
        # Print citations
        for citation in msg.citations:
            print(f"  Source: {citation.source} - {citation.url}")
```

---

## 🔧 Agent Framework Integration

### Using LangChain with Foundry IQ

```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import AzureChatOpenAI
from langchain.tools import Tool
from azure.ai.foundry import FoundryClient

# Initialize Foundry client
foundry_client = FoundryClient(
    endpoint="https://my-foundry-hub.api.azureml.ms",
    credential=DefaultAzureCredential()
)

# Create a tool that queries Foundry IQ
def query_foundry_kb(query: str) -> str:
    """Query the Foundry IQ knowledge base"""
    result = foundry_client.knowledge_bases.query(
        knowledge_base_id="my-kb-id",
        query=query,
        max_results=5
    )
    return result.answer

foundry_tool = Tool(
    name="FoundryKnowledgeBase",
    func=query_foundry_kb,
    description="Query enterprise knowledge base for information"
)

# Create LangChain agent with Foundry tool
llm = AzureChatOpenAI(
    deployment_name="gpt-4",
    temperature=0.7
)

agent = create_openai_functions_agent(
    llm=llm,
    tools=[foundry_tool],
    prompt="You are a helpful assistant with access to enterprise knowledge."
)

agent_executor = AgentExecutor(agent=agent, tools=[foundry_tool])

# Use the agent
response = agent_executor.invoke({
    "input": "What are our Q4 sales targets?"
})
print(response["output"])
```

### Using Semantic Kernel with Foundry IQ

```python
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from azure.ai.foundry import FoundryClient

# Initialize kernel
kernel = sk.Kernel()

# Add Azure OpenAI service
kernel.add_chat_service(
    "chat",
    AzureChatCompletion(
        deployment_name="gpt-4",
        endpoint="https://my-openai.openai.azure.com",
        api_key="<api-key>"
    )
)

# Initialize Foundry client
foundry_client = FoundryClient(
    endpoint="https://my-foundry-hub.api.azureml.ms",
    credential=DefaultAzureCredential()
)

# Create a native function
@sk.kernel_function(
    name="QueryKnowledgeBase",
    description="Query the enterprise knowledge base"
)
def query_kb(query: str, context: sk.SKContext) -> str:
    result = foundry_client.knowledge_bases.query(
        knowledge_base_id="my-kb-id",
        query=query
    )
    return result.answer

# Register function
kernel.import_skill({"QueryKnowledgeBase": query_kb}, "FoundrySkills")

# Use in a semantic function
prompt = """
Answer the following question using the knowledge base:
{{$input}}

{{FoundrySkills.QueryKnowledgeBase $input}}
"""

semantic_function = kernel.create_semantic_function(prompt)
result = semantic_function("What is our return policy?")
print(result)
```

---

## 💡 Code Examples

### Example 1: Customer Support Agent

```python
from azure.ai.foundry import FoundryClient
from azure.identity import DefaultAzureCredential

# Initialize
credential = DefaultAzureCredential()
client = FoundryClient(
    endpoint="https://my-foundry-hub.api.azureml.ms",
    credential=credential
)

# Create support KB with multiple sources
kb = client.knowledge_bases.create(
    name="customer-support-kb",
    description="Customer support documentation and FAQs"
)

# Add product manuals
client.knowledge_bases.add_data_source(
    knowledge_base_id=kb.id,
    data_source={
        "type": "azure_blob",
        "name": "product-manuals",
        "container": "manuals",
        "connection_string": "<connection-string>"
    }
)

# Add FAQ from SharePoint
client.knowledge_bases.add_data_source(
    knowledge_base_id=kb.id,
    data_source={
        "type": "sharepoint",
        "name": "support-faqs",
        "site_url": "https://contoso.sharepoint.com/sites/support"
    }
)

# Create support agent
agent = client.agents.create(
    config={
        "name": "customer-support-agent",
        "model": "gpt-4",
        "instructions": """
        You are a friendly customer support agent. Help customers with:
        - Product information and specifications
        - Troubleshooting common issues
        - Return and warranty policies
        - General inquiries
        
        Always be polite, empathetic, and solution-oriented.
        Cite sources when providing technical information.
        """
    },
    knowledge_base_ids=[kb.id]
)

# Handle customer query
def handle_customer_query(customer_message: str):
    thread = client.threads.create()
    
    client.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=customer_message
    )
    
    run = client.threads.runs.create_and_wait(
        thread_id=thread.id,
        agent_id=agent.id
    )
    
    messages = client.threads.messages.list(thread_id=thread.id)
    return messages[-1].content

# Example usage
response = handle_customer_query(
    "How do I reset my device to factory settings?"
)
print(response)
```

### Example 2: Research Assistant with Web Sources

```python
from azure.ai.foundry import FoundryClient
from azure.ai.foundry.models import WebDataSource

client = FoundryClient(
    endpoint="https://my-foundry-hub.api.azureml.ms",
    credential=DefaultAzureCredential()
)

# Create research KB
kb = client.knowledge_bases.create(
    name="research-kb",
    description="Academic and industry research sources"
)

# Add web sources
web_sources = [
    "https://arxiv.org",
    "https://papers.nips.cc",
    "https://www.nature.com"
]

for url in web_sources:
    client.knowledge_bases.add_data_source(
        knowledge_base_id=kb.id,
        data_source=WebDataSource(
            name=f"web-{url}",
            url=url,
            crawl_depth=2,
            refresh_schedule="daily"
        )
    )

# Create research agent
agent = client.agents.create(
    config={
        "name": "research-assistant",
        "model": "gpt-4",
        "temperature": 0.3,
        "instructions": """
        You are a research assistant specializing in AI and machine learning.
        Provide accurate, well-cited information from academic sources.
        Explain complex concepts clearly and suggest related research areas.
        """
    },
    knowledge_base_ids=[kb.id]
)
```

### Example 3: Multi-Agent Collaboration

```python
from azure.ai.foundry import FoundryClient

client = FoundryClient(
    endpoint="https://my-foundry-hub.api.azureml.ms",
    credential=DefaultAzureCredential()
)

# Create specialized knowledge bases
sales_kb = client.knowledge_bases.create(name="sales-kb")
technical_kb = client.knowledge_bases.create(name="technical-kb")
legal_kb = client.knowledge_bases.create(name="legal-kb")

# Create specialized agents
sales_agent = client.agents.create(
    config={
        "name": "sales-agent",
        "model": "gpt-4",
        "instructions": "You are a sales specialist..."
    },
    knowledge_base_ids=[sales_kb.id]
)

technical_agent = client.agents.create(
    config={
        "name": "technical-agent",
        "model": "gpt-4",
        "instructions": "You are a technical expert..."
    },
    knowledge_base_ids=[technical_kb.id]
)

legal_agent = client.agents.create(
    config={
        "name": "legal-agent",
        "model": "gpt-4",
        "instructions": "You are a legal advisor..."
    },
    knowledge_base_ids=[legal_kb.id]
)

# Orchestration function
def handle_complex_query(query: str):
    # Determine which agents to involve
    agents_needed = classify_query(query)
    
    responses = {}
    for agent_type in agents_needed:
        if agent_type == "sales":
            responses["sales"] = query_agent(sales_agent, query)
        elif agent_type == "technical":
            responses["technical"] = query_agent(technical_agent, query)
        elif agent_type == "legal":
            responses["legal"] = query_agent(legal_agent, query)
    
    # Synthesize responses
    return synthesize_responses(responses)
```

---

## 🎯 Best Practices

### Knowledge Base Design

1. **Organize by Domain**
   - Create separate KBs for different business domains
   - Use clear, descriptive naming conventions
   - Document KB purpose and scope

2. **Data Source Selection**
   - Choose authoritative sources
   - Ensure data freshness with appropriate refresh schedules
   - Balance breadth and depth of coverage

3. **Indexing Strategy**
   - Use semantic chunking for long documents
   - Configure appropriate chunk sizes (512-1024 tokens)
   - Enable hybrid search (keyword + vector)

4. **Access Control**
   - Implement document-level permissions
   - Use managed identities for authentication
   - Regular access audits

### Agent Development

1. **Clear Instructions**
   - Define agent role and capabilities explicitly
   - Specify tone and communication style
   - Include edge case handling

2. **Context Management**
   - Limit conversation history length
   - Implement context summarization for long threads
   - Clear context when switching topics

3. **Error Handling**
   ```python
   try:
       response = agent.query(message)
   except KnowledgeBaseException as e:
       # Handle KB access errors
       logger.error(f"KB error: {e}")
       return "I'm having trouble accessing information. Please try again."
   except AgentException as e:
       # Handle agent errors
       logger.error(f"Agent error: {e}")
       return "I encountered an error processing your request."
   ```

4. **Testing**
   - Create comprehensive test suites
   - Test edge cases and failure modes
   - Monitor performance metrics

### Performance Optimization

1. **Query Optimization**
   - Use query decomposition for complex questions
   - Implement caching for frequent queries
   - Set appropriate timeouts

2. **Resource Management**
   - Monitor token usage
   - Implement rate limiting
   - Use streaming for long responses

3. **Monitoring**
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   
   # Enable telemetry
   configure_azure_monitor(
       connection_string="<connection-string>"
   )
   
   # Log agent interactions
   logger.info(f"Query: {query}")
   logger.info(f"Response time: {response_time}ms")
   logger.info(f"Tokens used: {tokens_used}")
   ```

---

## 🔒 Security & Compliance

### Authentication & Authorization

1. **Managed Identities**
   ```python
   from azure.identity import ManagedIdentityCredential
   
   credential = ManagedIdentityCredential()
   client = FoundryClient(
       endpoint="https://my-foundry-hub.api.azureml.ms",
       credential=credential
   )
   ```

2. **Role-Based Access Control (RBAC)**
   - Assign minimum required permissions
   - Use Azure AD groups for access management
   - Regular permission reviews

3. **Data Encryption**
   - Enable encryption at rest
   - Use TLS 1.2+ for data in transit
   - Implement key rotation policies

### Compliance

1. **Data Residency**
   - Choose appropriate Azure regions
   - Understand data processing locations
   - Document data flows

2. **Audit Logging**
   ```python
   # Enable audit logs
   client.knowledge_bases.update(
       knowledge_base_id=kb.id,
       settings={
           "audit_logging": {
               "enabled": True,
               "log_queries": True,
               "log_access": True
           }
       }
   )
   ```

3. **Microsoft Purview Integration**
   - Apply sensitivity labels
   - Enable DLP policies
   - Monitor compliance status

### Privacy

1. **PII Handling**
   - Implement PII detection and redaction
   - Use Azure AI Content Safety
   - Follow data minimization principles

2. **User Consent**
   - Obtain appropriate consents
   - Provide transparency about data usage
   - Honor data subject requests

---

## 🔍 Troubleshooting

### Common Issues

#### Issue: Agent not accessing knowledge base

**Symptoms**: Agent responses don't include KB information

**Solutions**:
```python
# Verify KB is connected to agent
agent_details = client.agents.retrieve(agent_id=agent.id)
print(f"Connected KBs: {agent_details.knowledge_base_ids}")

# Test KB directly
kb_result = client.knowledge_bases.query(
    knowledge_base_id=kb.id,
    query="test query"
)
print(f"KB Response: {kb_result}")

# Check data source status
sources = client.knowledge_bases.list_data_sources(kb.id)
for source in sources:
    print(f"Source: {source.name}, Status: {source.status}")
```

#### Issue: Slow response times

**Solutions**:
1. Reduce number of data sources queried
2. Implement query caching
3. Optimize chunk sizes
4. Use streaming responses

```python
# Enable streaming
run = client.threads.runs.create(
    thread_id=thread.id,
    agent_id=agent.id,
    stream=True
)

for event in run:
    if event.type == "thread.message.delta":
        print(event.content, end="", flush=True)
```

#### Issue: Incorrect or outdated information

**Solutions**:
1. Refresh data sources
   ```python
   client.knowledge_bases.refresh_data_source(
       knowledge_base_id=kb.id,
       data_source_name="my-source"
   )
   ```

2. Verify indexing status
3. Check source data quality
4. Adjust retrieval parameters

#### Issue: Authentication failures

**Solutions**:
```python
# Verify credentials
from azure.identity import DefaultAzureCredential

try:
    credential = DefaultAzureCredential()
    token = credential.get_token("https://ml.azure.com/.default")
    print("Authentication successful")
except Exception as e:
    print(f"Authentication failed: {e}")

# Use specific credential
from azure.identity import AzureCliCredential
credential = AzureCliCredential()
```

### Debugging Tips

1. **Enable Detailed Logging**
   ```python
   import logging
   
   logging.basicConfig(level=logging.DEBUG)
   logger = logging.getLogger("azure.ai.foundry")
   logger.setLevel(logging.DEBUG)
   ```

2. **Inspect Run Details**
   ```python
   run = client.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
   print(f"Status: {run.status}")
   print(f"Error: {run.last_error}")
   print(f"Steps: {run.steps}")
   ```

3. **Test Components Individually**
   - Test KB query separately
   - Test agent without KB
   - Verify data source connectivity

---

## 📚 Resources

### Official Documentation

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Foundry IQ Overview](https://learn.microsoft.com/azure/ai-foundry/concepts/knowledge-bases)
- [Agent Development Guide](https://learn.microsoft.com/azure/ai-foundry/how-to/agents)
- [Model Context Protocol Spec](https://spec.modelcontextprotocol.io/)

### SDKs & Tools

- [Python SDK](https://pypi.org/project/azure-ai-foundry/)
- [.NET SDK](https://www.nuget.org/packages/Azure.AI.Foundry/)
- [JavaScript SDK](https://www.npmjs.com/package/@azure/ai-foundry)
- [REST API Reference](https://learn.microsoft.com/rest/api/aiservices/)

### Sample Code & Templates

- [Foundry IQ Samples Repository](https://github.com/Azure-Samples/foundry-iq-samples)
- [Agent Templates](https://github.com/Azure-Samples/foundry-agent-templates)
- [Integration Examples](https://github.com/Azure-Samples/foundry-integrations)

### Community & Support

- [Microsoft Q&A Forum](https://aka.ms/azure-ai-qa)
- [Stack Overflow - Azure AI Tag](https://stackoverflow.com/questions/tagged/azure-ai)
- [Azure AI Blog](https://techcommunity.microsoft.com/t5/ai-azure-ai-services/bg-p/Azure-AI-Services-blog)
- [GitHub Issues](https://github.com/Azure/azure-sdk-for-python/issues)

### Training & Certifications

- [Microsoft Learn - AI Fundamentals](https://learn.microsoft.com/training/paths/get-started-with-artificial-intelligence-on-azure/)
- [AI Engineer Certification](https://learn.microsoft.com/certifications/azure-ai-engineer/)
- [Foundry IQ Workshop](https://learn.microsoft.com/training/modules/foundry-iq-workshop/)

### Architecture & Best Practices

- [Enterprise AI Architecture Guide](https://learn.microsoft.com/azure/architecture/ai-ml/)
- [Responsible AI Guidelines](https://www.microsoft.com/ai/responsible-ai)
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Microsoft Azure AI Team
- Foundry IQ Engineering Team
- Open-source community contributors
- All developers building with Foundry IQ

---

## 📞 Contact & Support

For questions, issues, or feedback:

- **GitHub Issues**: [Create an issue](https://github.com/prathapm14/foundry-iq/issues)
- **Email**: support@example.com
- **Twitter**: [@FoundryIQ](https://twitter.com/foundryiq)

---

**Last Updated**: January 2026

**Version**: 1.0.0

---

⭐ If you find this guide helpful, please star the repository!

🔔 Watch the repository for updates and new examples!