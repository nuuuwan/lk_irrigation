# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_07:12:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,243 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 07:12:03 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-26 07:11:17 | Rathnapura (Kalu Ganga) | 5.63 | 🟡 Alert | -0.044 |  |
| 2026-10-26 07:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-10-26 07:09:38 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-10-26 07:09:22 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 07:08:34 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.131 |  |
| 2026-10-26 07:08:18 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 07:08:12 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 07:07:31 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-26 07:07:07 | Glencourse (Kelani Ganga) | 12.16 | 🟢 Normal | -0.217 |  |
| 2026-10-26 07:06:39 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-10-26 07:06:02 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | -0.057 |  |
| 2026-10-26 07:05:50 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 07:05:40 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-26 07:05:32 | Giriulla (Maha Oya) | 3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-26 07:05:27 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 07:05:05 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-26 07:04:51 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 07:04:38 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-26 07:04:31 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.031 |  |
| 2026-10-26 07:04:31 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 07:04:21 | Galgamuwa (Mee Oya) | 2.33 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-26 07:04:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.128 |  |
| 2026-10-26 07:04:00 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:03:57 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.117 |  |
| 2026-10-26 07:03:33 | Moragaswewa (Deduru Oya) | 3.76 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-10-26 07:03:20 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:03:14 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.031 |  |
| 2026-10-26 07:03:01 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:02:18 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:02:17 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-10-26 07:02:08 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:02:01 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:01:24 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-10-26 07:01:14 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.140 |  |
| 2026-10-26 07:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-10-26 07:00:27 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-26 07:00:23 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 06:38:46 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | 0.164 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 07:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-10-26 07:05:05 | Magura (Kalu Ganga) | 4.28 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-26 07:11:17 | Rathnapura (Kalu Ganga) | 5.63 | 🟡 Alert | -0.044 |  |
| 2026-10-26 07:03:33 | Moragaswewa (Deduru Oya) | 3.76 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-10-26 07:02:17 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-10-26 07:04:21 | Galgamuwa (Mee Oya) | 2.33 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-26 07:06:39 | Putupaula (Kalu Ganga) | 2.16 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-10-26 07:05:40 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-26 07:08:18 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 07:05:50 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 07:05:27 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 07:00:27 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-26 07:07:31 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-26 07:04:38 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-26 07:08:12 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-26 07:09:22 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 07:12:03 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-26 07:04:31 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 07:04:51 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 07:00:23 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:02:18 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:03:01 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:03:20 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:04:00 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:02:01 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-26 07:02:08 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 06:06:10 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-26 07:09:38 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-10-26 07:05:32 | Giriulla (Maha Oya) | 3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-26 07:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-10-26 07:03:14 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.031 |  |
| 2026-10-26 07:01:24 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-10-26 07:04:31 | Holombuwa (Kelani Ganga) | 1.33 | 🟢 Normal | -0.031 |  |
| 2026-10-26 07:06:02 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | -0.057 |  |
| 2026-10-26 07:03:57 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.117 |  |
| 2026-10-26 07:04:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.128 |  |
| 2026-10-26 07:08:34 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.131 |  |
| 2026-10-26 07:01:14 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.140 |  |
| 2026-10-26 07:07:07 | Glencourse (Kelani Ganga) | 12.16 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)