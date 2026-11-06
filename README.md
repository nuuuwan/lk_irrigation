# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_04:03:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 04:03:06 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.029 |  |
| 2026-11-07 04:02:58 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.040 |  |
| 2026-11-07 04:02:57 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 04:02:51 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.050 |  |
| 2026-11-07 04:02:51 | Ellagawa (Kalu Ganga) | 0.62 | 🟢 Normal | -5.921 |  |
| 2026-11-07 04:02:15 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-07 04:01:48 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | -0.081 |  |
| 2026-11-07 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.157 |  |
| 2026-11-07 04:01:16 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-07 04:00:47 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.079 |  |
| 2026-11-07 04:00:44 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-07 04:00:41 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | -0.151 |  |
| 2026-11-07 04:00:25 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.021 |  |
| 2026-11-07 04:00:11 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.013 |  |
| 2026-11-07 03:29:47 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-07 03:18:45 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -18.000 |  |
| 2026-11-07 03:18:43 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -18.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 03:08:37 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-11-07 03:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.000 |  |
| 2026-11-07 03:08:01 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-07 03:05:54 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-11-07 04:00:44 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-07 04:02:15 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-07 03:11:43 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-07 03:02:16 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-07 04:01:16 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 02:12:05 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-07 04:02:57 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 03:29:47 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-07 03:05:10 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:20 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:37 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 02:08:56 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:01:54 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-07 04:00:11 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.013 |  |
| 2026-11-07 03:02:48 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-11-07 04:00:25 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.021 |  |
| 2026-11-07 04:03:06 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | -0.029 |  |
| 2026-11-07 03:04:23 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.033 |  |
| 2026-11-07 04:02:58 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.040 |  |
| 2026-11-07 04:02:51 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.050 |  |
| 2026-11-07 03:06:16 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2026-11-07 01:04:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-07 04:00:47 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.079 |  |
| 2026-11-07 04:01:48 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | -0.081 |  |
| 2026-11-07 04:00:41 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | -0.151 |  |
| 2026-11-07 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.157 |  |
| 2026-11-07 03:14:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.160 |  |
| 2026-11-07 03:16:04 | Holombuwa (Kelani Ganga) | 2.45 | 🟢 Normal | -0.323 |  |
| 2026-11-07 04:02:51 | Ellagawa (Kalu Ganga) | 0.62 | 🟢 Normal | -5.921 |  |
| 2026-11-07 03:18:45 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)