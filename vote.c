#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_QUESTIONS 10
#define MAX_OPTIONS 5
#define MAX_VOTERS 100

typedef struct {
    char question[100];
    char options[MAX_OPTIONS][50];
    int votes[MAX_OPTIONS];
    int numOptions;
} Poll;

Poll polls[MAX_QUESTIONS];
int numPolls = 0;
int numVoters = 0;

void createPoll() {
    if (numPolls < MAX_QUESTIONS) {
        printf("Entrez la question du sondage : ");
        fgets(polls[numPolls].question, sizeof(polls[numPolls].question), stdin);
        polls[numPolls].question[strlen(polls[numPolls].question) - 1] = '\0'; // Remove newline character

        printf("Entrez le nombre d'options (maximum %d) : ", MAX_OPTIONS);
        scanf("%d", &polls[numPolls].numOptions);
        getchar(); // Clear input buffer

        printf("Entrez les options :\n");
        for (int i = 0; i < polls[numPolls].numOptions; i++) {
            printf("Option %d: ", i + 1);
            fgets(polls[numPolls].options[i], sizeof(polls[numPolls].options[i]), stdin);
            polls[numPolls].options[i][strlen(polls[numPolls].options[i]) - 1] = '\0'; // Remove newline character
            polls[numPolls].votes[i] = 0; // Initialize votes to zero
        }

        printf("Sondage créé avec succès!\n");
        numPolls++;
    } else {
        printf("Nombre maximum de sondages atteint!\n");
    }
}

void vote() {
    if (numPolls == 0) {
        printf("Aucun sondage disponible pour voter!\n");
        return;
    }

    printf("Choisissez un sondage pour voter :\n");
    for (int i = 0; i < numPolls; i++) {
        printf("%d. %s\n", i + 1, polls[i].question);
    }
    int choice;
    printf("Votre choix : ");
    scanf("%d", &choice);
    getchar(); // Clear input buffer

    if (choice < 1 || choice > numPolls) {
        printf("Choix invalide!\n");
        return;
    }

    printf("Choisissez une option pour voter :\n");
    for (int i = 0; i < polls[choice - 1].numOptions; i++) {
        printf("%d. %s\n", i + 1, polls[choice - 1].options[i]);
    }
    int option;
    printf("Votre choix : ");
    scanf("%d", &option);
    getchar(); // Clear input buffer

    if (option < 1 || option > polls[choice - 1].numOptions) {
        printf("Choix invalide!\n");
        return;
    }

    polls[choice - 1].votes[option - 1]++;
    printf("Vote enregistré avec succès!\n");
    numVoters++;
}

void displayResults() {
    if (numPolls == 0) {
        printf("Aucun sondage disponible pour afficher les résultats!\n");
        return;
    }

    printf("Résultats des sondages :\n");
    for (int i = 0; i < numPolls; i++) {
        printf("%s\n", polls[i].question);
        for (int j = 0; j < polls[i].numOptions; j++) {
            printf("%s : %d votes\n", polls[i].options[j], polls[i].votes[j]);
        }
        printf("\n");
    }
}

int main() {
    int choice;
    do {
        printf("\nSystème de Vote en Ligne\n");
        printf("1. Créer un sondage\n");
        printf("2. Voter\n");
        printf("3. Afficher les résultats\n");
        printf("0. Quitter\n");
        printf("Choix : ");
        scanf("%d", &choice);
        getchar(); // Clear input buffer

        switch (choice) {
            case 1:
                createPoll();
                break;
            case 2:
                vote();
                break;
            case 3:
                displayResults();
                break;
            case 0:
                printf("Au revoir!\n");
                break;
            default:
                printf("Choix invalide!\n");
                break;
        }
    } while (choice != 0);

    return 0;
}
