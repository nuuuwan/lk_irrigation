# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_16:17:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,990 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 16:17:37 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-08 16:15:41 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:11:50 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-08 16:09:51 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:08:57 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:08:06 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-08 16:07:59 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-08 16:07:38 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:07:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:06:41 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:05:48 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-08-08 16:04:38 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.020 |  |
| 2026-08-08 16:04:33 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-08 16:03:56 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:03:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:03:40 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:03:30 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-08 16:03:23 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 16:03:19 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:03:03 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:03:02 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:03:01 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 16:02:57 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:02:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-08-08 16:02:45 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:02:31 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 16:02:24 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:02:22 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:02:17 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-08 16:02:05 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 16:01:50 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:01:34 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.041 |  |
| 2026-08-08 16:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:00:30 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:59:51 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 16:05:48 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-08-08 16:17:37 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-08 16:07:59 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-08 16:03:30 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-08 16:04:33 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-08 16:02:05 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 16:08:06 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-08 16:03:23 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 16:02:17 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-08 16:02:31 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 16:11:50 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-08 16:03:01 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 16:00:17 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:02:24 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:03:56 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:08:57 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:02:45 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:02:22 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:09:51 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:07:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:06:41 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:00:30 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:03:06 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-08 15:01:14 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:03:40 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:07:38 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:03:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:15:41 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 16:03:02 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:03:19 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:01:50 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:03:03 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-08-08 15:00:11 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:02:57 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-08-08 16:04:38 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.020 |  |
| 2026-08-08 16:02:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-08-08 16:01:34 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.041 |  |
| 2026-08-08 15:09:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)