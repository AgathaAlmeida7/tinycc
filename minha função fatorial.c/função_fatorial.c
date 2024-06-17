#include <stdio.h>

// Fun��o para calcular o fatorial de um n�mero
int fatorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * fatorial(n - 1);
    }
}

int main() {
    int numero, resultado;

    // Solicita ao usu�rio que entre com um n�mero inteiro
    printf("Digite um n�mero inteiro positivo: ");
    scanf("%d", &numero);

    // Verifica se o n�mero � negativo
    if (numero < 0) {
        printf("Erro: O n�mero deve ser positivo.\n");
        return 1; // Retorna 1 indicando erro
    }

    // Calcula o fatorial do n�mero fornecido
    resultado = fatorial(numero);

    // Exibe o resultado
    printf("O fatorial de %d �: %d\n", numero, resultado);

    return 0; // Retorna 0 indicando sucesso
}

