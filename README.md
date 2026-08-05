# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_07:01:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,332 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 07:01:23 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 07:01:16 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:00:57 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.052 |  |
| 2026-08-05 07:00:54 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:00:53 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:00:10 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-08-05 07:00:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:45:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:30:15 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-08-05 06:16:04 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:14:29 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 06:08:31 | Peradeniya (Mahaweli Ganga) | 4.62 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-05 06:06:36 | Kithulgala (Kelani Ganga) | 2.85 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-08-05 06:04:24 | Deraniyagala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-05 07:01:23 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 06:07:25 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-05 07:00:53 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:00:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:02:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:04:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:00:54 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:45:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:05:56 | Ellagawa (Kalu Ganga) | 8.94 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:03:33 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:14:29 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:05:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:03:37 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:10:19 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:16:04 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:03:37 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 07:01:16 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 06:05:12 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.009 |  |
| 2026-08-05 06:02:10 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-08-05 07:00:10 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-08-05 06:02:45 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-08-05 06:03:45 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-08-05 06:06:18 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.028 |  |
| 2026-08-05 06:30:15 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-08-05 06:05:47 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.031 |  |
| 2026-08-05 06:02:54 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.035 |  |
| 2026-08-05 06:02:06 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.042 |  |
| 2026-08-05 06:01:56 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.043 |  |
| 2026-08-05 06:04:57 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.048 |  |
| 2026-08-05 07:00:57 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.052 |  |
| 2026-08-05 06:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.62 | 🟢 Normal | -0.082 |  |
| 2026-08-05 06:03:10 | Rathnapura (Kalu Ganga) | 5.08 | 🟢 Normal | -0.086 |  |
| 2026-08-05 06:02:08 | Hanwella (Kelani Ganga) | 4.91 | 🟢 Normal | -0.110 |  |
| 2026-08-05 06:05:12 | Glencourse (Kelani Ganga) | 12.73 | 🟢 Normal | -0.123 |  |
| 2026-08-05 06:03:49 | Nawalapitiya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.387 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)