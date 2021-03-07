# PicoCTF 答題整理

## General Skills
題目名稱 | 問題說明 | 解題說明 
---|---|---
2Warm | 十進制轉二進制
Warmed Up | 十六進制轉十進制
Lets Warm Up | 十六進制轉 ASCII
strings it | 從檔案內容找答案 | 檔案用記事本打開會像亂碼，但搜尋 PicoCTF 就可以找到答案
Bases | 編碼轉換（[base64 介紹](Notes/常見編碼介紹.md)）
First Grep | 從檔案內容找答案 | 這題是想介紹 grep 這個工具，可是我還是直接把檔案打開來用搜尋的了...
what's a net cat? | 學習使用 netcat 工具 (Windows 需自行安裝) | nc {IP/DOMAIN} {PORT}
plumbing | 將 cmd 的查詢結果輸出成檔案 | xxxx > {DESTINATION}
Based | 不同進位方式的轉換 | 因為有限制回答時間，所以需要先刻好函數(或是找好轉換工具)
flag_shop | 找程式漏洞 | 程式邏輯看起來沒問題，但購買第一個項目時可以利用 int 的漏洞來賺錢：<Br>輸入的數字是很大的正數，但計算出的費用是負數。
mus1c | 解讀用 ROCKSTAR 寫的程式 | [ROCKSTAR 官網](https://codewithrockstar.com/docs#pronouns)<br>[ROCKSTAR 翻譯器](https://codewithrockstar.com/online)<br>[CODE 解讀](./Others/lyrics_parsed.txt)

## Cryptography
題目名稱 | 問題說明 | 詳細說明 
---|---|---
The Numbers | A\~Z 依序轉換成 1\~26
caesar | 凱撒密碼：將英文字平移k單位<br>例：k=2 時, A->C, B->D, ... | 將 k 從 1 開始依序帶入，挑一個看起來有意義的解密結果
Easy1 | one time pad<br>加密方法：查表，左邊(明文)加上面(密鑰)=中間(密文) | 反過來查，找上面=密鑰&中間=密文的位置，看左邊(明文)是什麼
13 | 凱薩密碼 k=13 的版本
la cifra de | 