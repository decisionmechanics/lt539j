import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    import altair as alt
    import janitor.polars
    import polars as pl
    return alt, janitor, pl


@app.cell
def __(pl):
    shark_incidents_df = (
        pl
        .read_csv("data/shark-incidents.csv", infer_schema_length=None)
        .clean_names()
    )
    return (shark_incidents_df,)


@app.cell
def __(shark_incidents_df):
    shark_incidents_df
    return


@app.cell
def __(alt, pl, shark_incidents_df):
    (
        shark_incidents_df
        .filter(
            pl.col("victim_injury") == "fatal",
            pl.col("shark_common_name").is_not_null(),
        )
        .get_column("shark_common_name")
        .value_counts()
        .plot
        .bar(
            x=alt.X("count", title="Fatalities"),
            y=alt.Y("shark_common_name", sort="-x", title="Species"),
        )
        .properties(
            width=500,
            height=100,
        )
    )
    return


if __name__ == "__main__":
    app.run()
