CREATE TABLE activity_votes (
  day TEXT NOT NULL,
  activity_id TEXT NOT NULL CHECK (activity_id IN ('hand-at-ease', 'familiar-route', 'notice-one-thing', 'music-or-silence', 'small-silly-mark', 'rest-or-leave')),
  votes INTEGER NOT NULL DEFAULT 0 CHECK (votes BETWEEN 0 AND 1000),
  PRIMARY KEY (day, activity_id)
);
--> statement-breakpoint
CREATE TABLE day_totals (
  day TEXT PRIMARY KEY NOT NULL,
  votes INTEGER NOT NULL DEFAULT 0 CHECK (votes BETWEEN 0 AND 2000)
);
