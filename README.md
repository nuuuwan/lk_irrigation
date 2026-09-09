# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_16:06:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,304 measurements** from **39** stations.
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
| 2026-09-09 16:06:10 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-09 16:05:49 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:48 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:40 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:25 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:20 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:05:11 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:04:54 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-09-09 16:04:28 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-09-09 16:04:18 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:03:54 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:03:47 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:03:28 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 16:03:27 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:10 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 16:03:09 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:02:58 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 16:02:42 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:02:40 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.052 |  |
| 2026-09-09 16:02:37 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 16:02:22 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.097 |  |
| 2026-09-09 16:02:15 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-09 16:02:12 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-09 16:01:54 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:01:22 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:01:08 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-09-09 16:00:58 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:00:37 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-09 16:00:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 16:02:12 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-09 15:04:18 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-09 16:02:15 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-09 16:03:28 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 16:02:37 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 16:06:10 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-09 16:02:58 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 16:03:10 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 16:03:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:04:49 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:57:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:01:54 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:11 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:00:58 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:02:42 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:09 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:25 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:00:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:48 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:04:18 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:40 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:05:49 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:27 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:01:22 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-09 16:03:54 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:05:20 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:03:47 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-09-09 16:01:08 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-09-09 16:04:54 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-09-09 15:03:02 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.020 |  |
| 2026-09-09 16:00:37 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-09 15:03:21 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-09-09 15:07:06 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.047 |  |
| 2026-09-09 16:02:40 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.052 |  |
| 2026-09-09 15:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.059 |  |
| 2026-09-09 15:03:26 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.074 |  |
| 2026-09-09 16:04:28 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-09-09 16:02:22 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)