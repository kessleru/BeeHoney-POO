# 🐝 BeeHoney - Jogo de Abelha em Python

Um jogo divertido desenvolvido em Python usando Pygame, onde você controla uma abelha que deve coletar flores e evitar aranhas!

## 📖 Sobre o Jogo

BeeHoney é um jogo arcade onde o jogador controla uma abelha que voa pelo cenário coletando flores para ganhar pontos, enquanto evita aranhas que podem causar dano. O objetivo é sobreviver o máximo de tempo possível e acumular a maior pontuação.

## 🎮 Como Jogar

- **Controle**: Use o mouse para mover a abelha pela tela
- **Objetivo**: Colete flores (🌸) para ganhar pontos
- **Evite**: Aranhas (🕷️) que causam dano
- **Vidas**: Você tem 3 vidas no total
- **Game Over**: O jogo termina quando suas vidas acabam

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado
- Pygame instalado

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd BeeHoney-POO
```

2. Instale o Pygame:
```bash
pip install pygame
```

3. Execute o jogo:
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
BeeHoney-POO/
├── main.py          # Arquivo principal do jogo
├── game.py          # Lógica principal do gameplay
├── obj.py           # Classes dos objetos (Abelha, Objetos genéricos)
├── menu.py          # Sistema de menus (início e game over)
├── assets/          # Recursos gráficos
│   ├── bee1-4.png   # Sprites da abelha (animação)
│   ├── spider1-4.png # Sprites das aranhas (animação)
│   ├── florwer1-2.png # Sprites das flores (animação)
│   ├── bg.png       # Imagem de fundo
│   ├── start.png    # Tela de início
│   ├── gameover.png # Tela de game over
│   └── youwin.png   # Tela de vitória
└── README.md        # Este arquivo
```

## 🎯 Características do Jogo

- **Sistema de Vidas**: 3 vidas iniciais
- **Sistema de Pontuação**: Ganhe pontos coletando flores
- **Animações**: Sprites animados para todos os objetos
- **Física Simples**: Movimento fluido e detecção de colisão
- **Interface**: Menus de início e game over
- **Controle Responsivo**: Controle suave com o mouse

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal
- **Pygame**: Biblioteca para desenvolvimento de jogos 2D
- **POO (Programação Orientada a Objetos)**: Estrutura do código

## 👨‍💻 Estrutura do Código

### Classes Principais

- **`Main`**: Classe principal que gerencia o loop do jogo e as transições entre telas
- **`Game`**: Contém a lógica principal do gameplay
- **`Obj`**: Classe base para todos os objetos do jogo
- **`Bee`**: Classe da abelha (herda de Obj), com controles e sistema de vida/pontos
- **`Menu`** e **`GameOver`**: Classes para gerenciar as telas de interface

### Funcionalidades

- Sistema de animação baseado em frames
- Detecção de colisão entre sprites
- Movimento contínuo de fundo (scrolling)
- Spawning aleatório de inimigos e itens
- Gerenciamento de estados do jogo

## 🎨 Assets

O jogo utiliza sprites personalizados para:
- Abelha com 4 frames de animação
- Aranhas com 4 frames de animação  
- Flores com 2 frames de animação
- Cenário de fundo com efeito parallax
- Telas de interface (menu e game over)

## 📈 Possíveis Melhorias

- [ ] Sistema de power-ups
- [ ] Diferentes tipos de inimigos
- [ ] Níveis de dificuldade
- [ ] Sistema de recordes
- [ ] Efeitos sonoros
- [ ] Mais tipos de flores/bônus

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abrir um Pull Request

---

**Divirta-se jogando BeeHoney! 🐝🍯**