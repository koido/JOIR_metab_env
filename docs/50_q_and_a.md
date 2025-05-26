# Q&A

## Conda 環境の作成時に out of memory が出た

環境構築自体は、より軽量な Micromamba を利用することで解決できる可能性がありますが、その後のモデル実行時にもメモリ不足が発生する可能性が高いと考えられます。

## Miniconda ではなく、Miniforge を使って環境を作成したい

[こちら](./52_miniforge.md) を参照してください。

## Miniconda ではなく、Micromamba を使って環境を作成したい (Apple Silicon)

Rosetta 2 をインストールしてから、次のコマンドで環境を作成します。

```bash
micromamba create -n tf24_env -c conda-forge \
    python==3.8.15 tensorflow==2.4.0 opencv==4.4.0 numpy==1.19 \
    --platform=osx-64
```