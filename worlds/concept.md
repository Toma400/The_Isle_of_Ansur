# Worldpack concept

---

> **worldpack_name**
> > **FILES**
> > - [main.json](concept.md#mainjson)
> > ---
> > **FOLDERS**
> > - locations
> > ---

---

> **locations**
> > **FILES**
> > - [loc_main.json](concept.md#loc_mainjson)
> > ---
> > **FOLDERS**
> > - sounds
> > - dialogues
> > ---

---

### MAIN.JSON
> Entrypoint {values}
> > Designates entry level:
> > - vanilla handling
> > - ship
> > - sleep (requires another condition)
> > - altar
> >
> Alternate conditions {values}
> > Allows entrypoint if returns *True*
> >
> Descript {value}
> > Name to be described

### LOC_MAIN.JSON
> Sound {list}
> > List of sounds run during entering the location
> > - [#]default - default sound folder contents
> > - other values
> Dialogue choices {list}
> > Entries from `dialogues` that are available from location point
> Descript {value}
> > Name of the location
> Utils {booleans}
> > is_bed, is_fire, etc. - serves as indicators if specific utils/workplaces are in location
> > [can be under separate file]
