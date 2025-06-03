# Q&A

## Conda 環境の作成時に out of memory が出た

環境構築自体は、より軽量な Micromamba を利用することで解決できる可能性がありますが、その後のモデル実行時にもメモリ不足が発生する可能性が高いと考えられます。

## Conda 環境作成がよくわからないが上手くいかない

ずっと処理が終わらない or ちゃんと指示通りやってるのに以下のエラーが出る

```
PackagesNotFoundError: The following packages are not available from current channels:
  - opencv==4.4.0
  - numpy==1.19
```

 → 一度次のコマンドを入力して、再度試してみてください

```bash
conda update -all
```

## Miniconda ではなく、Miniforge を使って環境を作成したい

[こちら](./52_miniforge.md) を参照してください。

## Miniconda ではなく、Micromamba を使って環境を作成したい (Apple Silicon)

Rosetta 2 をインストールしてから、次のコマンドで、micromambaをインストールします。

```bash
brew install micromamba
```

または、

```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```

次に、micromambaで仮想環境を作成します。

```bash
micromamba create -n tf24_env -c conda-forge \
    python==3.8.15 tensorflow==2.4.0 opencv==4.4.0 numpy==1.19 \
    --platform=osx-64
```

## Windows環境でのMiniforgeの利用の際、TensorFlowのインストールに失敗する

conda-forgeでは、Windows用のtensorflow>2.0.0が提供されていません。
その場合、若干トリッキーですが、`conda` で作った仮想環境（Pythonバージョン指定）に `pip` で必要なライブラリをインストールすることにします。

```powershell
conda create -n tf24_env -c conda-forge -y python==3.8.15
conda activate tf24_env
pip install tensorflow==2.4.0 opencv-python==4.3.0.36 numpy==1.19.2
```
