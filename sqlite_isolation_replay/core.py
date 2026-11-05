import sqlite3
from .common import number,integer,identifier
import tempfile
from pathlib import Path
def run(d):
 value=integer(d.get('value',2),-1000000,1000000)
 with tempfile.TemporaryDirectory()as tmp:
  p=str(Path(tmp)/'db.sqlite');a=sqlite3.connect(p,timeout=0,isolation_level=None);b=sqlite3.connect(p,timeout=0,isolation_level=None)
  try:
   assert a.execute('pragma journal_mode=wal').fetchone()[0]=='wal'
   a.executescript('create table t(v);insert into t values(1);');a.execute('begin');before=a.execute('select v from t').fetchone()[0]
   b.execute('begin immediate');b.execute('update t set v=?',(value,));uncommitted=a.execute('select v from t').fetchone()[0];b.execute('commit');snapshot=a.execute('select v from t').fetchone()[0]
   try:a.execute('update t set v=99');error=None
   except sqlite3.OperationalError as e:error=getattr(e,'sqlite_errorname','SQLITE_BUSY')
   a.execute('rollback');fresh=a.execute('select v from t').fetchone()[0]
   return dict(before=before,uncommitted=uncommitted,snapshot_after_commit=snapshot,fresh_after_restart=fresh,upgrade_error=error,journal_mode='wal')
  finally:a.close();b.close()
