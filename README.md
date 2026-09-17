# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_17:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 17:03:46 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:36 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-17 17:03:30 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-09-17 17:03:30 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:18 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | -0.011 |  |
| 2026-09-17 17:03:17 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-09-17 17:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 17:03:11 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.026 |  |
| 2026-09-17 17:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:23 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:17 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:08 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-09-17 17:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:49 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:43 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-17 17:01:32 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-09-17 17:01:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:01 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:57 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:36 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:59:01 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:33:16 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 17:03:17 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-09-17 17:03:18 | Baddegama (Gin Ganga) | 3.59 | 🟡 Alert | -0.011 |  |
| 2026-09-17 16:07:46 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-17 17:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-17 16:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-17 16:03:18 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-17 16:02:36 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-17 17:03:36 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-17 16:02:38 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-17 16:03:55 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 16:00:15 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:06:58 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:23 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:01 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:57 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:46 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:03:30 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:00:36 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:49 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:09:19 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:01:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 16:09:43 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.009 |  |
| 2026-09-17 17:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-09-17 16:01:19 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:02:17 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-09-17 17:03:30 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-09-17 17:01:32 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-09-17 16:05:52 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-09-17 17:01:43 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-17 16:00:50 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-09-17 17:03:11 | Panadugama (Nilwala Ganga) | 4.69 | 🟢 Normal | -0.026 |  |
| 2026-09-17 17:02:08 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-09-17 16:05:07 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)