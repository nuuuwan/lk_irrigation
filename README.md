# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_11:03:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,048 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 11:03:13 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | -0.039 |  |
| 2026-11-09 11:03:04 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-09 11:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:52 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:02:41 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-09 11:02:29 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:23 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | -0.068 |  |
| 2026-11-09 11:02:20 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:01:54 | Dunamale (Aththanagalu Oya) | 4.43 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-11-09 11:01:52 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.050 |  |
| 2026-11-09 11:01:42 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:01:37 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:01:35 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:00:54 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:00:53 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 11:00:44 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:44:24 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 11:01:54 | Dunamale (Aththanagalu Oya) | 4.43 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-11-09 10:12:47 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-09 11:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.98 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-09 10:06:44 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 10:44:24 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.044 |  |
| 2026-11-09 10:12:46 | Magura (Kalu Ganga) | 5.06 | 🟡 Alert | -0.053 |  |
| 2026-11-09 10:03:39 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-09 10:06:06 | Pitabeddara (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-11-09 10:06:54 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-09 11:00:53 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 10:04:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:05:16 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:13:34 | Badalgama (Maha Oya) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-11-09 11:00:44 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-09 10:10:01 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:20 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:01:35 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:05:15 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:03:04 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:02:29 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-11-09 11:00:54 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-09 10:05:01 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.019 |  |
| 2026-11-09 11:01:42 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:02:52 | Horowpothana (Yan Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-11-09 11:01:37 | Thanamalwila (Kirindi Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-11-09 10:01:37 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-09 11:02:41 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-09 10:09:08 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.035 |  |
| 2026-11-09 11:03:13 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | -0.039 |  |
| 2026-11-09 10:05:32 | Moragaswewa (Deduru Oya) | 2.77 | 🟢 Normal | -0.042 |  |
| 2026-11-09 11:01:52 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.050 |  |
| 2026-11-09 11:02:23 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | -0.068 |  |
| 2026-11-09 10:02:11 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.070 |  |
| 2026-11-09 10:03:57 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.075 |  |
| 2026-11-09 10:03:06 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.087 |  |
| 2026-11-09 10:04:17 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.108 |  |
| 2026-11-09 10:02:39 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | -0.140 |  |
| 2026-11-09 10:09:29 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)