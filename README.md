# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_06:27:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 06:27:22 | Panadugama (Nilwala Ganga) | 4.91 | 🟢 Normal | 22.737 | 🔺 Rising |
| 2026-08-09 06:27:03 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | 22.737 | 🔺 Rising |
| 2026-08-09 06:11:58 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-09 06:09:41 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:08:23 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-09 06:07:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:07:25 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.010 |  |
| 2026-08-09 06:06:04 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-08-09 06:06:01 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-08-09 06:05:54 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.010 |  |
| 2026-08-09 06:05:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:05:20 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:05:09 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.021 |  |
| 2026-08-09 06:05:01 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:04:56 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:04:21 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:03:56 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:03:47 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 06:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.023 |  |
| 2026-08-09 06:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-09 06:03:16 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.072 |  |
| 2026-08-09 06:02:53 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 06:02:53 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:02:51 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.405 | 🔺 Rising |
| 2026-08-09 06:02:36 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.054 |  |
| 2026-08-09 06:02:28 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:02:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:02:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 06:01:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:47 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-09 06:01:41 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:39 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-09 06:01:37 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-08-09 06:01:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:06 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:00:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:00:41 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:50:10 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 06:27:22 | Panadugama (Nilwala Ganga) | 4.91 | 🟢 Normal | 22.737 | 🔺 Rising |
| 2026-08-09 06:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.405 | 🔺 Rising |
| 2026-08-09 06:01:39 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-09 06:03:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-09 06:08:23 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-09 06:02:53 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 06:11:58 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-09 06:02:09 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 06:03:47 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 06:05:01 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:02:16 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:07:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:04:56 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:32 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:41 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:02:28 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:09:41 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:05:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:00:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:02:53 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:04:21 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:06 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:05:20 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:00:41 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:01:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:03:56 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-09 06:07:25 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.010 |  |
| 2026-08-09 06:05:54 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.010 |  |
| 2026-08-09 06:01:47 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-09 06:06:04 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-08-09 06:06:01 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-08-09 06:05:09 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.021 |  |
| 2026-08-09 06:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.023 |  |
| 2026-08-09 06:01:37 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-08-09 06:02:36 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.054 |  |
| 2026-08-09 06:03:16 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)