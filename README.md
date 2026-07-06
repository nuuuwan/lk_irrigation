# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_02:25:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,326 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 02:25:46 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -43.902 |  |
| 2026-07-07 02:24:24 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -43.902 |  |
| 2026-07-07 02:21:49 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-07-07 02:20:14 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-07 02:19:59 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:16:33 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-07 02:15:51 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:15:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.017 |  |
| 2026-07-07 02:12:29 | Yaka Wewa (Ma Oya) | 0.12 | 🟢 Normal | -0.314 |  |
| 2026-07-07 02:12:24 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:10:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:08:11 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-07 02:06:45 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-07 02:06:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-07 02:05:02 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:04:42 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:04:41 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.485 |  |
| 2026-07-07 02:03:44 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-07 02:03:36 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:03:05 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-07-07 02:02:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-07 02:02:51 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:02:42 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-07-07 02:02:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:02:10 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:02:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:02:09 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.014 |  |
| 2026-07-07 02:01:59 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:46 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-07-07 02:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:10 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:04 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 02:02:42 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-07-07 02:06:45 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-07 02:06:03 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-07 02:08:11 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-07 02:02:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-07 02:20:14 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-07 02:16:33 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-07 02:05:02 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:02:10 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:04 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:01:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:02:51 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:10 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:12:11 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:24 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:02:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:19:59 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:01:46 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:15:51 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-06 18:00:56 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:08:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:04:42 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:03:36 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-07 02:10:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 01:02:31 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.005 |  |
| 2026-07-07 01:37:37 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.007 |  |
| 2026-07-07 02:21:49 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-07-07 01:10:32 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-07-06 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 18:06:11 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-07-07 02:03:44 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-07 02:01:26 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-07-07 02:02:09 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.014 |  |
| 2026-07-07 02:15:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.017 |  |
| 2026-07-07 02:03:05 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.030 |  |
| 2026-07-07 02:12:29 | Yaka Wewa (Ma Oya) | 0.12 | 🟢 Normal | -0.314 |  |
| 2026-07-07 02:04:41 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.485 |  |
| 2026-07-07 02:25:46 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -43.902 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)