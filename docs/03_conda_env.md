# Condaの仮想環境設定

仮想環境とはプロジェクトごとにパッケージを分離する仕組みです。

複数のプロジェクトを扱う際は、それぞれで必要とするライブラリのバージョンが異なることがよくあります。

`conda create` で個別の環境を用意し、`conda activate` で切り替えること（有効化する）で、依存関係を分離して互いの環境が干渉するのを防げます。

こうした環境の独立性により、再現性を保ちつつ安心して作業を進められます。

## 新しい環境の作成と有効化

実際に、*解析実践ハンズオンセミナー*で使用する環境を、`conda create` で作成してみましょう。

OS・環境ごとに利用可能なライブラリが一部異なる場合があります。
ただし、TensorFlow のバージョンは重要なため、実際にモデル構築時に使用されていた TensorFlow 2.4.0 になるべく近いバージョンを優先して環境を構築します。
そのため、JOIRの公開されているモデルに付随する `requirements.txt` に記載されたライブラリのバージョンと一部異なる場合があることにご留意ください。

今回は、CPU での実行を想定した環境を構築します。

### Windows

なぜか tensorflow==2.4.0 がconda-forgeにないので、近いバージョン（2.3.0）を使います。
他の依存関係も複雑ですが、Windows端末でインストールが正常に完了した以下のバージョンを、本セミナーでは使用します。

```bash
conda create -n tf24_env -c conda-forge -y python==3.8.15 tensorflow==2.3.0 opencv==4.6.0 numpy==1.23.5
```

### macOS (Apple Silicon)

Apple Silicon では TensorFlow 2.4 がネイティブ対応していないため、x86_64（つまり、Intel CPUの環境） 向けパッケージを流用します。

まず、Intel 向けにのみ提供されているパッケージを利用する際、Rosetta 2 が必要です。次のコマンドでインストールできます。

```bash
softwareupdate --install-rosetta --agree-to-license
```

`--agree-to-license` フラグを付けることで非対話的にインストールを完了できます。

インストールを確認するには以下を実行します。

```bash
/usr/bin/pgrep oahd >/dev/null && echo "Rosetta 2 is installed" || echo "Rosetta 2 is NOT installed"
```

```bash
CONDA_SUBDIR=osx-64 conda create -n tf24_env -c conda-forge -y \
    python==3.8.15 tensorflow==2.4.0 opencv==4.4.0 numpy==1.19
```

### macOS (Intel)

以下のコマンドで環境を作成できます（未検証）。

```bash
conda create -n tf24_env -c conda-forge -y \
    python==3.8.15 tensorflow==2.4.0 opencv==4.4.0 numpy==1.19
```


## 環境を削除するには

不要になった環境（例: `tf24_env`という名前の環境）は次のコマンドで削除できます:

```bash
conda env remove -n tf24_env
```

このコマンドを実行すると、環境が完全に削除されます。
