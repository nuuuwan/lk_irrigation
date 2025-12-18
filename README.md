# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_01:01:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,714 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 01:01:10 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:00:19 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:16:57 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 00:09:21 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:08:54 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.009 |  |
| 2025-12-19 00:07:32 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.123 |  |
| 2025-12-19 00:07:30 | Padiyathalawa (Maduru Oya) | 1.75 | 🟢 Normal | -0.096 |  |
| 2025-12-19 00:06:38 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2025-12-19 00:05:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:05:18 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.009 |  |
| 2025-12-19 00:04:58 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2025-12-19 00:04:54 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-19 00:04:43 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:04:32 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.037 |  |
| 2025-12-19 00:04:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.241 |  |
| 2025-12-19 00:04:06 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:03:59 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 00:03:32 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:03:23 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-19 00:03:19 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.089 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 00:00:35 | Manampitiya (Mahaweli Ganga) | 4.97 | 🟠 Minor Flood | 0.043 | 🔺 Rising |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-19 00:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-19 00:03:19 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-19 00:03:23 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-19 00:04:54 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-19 00:00:53 | Horowpothana (Yan Oya) | 5.54 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-19 00:16:57 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 00:02:18 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 00:03:59 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 00:01:14 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:04:06 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:00:55 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:02:58 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:01:10 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:03:32 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:02:04 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:05:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:00:16 | Siyambalanduwa (Heda Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-19 01:00:19 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:09:21 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:02:56 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 23:04:01 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:01:46 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:04:43 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-19 00:08:54 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.009 |  |
| 2025-12-19 00:05:18 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.009 |  |
| 2025-12-19 00:02:24 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-19 00:04:58 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.011 |  |
| 2025-12-19 00:00:47 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-19 00:06:38 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.021 |  |
| 2025-12-19 00:04:32 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.037 |  |
| 2025-12-19 00:00:34 | Nakkala (Kumbukkan Oya) | 2.06 | 🟢 Normal | -0.043 |  |
| 2025-12-19 00:07:30 | Padiyathalawa (Maduru Oya) | 1.75 | 🟢 Normal | -0.096 |  |
| 2025-12-19 00:07:32 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -0.123 |  |
| 2025-12-19 00:04:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.241 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)