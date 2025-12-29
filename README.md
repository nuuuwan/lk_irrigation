# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_13:13:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,074 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 13:13:26 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:12:11 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:07:07 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:06:47 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-29 13:06:18 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:06:08 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:06:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2025-12-29 13:05:49 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 13:05:43 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-29 13:05:32 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:05:15 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:05:10 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:04:40 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2025-12-29 13:04:35 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2025-12-29 13:04:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:04:09 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.068 |  |
| 2025-12-29 13:04:03 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 13:04:03 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 13:03:53 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-29 13:03:45 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:03:42 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:03:39 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:03:17 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 13:03:14 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.139 |  |
| 2025-12-29 13:03:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:02:51 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:43 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2025-12-29 13:02:37 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:02:29 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:08 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:01:25 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-29 13:01:21 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:01:03 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:00:38 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:00:27 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:00:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 12:24:00 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 13:04:40 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 7.200 | 🔺 Rising |
| 2025-12-29 12:02:30 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-29 13:01:25 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-29 13:04:03 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 13:03:17 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 13:00:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-29 13:05:43 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-29 13:03:53 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-29 13:04:03 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 13:05:49 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-29 13:00:27 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:02:55 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:12:11 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:01:03 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:03:45 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:05:15 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:03:42 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:06:18 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:13:26 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:06:08 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:02:37 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:02:08 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:03:39 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:05:10 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:04:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:07:07 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:05:32 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-29 13:02:51 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:03:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:00:38 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:02:29 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.010 |  |
| 2025-12-29 13:06:47 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-29 13:06:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2025-12-29 13:02:43 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2025-12-29 13:04:09 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.068 |  |
| 2025-12-29 13:03:14 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)