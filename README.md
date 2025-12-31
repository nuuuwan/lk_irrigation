# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_08:16:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,651 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 08:16:41 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:15:45 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:13:03 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.017 |  |
| 2025-12-31 08:11:18 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2025-12-31 08:10:55 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:10:44 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.054 |  |
| 2025-12-31 08:08:56 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:08:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-31 08:07:01 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.091 |  |
| 2025-12-31 08:06:54 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2025-12-31 08:06:32 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.009 |  |
| 2025-12-31 08:06:06 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 08:05:40 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:05:08 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:04:46 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 08:04:45 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 08:04:21 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 08:03:52 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 08:03:39 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:03:19 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:03:06 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.079 |  |
| 2025-12-31 08:02:54 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:02:40 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:02:34 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 08:02:31 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:02:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:02:25 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:46 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:41 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:41 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:29 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.011 |  |
| 2025-12-31 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:24 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-31 08:01:15 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.014 |  |
| 2025-12-31 08:01:12 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:01:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:00:12 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 07:51:18 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 08:01:24 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-31 08:08:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-31 08:04:21 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-31 08:04:45 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 08:03:52 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 08:06:06 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 08:02:34 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 08:04:46 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 08:01:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:46 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:02:31 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:00:12 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:02:54 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:02:25 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:08:56 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:15:45 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:16:41 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:05:08 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:05:40 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:41 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:01:41 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:03:19 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:10:55 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:02:29 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:06:32 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.009 |  |
| 2025-12-31 08:03:39 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:03:06 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:01:12 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:02:40 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2025-12-31 08:01:29 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.011 |  |
| 2025-12-31 08:01:15 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.014 |  |
| 2025-12-31 08:13:03 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.017 |  |
| 2025-12-31 08:06:54 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | -0.019 |  |
| 2025-12-31 08:11:18 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2025-12-31 07:04:40 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2025-12-31 08:10:44 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.054 |  |
| 2025-12-31 08:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.079 |  |
| 2025-12-31 08:07:01 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)