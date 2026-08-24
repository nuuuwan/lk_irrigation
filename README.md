# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_12:14:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,171 measurements** from **39** stations.
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
| 2026-08-24 12:14:04 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:09:49 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:09:34 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 12:09:25 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-24 12:06:35 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-24 12:05:59 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-08-24 12:05:48 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:05:30 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:05:22 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:04:27 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:04:14 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 12:03:36 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:35 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:32 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:30 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 12:03:28 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-08-24 12:03:17 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 12:03:12 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.020 |  |
| 2026-08-24 12:03:05 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:04 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:53 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:40 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:35 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 12:02:24 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-08-24 12:02:10 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.090 |  |
| 2026-08-24 12:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-08-24 12:02:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-24 12:01:54 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:01:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:01:33 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | -0.012 |  |
| 2026-08-24 12:01:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 12:01:23 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:01:17 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:00:35 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:00:24 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.040 |  |
| 2026-08-24 12:00:14 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-24 11:34:09 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.034 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 12:02:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-24 12:09:25 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-24 12:06:35 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-24 12:02:35 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 12:01:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 12:04:14 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 12:03:30 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 12:09:34 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 12:05:48 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:53 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:01:17 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:14:04 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:53 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 11:03:01 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:05:22 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:04 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:35 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:01:54 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:09:49 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:32 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:05 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:01:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:04:27 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:00:35 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:40 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:05:30 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:02:24 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:36 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:00:14 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:01:23 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 12:03:28 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-08-24 12:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-08-24 12:03:17 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 12:01:33 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | -0.012 |  |
| 2026-08-24 12:03:12 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.020 |  |
| 2026-08-24 12:05:59 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-08-24 12:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-08-24 12:00:24 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.040 |  |
| 2026-08-24 12:02:10 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)