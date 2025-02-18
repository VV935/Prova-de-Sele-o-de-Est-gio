def get_empresa_with_obrigacoes(db: Session, fk_empresa: int):
    empresa = db.query(Empresa).filter(fk.empresa == fk_empresa).first()
    if empresa:
        return empresa
    return None
