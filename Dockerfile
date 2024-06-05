# 使用基础镜像
FROM elodielaine/gemme:gemme

# 设置维护者信息（可选）
LABEL maintainer="lmc1998@qq.com"

# 安装必要的软件包
RUN apt-get update && \
    apt-get install -y software-properties-common

# 安装OpenSSH服务器
RUN apt-get install -y openssh-server

# 安装miniconda
RUN mkdir -p ~/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
RUN rm -rf ~/miniconda3/miniconda.sh

# 激活base环境并安装所需的包
RUN /bin/bash -c "source /opt/conda/bin/activate base && pip install numpy pandas biopython flask"

# 创建SSH运行目录
RUN mkdir /var/run/sshd

# 配置SSH允许root用户登录（可选，根据需要）
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config

# 设置root用户密码（强烈建议根据需求更改密码）
RUN echo 'root:root_password' | chpasswd

# 暴露12112端口
EXPOSE 12112

# 启动SSH服务
CMD ["/usr/sbin/sshd", "-D"]
