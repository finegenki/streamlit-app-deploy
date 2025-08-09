# Streamlit App Deploy Demo

これは、Streamlitアプリケーションのデプロイメントデモプロジェクトです。

## 特徴

- 📊 インタラクティブなデータ可視化
- 🎛️ リアルタイムでのパラメータ調整
- 🐳 Dockerコンテナ対応
- 🚀 デプロイメント対応

## セットアップ

### ローカル環境での実行

1. 仮想環境を作成・有効化
```bash
python3 -m venv env
source env/bin/activate  # macOS/Linux
# または
env\Scripts\activate  # Windows
```

2. 依存関係をインストール
```bash
pip install -r requirements.txt
```

3. アプリを実行
```bash
streamlit run app.py
```

### Dockerを使用した実行

1. Dockerイメージをビルド
```bash
docker build -t streamlit-app .
```

2. コンテナを実行
```bash
docker run -p 8501:8501 streamlit-app
```

## ファイル構成

- `app.py` - メインのStreamlitアプリケーション
- `requirements.txt` - Python依存関係
- `Dockerfile` - Dockerコンテナ設定
- `healthcheck.sh` - ヘルスチェックスクリプト
- `.gitignore` - Git除外設定

## デプロイメント

このアプリは以下のプラットフォームにデプロイできます：

- Streamlit Cloud
- Heroku
- Google Cloud Run
- AWS ECS
- その他のクラウドプロバイダー

## ライセンス

MIT License