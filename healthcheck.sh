#!/bin/bash

# Streamlitアプリの健全性をチェックするスクリプト
curl -f http://localhost:8501/_stcore/health || exit 1
