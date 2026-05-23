---
layout: default
---

# 顧客Aは健全だった ─ それでも清算された経路

<div class="text-xs opacity-60 mb-2">Current Finance (Sui レバレッジLending) ／ Sherlock contest #312 ／ <span class="font-mono">market.move :580</span></div>

<img :src="'/images/diagrams/sl13b_scenario.svg'" class="w-full mx-auto block mt-1" style="max-height: 400px;" alt="顧客Aは健全だったのに清算された経路 ─ ユーザシナリオ" />

<!--
顧客Aは健全だったのになぜ清算されたか、ユーザシナリオを絵で見てみます。Current FinanceはSui上のレバレッジLending。左、顧客AはeMode Group A、LSTグループ。stSUIの金庫に50M担保を預けて、健全な範囲でUSDCを30M借りる。Group AのADL閾値は50M、借入30Mは下回っているので健全。右、顧客Bは別グループのGroup B、ETHグループ。wETHの金庫に100M担保を預けてUSDCを80M借りる。顧客Aとは別の世界です。ここからが重要。二人が借りたUSDCは同じUSDC reserve、中央の黒い金庫に合算され、110Mに膨らむ。下、market.move 580行目のADL判定は、本来Group Aの借入30Mを見るべきところ、reserve全体の110Mを読んでしまう。閾値50Mと比較して110M > 50Mで誤発動。結果、雷が落ちて顧客Aの健全なstSUI金庫が破壊、強制清算される。これがDeFiセキュリティで現場で起きていることです。次のスライドでコードの3つの管理ポイントを並べて読みます。
-->
