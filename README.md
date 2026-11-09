# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_17:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,281 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 17:03:18 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.033 |  |
| 2026-11-09 17:03:04 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.061 |  |
| 2026-11-09 17:02:49 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-09 17:02:42 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:02:30 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-09 17:02:27 | Wellawaya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-09 17:02:23 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-11-09 17:02:09 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-11-09 17:01:49 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 17:01:31 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-11-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:00:49 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:00:09 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-11-09 16:46:09 | Baddegama (Gin Ganga) | 3.61 | 🟡 Alert | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 17:00:09 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-11-09 16:11:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-11-09 16:46:09 | Baddegama (Gin Ganga) | 3.61 | 🟡 Alert | -0.006 |  |
| 2026-11-09 16:15:27 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | -0.025 |  |
| 2026-11-09 16:08:24 | Dunamale (Aththanagalu Oya) | 4.38 | 🟡 Alert | -0.028 |  |
| 2026-11-09 16:09:34 | Magura (Kalu Ganga) | 4.51 | 🟡 Alert | -0.122 |  |
| 2026-11-09 16:11:07 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-11-09 17:02:49 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-09 17:02:27 | Wellawaya (Kirindi Oya) | 1.91 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-09 16:08:38 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-09 16:03:31 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-09 16:05:34 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-09 16:05:48 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-09 17:01:49 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 16:03:01 | Moragaswewa (Deduru Oya) | 2.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 16:04:27 | Horowpothana (Yan Oya) | 2.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 16:01:52 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-09 16:01:32 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-09 16:01:30 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:00:49 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-09 16:07:06 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 16:01:11 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 17:02:42 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.010 |  |
| 2026-11-09 16:02:18 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-11-09 16:10:40 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.018 |  |
| 2026-11-09 17:02:30 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-09 17:02:23 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | -0.021 |  |
| 2026-11-09 17:01:31 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-11-09 17:03:18 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.033 |  |
| 2026-11-09 16:04:17 | Giriulla (Maha Oya) | 2.64 | 🟢 Normal | -0.039 |  |
| 2026-11-09 17:02:09 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.040 |  |
| 2026-11-09 16:04:00 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.040 |  |
| 2026-11-09 16:05:09 | Badalgama (Maha Oya) | 3.85 | 🟢 Normal | -0.050 |  |
| 2026-11-09 17:03:04 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.061 |  |
| 2026-11-09 16:03:40 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | -0.091 |  |
| 2026-11-09 16:04:51 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.095 |  |
| 2026-11-09 16:04:02 | Hanwella (Kelani Ganga) | 3.89 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)