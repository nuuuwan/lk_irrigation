# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_11:11:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,471 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 11:11:22 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:09:29 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:08:19 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:08:13 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:06:44 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-05-05 11:06:36 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:05:57 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:05:34 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 11:05:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:04:56 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 11:04:46 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.110 |  |
| 2026-05-05 11:04:42 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-05-05 11:04:21 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:04:06 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-05 11:04:00 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.054 |  |
| 2026-05-05 11:03:44 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-05 11:03:33 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-05 11:03:30 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:03:26 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:03:12 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:03:09 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-05-05 11:03:04 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:02:50 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:02:41 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.012 |  |
| 2026-05-05 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-05 11:02:18 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.039 |  |
| 2026-05-05 11:02:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:02:05 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-05-05 11:01:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:01:58 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-05 11:01:32 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 11:01:18 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-05-05 11:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:01:10 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:01:09 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:59 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:53 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:46 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:26 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:00:15 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 11:01:58 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-05 11:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-05 11:03:44 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-05 11:03:33 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-05 11:04:06 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-05 11:01:32 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 11:04:56 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 11:05:34 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 11:02:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:03:04 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:11:22 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:03:26 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:02:50 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:03:30 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:15 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:04:21 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:05:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:08:13 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:01:58 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:06:36 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:53 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:59 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:08:19 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:09:29 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:00:46 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:03:12 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-05 11:01:10 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:05:57 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:00:26 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-05 11:02:41 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.012 |  |
| 2026-05-05 11:06:44 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-05-05 11:01:18 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-05-05 11:04:42 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-05-05 11:02:18 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.039 |  |
| 2026-05-05 11:03:09 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | -0.040 |  |
| 2026-05-05 11:02:05 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-05-05 11:04:00 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.054 |  |
| 2026-05-05 11:04:46 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)