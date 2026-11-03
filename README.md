# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_22:33:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,071 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 22:33:15 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-03 22:16:31 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-03 22:12:59 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-03 22:10:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-03 22:10:22 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:10:21 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-03 22:10:12 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-11-03 22:09:50 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.369 | 🔺 Rising |
| 2026-11-03 22:08:56 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-11-03 22:08:07 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.037 |  |
| 2026-11-03 22:08:03 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.132 |  |
| 2026-11-03 22:08:02 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:07:38 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-03 22:07:14 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.086 |  |
| 2026-11-03 22:06:56 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-03 22:06:29 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-11-03 22:05:59 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-03 22:05:29 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 22:05:08 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-11-03 22:04:41 | Moraketiya (Walawe Ganga) | 3.12 | 🟡 Alert | 0.451 | 🔺 Rising |
| 2026-11-03 22:04:40 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.042 |  |
| 2026-11-03 22:03:37 | Urawa (Nilwala Ganga) | 3.20 | 🟡 Alert | 0.212 | 🔺 Rising |
| 2026-11-03 22:03:19 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:03:18 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-03 22:03:08 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.089 |  |
| 2026-11-03 22:03:08 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-11-03 22:03:07 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-11-03 22:02:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 22:01:47 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-03 22:01:40 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-03 22:01:34 | Thanamalwila (Kirindi Oya) | 2.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-03 22:00:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 22:04:41 | Moraketiya (Walawe Ganga) | 3.12 | 🟡 Alert | 0.451 | 🔺 Rising |
| 2026-11-03 22:03:37 | Urawa (Nilwala Ganga) | 3.20 | 🟡 Alert | 0.212 | 🔺 Rising |
| 2026-11-03 21:07:37 | Kuda Oya (Kirindi Oya) | 2.89 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2026-11-03 22:09:50 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.369 | 🔺 Rising |
| 2026-11-03 22:01:40 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.335 | 🔺 Rising |
| 2026-11-03 22:03:18 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-03 22:06:29 | Magura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-11-03 22:10:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-03 22:12:59 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 22:00:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-03 22:07:38 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-03 22:06:56 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-03 22:05:59 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-03 22:33:15 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-03 22:10:21 | Peradeniya (Mahaweli Ganga) | 3.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-03 22:01:34 | Thanamalwila (Kirindi Oya) | 2.56 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-03 22:02:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 22:05:29 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 22:16:31 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-03 22:03:07 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:03:19 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-03 21:01:20 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 21:02:55 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:10:22 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:08:02 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:10:12 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-11-03 22:03:08 | Moragaswewa (Deduru Oya) | 4.20 | 🟢 Normal | -0.010 |  |
| 2026-11-03 22:01:47 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-03 22:08:56 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.019 |  |
| 2026-11-03 22:05:08 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-11-03 22:08:07 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.037 |  |
| 2026-11-03 22:04:40 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.042 |  |
| 2026-11-03 22:07:14 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.086 |  |
| 2026-11-03 22:03:08 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.089 |  |
| 2026-11-03 22:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-11-03 22:08:03 | Holombuwa (Kelani Ganga) | 1.81 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)