# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--17_23:38:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,745 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 23:38:12 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:17:22 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.018 |  |
| 2026-09-17 23:11:23 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.045 |  |
| 2026-09-17 23:10:58 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:07:50 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | -0.010 |  |
| 2026-09-17 23:07:02 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-09-17 23:06:28 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:06:23 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-17 23:05:48 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 23:05:48 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.012 |  |
| 2026-09-17 23:05:42 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:05:40 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:04:40 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:04:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:04:02 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-09-17 23:03:49 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 23:03:47 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:03:04 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:02:52 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:02:51 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-09-17 23:02:38 | Yaka Wewa (Ma Oya) | 0.04 | 🟢 Normal | -0.364 |  |
| 2026-09-17 23:02:24 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 23:02:22 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:02:14 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-17 23:01:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:01:26 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 23:01:25 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:01:14 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:01:12 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:00:34 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.036 |  |
| 2026-09-17 23:00:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-17 22:07:02 | Magura (Kalu Ganga) | 5.02 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-17 23:07:50 | Baddegama (Gin Ganga) | 3.52 | 🟡 Alert | -0.010 |  |
| 2026-09-17 22:07:38 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-09-17 22:02:02 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-17 23:05:48 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 23:01:26 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 23:02:24 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 23:03:49 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:05:42 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:01:25 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:05:40 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:01:12 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:03:04 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:02:52 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:06:28 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-09-17 22:28:05 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:04:40 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:01:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:10:58 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:38:12 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:00:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:08:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-09-17 23:04:33 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:01:14 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:02:22 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:03:47 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-17 23:07:02 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-09-17 23:05:48 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.012 |  |
| 2026-09-17 23:17:22 | Panadugama (Nilwala Ganga) | 4.57 | 🟢 Normal | -0.018 |  |
| 2026-09-17 23:04:02 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-09-17 23:06:23 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-17 23:02:51 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-09-17 23:02:14 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-09-17 23:00:34 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.036 |  |
| 2026-09-17 23:11:23 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.045 |  |
| 2026-09-17 23:02:38 | Yaka Wewa (Ma Oya) | 0.04 | 🟢 Normal | -0.364 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)