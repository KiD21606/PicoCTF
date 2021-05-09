# PicoCTF 答題整理

## 目錄
1. [General Skills](#General_Skills)

## General_Skills
題目名稱 | 問題類型 | 問題說明
---|---|---
2Warm | 十進制轉二進制
Warmed Up | 十六進制轉十進制
Lets Warm Up | 十六進制轉 ASCII
strings it | 從檔案內容找答案 | 
Bases | 編碼轉換（[base64 介紹](Notes/常見編碼介紹.md)）
First Grep | 從檔案內容找答案 | 介紹 grep 這個工具
what's a net cat? | 學習使用 netcat 工具 (Windows 需自行安裝) | nc {IP/DOMAIN} {PORT}
plumbing | 將 cmd 的查詢結果輸出成檔案 | xxxx > {DESTINATION}
Based | 不同進位方式的轉換 | 有限制回答時間，所以需要先刻好函數(或是找好轉換工具)
flag_shop | 找程式漏洞 | 整數溢位的漏洞
mus1c | 解讀用 ROCKSTAR 寫的程式 | [ROCKSTAR 官網](https://codewithrockstar.com/docs#pronouns)<br>[ROCKSTAR 翻譯器](https://codewithrockstar.com/online)<br>[CODE 解讀](./Others/lyrics_parsed.txt)
1_wanna_b3_a_r0ck5tar | 解讀用 ROCKSTAR 寫的程式 | [ROCKSTAR 官網](https://codewithrockstar.com/docs#pronouns)<br>[ROCKSTAR 翻譯器](https://codewithrockstar.com/online)<br>[CODE 解讀](./Others/1_wanna_b3_a_r0ck_parsed.py)

## Cryptography
題目名稱 | 問題說明 | 詳細說明 
---|---|---
The Numbers | A\~Z 依序轉換成 1\~26 | 
caesar | 凱撒密碼 | 
Easy1 | one time pad | 左邊(明文)加上面(密鑰)=中間(密文)
13 | 凱薩密碼 | 
la cifra de | 凱薩密碼變形 | 