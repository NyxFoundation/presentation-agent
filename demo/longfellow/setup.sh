#!/usr/bin/env bash
# Longfellow ライブデモ環境セットアップ (SL23)
# upstream README (github.com/google/longfellow-zk) の手順を自動化しただけ。
set -euo pipefail

cd "$(dirname "$0")"

if [ "$(uname)" = "Darwin" ]; then
  brew install googletest google-benchmark zstd cmake
else
  sudo apt install -y build-essential clang cmake libssl-dev libzstd-dev \
                      libgtest-dev libbenchmark-dev zlib1g-dev
fi

if [ ! -d longfellow-zk ]; then
  git clone https://github.com/google/longfellow-zk
fi
cd longfellow-zk

CXX=clang++ cmake -D CMAKE_BUILD_TYPE=Release -S lib -B clang-build-release \
    --install-prefix "${PWD}/install"
cd clang-build-release
make -j "$(nproc 2>/dev/null || sysctl -n hw.ncpu)"
ctest -j "$(nproc 2>/dev/null || sysctl -n hw.ncpu)"

echo
echo "OK. デモ用ベンチ:"
echo "  cd $(pwd) && ./circuits/sha/flatsha256_circuit_test --benchmark_filter=BM_ShaZK_fp2_128"
