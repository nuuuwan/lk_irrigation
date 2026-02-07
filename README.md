# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_22:28:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,947 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 22:28:39 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-07 22:25:04 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:20:34 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:16:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:15:03 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.038 |  |
| 2026-02-07 22:13:01 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-02-07 22:12:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.113 |  |
| 2026-02-07 22:09:53 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:09:03 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-02-07 22:07:12 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:05:54 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:05:30 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:04:41 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:04:13 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |
| 2026-02-07 22:04:08 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:03:54 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 22:03:20 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:03:13 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-07 22:03:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:02:59 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:02:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-07 22:02:58 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-02-07 22:02:52 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-02-07 22:02:43 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-07 22:02:11 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 22:02:07 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-02-07 22:01:39 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:01:33 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.030 |  |
| 2026-02-07 22:01:30 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:01:18 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:00:36 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 22:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 22:13:01 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.354 | 🔺 Rising |
| 2026-02-07 22:03:13 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-07 22:28:39 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-07 21:05:46 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-07 22:03:54 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 22:02:11 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 22:00:36 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 22:20:34 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:01:39 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:07:12 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:03:20 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:02:59 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:05:20 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:16:04 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:05:30 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:05:54 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:25:04 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:16:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:04:41 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:03:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:09:53 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:01:30 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-07 21:19:13 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-07 22:04:08 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-07 18:23:08 | Thanthirimale (Malwathu Oya) | 1.85 | 🟢 Normal | -0.007 |  |
| 2026-02-07 22:09:03 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-02-07 22:02:58 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-07 22:02:43 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-07 22:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 21:00:47 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-02-07 22:02:07 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-02-07 22:02:52 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-02-07 21:10:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2026-02-07 22:02:58 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-02-07 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.08 | 🟢 Normal | -0.020 |  |
| 2026-02-07 22:01:33 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.030 |  |
| 2026-02-07 22:15:03 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.038 |  |
| 2026-02-07 22:04:13 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |
| 2026-02-07 22:12:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)