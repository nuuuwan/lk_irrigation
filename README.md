# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--27_13:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,075 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 13:03:17 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:03:05 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.039 |  |
| 2026-11-27 13:03:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 13:03:04 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:03:01 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-11-27 13:02:37 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-27 13:02:37 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.060 |  |
| 2026-11-27 13:02:26 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.075 |  |
| 2026-11-27 13:02:16 | Thanamalwila (Kirindi Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-11-27 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | -0.010 |  |
| 2026-11-27 13:02:15 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.061 |  |
| 2026-11-27 13:02:04 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.050 |  |
| 2026-11-27 13:02:02 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-11-27 13:01:11 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-27 13:00:58 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.135 |  |
| 2026-11-27 13:00:44 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:00:29 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-27 13:00:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-27 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.31 | 🟡 Alert | -0.010 |  |
| 2026-11-27 13:02:37 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.060 |  |
| 2026-11-27 12:04:39 | Magura (Kalu Ganga) | 4.18 | 🟡 Alert | -0.115 |  |
| 2026-11-27 13:00:58 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.135 |  |
| 2026-11-27 12:03:01 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-27 13:03:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-27 13:02:37 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-27 12:00:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:00:44 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:04:11 | Galgamuwa (Mee Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:03:17 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-27 13:03:04 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:01:06 | Manampitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:03:21 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-27 12:02:36 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-27 13:01:11 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-27 12:04:23 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-11-27 13:03:01 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-11-27 13:00:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-11-27 13:02:02 | Moragaswewa (Deduru Oya) | 3.35 | 🟢 Normal | -0.020 |  |
| 2026-11-27 12:03:23 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-27 13:00:29 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-27 12:04:33 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.022 |  |
| 2026-11-27 12:01:55 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-11-27 13:03:05 | Ellagawa (Kalu Ganga) | 6.64 | 🟢 Normal | -0.039 |  |
| 2026-11-27 12:03:55 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-11-27 12:00:22 | Kuda Oya (Kirindi Oya) | 2.53 | 🟢 Normal | -0.041 |  |
| 2026-11-27 12:07:49 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.046 |  |
| 2026-11-27 13:02:04 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.050 |  |
| 2026-11-27 13:02:16 | Thanamalwila (Kirindi Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-11-27 13:02:15 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.061 |  |
| 2026-11-27 12:03:35 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.065 |  |
| 2026-11-27 12:03:18 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.066 |  |
| 2026-11-27 12:06:09 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | -0.069 |  |
| 2026-11-27 13:02:26 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.075 |  |
| 2026-11-27 12:01:11 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | -0.082 |  |
| 2026-11-27 12:01:57 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.091 |  |
| 2026-11-27 12:02:23 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | -0.105 |  |
| 2026-11-27 12:01:50 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)