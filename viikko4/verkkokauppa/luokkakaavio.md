
```mermaid
sequenceDiagram
    Alice->>Bob: Hello Bob, how are you ?
    Bob->>Alice: Fine, thank you. And you?
    create participant Carl
    Alice->>Carl: Hi Carl!
    create actor D as Donald
    Carl->>D: Hi!
    destroy Carl
    Alice-xCarl: We are too many
    destroy Bob
    Bob->>Alice: I agree
``` 

```mermaid
sequenceDiagram
    Varasto->>main: varasto
    Pankki->>main: pankki
    Viitegeneraattori->>main: main
    main->>kauppa: Kauppa(varasto, pankki, viitegeneraattori)
    kauppa->>varasto: 
``` 