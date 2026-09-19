# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_15:04:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,227 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 15:04:20 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.058 |  |
| 2026-09-19 15:04:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:03:59 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-19 15:03:45 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-09-19 15:03:43 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 15:03:40 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:03:17 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-19 15:03:16 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-19 15:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:03:01 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:03:00 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-19 15:02:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:02:50 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.031 |  |
| 2026-09-19 15:02:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 15:02:24 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:02:19 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-19 15:02:14 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-09-19 15:01:51 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:01:51 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:01:49 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:01:25 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.037 |  |
| 2026-09-19 15:01:21 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-09-19 15:01:07 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-09-19 15:00:58 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:00:39 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.024 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 15:03:17 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-09-19 15:03:00 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-19 14:06:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-19 15:03:59 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-19 14:07:38 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-19 14:14:34 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-19 15:00:39 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-19 15:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 15:03:43 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 15:01:51 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:00:58 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:03:01 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:02:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:03:40 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-19 14:06:29 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:02:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:04:16 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-19 14:06:53 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:02:24 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-19 14:04:48 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-19 14:02:04 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:01:51 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:01:49 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-19 14:00:54 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 15:02:19 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-19 15:03:45 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-09-19 15:01:07 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-09-19 15:02:14 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-09-19 14:03:26 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.012 |  |
| 2026-09-19 14:05:05 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.019 |  |
| 2026-09-19 15:01:21 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-09-19 14:11:05 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.023 |  |
| 2026-09-19 14:07:58 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.029 |  |
| 2026-09-19 15:02:50 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.031 |  |
| 2026-09-19 13:07:37 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.037 |  |
| 2026-09-19 15:01:25 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.037 |  |
| 2026-09-19 14:03:36 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-09-19 15:04:20 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)