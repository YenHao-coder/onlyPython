# 🚗 Turtle Crossing Game

## 📌 專案簡介
本專案是一款基於 `turtle` 模組開發的簡單過馬路遊戲。玩家控制烏龜穿越馬路，避開來往的車輛，成功到達終點後進入下一關，遊戲難度隨著等級提升而增加。

## 🎮 功能特色
- 使用 `turtle` 模組繪製遊戲畫面。
- 隨機生成車輛，並從右向左移動。
- 玩家可透過 `Up` 鍵控制烏龜前進。
- 等級提升後車輛速度增加，增加挑戰性。
- 碰撞偵測：若烏龜撞到車輛，遊戲結束並顯示 `Game Over`。
- 提供重新開始選項。

## 📜 遊戲規則
1. 按 `Up` 鍵讓烏龜向前移動。
2. 避開來回行駛的車輛，成功到達對面即可晉級。
3. 每當通過一關，車輛速度會加快。
4. 若與車輛碰撞，遊戲結束，畫面顯示 `Game Over`。
5. 玩家可以選擇是否重新開始遊戲。

## 🚀 如何運行
### **環境需求**
- Python 3.x
- `turtle` 模組（Python 內建，無需額外安裝）

### **執行步驟**
1. 下載所有 `.py` 檔案。
2. 確保所有檔案位於同一資料夾內。
3. 在終端機或命令提示字元中運行：
   ```sh
   python main.py
   ```
4. 遊戲將開啟 `turtle` 視窗，開始遊戲。

## 📂 檔案結構
```
Turtle_Crossing_Game/
│── main.py          # 主程式，負責遊戲流程與迴圈
│── player.py        # 玩家控制的烏龜角色
│── car_manager.py   # 車輛管理，包括車輛生成與移動
│── scoreboard.py    # 記分板，顯示等級與遊戲結束畫面
│── README.md        # 專案說明文件
```

## 📖 參考來源
- 本專案靈感來自於 [Udemy - 100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code-the-complete-python-pro-bootcamp-for-2023/) by Angela Yu
- 此專案為個人 Python 學習作品
---
✨ 祝你玩得開心！

