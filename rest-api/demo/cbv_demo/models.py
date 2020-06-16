from django.db import models
from demo import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

OFFICIAL_TYPE = (
    ('REF', 'Referee'),
    ('GAM', 'Game Manager'),
    ('GRS', 'Ground Staff'),

)

POSITION_TYPE = (
    ('CO', 'Coach'),
    ('MA', 'Manager'),
    ('AM', 'Assistant Manager')
)

TITLE = (
    ('MR.', 'MR.'),
    ('MRS.', 'MRS.'),
    ('MS.', 'MS.')
)

PLAYER_POSITION = (
    ('CEN', 'Centre'),
    ('PWF', 'Power Forward'),
    ('SMF', 'Small Forward'),
    ('SHG', 'Shooting Guard'),
    ('POG', 'Point Guard')
)

TOURNAMENT_STATUS = (
    ('ST', 'STARTED'),
    ('PL', 'PLANNING'),
    ('EN', 'END'),
    ('HL', 'HOLD'),
    ('PB', 'PUBLISHED'),
    ('CL', 'CANCELLED'),
    ('PP', 'POSTPONED')
)

GAME_STATUS = (
    ('ST', 'STARTED'),
    ('NP', 'NOT YET PLAYED'),
    ('EN', 'END'),
    ('HL', 'HOLD'),
    ('CL', 'CANCELLED'),
    ('PP', 'POSTPONED')
)

SQUAD_TYPE = (
    ('PL', 'PLAYER'),
    ('MG', 'MANAGEMENT'),
    ('OF', 'OFFICIALS')
)

STAGE_TYPE = (
    ('DE', 'Duel Elimination'),
    ('LG', 'League'),
)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    record_status = models.PositiveIntegerField(default=1)
    version = models.BigIntegerField(default=1)

    class Meta:
        abstract = True


class User(AbstractUser):
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "t_users"


class Venue(BaseModel):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    geo_location = models.CharField(max_length=100)

    class Meta:
        db_table = "t_venues"


class Team(BaseModel):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=250)

    class Meta:
        db_table = "t_teams"


class Person(BaseModel):
    name_in_full = models.CharField(max_length=150)
    title = models.CharField(
        max_length=4,
        choices=TITLE,
        default="MR.",
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    age = models.SmallIntegerField()
    initials = models.CharField(max_length=50)
    calling_name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default="F",
    )
    email = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)

    class Meta:
        abstract = True


class Official(Person):
    official_type = models.CharField(
        max_length=3,
        choices=OFFICIAL_TYPE,
        default="REF",
    )

    class Meta:
        db_table = "t_officials"


class Player(Person):
    player_position = models.CharField(
        max_length=3,
        choices=PLAYER_POSITION,
        default="CEN",
    )

    class Meta:
        db_table = "t_players"


class Management(Person):
    position_type = models.CharField(
        max_length=2,
        choices=POSITION_TYPE,
        default="CO",
    )

    class Meta:
        db_table = "t_team_management"


class LoginSummary(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    logged_in_time = models.DateTimeField()
    logged_out_time = models.DateTimeField()

    class Meta:
        db_table = "t_login_summary"


class Tournament(BaseModel):
    tournament_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tournament_status = models.CharField(
        max_length=2,
        choices=TOURNAMENT_STATUS,
        default="EN",
    )

    class Meta:
        db_table = "t_tournaments"


class TournamentOfficial(BaseModel):
    official = models.ForeignKey(Official,
                                 null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    class Meta:
        db_table = "t_tournament_officials"


class TournamentSquad(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    team = models.ForeignKey(Team,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    squad_type = models.CharField(
        max_length=2,
        choices=SQUAD_TYPE,
        default="PL",
    )
    player = models.ForeignKey(Player,
                               null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    management = models.ForeignKey(Management,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    is_captain = models.BooleanField()

    class Meta:
        db_table = "t_tournament_squad"


class TournamentStage(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    stage_no = models.SmallIntegerField()
    stage_name = models.CharField(max_length=100)
    no_of_teams = models.SmallIntegerField()
    stage_type = models.SmallIntegerField()
    point_won = models.SmallIntegerField()
    point_lost = models.SmallIntegerField()
    point_draw = models.SmallIntegerField()

    class Meta:
        db_table = "t_tournament_stages"


class TournamentTeam(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    team = models.ForeignKey(Team,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    sequence_no = models.SmallIntegerField()
    stage = models.ForeignKey(TournamentStage,
                              null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    tournament_position = models.SmallIntegerField()
    points = models.SmallIntegerField()
    games = models.SmallIntegerField()
    won = models.SmallIntegerField()
    lost = models.SmallIntegerField()
    draw = models.SmallIntegerField()
    rate_cal = models.DecimalField(max_digits=8,decimal_places=2)

    class Meta:
        db_table = "t_tournament_teams"


class Game(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    team_1 = models.ForeignKey(Team,
                               null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    team_2 = models.ForeignKey(Team,
                               null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    stage = models.ForeignKey(TournamentStage,
                              null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    from_game_1 = models.ForeignKey('self',
                                    null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    from_game_2 = models.ForeignKey('self',
                                    null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    round = models.SmallIntegerField()
    venue = models.ForeignKey(Venue,
                              null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    game_time = models.DateTimeField()
    game_status = models.CharField(
        max_length=2,
        choices=GAME_STATUS,
        default="ST",
    )
    team_1_score = models.SmallIntegerField()
    team_2_score = models.SmallIntegerField()
    game_sequence = models.SmallIntegerField()

    class Meta:
        db_table = "t_games"


class GamePlayer(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    game = models.ForeignKey(Game,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    team = models.ForeignKey(Team,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    player = models.ForeignKey(Player,
                               null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    class Meta:
        db_table = "t_game_players"


class PlayerAttempts(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    game = models.ForeignKey(Game,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    team = models.ForeignKey(Team,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    player = models.ForeignKey(Player,
                               null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    attempt_time = models.DateTimeField()
    score = models.SmallIntegerField()

    class Meta:
        db_table = "t_game_player_attempts"


class EventType(BaseModel):
    event_type = models.CharField(max_length=250)

    class Meta:
        db_table = "t_event_types"


class GameEvent(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    game = models.ForeignKey(Game,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    team = models.ForeignKey(Team,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    player_attempt = models.ForeignKey(PlayerAttempts,
                                       null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    event_time = models.DateTimeField()
    event_type = models.ForeignKey(EventType,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    event_description = models.CharField(max_length=250)

    class Meta:
        db_table = "t_game_events"


class GameOfficial(BaseModel):
    tournament = models.ForeignKey(Tournament,
                                   null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    game = models.ForeignKey(Game,
                             null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    official = models.ForeignKey(Official,
                                 null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    class Meta:
        db_table = "t_game_officials"
