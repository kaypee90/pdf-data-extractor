import fitz

filename = "foo.pdf"

FIGURE_KEYWORD = "Figure"
IDLE_KEYWORD = "Idle"


def is_beginning_of_table(block):
    return str(block).startswith(IDLE_KEYWORD)


def is_end_of_table(block):
    return FIGURE_KEYWORD in str(block)


def print_table(table_rows):
    header = (
        f"\n========================================================================================================================\n"
        f"                    Table 2-1. Simulated fuel savings from isolated cycle improvements      \n"
        f"========================================================================================================================\n\n"
        f"Cycle         KI          Distance        Improved           Decreased           Eliminate            Decreased\n"
        f"Name        (1/km)         (mi)           Speed              Accel               Stops                Idle\n"
        f"=====      =======       ========        ========          ===========          ============        ==============\n"
    )

    print(header)
    print("".join(table_rows))


def main():
    with fitz.open(filename) as doc:
        page = doc[0]
        blocks = page.get_text("blocks")
        start_capture = False
        rows = []

        for block in blocks:
            if is_end_of_table(block[4]):
                break

            if start_capture:
                records = str(block[4]).split("\n")
                cycle_name = records[0]
                ki = records[1]
                distance = records[2]
                improved_speed = records[3]
                decreased_accl = records[4]
                elimiate_stops = records[5]
                decreased_idle = records[6]
                row = (
                    f"{cycle_name}      {ki}         {distance}          {improved_speed}               {decreased_accl}               {elimiate_stops}               {decreased_idle} \n"
                    f"=====      =======       ========        ========       ==============       ===============        ==============\n"
                )
                rows.append(row)
            if is_beginning_of_table(block[4]):
                start_capture = True

        print_table(rows)


if __name__ == "__main__":
    main()
