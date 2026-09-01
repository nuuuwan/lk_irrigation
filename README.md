# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_15:14:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,029 measurements** from **39** stations.
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
| 2026-09-01 15:14:55 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:09:47 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-01 15:08:54 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:07:59 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:07:03 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:07:00 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:06:38 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-09-01 15:05:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 15:05:28 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:05:00 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:43 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:21 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:17 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:02 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-09-01 15:04:00 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:44 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:38 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.116 |  |
| 2026-09-01 15:03:33 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:31 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-01 15:03:14 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-01 15:02:55 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:49 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:45 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.010 |  |
| 2026-09-01 15:02:43 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:40 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.042 |  |
| 2026-09-01 15:02:33 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:30 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:24 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:21 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.071 |  |
| 2026-09-01 15:01:51 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 15:01:39 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:00:59 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:00:11 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 15:03:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-01 15:03:31 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-01 15:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 15:05:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 15:09:47 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-01 15:05:28 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:44 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:55 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:05:00 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:14 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:00:59 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:33 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:30 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:03:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:49 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-01 11:02:11 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:33 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:07:00 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:17 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:00:11 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:01:39 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:24 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:04:43 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:14:55 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:07:59 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:21 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:01:51 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:08:54 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:02:43 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:07:03 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 15:06:38 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-09-01 15:04:02 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-09-01 15:02:45 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:05:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.034 |  |
| 2026-09-01 15:02:40 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.042 |  |
| 2026-09-01 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.071 |  |
| 2026-09-01 15:03:38 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)