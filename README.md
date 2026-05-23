# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_12:15:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,612 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 12:15:21 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.024 |  |
| 2026-05-23 12:11:48 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:07:49 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.019 |  |
| 2026-05-23 12:06:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:05:59 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:05:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:05:11 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:05:00 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-05-23 12:04:56 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | -0.030 |  |
| 2026-05-23 12:04:43 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.037 |  |
| 2026-05-23 12:04:42 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.125 |  |
| 2026-05-23 12:04:23 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-23 12:04:21 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.032 |  |
| 2026-05-23 12:04:18 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-05-23 12:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:03:48 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:03:44 | Putupaula (Kalu Ganga) | 3.06 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 12:03:43 | Rathnapura (Kalu Ganga) | 5.98 | 🟡 Alert | -0.059 |  |
| 2026-05-23 12:03:37 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:03:35 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:03:28 | Hanwella (Kelani Ganga) | 6.67 | 🟢 Normal | -0.090 |  |
| 2026-05-23 12:02:52 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:02:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.059 |  |
| 2026-05-23 12:02:31 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:02:23 | Dunamale (Aththanagalu Oya) | 5.08 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 12:02:19 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 12:01:38 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.064 |  |
| 2026-05-23 12:01:38 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:01:32 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:01:27 | Ellagawa (Kalu Ganga) | 10.20 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 12:01:26 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-05-23 12:01:25 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-05-23 12:01:22 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:01:18 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-23 12:01:06 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:00:18 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:00:12 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.59 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 12:02:23 | Dunamale (Aththanagalu Oya) | 5.08 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 12:03:44 | Putupaula (Kalu Ganga) | 3.06 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 12:01:27 | Ellagawa (Kalu Ganga) | 10.20 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 12:04:56 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | -0.030 |  |
| 2026-05-23 12:03:43 | Rathnapura (Kalu Ganga) | 5.98 | 🟡 Alert | -0.059 |  |
| 2026-05-23 12:05:00 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-05-23 12:04:23 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-23 12:02:31 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:01:22 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:02:52 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:03:35 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:03:48 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:05:11 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:01:38 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:03:37 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:02:19 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:06:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:01:06 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:05:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:00:18 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-23 12:05:59 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:06:22 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:11:48 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:00:12 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:01:32 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-23 12:04:18 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-05-23 12:07:49 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.019 |  |
| 2026-05-23 12:01:18 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-23 12:15:21 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.024 |  |
| 2026-05-23 12:01:25 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.030 |  |
| 2026-05-23 12:04:21 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.032 |  |
| 2026-05-23 12:04:43 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.037 |  |
| 2026-05-23 12:01:26 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.059 |  |
| 2026-05-23 12:02:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.059 |  |
| 2026-05-23 12:01:38 | Glencourse (Kelani Ganga) | 12.11 | 🟢 Normal | -0.064 |  |
| 2026-05-23 12:03:28 | Hanwella (Kelani Ganga) | 6.67 | 🟢 Normal | -0.090 |  |
| 2026-05-23 12:04:42 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)