import pandas as pd
from pipeline import run_pipeline


def main():

    df = run_pipeline()

    df.to_csv("data/processed/dados_re.csv", index=False, sep=";")
    df.to_parquet("data/processed/dados_re.parquet", index=False)
    df.to_pickle("data/processed/dados-re.pkl")

    df_new = pd.read_parquet("data/processed/dados_re.parquet")
    print(df_new)


if __name__ == "__main__": #“Só roda o main se eu executar esse arquivo diretamente.”
    main()