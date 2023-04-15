# NTP Clock

NTPサーバーから時刻を取得し表示します。

# Ues

Releasesからバイナリをダウンロードして実行してください。

# Build

`nuitka`が実行できる環境で下記コマンドを実行してください

```bash
nuitka --standalone --onefile --follow-imports --enable-plugin=tk-inter --windows-disable-console src/main.py
```
