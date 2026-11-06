# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_05:32:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,127 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 05:32:21 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.022 |  |
| 2026-11-06 05:18:39 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-06 05:17:31 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.074 |  |
| 2026-11-06 05:15:57 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.139 |  |
| 2026-11-06 05:10:13 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-11-06 05:09:31 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-11-06 05:07:59 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-06 05:07:49 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.138 |  |
| 2026-11-06 05:07:11 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-11-06 05:07:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -0.060 |  |
| 2026-11-06 05:06:13 | Panadugama (Nilwala Ganga) | 5.23 | 🟡 Alert | 0.489 | 🔺 Rising |
| 2026-11-06 05:05:52 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-06 05:05:21 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:05:14 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.023 |  |
| 2026-11-06 05:04:37 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.037 |  |
| 2026-11-06 05:04:32 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-11-06 05:04:04 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | 25.714 | 🔺 Rising |
| 2026-11-06 05:03:59 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:03:50 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.021 |  |
| 2026-11-06 05:03:33 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-11-06 05:03:07 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.030 |  |
| 2026-11-06 05:02:59 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:58 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:02:55 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.049 |  |
| 2026-11-06 05:02:23 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:20 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 05:02:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:01:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:01:44 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:01:44 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 25.714 | 🔺 Rising |
| 2026-11-06 05:01:15 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:00:44 | Moraketiya (Walawe Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 05:00:20 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 05:06:13 | Panadugama (Nilwala Ganga) | 5.23 | 🟡 Alert | 0.489 | 🔺 Rising |
| 2026-11-06 05:04:04 | Kuda Oya (Kirindi Oya) | 2.05 | 🟢 Normal | 25.714 | 🔺 Rising |
| 2026-11-06 05:00:44 | Moraketiya (Walawe Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 05:18:39 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-06 04:23:36 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-06 05:02:20 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 05:07:59 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-06 05:02:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:01:15 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:02:58 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:03:59 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:01:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:07:09 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:52:19 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-11-06 05:09:31 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-11-06 05:05:21 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:59 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:23 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:01:44 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:00:20 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:07:11 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-06 05:10:13 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-11-06 05:04:32 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-11-06 05:05:52 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-11-06 05:03:50 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | -0.021 |  |
| 2026-11-06 05:32:21 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.022 |  |
| 2026-11-06 05:05:14 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.023 |  |
| 2026-11-06 05:03:33 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-11-06 05:03:07 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.030 |  |
| 2026-11-06 05:04:37 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.037 |  |
| 2026-11-06 05:02:55 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.049 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-06 05:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -0.060 |  |
| 2026-11-06 05:17:31 | Rathnapura (Kalu Ganga) | 2.61 | 🟢 Normal | -0.074 |  |
| 2026-11-06 05:07:49 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.138 |  |
| 2026-11-06 05:15:57 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)