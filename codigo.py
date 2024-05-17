import flet as ft

def main(pagina: ft.Page):
    pagina.bgcolor = ft.colors.BLACK
    pagina.window_always_on_top = True
    pagina.scroll = ft.ScrollMode.AUTO

    def mudar_imagem(e):
        for elemento in opcoes.controls:
            if elemento == e.control:
                elemento.opacity = 1
                imagem_principal.src = elemento.image_src
            else:
                elemento.opacity = 0.5
        imagem_principal.update()
        opcoes.update()
    
    imagem_produto = ft.Container(
       col={'xs':12,'md':6},
       bgcolor=ft.colors.WHITE,
       padding=ft.padding.all(30),
       aspect_ratio=10/16,
       content=ft.Column(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                         controls=[
                             imagem_principal := ft.Image(src='https://woodprime.vtexassets.com/arquivos/ids/238702/cadeira-018-3001-14161-compuse-02.jpg?v=638100993053030000'),
                             opcoes := ft.Row(
                                 alignment=ft.MainAxisAlignment.CENTER,
                                 controls=[
                                     ft.Container(
                                         image_src='https://woodprime.vtexassets.com/arquivos/ids/238702/cadeira-018-3001-14161-compuse-02.jpg?v=638100993053030000',
                                         height=80,
                                         width=80,
                                         on_click=mudar_imagem,
                                     ),
                                     ft.Container(
                                         image_src='https://images.tcdn.com.br/img/img_prod/824768/cadeira_mineira_almofada_91_1_871f520e5c964f2a902a2a7854fa2f30.jpg',
                                         height=80,
                                         width=80,
                                         opacity=0.5,
                                         on_click=mudar_imagem,
                                     ),
                                     ft.Container(
                                         image_src='https://global.cdn.magazord.com.br/gamma/img/2023/11/produto/1340/01-cadeira-telinha-madeira-macica-berlim-nozes.png?ims=435x435',
                                         height=80,
                                         width=80,
                                         opacity=0.5,
                                         on_click=mudar_imagem
                                     )
                                 ]
                             )
                         ]
                   )
    )

    detalhes_produto = ft.Container(
        col={'xs':12, 'md':6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=10/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='CADEIRAS',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Text(
                    value='Poltrona rustica',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=25
                ),
                ft.Text(
                    value='Sala de estar',
                    color=ft.colors.GREY,
                    italic=True
                ),
                ft.ResponsiveRow(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs':12,'sm':6},
                            value='R$ 399',
                            color=ft.colors.WHITE,
                            size=30
                        ),
                        ft.Row(
                            col={'xs':12,'sm':6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        ),

                        ft.Tabs(
                            height=200,
                            selected_index=0,
                            indicator_color=ft.colors.AMBER,
                            label_color=ft.colors.AMBER,
                            unselected_label_color=ft.colors.GREY,
                            tabs=[
                                ft.Tab(
                                    text='Descrição',
                                    content=ft.Container(
                                        padding=ft.padding.all(30),
                                        content=ft.Text(
                                            value='Esta cadeira combina o conforto e o charme do estilo rural tradicional com a sofisticação e elegância do design moderno. Feita de madeira de alta qualidade, como pinho ou carvalho, essa cadeira apresenta uma estrutura robusta e durável que exala uma sensação de calor e acolhimento.'
                                        )
                                    )
                                ),
                                ft.Tab(
                                    text='Detalhes',
                                    content=ft.Container(
                                        padding=ft.padding.all(30),
                                        content=ft.Text(
                                            value='Dimensões: 0.8m de largura, 0.9m de altura e 0.76m de profundidade     Material dos pés: Eucalipto'
                                        )
                                    )
                                )
                            ]
                        ),
                        ft.ResponsiveRow(
                            columns=12,
                            controls=[
                                ft.Dropdown(
                                    col=6,
                                    label='cor',
                                    label_style=ft.TextStyle(color=ft.colors.WHITE,size=16),
                                    border_color=ft.colors.GREY,
                                    border_width=0.5,
                                    options=[
                                        ft.dropdown.Option(text='azul'),
                                        ft.dropdown.Option(text='Vermelho'),
                                        ft.dropdown.Option(text='Amarelo'),
                                    ]
                                ),
                                ft.Dropdown(
                                    col=6,
                                    label='quantidade',
                                    label_style=ft.TextStyle(color=ft.colors.WHITE,size=16),
                                    border_color=ft.colors.GREY,
                                    border_width=0.5,
                                    options=[
                                        ft.dropdown.Option(text=f'{num}') for num in range(1,11)
                                    ]
                                )
                            ]
                        ),
                        ft.Container(expand=True),
                        ft.ElevatedButton(
                            width=900,
                            text='Adicionar a lista de desejo',
                            style=ft.ButtonStyle(
                                padding=ft.padding.all(20),
                                side={
                                    ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                                },
                                bgcolor={
                                    ft.MaterialState.DEFAULT: ft.colors.AMBER
                                },
                                color={
                                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                                    ft.MaterialState.HOVERED: ft.colors.AMBER_100
                                }
                            )
                        ),
                        ft.ElevatedButton(
                            width=900,
                            text='Adicionar ao carrinho',
                            style=ft.ButtonStyle(
                                padding=ft.padding.all(20),
                                side={
                                    ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                                },
                                bgcolor={
                                    ft.MaterialState.DEFAULT: ft.colors.AMBER
                                },
                                color={
                                    ft.MaterialState.DEFAULT: ft.colors.BLACK,
                                    ft.MaterialState.HOVERED: ft.colors.AMBER_100
                                }
                            )
                        )
                    ]
                )
            ]
        )
    )



    display = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                imagem_produto,
                detalhes_produto
            ]
        )
    )
    pagina.add(display)

if __name__ == "__main__":
    ft.app(target=main)
