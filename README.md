# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_19:25:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,214 measurements** from **39** stations.
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
| 2026-08-26 19:25:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | -0.058 |  |
| 2026-08-26 19:18:12 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-08-26 19:15:12 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:13:13 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-08-26 19:12:46 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-08-26 19:12:36 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.098 |  |
| 2026-08-26 19:10:10 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 19:10:00 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.110 |  |
| 2026-08-26 19:08:24 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.084 |  |
| 2026-08-26 19:08:11 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-08-26 19:07:13 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:06:09 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:06:01 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:06:00 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:05:59 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-26 19:05:58 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.071 |  |
| 2026-08-26 19:05:14 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:05:13 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-26 19:05:05 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-08-26 19:05:04 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 19:04:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:03:25 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-26 19:03:09 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.020 |  |
| 2026-08-26 19:02:51 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.050 |  |
| 2026-08-26 19:02:45 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:02:38 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:02:37 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 19:02:01 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:57 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:40 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:22 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:00:49 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-26 19:00:41 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:00:34 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 19:05:59 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-26 19:05:13 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-26 19:03:25 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-26 19:00:49 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-26 19:05:04 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 19:10:10 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-26 19:02:37 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 19:00:34 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:00:41 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:02:01 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:22 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:03:09 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:02:45 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:15:12 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:07:13 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:04:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:02:38 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:05:14 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:06:09 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:06:00 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:40 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:01:57 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:06:01 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 19:18:12 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-08-26 19:08:11 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.010 |  |
| 2026-08-26 18:01:52 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-26 19:05:05 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-08-26 18:01:25 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-08-26 19:03:09 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.020 |  |
| 2026-08-26 19:13:13 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-08-26 19:12:46 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.044 |  |
| 2026-08-26 19:02:51 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.050 |  |
| 2026-08-26 19:25:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.32 | 🟢 Normal | -0.058 |  |
| 2026-08-26 19:05:58 | Glencourse (Kelani Ganga) | 9.69 | 🟢 Normal | -0.071 |  |
| 2026-08-26 19:08:24 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.084 |  |
| 2026-08-26 19:12:36 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.098 |  |
| 2026-08-26 19:10:00 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)