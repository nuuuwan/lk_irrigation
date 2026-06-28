# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_00:21:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,084 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 00:21:15 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:17:57 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:12:16 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-29 00:12:15 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-29 00:12:14 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-29 00:11:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.047 |  |
| 2026-06-29 00:10:23 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:10:01 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 00:09:09 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.162 |  |
| 2026-06-29 00:08:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:07:14 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:06:41 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-29 00:06:31 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:06:29 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 00:06:13 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-06-29 00:06:07 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:05:58 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-06-29 00:05:27 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-29 00:05:18 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 00:03:55 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-29 00:03:42 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-06-29 00:03:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.039 |  |
| 2026-06-29 00:03:23 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:23 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:17 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-29 00:02:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:02:54 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 00:02:50 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.005 |  |
| 2026-06-29 00:02:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-29 00:02:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:47 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:30 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 15.652 | 🔺 Rising |
| 2026-06-29 00:01:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:15 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-29 00:01:07 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 15.652 | 🔺 Rising |
| 2026-06-29 00:00:35 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 00:12:16 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-29 00:01:30 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 15.652 | 🔺 Rising |
| 2026-06-29 00:03:42 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-06-29 00:03:17 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-29 00:03:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-29 00:05:27 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-06-29 00:06:41 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-29 00:10:01 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 00:06:29 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 00:02:54 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 00:05:18 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:00:35 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:10:23 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:23 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:47 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:06:07 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:01:22 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:06:31 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:35 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:21:15 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:07:14 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:02:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:17:57 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 23:05:37 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:03:55 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:02:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:08:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-06-29 00:02:50 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.005 |  |
| 2026-06-29 00:05:58 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-06-29 00:02:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 00:01:15 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-29 00:06:13 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.011 |  |
| 2026-06-29 00:03:29 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.039 |  |
| 2026-06-29 00:11:36 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.047 |  |
| 2026-06-29 00:09:09 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)