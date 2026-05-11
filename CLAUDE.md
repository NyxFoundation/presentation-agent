# CLAUDE.md — プレゼンテーション制作タスク定義

## 1. 必読インプット (作業開始前に必ず読む)

1. `inputs/introduction.md` — 講義ブリーフ (YAML frontmatter + Notion 構成案完全転記)
2. `inputs/rules.md` — デザイン語彙・レイアウト・ブランディング・学術的正確性ルール
3. `inputs/journey.md` — 過去の判断・ピットフォール・試行錯誤の記録

これらを読まずに制作に着手しない。

## 2. リポジトリ構造

```
slides.md              # Slidev エントリポイント (src: で各スライドを include)
slides/SL*.md          # 個別スライドファイル
public/images/         # SVG/PNG アセット
style.css              # グローバル CSS (Noto Sans JP / BIZ UDPMincho)
layouts/cover.vue      # カバーレイアウト
global-bottom.vue      # 全スライド footer (Merkle Japan ロゴ + ページ番号)
components/            # Vue コンポーネント
inputs/                # ブリーフ・ルール・経緯
dist/                  # bun run build の出力
```

## 3. Slidev フォーマット規約

### slides.md (エントリ)
- YAML frontmatter に必ず `canvasWidth: 1280` と `aspectRatio: 16/9` を含める
- 各スライドは `--- src: ./slides/SLNN.md ---` で include

### 個別スライド (slides/SL*.md)
- 先頭に YAML frontmatter `layout: default | center | statement` (default が基本)
- 本文は Markdown + HTML (Tailwind/UnoCSS クラス使用可)
- Mermaid 図: ` ```mermaid {scale: 0.65-0.85} ` で囲む
- Speaker notes: `<!-- Speaker Notes: ... -->`

## 4. デザイン適用 (必須)

`inputs/rules.md` 第 3 章 (デザイン語彙) に従う。要点:

- 角丸: **`rounded-xl`**
- 枠線: **`border border-{c}-200/300`** (太線は使わない)
- 白カード: `bg-white rounded-xl border border-gray-200 shadow-sm`
- アクセントカード: `bg-{c}-50 rounded-xl border border-{c}-200`
- テキスト階層: `text-gray-900 / 700 / 500 / 400` (純黒禁止)
- アクセント色: `text-amber-600 / 700`
- Bullet: `&#9654;` (amber ▶) / `&#10003;` (green ✓) — 素の `•` は使わない
- 大数字: `font-black` (900)

## 5. 投影スライドに入れる / 入れない

`inputs/rules.md` 第 1 章に従う。

**入れない**:
- 詳細タイムテーブル / 時刻ごとの内訳
- 時間表記 (`(35分)`, `120分→180分` 等)
- 認知レベル分類 (Bloom's taxonomy 等)
- ルーブリック詳細・自己評価リスト
- 講師の心構え・台本

**入れる**:
- 図解 / 比較表 (3-7 行) / 用語定義 / 具体例 / Open Question / 出典

## 6. 出典 (Sources) 表示

論文・記事・OSS・事件レポートを参照しているスライドには必須:

```html
<div class="absolute bottom-3 left-6 text-[10px] text-gray-400 leading-tight max-w-3xl">
Sources: AUTHORS "TITLE" VENUE YEAR ｜ ...
</div>
```

区切り: 全角 ` ｜ `。Merkle Japan ロゴ (右下) と衝突しない位置。

## 7. ブランディング

- Footer ロゴ: `/images/merklejapan_logo.png` (96px width)
- Cover: `layout: center` + `merklejapan_logo.png` × パートナーロゴの並び
- 旧称 "ZK Tokyo" / "zktokyo" / "zk-tokyo" は **全削除**。grep で残存ゼロを確認

## 8. 文字エスケープ禁止事項

- `$` (通貨記号) は **escape しない**。`\$292M` ではなく `$292M` と書く
- 確認: `grep -r '\\\$' slides/ public/images/` で残存ゼロ

## 9. 学術的正確性 (Programmable Cryptography 関連)

`inputs/rules.md` 第 8 章に従う。要点:

- **Longfellow** は MPC-in-the-head 系 (Ligero 系)、Sumcheck 系ではない
- **Sumcheck prover** は無条件で「線形時間」と書かない。「structured ME 上で concretely efficient (Thaler 2013 系)」と限定
- **FHE 信頼前提**は「データ機密のみ。計算正しさは別途 (Verifiable FHE)」と分解
- **ZK 敵対モデル**は `malicious prover (soundness)` + `malicious verifier (ZK)` の二重性を併記
- **Programmable Cryptography** は 0xPARC スローガン。UC framework とは強さが質的に異なる
- 未来事象の数値は「仮想/最新シナリオ」明示か出典脚注

## 10. レイアウト原則

- **2 段 (2×2 grid) は使わない**。視線の起点が決まらないため
- 1 軸の線形フロー (top-to-bottom or left-to-right) を基本に
- 比較は横並び 3-4 カード
- 画像は `max-h-[300-460px]` (キャンバス 1280×720 で安全な範囲)
- 集合関係 (A ⊂ B) は **入れ子だ円** で描く。並列ボックスは禁止
- 同じ要素を 2 箇所に重複して書かない

## 11. 視覚的フィードバック (Playwright) ワークフロー

スライド編集後は必ず実機レンダリングを確認する。Playwright Chromium が動かない環境 (libglib 不足等) では Firefox CLI で代替する。

### A. ビルド
```bash
bun run build
```

### B. SPA fallback サーバ起動 (`/tmp/spa_server.py`)
```python
import http.server, socketserver, os
from pathlib import Path
ROOT = '/home/gohan/workspace/presentation-agent/dist'
os.chdir(ROOT)
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        p = self.path.split('?')[0]
        if not Path(ROOT+p).exists() or Path(ROOT+p).is_dir():
            self.path = '/index.html'
        return super().do_GET()
    def log_message(self,*a): pass
with socketserver.TCPServer(("",4002), H) as s: s.serve_forever()
```
起動:
```bash
nohup python3 /tmp/spa_server.py > /tmp/spa.log 2>&1 &
disown
```

### C. 各スライドをスクショ (3 回試行 + 最大サイズ採用)
```bash
for i in $(seq 1 28); do
  printf -v num "%02d" $i
  bestsize=0
  for attempt in 1 2 3; do
    firefox --headless --window-size=1920,1080 --screenshot=/tmp/_tmp.png "http://localhost:4002/${i}?print" 2>/dev/null
    size=$(stat -c %s /tmp/_tmp.png 2>/dev/null || echo 0)
    [ "$size" -gt "$bestsize" ] && mv /tmp/_tmp.png /tmp/slide_shots/slide_${num}.png && bestsize=$size
  done
done
```

### D. PNG を `Read` ツールで確認
- オーバーフロー (下端切れ) を検出
- 視線フロー (1 軸か / 2×2 になっていないか) を検証
- 余白・コントラスト・出典の有無を確認

### E. blank スライドの再撮影
ファイルサイズが極端に小さい (< 50KB 程度) スライドは Firefox の描画タイミングが間に合っていない。並列 5 回試行で最大を採用:
```bash
for a in $(seq 1 5); do
  firefox --headless --window-size=1920,1080 --screenshot=/tmp/_tmp_${a}.png "http://localhost:4002/${i}?print" 2>/dev/null &
done
wait
cp "$(ls -S /tmp/_tmp_*.png | head -1)" /tmp/slide_shots/slide_${num}.png
rm /tmp/_tmp_*.png
```

## 12. 完了前のチェックリスト

```bash
# 1. 古いスタイル残存ゼロ
grep -r "rounded-lg\|border-2 border-" slides/

# 2. $ エスケープ残存ゼロ
grep -r '\\\$' slides/ public/images/

# 3. 旧ブランド名残存ゼロ
grep -rI 'zktokyo\|zk tokyo\|zk-tokyo' slides/ public/images/ *.vue style.css

# 4. ビルド成功
bun run build

# 5. 全スライド (28 枚目安) スクショ取得・目視確認
ls /tmp/slide_shots/slide_*.png | wc -l
```

すべて通過するまで完了報告しない。

## 13. ピットフォール (繰り返し禁止)

`inputs/rules.md` 第 10 章の表を確認。代表例:
- Notion 全情報の貼り付け (30 枚超 → 運営情報混入)
- canvasWidth デフォルト (980) で日本語密度過多
- 2×2 grid で視線迷子
- 集合関係を並列ボックス (重複発生)
- 数値・事件名を出典なしで提示
- 「休憩」等の運営スライドを単独 1 枚
- 太枠 `border-2 border-{c}-700` の多用

## 14. 出力言語

`inputs/introduction.md` の YAML `output_language` に従う (現状: Japanese)。
