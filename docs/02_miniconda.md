# Miniconda セットアップガイド

Miniconda は conda による環境管理を最小構成で実現する軽量ディストリビューションです。
このドキュメントでは、Windows と macOS/Linux で Miniconda をダウンロードし、インストール、初期設定する方法を説明します。

## 目次


## 1. Windowsユーザー向け

### 1.1 ダウンロード

まずは [Anaconda のダウンロードページ](https://www.anaconda.com/download) にアクセスします。
表示される画面右側の枠の下の方にある **Skip registration** を選択すると、"**Miniconda Installers**" の一覧が表示されます。

ここから、ご利用のOSに応じたインストーラーをダウンロードしてください。

### 1.2 インストール

ダウンロードした`.exe` インストーラー (Windows）を実行します。

基本的に、チェック項目はデフォルトのままでインストール作業を進めてください。

以下の手順は、デフォルト設定の想定です。

### 1.3 VS Code での初期設定

インストールが完了したら、VS Code を開き、VS Code のターミナルを開きます（TODO: VS Code のターミナルを使う方法をどこかで追記

Windowsの場合、初期設定だと PowerShell が使われているはずです。

次のコマンドを実行します。

```bash
C:\ProgramData\miniconda3\condabin\conda init
```

一度ターミナル（かVS Codeそのもの）を閉じて開くと、次からは `C:\ProgramData\miniconda3\condabin\conda` なんて打たなくても `conda` だけでよくなります。

## 2. macOSユーザー向け

GUIでインストールすることも可能ですが、ここではコマンドラインでインストールします。

### 2.1 ターミナルを開く

VS Code のターミナルを開くか、ターミナルアプリを開きます。

### 2.2 Apple Silicon か Intel かを確認する

M1 ~ M4チップが搭載されたMacの場合、Apple Silicon です。それ以外は Intel です。

不明な場合は、ターミナル（後述）で次のコマンドを実行すると、CPUの種類を確認できます。

```bash
sysctl -a | grep machdep.cpu.brand_string
```

### 2.3 ダウンロード

Apple Silicon の場合:

```bash
cd Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
```

Intel の場合:

```bash
cd Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
```

### 2.4 インストール (最初のコマンド)

Apple Silicon の場合:

```bash
bash Miniconda3-latest-MacOSX-arm64.sh
```

Intel の場合:

```bash
bash Miniconda3-latest-MacOSX-x86_64.sh
```

### 2.5 インストール (続き)

以降は、Apple Silicon と Intel で同じです。

いくつかの質問が表示されますが、次の通り対応してください。

#### 2.5.1 ライセンスの確認

```text
Do you accept the license terms? [yes|no]
[no] >>> yes
```

ライセンス条項に同意するかを問われています。(確認して) `yes` と入力して進めます。

#### 2.5.2 インストール先ディレクトリの指定

```text
Miniconda3 will be installed into this location:
/home/user/miniconda3
- Press ENTER to confirm the location
- Or specify a different location below
[/home/user/miniconda3] >>>
```

インストール先ディレクトリを問われています。エンターキーを押すと、デフォルトの場所（四角カッコ内に表示）にインストールされます。
別の場所にインストールしたい場合は、その場所を入力して、エンターキーを押してください。

本チュートリアルでは、デフォルトの場所にインストールされていることを前提とします。

#### 2.5.3 `conda init` の実行確認

```text
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>> yes
```

Miniconda3 の初期化を問われています。`yes` と入力してください。


#### 2.5.4 ターミナルを再起動するか、またはシェルの設定をリロードして、以下のコマンドでインストールを確認します。

```bash
conda --version
```

バージョンが表示されれば、以降はターミナルで `conda` コマンドを使って環境を作成、管理できるようになります。
