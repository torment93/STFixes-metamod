# CS2 1.41.9.2: IVEngineServer2 gana IsSpawnGroupLoadedForClient tras MakeSpawnGroupActive (alliedmodders/hl2sdk#438).
import re, sys
f = sys.argv[1]; t = open(f).read()
if "IsSpawnGroupLoadedForClient" not in t:
    t, n = re.subn(r"(\n[ \t]*virtual void\s+MakeSpawnGroupActive\( SpawnGroupHandle_t spawnGroup \) = 0;\n)",
                   r"\1\tvirtual bool\tIsSpawnGroupLoadedForClient( CPlayerSlot nSlot, SpawnGroupHandle_t spawnGroup ) = 0;\n", t)
    assert n == 1, n
    open(f, "w").write(t)
