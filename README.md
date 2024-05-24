# find-image-with-image

使用 [CLIP](https://github.com/openai/CLIP) 模型对图象进行模式匹配——简单的说就是“按图索骥”。

## 使用

1. 模型下载

推理使用了 clip.cpp，支持 gguf 模式格式。

gguf 格式可以到 https://huggingface.co/mys/ggml_clip-vit-large-patch14/tree/main 下载。

推荐选择 Q5_1 或 Q8_0 的量化版本，当前使用 `CLIP-ViT-L-14-laion2B-s32B-b82K_ggml-model-q5_1.gguf` 进行测试。将下载得到的
gguf 文件放置到 models 目录下。

2. 安装依赖

```sh
$ uv venv
$ . .venv/Scripts/activate
$ uv pip install -r requirements.txt
```

3. 执行

```sh
$ python clip_service_test.py

(d2c) $ python main.py
input1 vs input2 0.937790036201477
input1 vs input2 switch 0.937790036201477
input1 vs input3 0.9472988247871399
input1 vs select1 0.9491289258003235
input1 vs button1 0.7936016917228699
```

注意 clip.cpp 的 pip 包并没有带上 windows 的 dll 文件。可以将 dlls/win64.7z 解压到 .venv/Lib/site-packages/clip_cpp
目录下。如果出现无法找到符号的揭示，可以尝试手工修改代码。

### HACK

修改 .venv/Lib/site-packages/clip_cpp/clip.py

```diff
--- clip.old.py 2024-05-20 23:00:54.086530300 +0800
+++ clip.py     2024-05-20 22:56:00.251379000 +0800
@@ -15,7 +15,7 @@
     if os_name == "Linux":
         return f"./lib{name}.so"
     elif os_name == "Windows":
-        return f"{name}.dll"
+        return f"./{name}.dll"
     elif os_name == "Mac":
         return f"lib{name}.dylib"

@@ -199,11 +199,11 @@
 # ]
 # clip_image_batch_encode.restype = ctypes.c_bool

-make_clip_image_u8 = clip_lib.make_clip_image_u8
+make_clip_image_u8 = clip_lib.clip_image_u8_make
 make_clip_image_u8.argtypes = []
 make_clip_image_u8.restype = ctypes.POINTER(ClipImageU8)

-make_clip_image_f32 = clip_lib.make_clip_image_f32
+make_clip_image_f32 = clip_lib.clip_image_f32_make
 make_clip_image_f32.argtypes = []
 make_clip_image_f32.restype = ctypes.POINTER(ClipImageF32)
```

## LICENSE

MIT
