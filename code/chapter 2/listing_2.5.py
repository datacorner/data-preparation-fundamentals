import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    ticket_counts = df.groupby('Ticket')['PassengerId'].count().reset_index()
    same_tickets = ticket_counts[ticket_counts['PassengerId'] > 1] 
    dfTickAna = df.merge(same_tickets [['Ticket']], 
                        on='Ticket', 
                        how='inner') 
    dfTickAna[["PassengerId", "Ticket", "Fare"]].sort_values(by=["Ticket"])
    print (dfTickAna)