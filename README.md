# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_22:08:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,529 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 22:08:53 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:05:30 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 22:05:09 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-19 22:05:04 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2025-12-19 22:04:48 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:50 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-19 22:03:42 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:33 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:07 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:06 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:46 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:35 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-19 22:02:25 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-19 22:02:19 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:13 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:12 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2025-12-19 22:02:10 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:01:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:01:37 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:01:24 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 22:01:14 | Horowpothana (Yan Oya) | 6.33 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2025-12-19 22:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:00:54 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 22:00:15 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-19 22:00:07 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:59:37 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.113 |  |
| 2025-12-19 21:23:04 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:14:02 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:13:06 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-19 22:01:14 | Horowpothana (Yan Oya) | 6.33 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2025-12-19 21:03:15 | Manampitiya (Mahaweli Ganga) | 4.14 | 🟡 Alert | -0.020 |  |
| 2025-12-19 21:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-19 22:05:09 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-19 21:06:47 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-19 22:00:54 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 22:01:24 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 22:05:30 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 22:00:07 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:33 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:01:37 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:08:53 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:13 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:23:04 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:07 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:10 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:13:06 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:01:54 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:46 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:03:22 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:06 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:04:48 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:05:10 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:19 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:01:18 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 21:02:18 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:03:42 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 22:02:25 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-19 22:02:35 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2025-12-19 22:05:04 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2025-12-19 22:00:15 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-19 22:03:50 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-19 21:03:14 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2025-12-19 22:02:12 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2025-12-19 21:59:37 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)