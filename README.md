# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_17:28:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **257,250 measurements** from **39** stations.
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
| 2026-09-10 17:28:42 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:24:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:24:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-09-10 17:17:45 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:13:32 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:09:43 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-10 17:08:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:07:24 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-09-10 17:07:15 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:07:08 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.047 |  |
| 2026-09-10 17:06:28 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:06:13 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.020 |  |
| 2026-09-10 17:06:04 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-09-10 17:05:32 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:05:10 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:05:10 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:05:07 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:04:58 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-10 17:04:46 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.081 |  |
| 2026-09-10 17:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.053 |  |
| 2026-09-10 17:04:35 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:04:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:04:18 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:04:12 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:03:21 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:03:00 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 17:03:00 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:02:56 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:02:33 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:02:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.091 |  |
| 2026-09-10 17:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 17:02:10 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:01:53 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-10 17:01:38 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-10 17:01:27 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 17:01:22 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:01:08 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:01:06 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-09-10 17:00:22 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 17:04:58 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-10 17:01:53 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-10 17:09:43 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-10 17:01:27 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 17:03:00 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 17:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 17:04:35 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:02:56 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:01:08 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:08:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:03:21 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:04:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:04:18 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:17:45 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:05:07 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:05:32 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:01:22 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:05:10 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:24:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:02:33 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:28:42 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:07:15 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:13:32 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:06:28 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 17:06:04 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-09-10 17:04:12 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:03:00 | Ellagawa (Kalu Ganga) | 4.41 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:02:10 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:05:10 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-10 17:01:06 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-09-10 17:06:13 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | -0.020 |  |
| 2026-09-10 17:01:38 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-10 17:07:08 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.047 |  |
| 2026-09-10 17:07:24 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-09-10 17:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.053 |  |
| 2026-09-10 17:00:22 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.056 |  |
| 2026-09-10 17:24:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-09-10 17:04:46 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.081 |  |
| 2026-09-10 17:02:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)