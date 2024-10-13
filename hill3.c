#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(){
    int choice;
    float encrypt[3][1], decrypt[3][1], a[3][3], b[3][3], mes[3][1], c[3][3], d[3][3];
    printf("Enter a number between 1 and 3: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            int i, j; 
            char key[20];
            printf("Enter key text\n ");
            scanf("%s", key);
            int count=0;

            for (i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++)
                {
                    key[i] = toupper(key[count]);
                    a[i][j] = key[i] - 65;
                    printf("%d ", a[i][j]);
                    count++;
                }
            }
            char msg[20];
            int determinant = 0, t = 0;
            printf("\nEnter plain text\n ");
            scanf("%s", msg);
            for (i = 0; i < 3; i++) {
                msg[i] = toupper(msg[i]);
                c[i] = msg[i] - 65;
                printf("%d ", c[i]);
            }

            for (i = 0; i < 3; i++) {
                t = 0;
                for (j = 0; j < 3; j++) {
                    t = t + (a[i][j] * c[j]);
                }
                d[i] = t % 26;
            }
            printf("\nEncrypted Cipher Text :");
            for (i = 0; i < 3; i++)
                printf(" %c", d[i] + 65);
            break;

        case 2:
            char msg[20];
            int determinant = 0, t = 0;
            printf("\nEnter cipher text\n ");
            scanf("%s", msg);
            for (i = 0; i < 3; i++) {
                msg[i] = toupper(msg[i]);
                c[i] = msg[i] - 65;
                printf("%d ", c[i]);
            }
            break;
        default:
            printf("Invalid choice! Please select a number between 1 or 2.\n");
    }
}
