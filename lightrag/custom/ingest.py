import asyncio

import pandas as pd
from loguru import logger

from lightrag.custom.init_rag import initialize_rag


def parse_text(text: str) -> str:
    """
    Parse the text to a string
    """
    import json

    data = json.loads(text)
    return data["content"]["S"]


def get_data_from_csv(csv_file: str):
    import pandas as pd

    df = pd.read_csv(csv_file)

    # keep on row that text is not null
    df = df.dropna(subset=["text"])

    # parse the text
    df["text"] = df["text"].apply(parse_text)

    return df[["document_id", "text"]]


def get_data():
    file_1 = "/Users/mac/Downloads/VNS_Data_Protection_Policy.csv"
    file_2 = "/Users/mac/Downloads/VNS_Onboarding_for_New_Comers.csv"
    data_1 = get_data_from_csv(file_1)
    data_2 = get_data_from_csv(file_2)
    data = pd.concat([data_1, data_2]).reset_index(drop=True)
    return data


async def ingest(data: pd.DataFrame):
    logger.info(f"Ingesting {len(data)} documents")
    rag = await initialize_rag()
    logger.info("RAG initialized!!")
    for index, row in data.iterrows():
        await rag.ainsert(row["text"], row["document_id"])
        logger.info(f"Document {index} of {len(data)} ingested")

    logger.info("Ingestion completed!!")


async def main():
    data = get_data()
    print(data)

    await ingest(data)


if __name__ == "__main__":
    asyncio.run(main())
