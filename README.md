# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_11:07:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 11:07:15 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.000 |  |
| 2025-12-19 11:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:07:00 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:06:58 | Manampitiya (Mahaweli Ganga) | 4.73 | 🟠 Minor Flood | -0.038 |  |
| 2025-12-19 11:06:40 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2025-12-19 11:06:22 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2025-12-19 11:05:37 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 11:05:37 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.059 |  |
| 2025-12-19 11:05:36 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.020 |  |
| 2025-12-19 11:05:07 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:04:52 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:04:04 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:03:53 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.090 |  |
| 2025-12-19 11:03:48 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-19 11:03:38 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-19 11:03:34 | Weraganthota (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.863 |  |
| 2025-12-19 11:03:34 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:03:34 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2025-12-19 11:02:40 | Horowpothana (Yan Oya) | 6.17 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2025-12-19 11:02:18 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-19 11:02:03 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2025-12-19 11:01:58 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.031 |  |
| 2025-12-19 11:01:47 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:01:30 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:01:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2025-12-19 11:01:09 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:00:53 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:00:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:00:11 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:00:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:00:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:19:47 | Weraganthota (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.863 |  |
| 2025-12-19 10:18:23 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:12:49 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2025-12-19 10:11:15 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:11:07 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:10:41 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 10:08:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.049 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 11:06:58 | Manampitiya (Mahaweli Ganga) | 4.73 | 🟠 Minor Flood | -0.038 |  |
| 2025-12-19 11:02:40 | Horowpothana (Yan Oya) | 6.17 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2025-12-19 11:07:15 | Thanthirimale (Malwathu Oya) | 5.36 | 🟡 Alert | 0.000 |  |
| 2025-12-19 11:02:18 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-19 11:03:48 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-19 11:03:38 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-19 11:05:37 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 11:00:34 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:01:09 | Moragaswewa (Deduru Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:00:08 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:11:07 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:04:52 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:18:23 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:00:10 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:05:07 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:11:15 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 11:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-19 10:12:49 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2025-12-19 10:06:41 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:03:34 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:04:04 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:07:00 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:00:11 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:01:30 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:00:53 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:01:47 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-19 11:02:03 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2025-12-19 10:03:23 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2025-12-19 11:06:22 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2025-12-19 11:05:36 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.020 |  |
| 2025-12-19 10:03:48 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | -0.021 |  |
| 2025-12-19 11:06:40 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2025-12-19 11:01:58 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.031 |  |
| 2025-12-19 11:01:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2025-12-19 11:03:34 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2025-12-19 10:08:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.049 |  |
| 2025-12-19 11:05:37 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.059 |  |
| 2025-12-19 11:03:53 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.090 |  |
| 2025-12-19 11:03:34 | Weraganthota (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.863 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)