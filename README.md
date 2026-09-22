# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_07:18:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,638 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 07:18:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:18:32 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:18:31 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:18:29 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:18:28 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:15:30 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.014 |  |
| 2026-09-22 07:14:04 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 07:13:17 | Panadugama (Nilwala Ganga) | 5.06 | 🟡 Alert | -0.035 |  |
| 2026-09-22 07:11:48 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.027 |  |
| 2026-09-22 07:11:21 | Rathnapura (Kalu Ganga) | 4.68 | 🟢 Normal | -0.057 |  |
| 2026-09-22 07:09:28 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:08:24 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:08:01 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 07:06:32 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.452 |  |
| 2026-09-22 07:06:07 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-22 07:05:45 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 07:05:38 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.028 |  |
| 2026-09-22 07:05:37 | Hanwella (Kelani Ganga) | 4.66 | 🟢 Normal | -0.086 |  |
| 2026-09-22 07:05:36 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | -0.028 |  |
| 2026-09-22 07:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-22 07:04:21 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:04:17 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:04:17 | Holombuwa (Kelani Ganga) | 2.43 | 🟢 Normal | -0.053 |  |
| 2026-09-22 07:03:59 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-09-22 07:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 07:03:14 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:03:13 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-09-22 07:03:01 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 07:02:42 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-09-22 07:02:41 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.002 |  |
| 2026-09-22 07:02:32 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:02:19 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:02:00 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.010 |  |
| 2026-09-22 07:01:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-22 07:01:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 07:01:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-09-22 07:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:00:57 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:00:56 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | -0.016 |  |
| 2026-09-22 07:00:49 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:00:21 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.052 |  |
| 2026-09-22 07:00:05 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 07:14:04 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 07:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 07:00:05 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | 0.000 |  |
| 2026-09-22 07:05:36 | Magura (Kalu Ganga) | 4.79 | 🟡 Alert | -0.028 |  |
| 2026-09-22 07:13:17 | Panadugama (Nilwala Ganga) | 5.06 | 🟡 Alert | -0.035 |  |
| 2026-09-22 07:04:41 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-22 07:01:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 07:06:07 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-22 07:03:01 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 07:05:45 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 07:08:01 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 07:02:32 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:00:49 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:09:28 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:04:21 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:18:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:08:24 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:04:17 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:02:28 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:00:57 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:03:14 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:02:19 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 07:02:41 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.002 |  |
| 2026-09-22 07:01:55 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-22 07:02:00 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.010 |  |
| 2026-09-22 07:15:30 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.014 |  |
| 2026-09-22 07:00:56 | Nagalagam Street (Kelani Ganga) | 0.72 | 🟢 Normal | -0.016 |  |
| 2026-09-22 07:01:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-09-22 07:03:59 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-09-22 07:11:48 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | -0.027 |  |
| 2026-09-22 07:05:38 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.028 |  |
| 2026-09-22 07:02:42 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-09-22 07:00:21 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.052 |  |
| 2026-09-22 07:04:17 | Holombuwa (Kelani Ganga) | 2.43 | 🟢 Normal | -0.053 |  |
| 2026-09-22 07:11:21 | Rathnapura (Kalu Ganga) | 4.68 | 🟢 Normal | -0.057 |  |
| 2026-09-22 07:03:13 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-09-22 07:05:37 | Hanwella (Kelani Ganga) | 4.66 | 🟢 Normal | -0.086 |  |
| 2026-09-22 07:06:32 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.452 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)