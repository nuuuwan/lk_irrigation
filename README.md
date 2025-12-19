# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_19:23:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,430 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 19:23:28 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:12:56 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -1080.000 |  |
| 2025-12-19 19:12:55 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | -1080.000 |  |
| 2025-12-19 19:12:00 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:10:33 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:10:16 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-19 19:08:25 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:06:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.061 |  |
| 2025-12-19 19:06:35 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:06:30 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2025-12-19 19:06:16 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.009 |  |
| 2025-12-19 19:05:54 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.027 |  |
| 2025-12-19 19:05:43 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:05:32 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-19 19:04:34 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | -0.080 |  |
| 2025-12-19 19:04:22 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-19 19:04:10 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-19 19:04:01 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:03:53 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:03:40 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:03:00 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.038 |  |
| 2025-12-19 19:02:48 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2025-12-19 19:02:41 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2025-12-19 19:02:34 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:34 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 19:02:30 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:01 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:00 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2025-12-19 19:01:56 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 19:01:55 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-19 19:01:53 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:01:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:01:18 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:00:58 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.031 |  |
| 2025-12-19 19:00:39 | Horowpothana (Yan Oya) | 6.29 | 🟡 Alert | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-19 19:00:39 | Horowpothana (Yan Oya) | 6.29 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-19 19:04:34 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | -0.080 |  |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-19 19:02:34 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 19:10:16 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-19 19:05:32 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-19 19:01:56 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 19:01:53 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:34 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:23:28 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:01:18 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:08:25 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:30 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:03:53 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:05:43 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:01:46 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:04:01 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:03:40 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:12:00 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:10:33 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:06:35 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:01 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:02:41 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 19:04:22 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-19 19:06:16 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.009 |  |
| 2025-12-19 19:02:48 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2025-12-19 19:01:55 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-19 19:02:00 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2025-12-19 19:04:10 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2025-12-19 19:05:54 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.027 |  |
| 2025-12-19 19:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2025-12-19 19:06:30 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.031 |  |
| 2025-12-19 19:00:58 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | -0.031 |  |
| 2025-12-19 19:03:00 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.038 |  |
| 2025-12-19 19:06:46 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.061 |  |
| 2025-12-19 19:12:56 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -1080.000 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)