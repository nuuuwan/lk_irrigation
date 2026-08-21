# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_10:09:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 10:09:05 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.019 |  |
| 2026-08-21 10:08:41 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:08:16 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 10:06:04 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:05:24 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:05:14 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:04:49 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:04:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:04:40 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-21 10:04:06 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.021 |  |
| 2026-08-21 10:04:01 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:03:37 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:03:32 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 10:03:25 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-08-21 10:03:09 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.030 |  |
| 2026-08-21 10:03:05 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.029 |  |
| 2026-08-21 10:02:49 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-21 10:02:44 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:43 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-08-21 10:02:42 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:42 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:19 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-08-21 10:02:18 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 10:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.010 |  |
| 2026-08-21 10:01:46 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.049 |  |
| 2026-08-21 10:01:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:01:27 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:01:22 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-21 10:01:21 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.054 |  |
| 2026-08-21 10:01:20 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-08-21 10:01:02 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 10:00:42 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:00:24 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:00:18 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:00:15 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 10:02:49 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-21 10:01:02 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 10:01:22 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-21 10:08:16 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 10:02:18 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 10:03:32 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 10:01:27 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:00:42 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:42 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:06:04 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:42 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:00:18 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:01:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:00:15 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:04:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:03:37 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:00:24 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:04:01 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:04:49 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:05:24 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:44 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:08:41 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:19:49 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 09:07:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:05:14 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:01:20 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 10:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.010 |  |
| 2026-08-21 10:02:43 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-08-21 10:04:40 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-21 10:03:25 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-08-21 10:09:05 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.019 |  |
| 2026-08-21 10:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-08-21 10:02:19 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-08-21 10:04:06 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.021 |  |
| 2026-08-21 10:03:05 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.029 |  |
| 2026-08-21 10:03:09 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.030 |  |
| 2026-08-21 10:01:46 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.049 |  |
| 2026-08-21 10:01:21 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)