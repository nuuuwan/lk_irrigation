# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_08:21:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,679 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 08:21:47 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.022 |  |
| 2026-10-12 08:12:52 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.062 |  |
| 2026-10-12 08:11:11 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.027 |  |
| 2026-10-12 08:10:17 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 08:08:23 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.102 |  |
| 2026-10-12 08:08:10 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 08:07:56 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.065 |  |
| 2026-10-12 08:07:54 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-12 08:06:58 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:06:45 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.021 |  |
| 2026-10-12 08:06:14 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.125 |  |
| 2026-10-12 08:05:46 | Dunamale (Aththanagalu Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-12 08:05:44 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.042 |  |
| 2026-10-12 08:05:14 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-10-12 08:04:49 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.081 |  |
| 2026-10-12 08:04:32 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-12 08:04:20 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-10-12 08:04:17 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-10-12 08:04:16 | Panadugama (Nilwala Ganga) | 4.84 | 🟢 Normal | -0.089 |  |
| 2026-10-12 08:04:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-10-12 08:03:59 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.178 |  |
| 2026-10-12 08:03:47 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-10-12 08:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-12 08:03:31 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-10-12 08:03:24 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:03:13 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-12 08:03:03 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-12 08:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.13 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-12 08:02:49 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-12 08:02:45 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:02:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.030 |  |
| 2026-10-12 08:02:38 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:01:53 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.105 |  |
| 2026-10-12 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-12 08:01:06 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.060 |  |
| 2026-10-12 08:00:52 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:00:36 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-10-12 08:00:15 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.041 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 08:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.13 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-12 08:04:32 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-12 08:03:03 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-12 08:03:13 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-12 08:00:15 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-12 08:01:26 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-12 08:10:17 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 08:07:54 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-12 08:08:10 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 06:09:56 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:00:52 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:02:38 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:02:45 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:06:58 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:03:24 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 08:03:47 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-10-12 08:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-12 08:02:49 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-12 08:00:36 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | -0.012 |  |
| 2026-10-12 08:05:14 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-10-12 08:05:46 | Dunamale (Aththanagalu Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-12 08:06:45 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.021 |  |
| 2026-10-12 08:04:20 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-10-12 08:21:47 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.022 |  |
| 2026-10-12 08:11:11 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.027 |  |
| 2026-10-12 08:02:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.030 |  |
| 2026-10-12 08:04:17 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-10-12 08:03:31 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-10-12 08:05:44 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.042 |  |
| 2026-10-12 08:01:06 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.060 |  |
| 2026-10-12 08:12:52 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.062 |  |
| 2026-10-12 08:07:56 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.065 |  |
| 2026-10-12 08:04:49 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.081 |  |
| 2026-10-12 08:04:16 | Panadugama (Nilwala Ganga) | 4.84 | 🟢 Normal | -0.089 |  |
| 2026-10-12 08:04:07 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.089 |  |
| 2026-10-12 08:08:23 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.102 |  |
| 2026-10-12 08:01:53 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.105 |  |
| 2026-10-12 08:06:14 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.125 |  |
| 2026-10-12 08:03:59 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)