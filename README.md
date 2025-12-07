# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_13:23:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,622 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 13:23:39 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:16:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.046 |  |
| 2025-12-07 13:13:18 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:12:48 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.054 |  |
| 2025-12-07 13:11:42 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.009 |  |
| 2025-12-07 13:10:17 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2025-12-07 13:07:44 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:06:28 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:06:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2025-12-07 13:05:46 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2025-12-07 13:05:44 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:05:31 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.086 |  |
| 2025-12-07 13:05:07 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:05:01 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.049 |  |
| 2025-12-07 13:04:31 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.040 |  |
| 2025-12-07 13:04:31 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:03:58 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:03:53 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:03:48 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:03:37 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:03:34 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2025-12-07 13:03:23 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.012 |  |
| 2025-12-07 13:03:18 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2025-12-07 13:02:53 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 13:02:52 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:02:44 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:02:43 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:02:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.060 |  |
| 2025-12-07 13:01:53 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.080 |  |
| 2025-12-07 13:01:49 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-07 13:01:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:01:08 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:01:07 | Thanthirimale (Malwathu Oya) | 5.85 | 🟡 Alert | -0.082 |  |
| 2025-12-07 13:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:01:03 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2025-12-07 13:00:54 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 13:01:07 | Thanthirimale (Malwathu Oya) | 5.85 | 🟡 Alert | -0.082 |  |
| 2025-12-07 13:06:14 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2025-12-07 13:02:53 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 13:01:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:01:08 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:02:43 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:00:54 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:13:18 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:03:48 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:02:44 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:07:44 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:02:52 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:23:39 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:05:44 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:03:53 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:05:31 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:04:31 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:03:37 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:06:28 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:11:42 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.009 |  |
| 2025-12-07 13:05:07 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:03:58 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:01:49 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-07 13:03:23 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.012 |  |
| 2025-12-07 13:01:03 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2025-12-07 13:10:17 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2025-12-07 13:05:46 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2025-12-07 13:03:18 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2025-12-07 13:04:31 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.040 |  |
| 2025-12-07 13:03:34 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2025-12-07 13:16:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.046 |  |
| 2025-12-07 13:05:01 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.049 |  |
| 2025-12-07 13:12:48 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.054 |  |
| 2025-12-07 13:02:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.060 |  |
| 2025-12-07 13:01:53 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.080 |  |
| 2025-12-07 13:05:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)