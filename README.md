# goodreads-book-picker
Ce programme permet de choisir un livre de votre pal aléatoirement à partir d'un fichier .csv téléchargé à partir du site Goodreads.

This Python program was made to choose a random book in your tbr shelf from a .csv file downloaded from Goodreads.

**_Comment utiliser ce programme Python ?_**

__!Si vous ne trouvez pas une des sections dans le site Goodreads, tapez `Ctrl + F` puis le nom de l'élément recherché!__

Afin d'utiliser ce programme, il vous faudra :
1) Aller sur le site _`goodreads.com`_
2) Cliquer sur `My Books` et dans la section `Tools`, cliquez sur le lien `Import and export`.
3) Un bouton `Export library` devrait apparaître parmis une nouvelle page. Cliquer dessus. Cela peut prendre du temps mais on devrait finir par avoir un lien type *your export from ...* qui, une fois cliqué, télécharge un fichier au format .csv.
4) Après avoir installé tous les modules nécéssaires (voir étape ), lancer le programme Python téléchargé au préalable.
5) Une boîte de dialogue devrait s'ouvrir. Sélectionner le fichier .csv téléchargé à partir de Goodreads.
6) Et voilà! Dans la console, le livre choisi devrait s'afficher :)
7) Si le programme ne marche pas, assurez vous d'avoir installé les modules avec `pip install *le nom du module, soit [random], [pandas] ou [tkinter]*`
