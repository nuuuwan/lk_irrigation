# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_14:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,533 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 14:12:05 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.145 |  |
| 2026-10-16 14:11:13 | Galgamuwa (Mee Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:11:06 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.062 |  |
| 2026-10-16 14:10:35 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-10-16 14:09:28 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.094 |  |
| 2026-10-16 14:08:23 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-10-16 14:08:06 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-16 14:07:48 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-10-16 14:07:04 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 14:06:28 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.062 |  |
| 2026-10-16 14:06:21 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.030 |  |
| 2026-10-16 14:06:01 | Baddegama (Gin Ganga) | 3.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-16 14:05:24 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-10-16 14:04:43 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -1.030 |  |
| 2026-10-16 14:04:24 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:04:22 | Dunamale (Aththanagalu Oya) | 3.38 | 🟡 Alert | -0.041 |  |
| 2026-10-16 14:04:00 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.030 |  |
| 2026-10-16 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-16 14:03:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:03:19 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | 0.000 |  |
| 2026-10-16 14:02:55 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | -0.020 |  |
| 2026-10-16 14:02:47 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:02:40 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-10-16 14:02:32 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-10-16 14:02:31 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:02:25 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-10-16 14:02:12 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.014 |  |
| 2026-10-16 14:01:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:01:35 | Moragaswewa (Deduru Oya) | 2.22 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-16 14:01:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:01:19 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 14:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:00:48 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:00:46 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.060 |  |
| 2026-10-16 14:00:45 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-16 14:00:43 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 13:02:18 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 13:04:43 | Panadugama (Nilwala Ganga) | 6.58 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-16 14:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | 0.000 |  |
| 2026-10-16 14:04:22 | Dunamale (Aththanagalu Oya) | 3.38 | 🟡 Alert | -0.041 |  |
| 2026-10-16 14:01:35 | Moragaswewa (Deduru Oya) | 2.22 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-16 14:00:45 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-16 14:08:06 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-16 14:06:01 | Baddegama (Gin Ganga) | 3.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-16 14:01:19 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-16 14:07:04 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 14:00:48 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:01:36 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:11:13 | Galgamuwa (Mee Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:02:47 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:00:43 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:03:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 14:08:23 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-10-16 14:04:24 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:03:19 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:02:31 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:01:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-16 14:02:25 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-10-16 14:02:12 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.014 |  |
| 2026-10-16 14:05:24 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-10-16 14:02:32 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-10-16 14:02:55 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | -0.020 |  |
| 2026-10-16 14:07:48 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.027 |  |
| 2026-10-16 14:06:21 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.030 |  |
| 2026-10-16 14:04:00 | Hanwella (Kelani Ganga) | 3.49 | 🟢 Normal | -0.030 |  |
| 2026-10-16 14:10:35 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-10-16 14:02:40 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.041 |  |
| 2026-10-16 14:00:46 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.060 |  |
| 2026-10-16 14:11:06 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.062 |  |
| 2026-10-16 14:06:28 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.062 |  |
| 2026-10-16 14:09:28 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.094 |  |
| 2026-10-16 14:12:05 | Pitabeddara (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.145 |  |
| 2026-10-16 14:04:43 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -1.030 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)