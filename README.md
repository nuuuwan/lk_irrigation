# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_21:09:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,314 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 21:09:27 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-21 21:08:08 | Kithulgala (Kelani Ganga) | 2.47 | 🟢 Normal | -0.028 |  |
| 2026-10-21 21:07:53 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-21 21:07:16 | Peradeniya (Mahaweli Ganga) | 4.12 | 🟢 Normal | -0.074 |  |
| 2026-10-21 21:06:56 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | 1.168 | 🔺 Rising |
| 2026-10-21 21:06:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-21 21:06:11 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:05:35 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.010 |  |
| 2026-10-21 21:05:29 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:05:12 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.037 |  |
| 2026-10-21 21:05:01 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:04:53 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 21:04:51 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-21 21:04:20 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.138 |  |
| 2026-10-21 21:04:19 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:04:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:04:01 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.258 |  |
| 2026-10-21 21:03:46 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.115 |  |
| 2026-10-21 21:03:45 | Siyambalanduwa (Heda Oya) | 2.60 | 🟢 Normal | 1.894 | 🔺 Rising |
| 2026-10-21 21:03:34 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:03:25 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.066 |  |
| 2026-10-21 21:03:02 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.081 |  |
| 2026-10-21 21:02:50 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:02:49 | Deraniyagala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.658 |  |
| 2026-10-21 21:02:34 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-21 21:02:27 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.032 |  |
| 2026-10-21 21:01:54 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-21 21:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-21 21:01:32 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-10-21 21:01:18 | Yaka Wewa (Ma Oya) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 21:01:10 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-10-21 21:00:16 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:00:12 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 21:03:45 | Siyambalanduwa (Heda Oya) | 2.60 | 🟢 Normal | 1.894 | 🔺 Rising |
| 2026-10-21 21:06:56 | Rathnapura (Kalu Ganga) | 3.49 | 🟢 Normal | 1.168 | 🔺 Rising |
| 2026-10-21 21:01:10 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-10-21 21:02:34 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-21 21:06:34 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-21 21:04:51 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-21 21:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-21 21:09:27 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-21 21:01:54 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-21 21:07:53 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 21:04:53 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 21:01:18 | Yaka Wewa (Ma Oya) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:03:34 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:02:50 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:05:29 | Moragaswewa (Deduru Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 21:05:01 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 19:05:52 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 20:09:33 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 21:04:19 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:00:12 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:06:11 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:04:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:00:16 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 21:05:35 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.010 |  |
| 2026-10-21 21:01:32 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-10-21 21:08:08 | Kithulgala (Kelani Ganga) | 2.47 | 🟢 Normal | -0.028 |  |
| 2026-10-21 21:02:27 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.032 |  |
| 2026-10-21 21:05:12 | Pitabeddara (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.037 |  |
| 2026-10-21 21:03:25 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.066 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-21 21:07:16 | Peradeniya (Mahaweli Ganga) | 4.12 | 🟢 Normal | -0.074 |  |
| 2026-10-21 21:03:02 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.081 |  |
| 2026-10-21 21:03:46 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.115 |  |
| 2026-10-21 21:04:20 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.138 |  |
| 2026-10-21 21:04:01 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.258 |  |
| 2026-10-21 21:02:49 | Deraniyagala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.658 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)