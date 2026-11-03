# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_17:18:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,891 measurements** from **39** stations.
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
| 2026-11-03 17:18:08 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.027 |  |
| 2026-11-03 17:11:28 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-03 17:10:38 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-11-03 17:10:09 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-11-03 17:09:09 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:06:57 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:06:57 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.089 |  |
| 2026-11-03 17:06:57 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | -0.108 |  |
| 2026-11-03 17:06:52 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-11-03 17:06:34 | Wellawaya (Kirindi Oya) | 2.89 | 🟢 Normal | 0.892 | 🔺 Rising |
| 2026-11-03 17:06:13 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-03 17:05:59 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 17:05:38 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-03 17:05:36 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-11-03 17:05:30 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.049 |  |
| 2026-11-03 17:05:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:04:29 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.091 |  |
| 2026-11-03 17:04:00 | Moragaswewa (Deduru Oya) | 4.25 | 🟢 Normal | -0.019 |  |
| 2026-11-03 17:03:59 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-03 17:03:45 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.028 |  |
| 2026-11-03 17:03:32 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-03 17:03:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-11-03 17:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-11-03 17:02:50 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-03 17:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.062 |  |
| 2026-11-03 17:02:27 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 17:02:27 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:02:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-03 17:02:21 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.062 |  |
| 2026-11-03 17:02:14 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:02:11 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:01:50 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:01:44 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 17:01:41 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-11-03 17:01:37 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-03 17:01:37 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:01:32 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.081 |  |
| 2026-11-03 17:01:00 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:00:55 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-03 17:00:10 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 17:06:34 | Wellawaya (Kirindi Oya) | 2.89 | 🟢 Normal | 0.892 | 🔺 Rising |
| 2026-11-03 17:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-11-03 17:03:59 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-03 17:01:37 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-03 17:02:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-03 17:02:50 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-03 17:11:28 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-11-03 17:03:32 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-03 17:06:13 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-03 17:01:44 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-03 17:00:10 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 17:05:59 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 17:02:27 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 17:00:55 | Horowpothana (Yan Oya) | 2.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-03 17:01:37 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:02:11 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:05:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:02:27 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:01:00 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:01:50 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:06:57 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:09:09 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:05:38 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-03 17:06:52 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-11-03 17:04:00 | Moragaswewa (Deduru Oya) | 4.25 | 🟢 Normal | -0.019 |  |
| 2026-11-03 17:10:38 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-11-03 17:10:09 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-11-03 17:18:08 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.027 |  |
| 2026-11-03 17:03:45 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.028 |  |
| 2026-11-03 17:05:36 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-11-03 17:01:41 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-11-03 17:03:27 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-11-03 17:05:30 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.049 |  |
| 2026-11-03 17:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.64 | 🟢 Normal | -0.062 |  |
| 2026-11-03 17:02:21 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.062 |  |
| 2026-11-03 17:01:32 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.081 |  |
| 2026-11-03 17:06:57 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.089 |  |
| 2026-11-03 17:04:29 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.091 |  |
| 2026-11-03 17:06:57 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)