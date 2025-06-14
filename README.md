# 🐝 BeeHoney - POO Game

Um jogo simples desenvolvido em Python usando Pygame, onde você controla uma abelha que deve coletar flores enquanto evita aranhas!

## 🎮 Sobre o Jogo

BeeHoney é um jogo de ação onde o jogador controla uma abelha que precisa:
- ✅ Coletar flores para ganhar pontos
- ❌ Evitar aranhas que fazem você perder vida
- 🎯 Sobreviver o máximo de tempo possível

## 🎯 Características

- **Movimento fluido**: Controle a abelha com as teclas direcionais
- **Sistema de pontuação**: Ganhe pontos coletando flores
- **Sistema de vida**: Você tem 3 vidas, perde uma ao tocar em aranhas
- **Animações**: Personagens animados (abelha, aranhas, flores)
- **Cenário dinâmico**: Fundo em movimento contínuo

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pygame** - Biblioteca para desenvolvimento de jogos

## 📋 Pré-requisitos

Antes de executar o jogo, certifique-se de ter:

```bash
# Python 3.x instalado
python --version

# Pygame instalado
pip install pygame
```

## 🚀 Como Executar

1. **Clone o repositório**:
```bash
git clone https://github.com/seu-usuario/BeeHoney-POO.git
cd BeeHoney-POO
```

2. **Execute o jogo**:
```bash
python main.py
```

## 🎮 Como Jogar

1. **Menu Principal**: Pressione qualquer tecla para começar
2. **Controles**: Use as setas do teclado para mover a abelha
   - ⬆️ Seta para cima: Move para cima
   - ⬇️ Seta para baixo: Move para baixo
   - ⬅️ Seta para esquerda: Move para esquerda
   - ➡️ Seta para direita: Move para direita
3. **Objetivo**: Colete flores (pontos) e evite aranhas (perdem vida)
4. **Game Over**: O jogo termina quando suas 3 vidas acabam

## 📁 Estrutura do Projeto

```
BeeHoney-POO/
├── main.py           # Arquivo principal do jogo
├── game.py           # Lógica principal do gameplay
├── menu.py           # Sistema de menus
├── obj.py            # Classes de objetos (Bee, Obj, Text)
├── assets/           # Recursos gráficos
│   ├── bee1-4.png    # Sprites da abelha
│   ├── spider1-4.png # Sprites das aranhas
│   ├── flower1-2.png # Sprites das flores
│   ├── bg.png        # Fundo do jogo
│   ├── start.png     # Tela de início
│   ├── gameover.png  # Tela de game over
│   └── youwin.png    # Tela de vitória
└── README.md         # Este arquivo
```

## 🎯 Conceitos de POO Aplicados

O projeto demonstra diversos conceitos de Programação Orientada a Objetos:

- **Classes e Objetos**: `Obj`, `Bee`, `Game`, `Menu`, etc.
- **Herança**: A classe `Bee` herda de `Obj`
- **Encapsulamento**: Métodos e atributos organizados dentro das classes
- **Abstração**: Interface simples para controle dos objetos do jogo

## 🎨 Assets

O jogo inclui sprites animados para:
- 🐝 Abelha (4 frames de animação)
- 🕷️ Aranhas (4 frames de animação)
- 🌸 Flores (2 frames de animação)
- 🖼️ Fundos e telas de interface

## 🔄 Funcionalidades

### Implementadas ✅
- Sistema de movimento da abelha
- Detecção de colisões
- Sistema de pontuação e vidas
- Animações dos sprites
- Menu principal e game over
- Movimento automático de inimigos e coletáveis

### Possíveis Melhorias 🔮
- Sistema de níveis de dificuldade
- Power-ups especiais
- Música e efeitos sonoros
- Rankings de pontuação
- Mais tipos de inimigos

## 👨‍💻 Desenvolvimento

Este jogo foi desenvolvido como projeto educacional para demonstrar conceitos de:
- Programação Orientada a Objetos em Python
- Desenvolvimento de jogos com Pygame
- Estruturação de código em módulos
- Gerenciamento de assets e recursos

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades  
- Enviar pull requests
- Melhorar a documentação

---

**Divirta-se jogando BeeHoney! 🐝🍯**

