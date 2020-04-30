from sqlalchemy.orm import Session

import models
import schemas


def create_alarm(db: Session, alarm: schemas.AlarmCreate):
    db_alarm = models.ALARM(EventID=alarm.EventID, SourceName=alarm.SourceName, SourcePath=alarm.SourcePath,
                            SourceID=alarm.SourceID, ServerName=alarm.ServerName, TicksTimeStamp=alarm.TicksTimeStamp, EventTimeStamp=alarm.EventTimeStamp,
                            EventCategory=alarm.EventCategory, Severity=alarm.Severity, Priority=alarm.Priority, State=alarm.State, Quality=alarm.Quality,
                            Message=alarm.Message)
    db.add(db_alarm)
    db.commit()
    db.refresh(db_alarm)
    # db.close()
