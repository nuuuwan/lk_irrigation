# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_03:32:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 03:32:54 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:26:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | -0.036 |  |
| 2026-11-01 03:13:24 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:10:56 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 03:10:02 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-01 03:09:02 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.034 |  |
| 2026-11-01 03:08:45 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:08:18 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-11-01 03:07:29 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:07:06 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -1.181 |  |
| 2026-11-01 03:05:31 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.087 |  |
| 2026-11-01 03:05:15 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-11-01 03:04:56 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:04:43 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-01 03:04:37 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-01 03:04:27 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-11-01 03:04:24 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 03:03:54 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-01 03:03:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:03:26 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:03:12 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 03:02:55 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-01 03:02:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-01 03:02:41 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-11-01 03:02:33 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:31 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.007 |  |
| 2026-11-01 03:02:24 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-01 03:02:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:20 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-01 03:01:53 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:01:40 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-01 03:01:34 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 03:02:41 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-11-01 03:02:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-01 03:02:20 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-01 03:01:40 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-01 03:03:54 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-01 03:03:12 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-01 03:04:37 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-01 03:04:24 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 03:10:56 | Pitabeddara (Nilwala Ganga) | 1.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 03:03:52 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:01:34 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:07:29 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:01:53 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:04:56 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:08:45 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:01:43 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:33 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:03:26 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:13:24 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:32:54 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-01 03:02:31 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.007 |  |
| 2026-11-01 03:10:02 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-11-01 03:08:18 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-11-01 03:04:43 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:27 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 03:02:55 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-11-01 03:04:27 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-01 03:05:15 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-11-01 03:02:24 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-01 03:09:02 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.034 |  |
| 2026-11-01 03:26:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.89 | 🟢 Normal | -0.036 |  |
| 2026-11-01 02:04:49 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.039 |  |
| 2026-11-01 03:05:31 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | -0.087 |  |
| 2026-11-01 03:07:06 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | -1.181 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)