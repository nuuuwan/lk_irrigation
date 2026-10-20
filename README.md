# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_17:06:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,257 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 17:06:06 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-20 17:06:05 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.062 |  |
| 2026-10-20 17:05:44 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-10-20 17:05:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:05:22 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:05:07 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.048 |  |
| 2026-10-20 17:04:36 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:04:33 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.022 |  |
| 2026-10-20 17:04:28 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:04:06 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-20 17:03:47 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-20 17:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.030 |  |
| 2026-10-20 17:03:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:03:03 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-10-20 17:02:54 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:02:46 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:02:36 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 17:02:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:02:22 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:02:10 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-10-20 17:01:51 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:01:41 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.050 |  |
| 2026-10-20 17:01:38 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-20 17:01:37 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.023 |  |
| 2026-10-20 17:01:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.158 |  |
| 2026-10-20 17:00:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-20 17:00:41 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-20 17:00:36 | Thalgahagoda (Nilwala Ganga) | 1.61 | 🟡 Alert | -0.016 |  |
| 2026-10-20 17:00:23 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 17:00:36 | Thalgahagoda (Nilwala Ganga) | 1.61 | 🟡 Alert | -0.016 |  |
| 2026-10-20 17:06:06 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-20 17:04:06 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-20 17:03:47 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-20 16:02:20 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 17:02:36 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 16:02:06 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:02:54 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:02:46 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:00:23 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:02:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:03:03 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:05:22 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-20 17:05:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:07:44 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-10-20 16:14:14 | Urawa (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-10-20 16:06:21 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:04:28 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:04:36 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:01:51 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:02:22 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-20 17:01:38 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-10-20 17:00:41 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-20 17:05:44 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-10-20 17:02:10 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-10-20 17:04:33 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | -0.022 |  |
| 2026-10-20 17:01:37 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.023 |  |
| 2026-10-20 16:08:29 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.027 |  |
| 2026-10-20 17:00:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-10-20 17:03:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.97 | 🟢 Normal | -0.030 |  |
| 2026-10-20 17:03:03 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.040 |  |
| 2026-10-20 16:04:06 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.041 |  |
| 2026-10-20 17:05:07 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.048 |  |
| 2026-10-20 17:01:41 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.050 |  |
| 2026-10-20 16:03:16 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.057 |  |
| 2026-10-20 17:06:05 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.062 |  |
| 2026-10-20 16:11:37 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.074 |  |
| 2026-10-20 17:01:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)