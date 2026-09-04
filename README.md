# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--04_23:31:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,017 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 23:31:18 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:18:39 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:15:57 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:15:18 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:11:54 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.019 |  |
| 2026-09-04 23:09:08 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-04 23:07:21 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-09-04 23:05:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.022 |  |
| 2026-09-04 23:04:39 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-04 23:04:23 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:04:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-09-04 23:03:52 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:40 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:38 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:22 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:16 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.030 |  |
| 2026-09-04 23:03:04 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:02:48 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:02:46 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-04 23:02:35 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:02:19 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:02:09 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:58 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:15 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:07 | Thanamalwila (Kirindi Oya) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-04 23:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:00:27 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.485 | 🔺 Rising |
| 2026-09-04 23:00:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:00:20 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-04 23:00:27 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.485 | 🔺 Rising |
| 2026-09-04 23:02:46 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-04 23:09:08 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-04 22:51:07 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-04 23:04:39 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-04 23:15:57 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:00:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:58 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:18:39 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:02:19 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:03:45 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:40 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:02:48 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:02:35 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:06:42 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:42 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:00:20 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:15:18 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:31:18 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:04 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:04:23 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:38 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:22 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:02:31 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:03:52 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-04 22:07:22 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:15 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-04 23:01:07 | Thanamalwila (Kirindi Oya) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-04 23:07:21 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-09-04 23:11:54 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | -0.019 |  |
| 2026-09-04 22:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.020 |  |
| 2026-09-04 22:03:01 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-09-04 23:05:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.022 |  |
| 2026-09-04 22:06:25 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-09-04 23:03:16 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.030 |  |
| 2026-09-04 23:04:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-09-04 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)