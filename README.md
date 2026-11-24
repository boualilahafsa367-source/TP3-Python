# Exercice 1 : Gestion des employés

**Figure 1 : Exécution du programme – Gestion des employés et calcul des salaires**

<img width="1920" height="578" alt="image" src="https://github.com/user-attachments/assets/02834aeb-f1d2-46de-be22-b952754b3d00" />


Cet exercice consiste à développer un système de gestion des employés d'une entreprise en utilisant le principe de l'héritage. L'objectif est de représenter plusieurs catégories d'employés qui possèdent des informations communes, mais dont les rémunérations peuvent être calculées différemment selon leur fonction.

Pour réaliser cette organisation, une classe parent appelée Employe a été créée. Elle contient les deux attributs communs à tous les employés : nom et salaire_base. Son constructeur __init__() permet d'initialiser ces informations lors de la création d'un objet. Elle possède également une méthode salaire_total() qui retourne le salaire de base, ainsi qu'une méthode spéciale __str__() qui permet d'afficher le nom de l'employé et son salaire total sous une forme lisible.

Deux classes enfants ont ensuite été développées à partir de cette classe principale. La classe Manager hérite de Employe et ajoute un attribut spécifique appelé prime, qui représente une somme supplémentaire accordée au manager. Son constructeur utilise super().__init__() pour récupérer et initialiser les attributs communs de la classe parent. La méthode salaire_total() est redéfinie afin de calculer la rémunération en additionnant le salaire de base et la prime.

La deuxième classe spécialisée, Developpeur, hérite également de Employe. Elle possède un attribut supplémentaire nommé technologie, qui représente la technologie de programmation maîtrisée par le développeur. Sa méthode salaire_total() est redéfinie pour calculer un bonus en fonction de cette technologie. Dans notre implémentation, un développeur utilisant Python reçoit un bonus de 500 €, tandis qu'un développeur utilisant une autre technologie reçoit un bonus de 300 €.

Pour vérifier le fonctionnement du programme, trois objets différents ont été créés : un employé standard nommé Nadia avec un salaire de base de 2800 €, un manager nommé Karim avec un salaire de base de 3500 € et une prime de 950 €, ainsi qu'une développeuse nommée Imane avec un salaire de base de 3200 € et une spécialisation en Java.

Les trois objets ont été regroupés dans une même liste appelée equipe. Une boucle for parcourt ensuite cette liste et affiche chaque employé à l'aide de l'instruction print(personne). Même si les objets appartiennent à des classes différentes, ils peuvent être traités de manière similaire grâce à leur classe parent commune et à la méthode __str__() héritée.

Le résultat affiché dans le terminal montre que Nadia conserve son salaire de base de 2800 €, que Karim reçoit un salaire total de 4450 € après l'ajout de sa prime, et qu'Imane obtient une rémunération de 3500 € après l'ajout du bonus correspondant à sa technologie.

Cet exercice permet ainsi de mettre en pratique plusieurs notions fondamentales de la programmation orientée objet : l'héritage, la réutilisation du constructeur parent avec super(), la redéfinition des méthodes et le polymorphisme. Il montre également comment une classe générale peut être réutilisée pour créer plusieurs classes spécialisées sans répéter inutilement les mêmes instructions.


# Exercice 2 : Bibliothèque

**Figure 2 : Exécution du programme – Gestion et affichage des documents d'une bibliothèque**

<img width="1920" height="561" alt="image" src="https://github.com/user-attachments/assets/d7950ea6-c670-4b14-8ece-8a6fd7410d84" />


Cet exercice consiste à développer un système simplifié de gestion des documents d'une bibliothèque en appliquant les principes de l'héritage. L'objectif est de créer une structure permettant de représenter plusieurs catégories de documents à partir d'une classe générale, tout en ajoutant des informations spécifiques à chaque catégorie.

La classe principale du programme est Document. Elle représente un document générique et contient deux attributs communs : titre et annee, qui correspondent respectivement au titre du document et à son année de publication. Son constructeur __init__() permet d'initialiser ces deux informations. Elle possède également une méthode afficher() chargée de présenter les informations générales du document.

Deux classes spécialisées ont été créées à partir de cette classe parent : Livre et Magazine.

La classe Livre hérite de Document et ajoute un attribut spécifique appelé auteur. Son constructeur utilise super().__init__(titre, annee) afin de récupérer les attributs communs de la classe parent, puis initialise l'auteur du livre. La méthode afficher() est redéfinie afin de présenter le titre, le nom de l'auteur et l'année de publication.

La classe Magazine hérite également de Document, mais elle ajoute un attribut différent appelé numero, qui permet d'identifier le numéro du magazine. Comme pour la classe Livre, son constructeur utilise super() pour initialiser les informations héritées. Sa méthode afficher() est ensuite redéfinie afin de présenter le titre du magazine, son numéro et son année de publication.

Pour tester le fonctionnement du système, trois objets ont été créés : deux livres intitulés « Les mystères du désert » et « Voyage au bout du monde », ainsi qu'un magazine intitulé « Science et Découverte ». Chaque objet possède ses propres informations, notamment son année de publication et les données spécifiques à sa catégorie.

Les trois documents ont ensuite été regroupés dans une seule liste appelée collection. Une boucle for parcourt cette collection et appelle la méthode afficher() pour chaque document.

Cette partie est particulièrement importante, car elle illustre le polymorphisme. En effet, le programme utilise le même appel document.afficher() pour tous les objets, mais le résultat obtenu dépend de leur classe réelle. Lorsqu'il s'agit d'un livre, la méthode affiche son auteur, tandis que pour un magazine, elle affiche son numéro. Chaque classe enfant possède donc sa propre version de la méthode afficher().

Le résultat obtenu dans le terminal présente correctement les trois documents avec leurs informations respectives. Les deux livres sont affichés avec leur titre, leur auteur et leur année de publication, tandis que le magazine apparaît avec son titre, son numéro et son année.

Cet exercice permet de comprendre comment l'héritage facilite la création de catégories spécialisées à partir d'une classe générale. Il met également en évidence l'utilité de super() pour éviter la répétition du code, de la redéfinition des méthodes pour adapter les comportements et du polymorphisme pour manipuler différents types d'objets à travers une même interface.
