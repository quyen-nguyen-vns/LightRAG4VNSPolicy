import asyncio

import pandas as pd
from loguru import logger

from lightrag.base import QueryParam
from lightrag.custom.data import qa_data
from lightrag.custom.init_rag import initialize_rag


async def query(rag, query: str, query_param: QueryParam):
    result = await rag.aquery(query, query_param)
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
        mode="naive",
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
    await query_qa(rag, query_param)


if __name__ == "__main__":
    asyncio.run(main())
