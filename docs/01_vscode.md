# Visual Studio Code セットアップ

Visual Studio Code (VS Code) は Microsoft が提供する軽量な開発用エディタです。

このガイドはWindowsとmacOSにVS Codeをインストールし、Python開発・実行に推奨される拡張機能を設定する方法を説明します。

この時点で、Python (or miniconda) のインストールが完了している必要はありません。

## 1-1. Windowsにインストール

1. [公式Visual Studio Codeサイト](https://code.visualstudio.com/Download)からWindowsインストーラーをダウンロードします。
    - Windows 10/11用の一番大きいアイコンをクリック
2. インストーラーを実行し、指示に従ってインストールを完了させます。
    - 基本的に、設定はデフォルトのままで問題ありません。
3. インストールが完了したら、スタートメニューから VS Code を起動します。

生成AI（GitHub Copilot）の案内が表示される場合がありますが、本セミナーの手順ではサインインは不要です。

4. 設定を同期したい場合は、プロンプトに従ってMicrosoftまたはGitHubアカウントにサインインしてください。

## 1-2. macOSにインストール

このセクションでは、macOS でアプリを展開して起動する基本手順を説明します。

1. [Visual Studio Codeのサイト](https://code.visualstudio.com/Download)からmacOS版をダウンロードします。
    - Mac用の一番大きいアイコンをクリック
2. ダウンロードした`.zip`ファイルを開き、**Visual Studio Code.app** を**Applications**フォルダへドラッグします。
3. **Launchpad**または**Applications**フォルダから **Visual Studio Code** を起動します。

## 2. VS Code の使い方概略

TODO: スクリーンショットを掲載するなどして、簡潔に説明を記載予定です。もしくは当日投影して説明します。

## 3. VS Code 拡張機能とは

拡張機能（extension）は、VS Code に後から機能を追加できるプラグインです。

必要なプログラミング言語サポートやデバッグツールなどをインストールして、自分好みにカスタマイズできます。

## 4. Python と Jupyter 拡張機能のインストール

1. Visual Studio Codeで、左サイドバーにある四角形アイコンをクリックする
2. **Python** を検索し、Microsoftが提供する拡張機能をインストールします。
    - Microsoft 社が提供しており、安心です
3. 同様に **Jupyter** を検索し、Microsoftが提供する拡張機能をインストールします。
    - こちらも Microsoft 社が提供しており、安心です
4. ウィンドウ再読み込みを提案されたら、対応して拡張機能を有効化します。

### Python拡張機能の主な機能

Python拡張機能を有効にすると、コード補完や IntelliSense、Linting によるコード解析、デバッグ、単体テスト実行など多くの機能が利用できます。また仮想環境や Conda 環境の切り替えも簡単に行え、Jupyter Notebook の作成・実行も VS Code 内で完結できます。

また、Python拡張機能にはエディタで開いているコードを直接ターミナルで実行する機能があります。
例えば、複数行を選択した状態で`Shift+Enter`を押すと、選択したコードがターミナルへ送信されます。
コードブロックの途中に改行があっても、インデントを基準にブロックの切れ目を自動で判断して実行します。


参考: <https://code.visualstudio.com/docs/languages/python>
