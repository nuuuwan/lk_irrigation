# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_08:11:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,585 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 08:11:26 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.018 |  |
| 2026-09-23 08:11:12 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -0.018 |  |
| 2026-09-23 08:10:37 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:09:29 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-09-23 08:09:15 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | -0.038 |  |
| 2026-09-23 08:07:59 | Magura (Kalu Ganga) | 4.07 | 🟡 Alert | -0.018 |  |
| 2026-09-23 08:07:00 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.021 |  |
| 2026-09-23 08:06:32 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | -0.029 |  |
| 2026-09-23 08:06:21 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:06:17 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:06:15 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-09-23 08:06:03 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.031 |  |
| 2026-09-23 08:05:55 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:05:09 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 08:05:04 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-09-23 08:04:54 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-09-23 08:04:47 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-23 08:04:28 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:04:17 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.029 |  |
| 2026-09-23 08:04:09 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.381 |  |
| 2026-09-23 08:03:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:03:27 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-23 08:03:09 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:02:37 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 08:02:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-23 08:02:23 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:02:15 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:02:15 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-23 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 08:02:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:58 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:51 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:50 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:02 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:00:41 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-23 08:00:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 08:00:21 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.020 |  |
| 2026-09-23 07:28:35 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 08:06:15 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-09-23 08:07:59 | Magura (Kalu Ganga) | 4.07 | 🟡 Alert | -0.018 |  |
| 2026-09-23 08:06:32 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | -0.029 |  |
| 2026-09-23 08:04:54 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-09-23 08:00:41 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-23 08:02:37 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 08:05:09 | Hanwella (Kelani Ganga) | 4.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 08:00:34 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 08:02:15 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 07:02:57 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:05:55 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:51 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:02:06 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:04:28 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:06:21 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:03:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:06:17 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:58 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:03:09 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:02 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:01:50 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:10:37 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:02:15 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-23 08:03:27 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-09-23 08:02:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-23 08:11:26 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | -0.018 |  |
| 2026-09-23 08:11:12 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -0.018 |  |
| 2026-09-23 08:00:21 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.020 |  |
| 2026-09-23 08:05:04 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-09-23 08:07:00 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.021 |  |
| 2026-09-23 08:04:47 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-09-23 08:04:17 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.029 |  |
| 2026-09-23 08:06:03 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.031 |  |
| 2026-09-23 08:09:15 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | -0.038 |  |
| 2026-09-23 07:09:07 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.038 |  |
| 2026-09-23 08:09:29 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-09-23 08:04:09 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.381 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)