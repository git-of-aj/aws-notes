### Bedrock Docs
- https://docs.aws.amazon.com/bedrock/latest/userguide/models-api-compatibility.html
### APIs
> not all API supported by All Models.. check docs Bottom line: No API is supported by every model in the table. InvokeModel has the broadest support and is the de facto common denominator across most Bedrock models.
- Invoke family: InvokeModel handles synchronous, single-response calls. InvokeModelWithResponseStream returns responses as a real-time stream. InvokeModelWithBidirectionalStream enables full-duplex streaming for interactive applications. AsyncInvoke submits long-running requests asynchronously, storing output to Amazon S3.
- Converse family: Converse provides a unified, model-agnostic interface for synchronous multi-turn conversations. ConverseStream delivers the same experience with streaming output.
- OpenAI-compatible family: ChatCompletions implements the OpenAI Chat Completions interface, enabling existing OpenAI-based integrations to run on Bedrock with minimal changes. Responses API implements the OpenAI Responses interface, supporting stateful, agentic interactions with built-in tool use and conversation history management.
- Messages family: Messages implements the Anthropic Messages interface, enabling existing Anthropic SDK-based integrations to run on Bedrock with minimal changes.

### Endpoints:
> `bedrock-runtime.{region}.amazonaws.com` (recommended) and supported by MOST of models
- Use bedrock-mantle when you specifically need capabilities that are currently available only there, such as server-side and pre-configured tools (including web search), background inference, Projects, or Workspaces. To


### routing Behaviour:
- In-Region: Your requests never leave the AWS Region you specify. Use this when regulations require strict single-Region data processing.
- Geographic (Geo): Bedrock routes your request to a Region within a defined geography (US, EU, Japan, Australia, or India), keeping data within that geography. Use this when you have data residency requirements tied to a geography rather than a single Region.
- Global: Bedrock routes your request to a supported commercial Region worldwide. For some models, global cross-Region inference is priced lower per token than geographic cross-Region inference. Use this when you have no data residency constraints.
