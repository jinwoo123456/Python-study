#include <stdio.h>
#include <stdlib.h>

typedef struct Term
{
    int coef;
    int exp;
    struct Term *next;
} Term;

// 생성
Term *new_term(int coef, int exp)
{
    Term *term = (Term *)malloc(sizeof(Term));
    term->coef = coef;
    term->exp = exp;
    term->next = NULL;
    return term;
}

// 항삽입
void insert2(Term **poly, int coef, int exp)
{
    if (coef == 0 || exp < 0 || exp > 3)
        return;

    Term *term = new_term(coef, exp);

    if (*poly == NULL)
    {
        *poly = term;
        return;
    }

    Term *curr = *poly;
    Term *prev = NULL;

    while (curr != NULL && curr->exp > exp)
    {
        prev = curr;
        curr = curr->next;
    }

    if (curr != NULL && curr->exp == exp)
    {
        curr->coef += coef;
        free(term);

        if (curr->coef == 0)
        {
            if (prev == NULL)
            {
                *poly = curr->next;
            }
            else
            {
                prev->next = curr->next;
            }
            free(curr);
        }
    }
    else
    {
        if (prev == NULL)
        {
            term->next = *poly;
            *poly = term;
        }
        else
        {
            term->next = curr;
            prev->next = term;
        }
    }
}

// 다항식 출력
void print_poly(Term *poly)
{
    if (poly == NULL)
    {
        printf("0\n");
        return;
    }
    Term *curr = poly;
    while (curr != NULL)
    {
        if (curr->coef > 0 && curr != poly)
            printf(" + ");
        else if (curr->coef < 0)
            printf(" - ");

        int abs_coef = abs(curr->coef);
        if (abs_coef != 1 || curr->exp == 0)
            printf("%d", abs_coef);

        if (curr->exp != 0)
        {
            printf("x");
            if (curr->exp != 1)
                printf("^%d", curr->exp);
        }
        curr = curr->next;
    }
    printf("\n");
}

// 다항식 더하기
Term *add_poly(Term *poly1, Term *poly2)
{
    Term *result = NULL;
    Term *p1 = poly1;
    Term *p2 = poly2;

    while (p1 != NULL || p2 != NULL)
    {
        if (p2 == NULL || (p1 != NULL && p1->exp > p2->exp))
        {
            insert2(&result, p1->coef, p1->exp);
            p1 = p1->next;
        }
        else if (p1 == NULL || p1->exp < p2->exp)
        {
            insert2(&result, p2->coef, p2->exp);
            p2 = p2->next;
        }
        else
        {
            insert2(&result, p1->coef + p2->coef, p1->exp);
            p1 = p1->next;
            p2 = p2->next;
        }
    }
    return result;
}

// 다항식 곱하기
Term *mul_poly(Term *poly1, Term *poly2)
{
    Term *result = NULL;
    for (Term *p1 = poly1; p1 != NULL; p1 = p1->next)
    {
        for (Term *p2 = poly2; p2 != NULL; p2 = p2->next)
        {
            int coef = p1->coef * p2->coef;
            int exp = p1->exp + p2->exp;
            if (exp > 3)
                continue;
            insert2(&result, coef, exp);
        }
    }
    return result;
}

// 다항식 해제
void free_poly(Term *poly)
{
    while (poly != NULL)
    {
        Term *temp = poly;
        poly = poly->next;
        free(temp);
    }
}

int main()
{
    Term *poly1 = NULL;
    Term *poly2 = NULL;
    int n, coef, exp;

    printf("1번째 다항식 입력  :\n");
    printf("항의 개수  : ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("항 %d - 계수  : ", i + 1);
        scanf("%d", &coef);
        printf("항 %d - 지수(0~3)  : ", i + 1);
        scanf("%d", &exp);
        insert2(&poly1, coef, exp);
    }

    printf("\n2번째 다항식 입력  :\n");
    printf("항의 개수  : ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("항 %d - 계수  : ", i + 1);
        scanf("%d", &coef);
        printf("항 %d - 지수 (0~3)  : ", i + 1);
        scanf("%d", &exp);
        insert2(&poly2, coef, exp);
    }

    printf("\n1번째 다항식  : ");
    print_poly(poly1);
    printf("2번째 다항식  : ");
    print_poly(poly2);

    Term *sum = add_poly(poly1, poly2);
    printf("\n덧셈 결과  : ");
    print_poly(sum);

    Term *prod = mul_poly(poly1, poly2);
    printf("곱셈 결과   : ");
    print_poly(prod);

    free_poly(poly1);
    free_poly(poly2);
    free_poly(sum);
    free_poly(prod);

    return 0;
}
