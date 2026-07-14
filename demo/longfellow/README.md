# Longfellow ライブデモ環境

Week 1 ライブデモ (SL23) 用。Google の longfellow-zk (MPC-in-the-head 系 ZK、
mDL / mDOC の選択的開示に使われている実装) を手元でビルドして動かす。

## 必要環境

- Linux (Ubuntu/Debian 系) or macOS
- clang / cmake / OpenSSL ヘッダ (下のセットアップスクリプトが導入)

## セットアップ

```bash
./setup.sh            # 依存導入 → clone → ビルド → テスト実行まで
```

やっていることは upstream README の手順そのまま:

```bash
# 依存 (Ubuntu/Debian)
sudo apt install -y build-essential clang cmake libssl-dev libzstd-dev \
                    libgtest-dev libbenchmark-dev zlib1g-dev

git clone https://github.com/google/longfellow-zk
cd longfellow-zk
CXX=clang++ cmake -D CMAKE_BUILD_TYPE=Release -S lib -B clang-build-release \
    --install-prefix ${PWD}/install
cd clang-build-release && make -j 16 && ctest -j 16
```

## デモで見せるもの

- SHA-256 回路の ZK 証明ベンチ (mDL 署名検証の心臓部):

  ```bash
  ./circuits/sha/flatsha256_circuit_test --benchmark_filter=BM_ShaZK_fp2_128
  ```

  「既存の ECDSA + SHA-256 署名をそのまま ZK 化できる」= 発行者 (政府) 側の
  変更ゼロ、を数秒オーダーの証明時間とともに体感する。

- スマホ側の年齢証明 UI (Google Wallet) は本番アプリでの実演 or 録画
  (`public/videos/longfellow-demo.mp4`) を使う。

## 参考

- https://github.com/google/longfellow-zk
- Google "Longfellow: ZK over Existing Identity Standards" (Jul 2025)
- Frigo & shelat, eprint 2024/2010
