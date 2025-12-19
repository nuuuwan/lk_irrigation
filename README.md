# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_06:37:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 06:37:34 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:33:07 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:32:32 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-19 06:17:58 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:11:31 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.079 |  |
| 2025-12-19 06:11:22 | Padiyathalawa (Maduru Oya) | 1.78 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-19 06:09:50 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-19 06:09:09 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.066 |  |
| 2025-12-19 06:09:08 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:07:43 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-19 06:06:52 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-19 06:06:52 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:06:38 | Glencourse (Kelani Ganga) | 9.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 06:06:36 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:06:30 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:05:01 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2025-12-19 06:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.057 |  |
| 2025-12-19 06:04:17 | Manampitiya (Mahaweli Ganga) | 4.93 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-19 06:04:05 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:53 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-19 06:03:34 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:24 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2025-12-19 06:03:20 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:10 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:05 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:02:41 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-19 06:02:28 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:02:16 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:02:14 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:01:55 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:01:42 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.067 |  |
| 2025-12-19 06:01:28 | Horowpothana (Yan Oya) | 5.92 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2025-12-19 06:01:25 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:01:21 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-19 06:01:03 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.011 |  |
| 2025-12-19 06:00:50 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:00:31 | Nakkala (Kumbukkan Oya) | 1.75 | 🟢 Normal | -0.021 |  |
| 2025-12-19 06:00:22 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2025-12-19 06:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:53:56 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-19 05:40:50 | Padiyathalawa (Maduru Oya) | 1.71 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-19 05:40:49 | Padiyathalawa (Maduru Oya) | 1.76 | 🟢 Normal | 0.138 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 06:04:17 | Manampitiya (Mahaweli Ganga) | 4.93 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-19 06:03:53 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-19 06:01:28 | Horowpothana (Yan Oya) | 5.92 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2025-12-19 06:11:22 | Padiyathalawa (Maduru Oya) | 1.78 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-19 06:02:41 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-19 06:07:43 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-19 06:32:32 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-19 06:06:38 | Glencourse (Kelani Ganga) | 9.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 06:01:25 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:33:07 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:06:52 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:05 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:20 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:01:55 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:37:34 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:03:34 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:06:30 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:17:58 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:02:16 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:02:28 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:02:14 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:06:36 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:09:08 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:00:50 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:09:50 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-19 06:01:21 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-19 06:03:24 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2025-12-19 06:01:03 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | -0.011 |  |
| 2025-12-19 06:05:01 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.011 |  |
| 2025-12-19 06:00:22 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2025-12-19 06:06:52 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.013 |  |
| 2025-12-19 06:00:31 | Nakkala (Kumbukkan Oya) | 1.75 | 🟢 Normal | -0.021 |  |
| 2025-12-19 06:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.057 |  |
| 2025-12-19 06:09:09 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.066 |  |
| 2025-12-19 06:01:42 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.067 |  |
| 2025-12-19 06:11:31 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)