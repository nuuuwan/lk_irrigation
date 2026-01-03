# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_06:10:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,247 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 06:10:01 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 06:08:00 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:07:21 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.005 |  |
| 2026-01-03 06:06:08 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-01-03 06:06:05 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.691 |  |
| 2026-01-03 06:05:54 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -36.000 |  |
| 2026-01-03 06:05:53 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -36.000 |  |
| 2026-01-03 06:05:52 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-01-03 06:05:27 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-01-03 06:05:19 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:05:12 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.038 |  |
| 2026-01-03 06:05:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.088 |  |
| 2026-01-03 06:04:41 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-01-03 06:04:27 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:04:22 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 06:04:11 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:03:59 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:03:35 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.042 |  |
| 2026-01-03 06:03:30 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:03:28 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:03:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-01-03 06:02:54 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-03 06:02:49 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-01-03 06:02:34 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 06:02:24 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.012 |  |
| 2026-01-03 06:02:20 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:02:02 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:02:00 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:01:46 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-01-03 06:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.286 |  |
| 2026-01-03 06:01:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:00:54 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.247 |  |
| 2026-01-03 06:00:41 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-01-03 05:56:03 | Horowpothana (Yan Oya) | 2.46 | 🟢 Normal | -0.247 |  |
| 2026-01-03 05:48:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.286 |  |
| 2026-01-03 05:43:35 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-03 05:42:38 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.691 |  |
| 2026-01-03 05:31:28 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-03 05:18:12 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:13:46 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 05:43:35 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-03 06:02:54 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-03 05:31:28 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-03 06:02:34 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 06:10:01 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 06:04:22 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 06:02:02 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:04:11 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:05:19 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:03:28 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:06:16 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:01:13 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:08:00 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:04:27 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-03 05:07:55 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-01-03 06:07:21 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.005 |  |
| 2026-01-03 06:02:20 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:03:59 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:02:00 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:03:30 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-03 06:06:08 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-01-03 06:02:24 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | -0.012 |  |
| 2026-01-03 06:04:41 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-01-03 06:05:27 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-01-03 06:00:41 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.021 |  |
| 2026-01-03 06:02:49 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-03 06:03:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-01-03 06:05:52 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-01-03 06:01:46 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-01-03 06:05:12 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.038 |  |
| 2026-01-03 06:03:35 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.042 |  |
| 2026-01-03 06:05:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.088 |  |
| 2026-01-03 06:00:54 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.247 |  |
| 2026-01-03 06:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.286 |  |
| 2026-01-03 06:06:05 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.691 |  |
| 2026-01-03 06:05:54 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)