# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_17:20:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,468 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 17:20:31 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-22 17:16:27 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:11:53 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-03-22 17:11:02 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:10:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:10:21 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.074 |  |
| 2026-03-22 17:09:02 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.058 |  |
| 2026-03-22 17:08:27 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-03-22 17:07:29 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:07:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.945 | 🔺 Rising |
| 2026-03-22 17:06:51 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-03-22 17:05:53 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:05:50 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 17:04:53 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-03-22 17:03:49 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-22 17:03:48 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-22 17:03:35 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:03:31 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:03:19 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-03-22 17:03:00 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-22 17:02:56 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:48 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-03-22 17:02:44 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-22 17:02:41 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:37 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 17:02:25 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.122 |  |
| 2026-03-22 17:02:21 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:17 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 17:02:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:09 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-22 17:02:04 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:01:27 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-22 17:01:11 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:01:09 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-22 17:00:43 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:00:20 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 17:07:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.945 | 🔺 Rising |
| 2026-03-22 17:03:19 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-03-22 17:02:44 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-22 17:01:27 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-22 17:01:09 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-22 17:03:49 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-22 17:20:31 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-22 17:02:17 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 17:05:50 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 17:02:09 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-22 17:00:20 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 17:02:37 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 17:02:41 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:01:11 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-22 16:03:59 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:10:42 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:00:43 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:03:31 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:07:29 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:03:35 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:04 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:56 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:04:53 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 16:04:43 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:21 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:16:27 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:02:13 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:05:53 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 17:11:53 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-03-22 17:03:00 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-22 17:03:48 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-03-22 17:06:51 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-03-22 17:02:48 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-03-22 17:08:27 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-03-22 17:04:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.030 |  |
| 2026-03-22 17:09:02 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.058 |  |
| 2026-03-22 17:10:21 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.074 |  |
| 2026-03-22 17:02:25 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)