#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SERIES 10
#define MAX_NAME_LENGTH 50

typedef struct {
    char name[MAX_NAME_LENGTH];
    int season;
    int episode;
} Series;

Series seriesList[MAX_SERIES];
int numSeries = 0;

// Fonction pour ajouter une série
void addSeries() {
    if (numSeries < MAX_SERIES) {
        printf("Nom de la série : ");
        scanf("%s", seriesList[numSeries].name);
        printf("Saison en cours : ");
        scanf("%d", &seriesList[numSeries].season);
        printf("Épisode en cours : ");
        scanf("%d", &seriesList[numSeries].episode);
        numSeries++;
        printf("Série ajoutée avec succès!\n");
    } else {
        printf("Nombre maximum de séries atteint!\n");
    }
}

// Fonction pour mettre à jour les informations sur une série
void updateSeries() {
    char name[MAX_NAME_LENGTH];
    printf("Nom de la série à mettre à jour : ");
    scanf("%s", name);
    int found = 0;
    for (int i = 0; i < numSeries; i++) {
        if (strcmp(seriesList[i].name, name) == 0) {
            printf("Nouvelle saison en cours : ");
            scanf("%d", &seriesList[i].season);
            printf("Nouvel épisode en cours : ");
            scanf("%d", &seriesList[i].episode);
            found = 1;
            printf("Informations de %s mises à jour avec succès!\n", name);
            break;
        }
    }
    if (!found) {
        printf("Série non trouvée!\n");
    }
}

// Fonction pour afficher les séries en cours
void displaySeries() {
    if (numSeries == 0) {
        printf("Aucune série enregistrée!\n");
    } else {
        printf("Séries en cours :\n");
        for (int i = 0; i < numSeries; i++) {
            printf("%s - Saison %d, Épisode %d\n", seriesList[i].name, seriesList[i].season, seriesList[i].episode);
        }
    }
}

int main() {
    int choice;
    do {
        printf("\nTracker de Séries TV\n");
        printf("1. Ajouter une série\n");
        printf("2. Mettre à jour une série\n");
        printf("3. Afficher les séries en cours\n");
        printf("0. Quitter\n");
        printf("Choix : ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addSeries();
                break;
            case 2:
                updateSeries();
                break;
            case 3:
                displaySeries();
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
