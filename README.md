# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_07:35:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,312 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 07:35:28 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.014 |  |
| 2026-05-24 07:27:06 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:15:51 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:15:40 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | -0.153 |  |
| 2026-05-24 07:15:32 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.025 |  |
| 2026-05-24 07:12:50 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:12:39 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:12:02 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.097 |  |
| 2026-05-24 07:11:50 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 07:10:26 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.973 | 🔺 Rising |
| 2026-05-24 07:09:49 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.973 | 🔺 Rising |
| 2026-05-24 07:09:22 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-05-24 07:08:43 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:08:32 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-24 07:07:24 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 07:07:09 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:06:04 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.030 |  |
| 2026-05-24 07:05:58 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-24 07:05:49 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.038 |  |
| 2026-05-24 07:05:44 | Hanwella (Kelani Ganga) | 4.86 | 🟢 Normal | -0.104 |  |
| 2026-05-24 07:05:38 | Putupaula (Kalu Ganga) | 3.31 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-24 07:05:29 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-24 07:04:58 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-24 07:04:48 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 07:04:28 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-24 07:04:20 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | 0.000 |  |
| 2026-05-24 07:04:16 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:04:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 07:04:07 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-05-24 07:03:08 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:02:29 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:02:23 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.150 |  |
| 2026-05-24 07:02:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-24 07:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:02:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 07:01:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:01:25 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:00:37 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.002 |  |
| 2026-05-24 07:00:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:00:22 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 06:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.61 | 🟠 Minor Flood | -0.064 |  |
| 2026-05-24 07:05:38 | Putupaula (Kalu Ganga) | 3.31 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-24 07:04:20 | Ellagawa (Kalu Ganga) | 10.10 | 🟡 Alert | 0.000 |  |
| 2026-05-24 07:02:23 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.150 |  |
| 2026-05-24 07:10:26 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.973 | 🔺 Rising |
| 2026-05-24 07:05:29 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-24 07:08:32 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-24 07:04:48 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 07:04:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-24 07:05:58 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-24 07:02:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 07:07:24 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 07:11:50 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-24 07:02:20 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-24 07:04:16 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:07:09 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:01:42 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:03:08 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:12:50 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:02:29 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:15:51 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:00:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:08:43 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:27:06 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:01:25 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-24 07:00:37 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.002 |  |
| 2026-05-24 07:04:58 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | -0.010 |  |
| 2026-05-24 07:04:28 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-05-24 07:35:28 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.014 |  |
| 2026-05-24 07:04:07 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2026-05-24 07:15:32 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | -0.025 |  |
| 2026-05-24 07:06:04 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.030 |  |
| 2026-05-24 07:05:49 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.038 |  |
| 2026-05-24 07:00:22 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.050 |  |
| 2026-05-24 07:09:22 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-05-24 07:12:02 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.097 |  |
| 2026-05-24 07:05:44 | Hanwella (Kelani Ganga) | 4.86 | 🟢 Normal | -0.104 |  |
| 2026-05-24 07:15:40 | Rathnapura (Kalu Ganga) | 4.50 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)