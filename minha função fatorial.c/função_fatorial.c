#include <stdio.h>

// Função para calcular o fatorial de um número
int fatorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * fatorial(n - 1);
    }
}

int main() {
    int numero, resultado;

    // Solicita ao usuário que entre com um número inteiro
    printf("Digite um número inteiro positivo: ");
    scanf("%d", &numero);

    // Verifica se o número é negativo
    if (numero < 0) {
        printf("Erro: O número deve ser positivo.\n");
        return 1; // Retorna 1 indicando erro
    }

    // Calcula o fatorial do número fornecido
    resultado = fatorial(numero);

    // Exibe o resultado
    printf("O fatorial de %d é: %d\n", numero, resultado);

    return 0; // Retorna 0 indicando sucesso
}

