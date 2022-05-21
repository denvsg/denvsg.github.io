# first

#### Description
{**When you're done, you can delete the content in this README and update the file with details for others getting started with your repository**}

#### Software Architecture
Software architecture description

#### Installation

要测试通过 HTTPS 端口的 SSH 是否可行，请运行以下 SSH 命令：

$ ssh -T -p 443 git@ssh.github.com
> Hi username! You've successfully authenticated, but GitHub does not
> provide shell access.
如果这样有效，万事大吉！ 如果无效，您可能需要遵循我们的故障排除指南。

启用通过 HTTPS 的 SSH 连接
如果您能在端口 443 上通过 SSH 连接到 git@ssh.github.com，则可以覆盖您的 SSH 设置以强制与 GitHub.com 的任何连接均通过该服务器和端口运行。

要在 SSH 配置文件中设置此设置，请在 ~/.ssh/config 编辑该文件，并添加以下部分：

Host github.com
Hostname ssh.github.com
Port 443
User git
您可以通过再次连接到 GitHub.com 测试此项是否有效：

$ ssh -T git@github.com
> Hi username! You've successfully authenticated, but GitHub does not
> provide shell access.

<br />
<br />
<br />
<br />

Welcome to study together, and welcome pr.

<br />
<br />
<br />

