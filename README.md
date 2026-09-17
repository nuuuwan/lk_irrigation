# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_00:09:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,777 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 00:09:27 | Baddegama (Gin Ganga) | 3.51 | 🟡 Alert | -0.010 |  |
| 2026-09-18 00:09:10 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:08:48 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 00:07:34 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-09-18 00:07:26 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-09-18 00:07:05 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.024 |  |
| 2026-09-18 00:06:54 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:06:53 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:06:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-18 00:06:28 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.050 |  |
| 2026-09-18 00:05:41 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:05:21 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:05:14 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:04:45 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 00:04:40 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:04:33 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-09-18 00:04:30 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:04:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:03:51 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.006 |  |
| 2026-09-18 00:03:46 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.023 |  |
| 2026-09-18 00:03:34 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 00:03:32 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:02:50 | Magura (Kalu Ganga) | 5.04 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-18 00:02:39 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 00:02:00 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-18 00:01:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:01:47 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.060 |  |
| 2026-09-18 00:01:43 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-18 00:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-18 00:01:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-18 00:00:52 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:00:18 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-09-17 23:38:12 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 00:02:50 | Magura (Kalu Ganga) | 5.04 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-18 00:09:27 | Baddegama (Gin Ganga) | 3.51 | 🟡 Alert | -0.010 |  |
| 2026-09-18 00:07:34 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-09-18 00:06:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-18 00:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-18 00:02:39 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 00:03:34 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 00:04:45 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 00:08:48 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:05:42 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:03:32 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:04:40 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:09:10 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:06:54 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:03:04 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:04:30 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:06:28 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:05:21 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:01:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:00:52 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:04:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:05:41 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:05:14 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:03:51 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.006 |  |
| 2026-09-18 00:07:26 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-09-18 00:01:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-18 00:02:00 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-09-18 00:01:43 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:05:48 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.012 |  |
| 2026-09-18 00:03:46 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.023 |  |
| 2026-09-18 00:07:05 | Panadugama (Nilwala Ganga) | 4.55 | 🟢 Normal | -0.024 |  |
| 2026-09-18 00:04:33 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-09-18 00:00:18 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-09-18 00:06:28 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.050 |  |
| 2026-09-18 00:01:47 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.060 |  |
| 2026-09-17 23:02:38 | Yaka Wewa (Ma Oya) | 0.04 | 🟢 Normal | -0.364 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)