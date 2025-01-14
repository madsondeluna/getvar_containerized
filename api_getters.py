import asyncio
import aiohttp


async def get_snp_summary(snp_id):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=snp&id={snp_id}&retmode=json"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()
    except aiohttp.ClientError as e:
        return {"error": f"Failed to fetch data: {e}"}


async def fetch_variation(session, id, headers):
    url = f"https://rest.ensembl.org/variation/human/{id}"
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.json()
        else:
            return {"id": id, "error": f"Failed to fetch data for {id}"}


async def fetch_all_variations(ids, headers):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_variation(session, id, headers) for id in ids]
        return await asyncio.gather(*tasks)
