# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_04:07:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,347 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 04:07:20 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:07:02 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-05-13 04:06:51 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 04:06:25 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 04:05:44 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-05-13 04:05:17 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | -0.087 |  |
| 2026-05-13 04:04:35 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 04:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-13 04:03:54 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-13 04:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:03:33 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2026-05-13 04:03:18 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:02:50 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:02:32 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:02:25 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:02:11 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-13 04:01:59 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 04:01:57 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 04:01:24 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | -0.020 |  |
| 2026-05-13 04:01:21 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:01:02 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.104 |  |
| 2026-05-13 04:01:01 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-13 04:00:35 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 04:00:26 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:00:24 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | -0.144 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 04:07:02 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-05-13 04:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-13 04:06:25 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-13 04:04:35 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-13 03:05:07 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-13 04:01:01 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-13 04:00:35 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-13 04:01:57 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 04:06:51 | Putupaula (Kalu Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 04:01:59 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 04:02:25 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:02:32 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:00:26 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:02:50 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:07:20 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:06:06 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:00:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:03:18 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-13 04:01:21 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:12:08 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.005 |  |
| 2026-05-13 04:03:54 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-13 04:02:11 | Thanamalwila (Kirindi Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-13 03:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-05-13 04:05:44 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | -0.019 |  |
| 2026-05-13 04:01:24 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-13 04:03:33 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.040 |  |
| 2026-05-13 03:10:35 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.057 |  |
| 2026-05-13 03:00:51 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.075 |  |
| 2026-05-13 04:05:17 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | -0.087 |  |
| 2026-05-13 03:05:50 | Katharagama (Menik Ganga) | 1.39 | 🟢 Normal | -0.096 |  |
| 2026-05-13 04:01:02 | Nakkala (Kumbukkan Oya) | 1.60 | 🟢 Normal | -0.104 |  |
| 2026-05-13 03:06:24 | Kithulgala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.110 |  |
| 2026-05-13 03:02:11 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.137 |  |
| 2026-05-13 04:00:24 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | -0.144 |  |
| 2026-05-13 03:05:16 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -1.503 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)