# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_22:26:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,225 measurements** from **39** stations.
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
| 2026-08-08 22:26:02 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-08 22:20:14 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-08 22:13:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-08 22:10:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-08-08 22:09:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:09:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:08:44 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-08 22:08:20 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:07:14 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.028 |  |
| 2026-08-08 22:06:54 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:06:37 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-08-08 22:06:20 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -144.000 |  |
| 2026-08-08 22:06:19 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -144.000 |  |
| 2026-08-08 22:05:54 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 22:05:18 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:05:11 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:04:30 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.130 |  |
| 2026-08-08 22:04:03 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-08-08 22:04:01 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.040 |  |
| 2026-08-08 22:03:45 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:03:22 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 22:02:55 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-08 22:02:52 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:25 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:16 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:11 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:09 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:02 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.053 |  |
| 2026-08-08 22:02:01 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:43 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:37 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:33 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:25 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-08 22:00:55 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:00:31 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:00:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 21:59:36 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 22:01:25 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-08 22:26:02 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-08 22:02:55 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-08 22:20:14 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-08 22:05:54 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-08 22:13:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-08 22:08:44 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-08 22:03:22 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:09:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:00:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:05:18 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:43 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:00:31 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:11 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:25 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:56 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:08:20 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:01 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 21:59:36 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:52 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:03:45 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:16 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:05:11 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:09:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:00:55 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:02:09 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:01:37 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-08 22:06:37 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-08-08 22:04:03 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-08-08 22:10:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-08-08 22:07:14 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.028 |  |
| 2026-08-08 22:04:01 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | -0.040 |  |
| 2026-08-08 22:02:02 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.053 |  |
| 2026-08-08 22:04:30 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.130 |  |
| 2026-08-08 22:06:20 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)