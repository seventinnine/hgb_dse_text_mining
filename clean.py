#!/usr/bin/env python3

import re

def clean(text: str, keep_sentences: bool = True) -> str:
    if keep_sentences:
        return re.sub(r"[^a-zA-Z\.\?\!\s]+", "", text)
    return re.sub(r"[^a-zA-Z\s]+", "", text)
