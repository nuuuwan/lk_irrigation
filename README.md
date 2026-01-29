# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_13:21:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,855 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 13:21:07 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.004 |  |
| 2026-01-29 13:18:57 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:15:46 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:12:59 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:12:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:11:54 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.045 |  |
| 2026-01-29 13:10:20 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:09:34 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:07:43 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:07:13 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-01-29 13:06:08 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.040 |  |
| 2026-01-29 13:05:52 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.128 |  |
| 2026-01-29 13:05:21 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-29 13:04:54 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.041 |  |
| 2026-01-29 13:04:36 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:04:34 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-29 13:04:31 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:04:12 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.029 |  |
| 2026-01-29 13:03:43 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:32 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:04 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:02 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-01-29 13:02:54 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:52 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:52 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 13:02:52 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:43 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:28 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-29 13:02:10 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:06 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:01:07 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:00:59 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 13:00:33 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:00:32 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-01-29 13:00:27 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-29 13:00:20 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.081 |  |
| 2026-01-29 12:33:42 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 13:04:34 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-29 13:05:21 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-29 13:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 13:02:52 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 13:00:27 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-29 13:02:10 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:04:31 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:00:33 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:15:46 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:04 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:43 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:06 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:10:20 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:32 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:54 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:00:59 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:52 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:43 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:12:59 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:09:34 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:07:43 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:18:57 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:01:07 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:04:12 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:12:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:03:02 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:02:52 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 13:21:07 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.004 |  |
| 2026-01-29 13:02:28 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-29 13:07:13 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-01-29 13:00:32 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-01-29 13:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.029 |  |
| 2026-01-29 13:02:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-01-29 13:06:08 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.040 |  |
| 2026-01-29 13:04:54 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.041 |  |
| 2026-01-29 13:11:54 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.045 |  |
| 2026-01-29 13:00:20 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.081 |  |
| 2026-01-29 13:05:52 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)