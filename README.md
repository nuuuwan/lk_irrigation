# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_10:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 10:18:49 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-11-07 10:17:35 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:13:08 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:11:26 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.103 |  |
| 2026-11-07 10:10:39 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.127 |  |
| 2026-11-07 10:10:38 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.052 |  |
| 2026-11-07 10:08:16 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.075 |  |
| 2026-11-07 10:08:09 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:07:49 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:06:04 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.212 |  |
| 2026-11-07 10:05:31 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.020 |  |
| 2026-11-07 10:05:18 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.100 |  |
| 2026-11-07 10:05:12 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.164 |  |
| 2026-11-07 10:04:45 | Badalgama (Maha Oya) | 4.23 | 🟢 Normal | -0.122 |  |
| 2026-11-07 10:04:17 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:03:53 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-11-07 10:03:52 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.209 |  |
| 2026-11-07 10:03:44 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:03:28 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | -0.060 |  |
| 2026-11-07 10:03:19 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.044 |  |
| 2026-11-07 10:03:06 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:02:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:02:50 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 10:02:49 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.060 |  |
| 2026-11-07 10:02:45 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:02:41 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.010 |  |
| 2026-11-07 10:02:27 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-07 10:02:07 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-11-07 10:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:01:45 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 10:01:39 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 10:01:30 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:01:26 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-11-07 10:01:24 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.040 |  |
| 2026-11-07 10:01:24 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-07 10:01:05 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 10:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.26 | 🟡 Alert | -0.010 |  |
| 2026-11-07 10:05:31 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | -0.020 |  |
| 2026-11-07 10:01:39 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 10:01:45 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 10:02:50 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 10:01:05 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 10:02:45 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:01:50 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:07:49 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:03:44 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:08:09 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:02:59 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:02:41 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 10:18:49 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-11-07 10:04:17 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:01:30 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:02:56 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:17:35 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:03:06 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:13:08 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-11-07 10:01:26 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-11-07 10:03:53 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-11-07 10:01:24 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-07 09:04:22 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.029 |  |
| 2026-11-07 10:02:27 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-11-07 10:01:24 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.040 |  |
| 2026-11-07 10:03:19 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.044 |  |
| 2026-11-07 10:10:38 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.052 |  |
| 2026-11-07 10:02:49 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.060 |  |
| 2026-11-07 10:03:28 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | -0.060 |  |
| 2026-11-07 10:02:07 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-11-07 10:08:16 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | -0.075 |  |
| 2026-11-07 10:05:18 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.100 |  |
| 2026-11-07 10:11:26 | Holombuwa (Kelani Ganga) | 1.64 | 🟢 Normal | -0.103 |  |
| 2026-11-07 10:04:45 | Badalgama (Maha Oya) | 4.23 | 🟢 Normal | -0.122 |  |
| 2026-11-07 10:10:39 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.127 |  |
| 2026-11-07 10:05:12 | Giriulla (Maha Oya) | 2.83 | 🟢 Normal | -0.164 |  |
| 2026-11-07 10:03:52 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.209 |  |
| 2026-11-07 10:06:04 | Kithulgala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)