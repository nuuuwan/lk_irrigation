# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_19:08:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,502 measurements** from **39** stations.
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
| 2026-09-18 19:08:33 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-18 19:08:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-09-18 19:07:03 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:06:05 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.059 |  |
| 2026-09-18 19:06:04 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | -0.009 |  |
| 2026-09-18 19:05:57 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.055 |  |
| 2026-09-18 19:05:44 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:38 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | -0.019 |  |
| 2026-09-18 19:05:35 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-18 19:05:18 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:16 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:06 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-18 19:04:50 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:04:23 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-18 19:04:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.058 |  |
| 2026-09-18 19:03:38 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:03:37 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 19:03:35 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:03:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:03:14 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-18 19:03:00 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 19:02:53 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:02:48 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:02:48 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:02:45 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 19:02:29 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-09-18 19:02:14 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:02:12 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:02:00 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-18 19:01:56 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:01:40 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:01:29 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:01:24 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.466 | 🔺 Rising |
| 2026-09-18 19:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-09-18 19:00:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:00:07 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 19:01:24 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.466 | 🔺 Rising |
| 2026-09-18 19:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-09-18 19:08:33 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-18 19:03:14 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-18 19:05:35 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-18 19:04:23 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-18 19:02:00 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-18 19:03:00 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-18 19:05:06 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-18 19:03:37 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 19:02:45 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 19:00:07 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:01:40 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:03:18 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:18 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:01:56 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:03:38 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:44 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:01:29 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:07:03 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:00:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:02:48 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:02:53 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:16 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:06:04 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:04:50 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 19:05:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | -0.009 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:03:35 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:02:48 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:02:12 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-18 19:05:38 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | -0.019 |  |
| 2026-09-18 19:08:28 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.031 |  |
| 2026-09-18 19:02:29 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.040 |  |
| 2026-09-18 19:05:57 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.055 |  |
| 2026-09-18 19:04:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.058 |  |
| 2026-09-18 19:06:05 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)