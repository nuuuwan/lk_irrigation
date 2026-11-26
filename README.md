# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_07:19:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 07:19:02 | Magura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-26 07:14:28 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.018 |  |
| 2026-11-26 07:11:40 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 07:10:12 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:09:47 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.048 |  |
| 2026-11-26 07:09:07 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-11-26 07:08:17 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-26 07:08:15 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:07:08 | Badalgama (Maha Oya) | 4.35 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-26 07:06:56 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.088 |  |
| 2026-11-26 07:06:43 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.055 |  |
| 2026-11-26 07:06:41 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-26 07:05:54 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.096 |  |
| 2026-11-26 07:05:45 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.040 |  |
| 2026-11-26 07:05:15 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.032 |  |
| 2026-11-26 07:05:02 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.031 |  |
| 2026-11-26 07:04:49 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.038 |  |
| 2026-11-26 07:04:45 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.038 |  |
| 2026-11-26 07:04:05 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | -0.043 |  |
| 2026-11-26 07:03:41 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.160 |  |
| 2026-11-26 07:02:46 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.079 |  |
| 2026-11-26 07:02:46 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-11-26 07:02:43 | Giriulla (Maha Oya) | 3.55 | 🟢 Normal | -0.098 |  |
| 2026-11-26 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.03 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-26 07:02:31 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-26 07:02:10 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.031 |  |
| 2026-11-26 07:02:08 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:01:52 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:01:49 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.000 |  |
| 2026-11-26 07:01:31 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 07:01:20 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-26 07:01:17 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-11-26 07:01:03 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.004 |  |
| 2026-11-26 07:00:51 | Moragaswewa (Deduru Oya) | 3.76 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-11-26 07:00:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.155 |  |
| 2026-11-26 07:00:18 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-11-26 07:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.03 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-26 07:01:49 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | 0.000 |  |
| 2026-11-26 07:01:17 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.331 | 🔺 Rising |
| 2026-11-26 07:00:51 | Moragaswewa (Deduru Oya) | 3.76 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-11-26 07:01:20 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-26 07:07:08 | Badalgama (Maha Oya) | 4.35 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-26 07:19:02 | Magura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-26 07:08:17 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-26 07:01:31 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 07:11:40 | Baddegama (Gin Ganga) | 1.92 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 07:01:03 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.004 |  |
| 2026-11-26 07:01:52 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:08:15 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:10:12 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:02:08 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-26 07:06:41 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-11-26 07:02:31 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-26 06:00:18 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-11-26 07:09:07 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.018 |  |
| 2026-11-26 07:14:28 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.018 |  |
| 2026-11-26 07:02:46 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-11-26 07:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-11-26 07:00:18 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 07:02:10 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.031 |  |
| 2026-11-26 07:05:02 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.031 |  |
| 2026-11-26 07:05:15 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.032 |  |
| 2026-11-26 07:04:49 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.038 |  |
| 2026-11-26 07:04:45 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | -0.038 |  |
| 2026-11-26 07:05:45 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.040 |  |
| 2026-11-26 07:04:05 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | -0.043 |  |
| 2026-11-26 07:09:47 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | -0.048 |  |
| 2026-11-26 07:06:43 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.055 |  |
| 2026-11-26 07:02:46 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.079 |  |
| 2026-11-26 07:06:56 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.088 |  |
| 2026-11-26 07:05:54 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.096 |  |
| 2026-11-26 07:02:43 | Giriulla (Maha Oya) | 3.55 | 🟢 Normal | -0.098 |  |
| 2026-11-26 07:00:47 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.155 |  |
| 2026-11-26 07:03:41 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)