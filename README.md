# lrc-tools

存放一些关于歌词处理的工具

## [mix_lyrics](./mix_lyrics/main.py)

合并 Waylyrics 导出的双语歌词到一个歌词文件

需要路径下存在 `xxx_orig.lrc` 和 `xxx_tran.lrc`

输出 `xxx_mixed.lrc`

Blog post: https://wyf9.top/posts/mix-lyrics

## [get_clip](./get_clip/main.py)

用于获取复制的双语歌词 (换行分隔) 并转换成以 ` / ` 分隔的歌词输出

启动后每 500ms 刷新一次剪贴板, ^C 退出

## [parse_mzh_lyrics](./parse_mzh_lyrics/main.py)

和上面的 get_clip 类似, 但是是在执行后获取一次剪贴板内容, 以换行为分隔符, 同样转换成以 ` / ` 分隔的歌词输出

> *如名称, 这个脚本适用于萌娘百科中全歌歌词的转换*
