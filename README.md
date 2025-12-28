# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_15:18:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,264 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 15:18:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-28 15:15:22 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:11:46 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:07:25 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.037 |  |
| 2025-12-28 15:07:04 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 15:06:56 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:06:17 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2025-12-28 15:06:14 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:06:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:05:59 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 15:05:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:05:53 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:59 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:53 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:50 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-28 15:04:25 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.029 |  |
| 2025-12-28 15:04:13 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:12 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:03:52 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:03:37 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 15:03:10 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:02:59 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:02:35 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:02:33 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.034 |  |
| 2025-12-28 15:02:31 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-28 15:02:29 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-28 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.041 |  |
| 2025-12-28 15:02:10 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:09 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2025-12-28 15:02:08 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:05 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:00 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 15:01:45 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:01:45 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 15:01:37 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:01:20 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:01:19 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 15:01:16 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:00:50 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:00:04 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 15:02:29 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-28 15:18:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-28 15:04:50 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-28 15:01:19 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 15:05:59 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 15:02:00 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 15:01:45 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-28 15:03:37 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 15:07:04 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 15:02:35 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:13 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:03:10 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:00:04 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:53 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:11:46 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:01:37 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:12 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:06:56 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:15:22 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:04:59 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:00:50 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:06:03 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:05:53 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:01:45 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:01:20 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:06:14 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:02:59 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:05:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 15:03:52 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:10 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:08 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:05 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.010 |  |
| 2025-12-28 15:02:09 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2025-12-28 15:06:17 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.019 |  |
| 2025-12-28 15:02:31 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2025-12-28 15:04:25 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.029 |  |
| 2025-12-28 15:02:33 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.034 |  |
| 2025-12-28 15:07:25 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.037 |  |
| 2025-12-28 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)