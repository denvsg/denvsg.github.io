# vim 使用  

## 目录  

[1、命令模式](#命令模式 )  
[2、插入模式](#插入模式 )  
[3、可视模式](#可视模式 )  
[4、底行模式](#底行模式 )  
[5、寄存器](#寄存器 )  
[6、宏](#宏 )  
[go back](./Readme.md )  

## 命令模式  

进入vi编辑器默认是命令模式，如在插入模式可以按 **【Esc】** 回到命令模式

### 1. 单个字符命令  

    移动：h(左)，j(上)，k(下)，l(右)  
    编辑：d(删除-delete) c(修改-change) y(复制-yank) p(粘帖-print)  
    对象：w(单词-words)，p(段落),   
    位置：i(单词中-不包括符号，空格分界) a(单词中-仅空格分界)

### 2.移动

    h/j/k/l  分别代表 左/下/上/右  
    gg       回到首行  
    G        回到尾行  
    ctrl+u/ctrl+b    上翻半/一页  
    ctrl+d/ctrl+f    下翻半/一页  
    {n}gg            跳到第n行  
    zz/zt/zb         光标设置到屏幕居中/第一行/最后一行  

    w    word  跳到下一单词开头
    b    back  跳到上一单词开头
    e    end   跳到下一单词结尾
    ge   跳到上一单词结尾
    web  小写对应单个单词，减号空格等可以作为分界
    WBE大写对应连续非空字符，空白字符作为分界

### 3.字符搜索移动  

#### 行内搜索  

    f{char}/t{char}  跳转到本行下一个char字符出现处/出现前  
    ;/，             快速向后/向前重复ft查找
    F{char}/T{char}  往前搜索

#### 文件中搜索  

    /{pattern}   跳转到文件下一个pattern处
    ?{pattern}   跳转到文件上一个pattern处
    *    等价于/pattern, pattern表示当前光标所在的单词
    n/N      快速重复/查找 n向下 / N向上
>pattern 代表要搜索的字符串，可以是正则表达式  

#### 基于标记的移动  

    m{mark}      标记当前位置为mark
    `{mark}      跳转到mark标记位置
        mark是[a-z]的字符
    内置标记
    ``   上次跳转前的位置
    `.   上次修改的位置
    `^   上次插入的位置

#### 其他跳转按键  

    ^/$ 跳转到本行开头/结尾
    %   跳转到匹配的配对符出，如括号引号等

### 高效编辑  

>operator + motion = action 操作+移动  

    c     修改，删除内容并进入编辑模式
    d     删除
    x     剪贴
    y     复制
    v     选中文本进入可视模式
    操作符重复表示对当前行生效
    dd   删除当前行
    
    例子：
        dgg    删除到第一行
        ye     复制到单词结尾
        d$     删除到行尾
        dt;    删除后面直到分号的内容

#### 重复命令  

    .       重复上一次修改
    u       撤销上一次修改
    ctrl+r  重做上一次修改，u的反向
    
    
    批量操作 数字➕动作
      4j    下移动4行
      3dw   删除3个单词
      2yy   复制2行
      4p    粘贴4次

#### 文本对象操作

    格式：i/a + 对象  
    对象有：  
        w/W, s, p       单词，句子，段落  
        () [] {} <> '"  配对符对象  
    i表示inner, 只包括单词或者配对符内部部分  
    a还额外包括单词后的空格，和前后的配对符如括号  


    示例：count+operator+textobject  
      diw    删除一个单词
      ci(    修改小括号内部内容，清除小括号内部并进入插入编辑模式
      yi{    复制大括号内部内容  

**操作➕移动**和**操作➕文本**对比  
>
>    1. 移动可以单独使用web  
>    2. 文本对象只能在操作后面，不能单独用，iw  
>    3. 移动可以查看光标位置，使用灵活，但范围不明确  
>    4. 文本对象显示指定操作对象，范围明确  

**相关插件**：  

    vim-easymotion  拓展移动，很强大的跳 功能  
    vim-surround    定义了添加配对符的跳转  
    vim-commentary  添加注释的操作  
    targets.vim  定义了新文本对象，比如函数参数  

#### 操作符补充  

        gu/gU/g~   转小写 /转大写/大小写翻转
        J          连接两行
        ctrl+a/ctrl+x   增加数字/减少数字
        g ctrl+a        创建递增序列
        </>             左/右缩进

## 插入模式  

  insert mode  

 字符  | 解释             
-----|----------------
 i   | 光标之前开始输入       
 a   | 光标之后开始输入       
 o   | 当前行下插入新一行开始输入  
 s   | 删除当前光标的字符并开始输入 
 I   | 在本行行首开始输入      
 A   | 在本行行尾开始输入      
 O   | 当前行上插入新一行并开始输入 
 S   | 删除当前行并开始输入     

## 可视模式  

1. 按v可进入可视模式  
2. 可视模式可以使用移动键选中文本  
3. x/y 是剪贴/复制, 后续可进行粘贴p  
4. normal模式按V进入可视模式可以按行选中  
5. 按esc回到normal模式  

### 添加多行注释  

    + 按ctrl+v进入可视模式
    + 选择吸引注释的行  
    + 按大写字母I，再输入注释符号 //  或 #  
    + 按Esc退出，注释符就会完成添加，可能需要稍等一会等待完成  
    + 取消同理

## 底行模式  

 操作  | 解释    
-----|-------
 :w  | 保存文件  
 :q  | 退出    
 :q! | 强制退出  
 :wq | 保存并退出 
 :h  | 帮助    
  :set relativenumber 开启相对行号，可以对复制删除操作更直观  

### 命令模式操作以行为单位  

global和normal 命令提供批量操作  

    命令格式：:[range]{excommand}[args]  
        range     作用范围，默认本行  
        excommand 特殊命令，适用于命令行模式  
        args      其他参数，按命令提供  
     示例Ex命令，x是可选的寄存器  
        :[range] delete [x]  删除x的行并存放到x寄存器，delete可以简写d  
        :[range] yank [x]    复制range行到寄存器x，yank可简写y  
        :[range] print       把range行输出出来，print可简写p

range 由一个或两个address构成，即{address}或{address,address}  

    address可选范围有：  
      行号lineno，0表示第一行之上的虚拟行，可用来插入新的第一行  
      $ 最后一行  
      .  光标所在行  
      /pattern/  下一个pattern的行  
    address 支持加减，.+3表示光标往下第三行$-3 表示倒数第四行
    示例：
        1，3     文件的1-3行。如1,3 d 删除1-3行
        .，.+4   当前及往下4行
        $-3,$    文件的最后4行
    %      特殊range,代表文件所有行
    '<,'>  可视模式选中的开头和结尾，可以在可视模式下选中按：直接设置

#### 行复制移动粘贴  

    :[range] copy {address}  把range中行复制到adress后面
    :[range] move {address}  把range中行移动到adress后面
    :[address] put [x]       把寄存器x的内容粘贴到adress后面
    0作为虚拟行可以用来插入第一行

#### normal命令  

格式    `:[range] normal {commands}`  

    对range的所有行执行normal模式下的commands命令
        range   是%时，对整个文件生效
    :[range] normal .  搭配.使用，可以先完一修改  
    :[range] normal @{register}.  搭配寄存器使用，因为.只记录一次修改  

#### global命令  

格式 ：`:[range] global/{pattern}/[cmd]`

    对range中的包含pattern的所有行执行command模式下的ex命令,cmd 默认是打印，另外上面的normal也是可以当ex命令使用  
    :[range] global/{pattern}/normal{commands} 对range中的所有带pattern的行行模式下的commang命令  
    :% global /TUDO/delete  删除所有带todo的行

#### 替换命令  

    :[range]s/{pattern}/{string}/[flags] pattern替换为 string  
    flags可选的有  
        g  替换一行的所有匹配  
        i  忽略大小写  
        c  替换前进行确认  
        n  计数而不是替换  
    :%s/vim//gn 统计文件所有vim出现的次数，有n不会执行替换  

## 寄存器  

> 一个字符对应一个寄存器0-9a-z  

    特殊寄存器  
    "    默认寄存器，存放复制删除的内容  
    %  当前文件名
    .     上一次插入的内容  
    :     上一次执行的命令  

**通过 `:reg {register寄存器}` 查看寄存器中的内容**  

指定寄存器使用 `"{register}`  即可使用指定寄存器  

    示例
        "ayy   复制当前行到a寄存器  
        "bdiw  删除单词并存放到b寄存器  
        "cp    把c寄存器的内容粘贴出来  

**使用大写寄存器字符表示追加内容而不是覆盖**  

## 宏  

>录制一些列键盘操作，并允许重放  

    操作序列存储在寄存器中  
    q{register}    开始录制宏，存放在register寄存器  中。开始录制时下方会显示recoding  @a  
    录制按q退出录制  
    @{register}   重放寄存器的宏  
    @@            重放上一次宏操作  
    常见用法：@{register}录制一段宏，@{register}重放，然后一直@@重放  
        注意.命令对宏不生效，.只记录上一次修改  
宏也可以搭配数字完成重放多次的操作［count ］@{register}  

[go top](#vim-使用 )  
[go back](./Readme.md )  
