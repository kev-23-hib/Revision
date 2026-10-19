class FilActualite:
    def trier(self, publications: list, mode: str) -> list:
        if mode == "chronologique":
            return sorted(publications, key=lambda p: p.date, reverse=True)
        elif mode == "populaire":
            return sorted(publications, key=lambda p: p.nb_likes, reverse=True)
        elif mode == "recommande":
            score = lambda p: p.nb_likes * 0.6 + p.nb_commentaires * 0.4
            return sorted(publications, key=score, reverse=True)
        else:
            raise ValueError(f"Mode inconnu : {mode}")