# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_13:34:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,192 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 13:34:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:21:49 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-09 13:21:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:18:45 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:09:39 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-09-09 13:09:05 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:08:27 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:08:07 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.045 |  |
| 2026-09-09 13:06:30 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:05:50 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-09 13:05:26 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:05:09 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:05:07 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:04:46 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:04:41 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-09-09 13:04:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-09 13:04:11 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:04:07 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-09-09 13:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-09 13:02:59 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:57 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-09 13:02:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:46 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-09 13:02:39 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:27 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:23 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.111 |  |
| 2026-09-09 13:02:08 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:03 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:02 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-09-09 13:01:50 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:01:49 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:01:05 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.030 |  |
| 2026-09-09 13:01:03 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-09 13:00:49 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:00:41 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:00:23 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.106 |  |
| 2026-09-09 13:00:08 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-09 13:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 13:01:03 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-09-09 13:21:49 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-09 13:04:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-09 13:05:50 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-09 13:02:46 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-09 13:00:08 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-09 13:09:05 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:04:11 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:01:50 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:03 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:00:49 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:39 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:04:46 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:05:09 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:59 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:06:30 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:05:26 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:01:49 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:34:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:18:45 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:27 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:05:07 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:08:27 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:21:09 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:00:41 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:02:08 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:03:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-09 13:02:57 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-09 13:02:02 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-09-09 13:09:39 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-09-09 13:04:07 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.029 |  |
| 2026-09-09 13:01:05 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.030 |  |
| 2026-09-09 13:04:41 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.039 |  |
| 2026-09-09 13:08:07 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.045 |  |
| 2026-09-09 13:00:23 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.106 |  |
| 2026-09-09 13:02:23 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)