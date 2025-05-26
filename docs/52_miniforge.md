# Conda セットアップガイド

Conda は、Python の依存関係や仮想環境を管理するツールです。
Miniforge は、conda-forge (コミュニティ主導のパッケージリポジトリ) による、conda による環境管理を最小構成で実現する軽量ディストリビューションです。
このドキュメントでは、Windows と macOS/Linux で Miniforge をダウンロードし、インストール、初期設定する方法を説明します。

## 目次

## 1. Windowsユーザー向け

### 1.1 ダウンロード

まずは [Miniforge のダウンロードページ](https://conda-forge.org/download/) にアクセスします。

右下に　Windows (x86_64) と表示されているので、それをクリックします。

### 1.2 インストール

ダウンロードした`Miniforge3-Windows-x86_64.exe` インストーラーを実行します。

基本的に、チェック項目はデフォルトのままでインストール作業を進めてください。

ただし、特にインストール先は控えておいてください。

以下の手順は、デフォルト設定の想定です。

### 1.3 VS Code での初期設定

インストールが完了したら、VS Code を開き、VS Code のターミナルを開きます（TODO: VS Code のターミナルを使う方法をどこかで追記

Windowsの場合、初期設定だと PowerShell が使われているはずです。

次のコマンドを実行します（最初の部分は、 "インストール先"\condabin/conda です）。

```powershell
C:\ProgramData\miniforge3\condabin\conda init
```

一度ターミナル（かVS Codeそのもの）を閉じて開くと、次からは `C:\ProgramData\miniforge3\condabin\conda` なんて打たなくても `conda` だけでよくなります。

#### 1.4 `conda` インストールの確認

以下のコマンドでインストールを確認します。

```powershell
conda --version
```

バージョンが表示されれば、以降はターミナルで `conda` コマンドを使って環境を作成、管理できるようになります。

なお、インストールされた場所を確認するには、以下のコマンドを実行します (PowerShell)。

```powershell
which.exe conda
```

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
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
```

Intel の場合:

```bash
cd Downloads
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh
```

### 2.4 インストール (最初のコマンド)

Apple Silicon の場合:

```bash
bash Miniforge3-MacOSX-arm64.sh
```

Intel の場合:

```bash
bash Miniforge3-MacOSX-x86_64.sh
```

### 2.5 インストール (続き)

以降は、Apple Silicon と Intel で同じです。

いくつかの質問が表示されますが、次の通り対応してください。

#### 2.5.1 ライセンスの確認

```text
In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
```

ライセンス条項に同意するかを問われています。まずEnterキーを押します。

すると、条項が出てくるので、下矢印 or スペースキー で（読みながら）下の方に遷移します。最後に

```text
Do you accept the license terms? [yes|no]
```

とでてくるので、 `yes` と入力して進めます。

#### 2.5.2 インストール先ディレクトリの指定

```text
Miniforge3 will now be installed into this location:
/Users/"your_name"/miniforge3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/Users/"your_name"/miniforge3] >>>
```

インストール先ディレクトリを問われています。エンターキーを押すと、デフォルトの場所（四角カッコ内に表示）にインストールされます。
別の場所にインストールしたい場合は、その場所を入力して、エンターキーを押してください。

いずれにせよ、このディレクトリは控えておいてください。

なお、本チュートリアルでは、デフォルトの場所にインストールされていることを前提とします。

#### 2.5.3 `conda init` の実行確認

```text
installation finished.
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>>
```

Miniforge3 の初期化設定を問われています。`yes` と入力してください。

すると、デフォルトのシェル ($SHELL) に、`conda` の初期化設定が追加されます。

#### 2.5.4 `conda` インストールの確認

ターミナルを再起動するか、またはシェルの設定をリロードします。

以下のコマンドでインストールを確認します。

```bash
conda --version
```

バージョンが表示されれば、以降はターミナルで `conda` コマンドを使って環境を作成、管理できるようになります。

なお、インストールされた場所を確認するには、以下のコマンドを実行します。

```bash
which conda
```
