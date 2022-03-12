FROM texlive/texlive

ARG uid
ARG gid

ENV RUNNING_IN_DOCKER true

RUN apt-get update \
    && apt-get install -y bash git vim curl zsh htop tmux unzip xindy\ 
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
#xindy: see https://tex.stackexchange.com/a/541990/108199


RUN groupadd -g ${gid} developer \
    && useradd -g developer -u ${uid} -m developer

RUN mkdir -p /app \
    && chown -R developer:developer /app

USER developer

RUN mkdir -p ~/.ssh \
    && mkdir -p ~/.vscode-server \
    && echo 'eval `ssh-agent -s`' >> ~/.profile

#https://dev.to/arctic_hen7/setting-up-zsh-in-docker-263f
RUN mkdir -p /home/developer/.antigen
RUN curl -L git.io/antigen > /home/developer/.antigen/antigen.zsh
COPY .dockershell.sh /home/developer/.zshrc
USER root
RUN chown -R developer:developer /home/developer/.antigen /home/developer/.zshrc
USER developer
RUN /bin/zsh /home/developer/.zshrc

#RUN curl -L https://get.oh-my.fish > /home/developer/install_omf \
#    && /usr/bin/fish /home/developer/install_omf --noninteractive --yes \
#    && rm /home/developer/install_omf

ENV HOME=/home/developer
ENV SHELL=/bin/zsh
