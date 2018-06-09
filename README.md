# python_common
整理的python基本操作， 包含字符串处理，http请求， tornado示例等

## 目录结构

```
|__src  
	|__mycommon
	|__server
	|__service
|__tools
|__README.md
```

### mycommon

整理的python相关操作，包括文件的读取，字符串处理，时间处理，http服务的访问等

### server

基于tornado框架搭建的web服务，执行

```
python common_server.py
```

访问 http://localhost:12358/common?params=1528516800&type=timestamp2time 可查看示例结果

### service

为tornado服务提供Handle处理，服务实际处理类。