# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_09:07:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,554 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 09:07:27 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:07:26 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.070 |  |
| 2026-03-18 09:05:20 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-18 09:04:55 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-03-18 09:04:17 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:04:10 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:04:03 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:04:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.041 |  |
| 2026-03-18 09:03:59 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-03-18 09:03:56 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-03-18 09:03:53 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:51 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-18 09:03:46 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-18 09:03:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:17 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:13 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:02:57 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 09:02:49 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:02:45 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-03-18 09:02:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.058 |  |
| 2026-03-18 09:02:32 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:02:11 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.051 |  |
| 2026-03-18 09:01:56 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:01:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:01:48 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:01:47 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.064 |  |
| 2026-03-18 09:01:39 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-18 09:01:23 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-03-18 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:00:59 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:00:53 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:17:04 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-03-18 08:14:31 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 09:02:45 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-03-18 09:03:51 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-18 09:01:39 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-18 09:03:46 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-18 08:06:02 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 09:02:57 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 08:14:31 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 09:02:11 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:02:49 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:45 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:01:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:13 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:04:17 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:02:32 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:01:48 | Ellagawa (Kalu Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:10:30 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:26 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:04:03 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:00:59 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:04:09 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:01:56 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:17 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:07:27 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:04:10 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-18 08:06:15 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:00:53 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:03:53 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 09:04:55 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-03-18 09:05:20 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-18 09:03:56 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-03-18 09:03:59 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-03-18 09:01:23 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.040 |  |
| 2026-03-18 09:04:03 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.041 |  |
| 2026-03-18 09:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.051 |  |
| 2026-03-18 09:02:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.058 |  |
| 2026-03-18 09:01:47 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.064 |  |
| 2026-03-18 09:07:26 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)