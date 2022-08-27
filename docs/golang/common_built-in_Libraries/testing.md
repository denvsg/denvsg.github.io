**golang 标准库 testing 包为 Go 代码支持了自动化测试。使用 go test 命令来执行。**

## 介绍

### 函数测试定义：

`func TestXxx(*testing.T)`

##### 这个 TestXxx 函数式放在一个文件尾部名 _test.go 中。

一个简单的测试：

```golang
func TestAbs(t *testing.T) {
    got := Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}
```

# Benchmarks

函数定义：

`func BenchmarkXxx(*testing.B)`
测试基准通过 go test -bench 来执行。

+ -cover 命令行参数，显示覆盖率信息 一个简单的基准测试：

```golang
func BenchmarkHello(b *testing.B) {
    for i := 0; i < b.N; i++ {
        fmt.Sprintf("hello")
    }
}

BenchmarkHello    10000000    282 ns/op
```

基准函数通过执行 b.N 次。例如上面 10000000 次每个执行时间在 282 ns。

## Subtests and Sub-benchmarks(子测试与子基准)

这种子测试可以实现表驱动基准测试和创建分层测试。也可以提供通用的 setup 和 teardown 方法。

```golang
func TestFoo(t *testing.T) {
    // <setup code>
    t.Run("A=1", func(t *testing.T) { ... })
    t.Run("A=2", func(t *testing.T) { ... })
    t.Run("B=1", func(t *testing.T) { ... })
    // <tear-down code>
}
```

## Main

有时测试必须为测试代码添加额外的 setup 和 teardown 在测试之前和之后。也有时必须控制那些代码在主线程执行，去支持其他情况。代码定义：

`func TestMain(m *testing.M)`
当执行测试时会调用 TestMain，而不是直接运行测试。这时可以在 m.Run 的前后调用 setup 和 teardown 方法。

```golang
func TestMain(m *testing.M) {
    // call flag.Parse() here if TestMain uses flags
    // setup
    code := m.Run()
    // teardown
    os.Exit(code)
}
```

# 常用的测试方法

Error(args ...interface{}) 输出测试错误信息。 Log(args ...interface{}) 输出测试日志信息。 Parallel() 并发测试。 Fatal(args ...interface{})
致命错误信息。 Skip(args ...interface{}) 跳过这个测试错误。

## testdata

testdata 测试文件夹下可以存放一些测试需要用到的测试数据、静态文件。

# 表驱动测试（Table-driven test）

表测试是通过构建数据表来运行测试的一种方法。可以结合 subtest 来覆盖各种测试情况。

```golang
func TestOrderSrv_OrderSendToPay(t *testing.T) {
    room := Room{}
    db.First(&room)
    order := test_createOrder(t, room)

    type args struct {
        order *models.Order
    }
    tests := []struct {
        name    string
        args    args
        wantErr bool
    }{
        {
            name: "提交订单",
            args: args{
                order: order,
            },
            wantErr: false,
        },
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            s := &OrderSrv{}
            if err := s.OrderSendToPay(tt.args.order); (err != nil) != tt.wantErr {
                t.Errorf("OrderSrv.OrderSendToPay() error = %v, wantErr %v", err, tt.wantErr)
            }
        })
    }
}
```

建议使用 vscode 或 golandIDE 的 Go 插件支持生成测试用例模板。