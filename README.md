# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_07:15:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,938 measurements** from **39** stations.
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
| 2026-09-29 07:15:05 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 07:14:51 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.028 |  |
| 2026-09-29 07:12:13 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:10:18 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:08:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.009 |  |
| 2026-09-29 07:08:09 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.132 |  |
| 2026-09-29 07:08:04 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:07:36 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | -0.021 |  |
| 2026-09-29 07:06:21 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-09-29 07:06:21 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 07:06:20 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:06:01 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.085 |  |
| 2026-09-29 07:05:58 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:05:35 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.093 |  |
| 2026-09-29 07:04:25 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-29 07:04:04 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:04:04 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-09-29 07:04:02 | Thaldena (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.021 |  |
| 2026-09-29 07:03:54 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:03:30 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:03:20 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-29 07:03:18 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-29 07:03:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:03:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-29 07:03:09 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:02:20 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-29 07:01:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.155 |  |
| 2026-09-29 07:01:53 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:01:37 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:01:12 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-09-29 07:01:09 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.092 |  |
| 2026-09-29 07:00:36 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:00:08 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:00:06 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 07:01:12 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-09-29 07:04:25 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-09-29 07:03:20 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-29 07:00:06 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 07:15:05 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 07:06:21 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-29 07:03:54 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:00:36 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:00:08 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:04:04 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:12:13 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 18:00:25 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:10:18 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:03:18 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:06:20 | Hanwella (Kelani Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:01:53 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:01:37 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:05:58 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:03:30 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:03:09 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 06:05:29 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:01:09 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:08:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.009 |  |
| 2026-09-29 06:07:24 | Thalgahagoda (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-09-29 07:03:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-29 07:02:20 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-29 07:03:18 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-29 07:04:04 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-09-29 07:04:02 | Thaldena (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.021 |  |
| 2026-09-29 07:07:36 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | -0.021 |  |
| 2026-09-29 07:06:21 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.028 |  |
| 2026-09-29 07:14:51 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.028 |  |
| 2026-09-29 07:06:01 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.085 |  |
| 2026-09-29 07:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.092 |  |
| 2026-09-29 07:05:35 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.093 |  |
| 2026-09-29 07:08:09 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.132 |  |
| 2026-09-29 07:01:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.155 |  |
| 2026-09-29 05:33:05 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -8.690 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)