"""Compare how real tokenizers split the same text.

Install:  pip install tiktoken tokenizers huggingface_hub
Run:      python compare_tokenizers.py
"""
import tiktoken
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

TEXTS = [
    "antidisestablishmentarianism",
    "2 + 2 = 4",
    "お誕生日おめでとう",
    "Good morning",
    "सुप्रभात",
    "সুপ্রভাত",
]

TIKTOKEN = {
    "GPT-3 (r50k_base)": "r50k_base",
    "GPT-4 (cl100k_base)": "cl100k_base",
    "GPT-4o (o200k_base)": "o200k_base",
}

HF = {
    "Llama 3.1": "unsloth/Meta-Llama-3.1-8B",  # ungated mirror of Meta's tokenizer
    "Qwen 2.5": "Qwen/Qwen2.5-7B-Instruct",
    "Mistral Nemo (Tekken)": "mistralai/Mistral-Nemo-Instruct-2407",
}


def byte_level_map():
    """Inverse of the GPT-2 byte<->unicode map used by byte-level BPE tokenizers."""
    bs = (
        list(range(ord("!"), ord("~") + 1))
        + list(range(ord("¡"), ord("¬") + 1))
        + list(range(ord("®"), ord("ÿ") + 1))
    )
    cs, n = bs[:], 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return {chr(c): b for b, c in zip(bs, cs)}


INV = byte_level_map()


def readable(token: str) -> str:
    return bytes(INV[ch] for ch in token).decode("utf-8", errors="replace")


def main():
    splits = {}
    for label, enc_name in TIKTOKEN.items():
        enc = tiktoken.get_encoding(enc_name)
        splits[label] = {
            t: [
                enc.decode_single_token_bytes(i).decode("utf-8", errors="replace")
                for i in enc.encode(t)
            ]
            for t in TEXTS
        }
    for label, repo in HF.items():
        tok = Tokenizer.from_file(hf_hub_download(repo, "tokenizer.json"))
        splits[label] = {
            t: [readable(x) for x in tok.encode(t, add_special_tokens=False).tokens]
            for t in TEXTS
        }

    for t in TEXTS:
        print(f"\n### {t}")
        for label, per_text in splits.items():
            print(f"{label:24} {len(per_text[t]):>2}  {per_text[t]}")


if __name__ == "__main__":
    main()
