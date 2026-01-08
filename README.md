# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_22:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 22:22:58 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:22:22 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.007 |  |
| 2026-01-08 22:15:56 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-08 22:11:42 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:08:55 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:07:57 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-08 22:07:07 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 22:06:35 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.005 |  |
| 2026-01-08 22:05:57 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:05:45 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.071 |  |
| 2026-01-08 22:04:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.064 |  |
| 2026-01-08 22:04:34 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-08 22:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:31 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:11 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:08 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.152 |  |
| 2026-01-08 22:03:07 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:05 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-08 22:02:54 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.072 |  |
| 2026-01-08 22:02:46 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-08 22:02:44 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:44 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.043 |  |
| 2026-01-08 22:02:34 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:33 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:29 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-01-08 22:02:20 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:07 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:55 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:30 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-08 22:01:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:03 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.034 |  |
| 2026-01-08 22:00:57 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:00:53 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 22:04:34 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-08 22:01:30 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-08 22:07:57 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 22:02:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:11:42 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:44 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:55 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:44 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:00:53 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:05:57 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:22:58 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:08:55 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:20 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:07 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:21 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:33 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:31 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:01:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:02:07 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:03:11 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 22:06:35 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.005 |  |
| 2026-01-08 22:22:22 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.007 |  |
| 2026-01-08 22:15:56 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-08 22:07:07 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 22:02:46 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-08 22:02:29 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-01-08 22:03:05 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-08 22:01:03 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.034 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 22:02:44 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.043 |  |
| 2026-01-08 21:00:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-01-08 22:04:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.064 |  |
| 2026-01-08 22:05:45 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.071 |  |
| 2026-01-08 22:02:54 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.072 |  |
| 2026-01-08 21:03:07 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.078 |  |
| 2026-01-08 22:03:08 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)