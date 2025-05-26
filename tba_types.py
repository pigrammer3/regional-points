from typing import TypedDict, NamedTuple, Literal, NotRequired, TypeIs, TypeAlias


class TeamEventOPR(NamedTuple):
    team: str
    event: str
    opr: float
    week: int
    regional_points: int


class DistrictList(TypedDict):
    abbreviation: str
    display_name: str
    key: str
    year: int


class Webcast(TypedDict):
    type: Literal[
        "youtube",
        "twitch",
        "ustream",
        "iframe",
        "html5",
        "rtmp",
        "livestream",
        "direct_link",
        "mms",
        "justin",
        "stemtv",
        "dacast",
    ]
    channel: str
    date: str | None
    file: str | None


class Event(TypedDict):
    key: str
    name: str
    event_code: str
    event_type: int
    district: DistrictList | None
    city: str | None
    state_prov: str | None
    country: str | None
    start_date: str
    end_date: str
    year: int
    short_name: str | None
    event_type_string: str
    week: int
    address: str | None
    postal_code: str | None
    gmaps_place_id: str | None
    gmaps_url: str | None
    lat: float | None
    lng: float | None
    location_name: str | None
    timezone: str
    website: str | None
    first_event_id: str | None
    first_event_code: str | None
    webcasts: list[Webcast]
    division_keys: list[str]
    parent_event_key: str | None
    playoff_type: int | None
    playoff_type_string: str | None


class SimpleTeam(TypedDict):
    key: str
    team_number: int
    nickname: str
    name: str
    city: str | None
    state_prov: str | None
    country: str | None

class Team(SimpleTeam):
    school_name: str | None
    address: str | None
    postal_code: str | None
    gmaps_place_id: str | None
    gmaps_url: str | None
    lat: float | None
    lng: float | None
    location_name: str | None
    website: NotRequired[str | None]
    rookie_year: int | None


class DistrictPoints(TypedDict):
    class PointsAtEventForTeam(TypedDict):
        total: int
        alliance_points: int
        elim_points: int
        award_points: int
        qual_points: int

    class TiebreakersAtEventForTeam(TypedDict):
        highest_qual_scores: list[int]
        qual_wins: list[int]

    points: dict[str, PointsAtEventForTeam]
    tiebreakers: dict[str, TiebreakersAtEventForTeam]


class OPRs(TypedDict):
    oprs: dict[str, float]
    dprs: dict[str, float]
    ccwms: dict[str, float]


class Award(TypedDict):
    class AwardRecepient(TypedDict):
        team_key: str
        awardee: str

    name: str
    award_type: int
    event_key: str
    recipient_list: list[AwardRecepient]
    year: int


class MatchAlliance(TypedDict):
    score: int
    team_keys: list[str]
    surrogate_team_keys: list[str]
    dq_team_keys: list[str]


class Alliances(TypedDict):
    red: MatchAlliance
    blue: MatchAlliance


class SimpleMatch(TypedDict):
    key: str
    comp_level: Literal["qm", "ef", "qf", "sf", "f"]
    set_number: int
    match_number: int
    alliances: Alliances
    winning_alliance: Literal["red", "blue", ""]
    event_key: str
    time: int | None
    actual_time: int | None
    predicted_time: int | None


class Video(TypedDict):
    type: Literal["youtube", "tba"]
    key: str


class Match(SimpleMatch):
    class MatchScoreBreakdown2015:
        class MatchScoreBreakdown2015Alliance:

            auto_points: int
            teleop_points: int
            container_points: int
            tote_points: int
            litter_points: int
            foul_points: int
            adjust_points: int
            total_points: int
            foul_count: int
            tote_count_far: int
            tote_count_near: int
            tote_set: bool
            tote_stack: bool
            container_count_level1: int
            container_count_level2: int
            container_count_level3: int
            container_count_level4: int
            container_count_level5: int
            container_count_level6: int
            container_set: bool
            litter_count_container: int
            litter_count_landfill: int
            litter_count_unprocessed: int
            robot_set: bool

        blue: MatchScoreBreakdown2015Alliance
        red: MatchScoreBreakdown2015Alliance
        coopertition: Literal["None", "Unknown", "Stack"]
        coopertition_points: int

    class MatchScoreBreakdown2016(TypedDict):
        class MatchScoreBreakdown2016Alliance(TypedDict):
            autoPoints: int
            teleopPoints: int
            breachPoints: int
            foulPoints: int
            capturePoints: int
            adjustPoints: int
            totalPoints: int
            robot1Auto: Literal["Crossed", "Reached", "None"]
            robot2Auto: Literal["Crossed", "Reached", "None"]
            robot3Auto: Literal["Crossed", "Reached", "None"]
            autoReachPoints: int
            autoCrossingPoints: int
            autoBouldersLow: int
            autoBouldersHigh: int
            autoBoulderPoints: int
            teleopCrossingPoints: int
            teleopBouldersLow: int
            teleopBouldersHigh: int
            teleopBoulderPoints: int
            teleopDefensesBreached: bool
            teleopChallengePoints: int
            teleopScalePoints: int
            teleopTowerCaptured: bool
            towerFaceA: str
            towerFaceB: str
            towerFaceC: str
            towerEndStrength: int
            techFoulCount: int
            foulCount: int
            position2: str
            position3: str
            position4: str
            position5: str
            position1crossings: int
            position2crossings: int
            position3crossings: int
            position4crossings: int
            position5crossings: int

        red: MatchScoreBreakdown2016Alliance
        blue: MatchScoreBreakdown2016Alliance

    class MatchScoreBreakdown2017:
        class MatchScoreBreakdown2017Alliance(TypedDict):
            autoPoints: int
            teleopPoints: int
            foulPoints: int
            adjustPoints: int
            totalPoints: int
            robot1Auto: Literal["Unknown", "Mobility", "None"]
            robot2Auto: Literal["Unknown", "Mobility", "None"]
            robot3Auto: Literal["Unknown", "Mobility", "None"]
            rotor1Auto: bool
            rotor2Auto: bool
            autoFuelLow: int
            autoFuelHigh: int
            autoMobilityPoints: int
            autoRotorPoints: int
            autoFuelPoints: int
            teleopFuelPoints: int
            teleopFuelLow: int
            teleopFuelHigh: int
            teleopRotorPoints: int
            kPaRankingPointAchieved: bool
            teleopTakeoffPoints: int
            kPaBonusPoints: int
            rotorBonusPoints: int
            rotor1Engaged: bool
            rotor2Engaged: bool
            rotor3Engaged: bool
            rotor4Engaged: bool
            rotorRankingPointAchieved: bool
            techFoulCount: int
            foulCount: int
            touchpadNear: str
            touchpadMiddle: str
            touchpadFar: str

        red: MatchScoreBreakdown2017Alliance
        blue: MatchScoreBreakdown2017Alliance

    class MatchScoreBreakdown2018(TypedDict):
        class MatchScoreBreakdown2018Alliance(TypedDict):
            adjustPoints: int
            autoOwnershipPoints: int
            autoPoints: int
            autoQuestRankingPoint: bool
            autoRobot1: str
            autoRobot2: str
            autoRobot3: str
            autoRunPoints: int
            autoScaleOwnershipSec: int
            autoSwitchAtZero: bool
            autoSwitchOwnershipSec: int
            endgamePoints: int
            endgameRobot1: str
            endgameRobot2: str
            endgameRobot3: str
            faceTheBossRankingPoint: bool
            foulCount: int
            foulPoints: int
            rp: int
            techFoulCount: int
            teleopOwnershipPoints: int
            teleopPoints: int
            teleopScaleBoostSec: int
            teleopScaleForceSec: int
            teleopScaleOwnershipSec: int
            teleopSwitchBoostSec: int
            teleopSwitchForceSec: int
            teleopSwitchOwnershipSec: int
            totalPoints: int
            vaultBoostPlayed: int
            vaultBoostTotal: int
            vaultForcePlayed: int
            vaultForceTotal: int
            vaultLevitatePlayed: int
            vaultLevitateTotal: int
            vaultPoints: int
            # Unofficial TBA-computed value of the FMS provided GameData given to the alliance teams at the start of the match.
            # 3 Character String containing `L` and `R` only. The first character represents the near switch, the 2nd the scale,
            # and the 3rd the far, opposing, switch from the alliance's perspective. An `L` in a position indicates the platform
            # on the left will be lit for the alliance while an `R` will indicate the right platform will be lit for the alliance.
            # See also [WPI Screen Steps](https://wpilib.screenstepslive.com/s/currentCS/m/getting_started/l/826278-2018-game-data-details).
            tba_gameData: str

        red: MatchScoreBreakdown2018Alliance
        blue: MatchScoreBreakdown2018Alliance

    class MatchScoreBreakdown2019(TypedDict):
        class MatchScoreBreakdown2019Alliance(TypedDict):
            adjustPoints: int
            autoPoints: int
            bay1: str
            bay2: str
            bay3: str
            bay4: str
            bay5: str
            bay6: str
            bay7: str
            bay8: str
            cargoPoints: int
            completeRocketRankingPoint: bool
            completedRocketFar: bool
            completedRocketNear: bool
            endgameRobot1: str
            endgameRobot2: str
            endgameRobot3: str
            foulCount: int
            foulPoints: int
            habClimbPoints: int
            habDockingRankingPoint: bool
            habLineRobot1: str
            habLineRobot2: str
            habLineRobot3: str
            hatchPanelPoints: int
            lowLeftRocketFar: str
            lowLeftRocketNear: str
            lowRightRocketFar: str
            lowRightRocketNear: str
            midLeftRocketFar: str
            midLeftRocketNear: str
            midRightRocketFar: str
            midRightRocketNear: str
            preMatchBay1: str
            preMatchBay2: str
            preMatchBay3: str
            preMatchBay6: str
            preMatchBay7: str
            preMatchBay8: str
            preMatchLevelRobot1: str
            preMatchLevelRobot2: str
            preMatchLevelRobot3: str
            rp: int
            sandStormBonusPoints: int
            techFoulCount: int
            teleopPoints: int
            topLeftRocketFar: str
            topLeftRocketNear: str
            topRightRocketFar: str
            topRightRocketNear: str
            totalPoints: int

        red: MatchScoreBreakdown2019Alliance
        blue: MatchScoreBreakdown2019Alliance

    class MatchScoreBreakdown2020(TypedDict):
        class MatchScoreBreakdown2020Alliance(TypedDict):
            initLineRobot1: str
            endgameRobot1: str
            initLineRobot2: str
            endgameRobot2: str
            initLineRobot3: str
            endgameRobot3: str
            autoCellsBottom: int
            autoCellsOuter: int
            autoCellsInner: int
            teleopCellsBottom: int
            teleopCellsOuter: int
            teleopCellsInner: int
            stage1Activated: bool
            stage2Activated: bool
            stage3Activated: bool
            stage3TargetColor: str
            endgameRungIsLevel: str
            autoInitLinePoints: int
            autoCellPoints: int
            autoPoints: int
            teleopCellPoints: int
            controlPanelPoints: int
            endgamePoints: int
            teleopPoints: int
            shieldOperationalRankingPoint: bool
            shieldEnergizedRankingPoint: bool
            # Unofficial TBA-computed value that indicates whether the shieldEnergizedRankingPoint was earned normally or awarded due to a foul.
            tba_shieldEnergizedRankingPointFromFoul: bool
            # Unofficial TBA-computed value that counts the number of robots who were hanging at the end of the match.
            tba_numRobotsHanging: int
            foulCount: int
            techFoulCount: int
            adjustPoints: int
            foulPoints: int
            rp: int
            totalPoints: int

        red: MatchScoreBreakdown2020Alliance
        blue: MatchScoreBreakdown2020Alliance

    class MatchScoreBreakdown2022(TypedDict):
        class MatchScoreBreakdown2022Alliance(TypedDict):
            taxiRobot1: Literal["Yes", "No"]
            endgameRobot1: Literal["Traversal", "High", "Mid", "Low", "None"]
            taxiRobot2: Literal["Yes", "No"]
            endgameRobot2: Literal["Traversal", "High", "Mid", "Low", "None"]
            taxiRobot3: Literal["Yes", "No"]
            endgameRobot3: Literal["Traversal", "High", "Mid", "Low", "None"]
            autoCargoLowerNear: int
            autoCargoLowerFar: int
            autoCargoLowerBlue: int
            autoCargoLowerRed: int
            autoCargoUpperNear: int
            autoCargoUpperFar: int
            autoCargoUpperBlue: int
            autoCargoUpperRed: int
            autoCargoTotal: int
            teleopCargoLowerNear: int
            teleopCargoLowerFar: int
            teleopCargoLowerBlue: int
            teleopCargoLowerRed: int
            teleopCargoUpperNear: int
            teleopCargoUpperFar: int
            teleopCargoUpperBlue: int
            teleopCargoUpperRed: int
            teleopCargoTotal: int
            matchCargoTotal: int
            autoTaxiPoints: int
            autoCargoPoints: int
            autoPoints: int
            quintetAchieved: bool
            teleopCargoPoints: int
            endgamePoints: int
            teleopPoints: int
            cargoBonusRankingPoint: bool
            hangarBonusRankingPoint: bool
            foulCount: int
            techFoulCount: int
            adjustPoints: int
            foulPoints: int
            rp: int
            totalPoints: int

        red: MatchScoreBreakdown2022Alliance
        blue: MatchScoreBreakdown2022Alliance

    class MatchScoreBreakdown2023(TypedDict):
        class MatchScoreBreakdown2023Alliance(TypedDict):
            class Community(TypedDict):
                B: list[Literal["None", "Cone", "Cube"]]
                M: list[Literal["None", "Cone", "Cube"]]
                T: list[Literal["None", "Cone", "Cube"]]

            class Link(TypedDict):
                nodes: list[Literal["None", "Cone", "Cube"]]
                row: Literal["Bottom", "Mid", "Top"]

            activationBonusAchieved: bool
            adjustPoints: int
            autoBridgeState: Literal["NotLevel", "Level"]
            autoChargeStationPoints: int
            autoChargeStationRobot1: Literal["None", "Docked"]
            autoChargeStationRobot2: Literal["None", "Docked"]
            autoChargeStationRobot3: Literal["None", "Docked"]
            autoDocked: bool
            autoCommunity: Community
            autoGamePieceCount: int
            autoGamePiecePoints: int
            autoMobilityPoints: int
            mobilityRobot1: Literal["Yes", "No"]
            mobilityRobot2: Literal["Yes", "No"]
            mobilityRobot3: Literal["Yes", "No"]
            autoPoints: int
            coopGamePieceCount: int
            coopertitionCriteriaMet: bool
            endGameBridgeState: Literal["NotLevel", "Level"]
            endGameChargeStationPoints: int
            endGameChargeStationRobot1: Literal["None", "Docked", "Park"]
            endGameChargeStationRobot2: Literal["None", "Docked", "Park"]
            endGameChargeStationRobot3: Literal["None", "Docked", "Park"]
            endGameParkPoints: int
            extraGamePieceCount: int
            foulCount: int
            foulPoints: int
            techFoulCount: int
            linkPoints: int
            links: list[Link]
            sustainabilityBonusAchieved: bool
            teleopCommunity: Community
            teleopGamePieceCount: int
            teleopGamePiecePoints: int
            totalChargeStationPoints: int
            teleopPoints: int
            rp: int
            totalPoints: int

    class MatchScoreBreakdown2024(TypedDict):
        class MatchScoreBreakdown2024Alliance(TypedDict):
            adjustPoints: int
            autoAmpNoteCount: int
            autoAmpNotePoints: int
            autoLeavePoints: int
            autoLineRobot1: str
            autoLineRobot2: str
            autoLineRobot3: str
            autoPoints: int
            autoSpeakerNoteCount: int
            autoSpeakerNotePoints: int
            autoTotalNotePoints: int
            coopNotePlayed: bool
            coopertitionBonusAchieved: bool
            coopertitionCriteriaMet: bool
            endGameHarmonyPoints: int
            endGameNoteInTrapPoints: int
            endGameOnStagePoints: int
            endGameParkPoints: int
            endGameRobot1: str
            endGameRobot2: str
            endGameRobot3: str
            endGameSpotLightBonusPoints: int
            endGameTotalStagePoints: int
            ensembleBonusAchieved: bool
            ensembleBonusOnStageRobotsThreshold: int
            ensembleBonusStagePointsThreshold: int
            foulCount: int
            foulPoints: int
            g206Penalty: bool
            g408Penalty: bool
            g424Penalty: bool
            melodyBonusAchieved: bool
            melodyBonusThreshold: int
            melodyBonusThresholdCoop: int
            melodyBonusThresholdNonCoop: int
            micCenterStage: bool
            micStageLeft: bool
            micStageRight: bool
            rp: int
            techFoulCount: int
            teleopAmpNoteCount: int
            teleopAmpNotePoints: int
            teleopPoints: int
            teleopSpeakerNoteAmplifiedCount: int
            teleopSpeakerNoteAmplifiedPoints: int
            teleopSpeakerNoteCount: int
            teleopSpeakerNotePoints: int
            teleopTotalNotePoints: int
            totalPoints: int
            trapCenterStage: bool
            trapStageLeft: bool
            trapStageRight: bool

        red: MatchScoreBreakdown2024Alliance
        blue: MatchScoreBreakdown2024Alliance

    class MatchScoreBreakdown2025(TypedDict):
        class MatchScoreBreakdown2025Alliance(TypedDict):
            class Reef(TypedDict):
                class ReefRow(TypedDict):
                    nodeA: bool
                    nodeB: bool
                    nodeC: bool
                    nodeD: bool
                    nodeE: bool
                    nodeF: bool
                    nodeG: bool
                    nodeH: bool
                    nodeI: bool
                    nodeJ: bool
                    nodeK: bool
                    nodeL: bool

                topRow: ReefRow
                midRow: ReefRow
                botRow: ReefRow
                trough: int
                # Unofficial TBA-computed value that sums the total number of game pieces scored in the botRow object.
                tba_botRowCount: int
                # Unofficial TBA-computed value that sums the total number of game pieces scored in the midRow object.
                tba_midRowCount: int
                # Unofficial TBA-computed value that sums the total number of game pieces scored in the topRow object.
                tba_topRowCount: int

            adjustPoints: int
            algaePoints: int
            autoBonusAchieved: bool
            autoCoralCount: int
            autoCoralPoints: int
            autoLineRobot1: Literal["No", "Yes"]
            autoLineRobot2: Literal["No", "Yes"]
            autoLineRobot3: Literal["No", "Yes"]
            autoMobilityPoints: int
            autoPoints: int
            autoReef: Reef
            bargeBonusAchieved: bool
            coopertitionCriteriaMet: bool
            coralBonusAchieved: bool
            endGameBargePoints: int
            endGameRobot1: Literal["None", "Parked", "ShallowCage", "DeepCage"]
            endGameRobot2: Literal["None", "Parked", "ShallowCage", "DeepCage"]
            endGameRobot3: Literal["None", "Parked", "ShallowCage", "DeepCage"]
            foulCount: int
            foulPoints: int
            g206Penalty: bool
            g410Penalty: bool
            g418Penalty: bool
            g428Penalty: bool
            netAlgaeCount: int
            rp: int
            techFoulCount: int
            teleopCoralCount: int
            teleopCoralPoints: int
            teleopPoints: int
            teleopReef: Reef
            totalPoints: int
            wallAlgaeCount: int

    Breakdown: TypeAlias = (
        MatchScoreBreakdown2015
        | MatchScoreBreakdown2016
        | MatchScoreBreakdown2017
        | MatchScoreBreakdown2018
        | MatchScoreBreakdown2019
        | MatchScoreBreakdown2020
        | MatchScoreBreakdown2022
        | MatchScoreBreakdown2023
        | MatchScoreBreakdown2024
        | MatchScoreBreakdown2025
        | None
    )

    @staticmethod
    def is2015(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2015]:
        return breakdown is not None and "tote_points" in breakdown["blue"]
    
    @staticmethod
    def is2016(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2016]:
        return breakdown is not None and "breachPoints" in breakdown["blue"]
    
    @staticmethod
    def is2017(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2017]:
        return breakdown is not None and "autoFuelLow" in breakdown["blue"]
    
    @staticmethod
    def is2018(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2018]:
        return breakdown is not None and "autoOwnershipPoints" in breakdown["blue"]
    
    @staticmethod
    def is2019(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2019]:
        return breakdown is not None and "completeRocketRankingPoint" in breakdown["blue"]
    
    @staticmethod
    def is2020(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2020]:
        return breakdown is not None and "autoCellsBottom" in breakdown["blue"]
    
    @staticmethod
    def is2022(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2022]:
        return breakdown is not None and "quintetAchieved" in breakdown["blue"]
    
    @staticmethod
    def is2023(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2023]:
        return breakdown is not None and "autoCommunity" in breakdown["blue"]
    
    @staticmethod
    def is2024(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2024]:
        return breakdown is not None and "autoAmpNoteCount" in breakdown["blue"]
    
    @staticmethod
    def is2025(breakdown: Breakdown) -> TypeIs[MatchScoreBreakdown2025]:
        return breakdown is not None and "autoReef" in breakdown["blue"]

    post_result_time = int | None
    videos: list[Video]
    score_breakdown: Breakdown
