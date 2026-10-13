# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_19:37:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 19:37:26 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 19:26:21 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:19:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.03 | 🟡 Alert | -0.008 |  |
| 2026-10-13 19:14:11 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-10-13 19:12:24 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.017 |  |
| 2026-10-13 19:11:46 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-13 19:09:30 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-13 19:08:41 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-13 19:07:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:06:56 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-10-13 19:05:33 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-10-13 19:05:20 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-13 19:05:19 | Thawalama (Gin Ganga) | 2.77 | 🟢 Normal | 1.231 | 🔺 Rising |
| 2026-10-13 19:05:17 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 19:04:47 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:04:45 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:04:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.205 |  |
| 2026-10-13 19:04:32 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-13 19:03:54 | Urawa (Nilwala Ganga) | 2.60 | 🟡 Alert | 0.697 | 🔺 Rising |
| 2026-10-13 19:03:50 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-13 19:03:41 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-13 19:03:40 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:03:17 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:02:58 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-13 19:02:57 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 19:02:36 | Panadugama (Nilwala Ganga) | 5.68 | 🟡 Alert | -0.031 |  |
| 2026-10-13 19:02:33 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:02:25 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:02:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:02:15 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-10-13 19:02:04 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:01:54 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:01:38 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.070 |  |
| 2026-10-13 19:01:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-13 19:01:02 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 18:59:55 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 19:03:54 | Urawa (Nilwala Ganga) | 2.60 | 🟡 Alert | 0.697 | 🔺 Rising |
| 2026-10-13 19:11:46 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-10-13 19:19:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.03 | 🟡 Alert | -0.008 |  |
| 2026-10-13 19:02:36 | Panadugama (Nilwala Ganga) | 5.68 | 🟡 Alert | -0.031 |  |
| 2026-10-13 19:05:19 | Thawalama (Gin Ganga) | 2.77 | 🟢 Normal | 1.231 | 🔺 Rising |
| 2026-10-13 19:14:11 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-10-13 19:09:30 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-13 19:08:41 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-13 19:03:50 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-13 19:05:20 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-13 19:03:41 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-13 19:01:02 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 19:04:32 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-13 19:05:17 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 19:37:26 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 19:02:57 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 19:02:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:01:54 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:02:33 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:04:47 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:26:21 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:07:00 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:03:40 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:02:04 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:02:25 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:03:17 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:01:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-13 19:04:45 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-13 19:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-13 19:02:58 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-13 19:12:24 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | -0.017 |  |
| 2026-10-13 19:05:33 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.019 |  |
| 2026-10-13 19:06:56 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | -0.020 |  |
| 2026-10-13 19:02:15 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-10-13 19:01:38 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | -0.070 |  |
| 2026-10-13 19:04:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)