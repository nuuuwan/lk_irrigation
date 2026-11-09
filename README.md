# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_01:03:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,564 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Magura — Alert; 🟡 Thawalama — Alert; 🟡 Rathnapura — Alert; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 01:03:18 | Hanwella (Kelani Ganga) | 5.82 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-10 01:03:03 | Giriulla (Maha Oya) | 2.86 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-11-10 01:02:37 | Glencourse (Kelani Ganga) | 14.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 01:02:35 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.030 |  |
| 2026-11-10 01:02:27 | Thaldena (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.116 |  |
| 2026-11-10 01:02:25 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-10 01:02:23 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.164 |  |
| 2026-11-10 01:02:09 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-10 01:01:40 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | -0.086 |  |
| 2026-11-10 01:01:40 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-10 01:01:23 | Kuda Oya (Kirindi Oya) | 2.89 | 🟢 Normal | -0.043 |  |
| 2026-11-10 01:01:13 | Peradeniya (Mahaweli Ganga) | 5.14 | 🟡 Alert | -0.021 |  |
| 2026-11-10 01:00:35 | Moraketiya (Walawe Ganga) | 4.40 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 00:06:14 | Dunamale (Aththanagalu Oya) | 4.48 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-11-09 23:06:17 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-11-10 00:02:38 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-11-10 00:03:05 | Rathnapura (Kalu Ganga) | 5.43 | 🟡 Alert | 0.066 | 🔺 Rising |
| 2026-11-10 00:05:00 | Baddegama (Gin Ganga) | 3.85 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-11-10 00:01:55 | Panadugama (Nilwala Ganga) | 5.30 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-11-10 00:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-11-10 01:00:35 | Moraketiya (Walawe Ganga) | 4.40 | 🟡 Alert | 0.000 |  |
| 2026-11-10 00:11:53 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-11-10 01:01:13 | Peradeniya (Mahaweli Ganga) | 5.14 | 🟡 Alert | -0.021 |  |
| 2026-11-10 01:03:18 | Hanwella (Kelani Ganga) | 5.82 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-10 00:01:34 | Pitabeddara (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-11-10 01:03:03 | Giriulla (Maha Oya) | 2.86 | 🟢 Normal | 0.244 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-10 00:06:44 | Thanamalwila (Kirindi Oya) | 3.22 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-10 00:10:29 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-10 01:02:09 | Ellagawa (Kalu Ganga) | 8.53 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-10 01:02:25 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-10 01:02:37 | Glencourse (Kelani Ganga) | 14.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 00:03:53 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-09 23:02:49 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 01:01:40 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-10 00:09:39 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-09 23:58:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.006 |  |
| 2026-11-10 00:08:09 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-10 00:02:11 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.011 |  |
| 2026-11-09 23:18:25 | Putupaula (Kalu Ganga) | 2.25 | 🟢 Normal | -0.018 |  |
| 2026-11-10 01:02:35 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.030 |  |
| 2026-11-10 01:01:23 | Kuda Oya (Kirindi Oya) | 2.89 | 🟢 Normal | -0.043 |  |
| 2026-11-10 00:02:17 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.050 |  |
| 2026-11-10 00:01:52 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.073 |  |
| 2026-11-10 01:01:40 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | -0.086 |  |
| 2026-11-10 00:05:43 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | -0.091 |  |
| 2026-11-10 00:01:47 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.092 |  |
| 2026-11-10 01:02:27 | Thaldena (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.116 |  |
| 2026-11-10 01:02:23 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)