import asyncio

import pandas as pd

from lightrag.base import QueryParam
from lightrag.custom.data import qa_data
from lightrag.custom.init_rag import initialize_rag
from lightrag.utils import logger, setup_logger

# Configure debug logging
setup_logger("lightrag", level="DEBUG", enable_file_logging=True)


async def query(rag, query: str, query_param: QueryParam):
    logger.debug(f"Starting query: {query[:100]}...")
    logger.debug(f"Query parameters: {query_param}")

    result = await rag.aquery(query, query_param)

    logger.debug(
        f"Query result: {result[:200]}..."
        if len(result) > 200
        else f"Query result: {result}"
    )
    logger.info("Query completed!!")
    return result


async def query_qa(rag, query_param: QueryParam):
    result = {"question": [], "lightrag_answer": [], "expected_answer": []}
    for data in qa_data:
        lighrag_result = await query(rag, data["question"], query_param)
        result["question"].append(data["question"])
        result["lightrag_answer"].append(lighrag_result)
        result["expected_answer"].append(data["expected_answer"])

    df_result = pd.DataFrame(result)
    mode = query_param.mode
    df_result.to_csv(f"qa_result_{mode}.csv", index=False)


async def main():
    # Disable caching for this run
    from lightrag.settings import settings

    settings.llm_settings.enable_llm_cache = False
    settings.llm_settings.enable_llm_cache_for_extract = False

    rag = await initialize_rag()
    logger.info("RAG initialized with caching disabled!!")
    query_param = QueryParam(
        mode="local",
        only_need_context=False,
        only_need_prompt=False,
        response_type="Single Paragraph",
        stream=False,
        top_k=10,
        chunk_top_k=5,
        max_entity_tokens=10000,
        max_relation_tokens=10000,
        enable_rerank=False,
    )
    example_query = "What is the document’s most recent update date and effective date?"
    a = await query(rag, example_query, query_param)
    print(a)


if __name__ == "__main__":
    asyncio.run(main())
