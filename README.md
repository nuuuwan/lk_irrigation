# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_15:16:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,468 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 15:16:24 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:08:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.045 |  |
| 2026-10-07 15:06:52 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:06:39 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.056 |  |
| 2026-10-07 15:06:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2026-10-07 15:05:16 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-10-07 15:05:15 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:05:13 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.000 |  |
| 2026-10-07 15:05:10 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.050 |  |
| 2026-10-07 15:05:10 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-10-07 15:04:53 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.000 |  |
| 2026-10-07 15:04:51 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.012 |  |
| 2026-10-07 15:04:42 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:04:29 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.044 |  |
| 2026-10-07 15:03:55 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:03:50 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:03:44 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-07 15:03:24 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.086 |  |
| 2026-10-07 15:03:21 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:03:21 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:03:18 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-10-07 15:03:08 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:03:07 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-10-07 15:03:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 15:03:04 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-10-07 15:03:01 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:02:23 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:02:19 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-07 15:02:11 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:02:11 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:02:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:02:05 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-07 15:01:34 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:01:34 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-10-07 15:01:22 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.045 |  |
| 2026-10-07 15:01:17 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 15:01:14 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:00:58 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 15:05:13 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.000 |  |
| 2026-10-07 15:02:19 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-07 15:03:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 15:02:05 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-07 15:01:17 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-07 15:03:55 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:01:14 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:05:15 | Baddegama (Gin Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:16:24 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:02:10 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:03:50 | Siyambalanduwa (Heda Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:03:08 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:06:52 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:02:23 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:04:42 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-07 15:03:44 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-07 15:05:10 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-10-07 15:03:04 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.011 |  |
| 2026-10-07 15:04:51 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.012 |  |
| 2026-10-07 15:03:18 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-10-07 15:03:21 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:01:34 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:02:11 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:03:01 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:02:11 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:00:58 | Weraganthota (Mahaweli Ganga) | -3.47 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:03:21 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-10-07 15:01:34 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-10-07 15:05:16 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.030 |  |
| 2026-10-07 15:06:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.033 |  |
| 2026-10-07 15:03:07 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.041 |  |
| 2026-10-07 14:13:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | -0.042 |  |
| 2026-10-07 15:04:29 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.044 |  |
| 2026-10-07 15:01:22 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.045 |  |
| 2026-10-07 15:08:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.045 |  |
| 2026-10-07 15:05:10 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.050 |  |
| 2026-10-07 15:06:39 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.056 |  |
| 2026-10-07 15:03:24 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)