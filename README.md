## python脚本文件执行方法

编写 py 脚本文件，在第一行加上解释器的路径。以下二者任选一：

```python
#!/usr/bin/python3
#!/usr/bin/env python3
```

二者的区别在于： 
`#!/usr/bin/python3`是告诉操作系统在调用脚本时调用`/usr/bin`目录下的 python3 解释器。

`#!/usr/bin/env python3`是为了防止用户没有将 python3 安装在默认的 `/usr/bin` 路径里。当系统读到这一行时，首先会到 env 环境设置里查找 python3 的路径，再调用对应路径下的解释器程序完成操作。通常推荐第二种写法。 

要注意 # 和 ! 还有 后面的路径之间不能有空格，否则会报错



增加可执行权限

```shell
chmod a+x test.py
```

执行

```shell
./test.py
```



