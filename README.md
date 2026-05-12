# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_03:12:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,322 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 03:12:08 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.005 |  |
| 2026-05-13 03:11:37 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-13 03:10:35 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.057 |  |
| 2026-05-13 03:10:21 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:09:28 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-05-13 03:09:11 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:09:11 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-05-13 03:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-13 03:07:55 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 03:06:37 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:06:30 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:06:24 | Kithulgala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.110 |  |
| 2026-05-13 03:06:06 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:05:50 | Katharagama (Menik Ganga) | 1.39 | 🟢 Normal | -0.096 |  |
| 2026-05-13 03:05:50 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:05:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2026-05-13 03:05:16 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -1.503 |  |
| 2026-05-13 03:05:07 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-13 03:04:42 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 03:03:54 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-05-13 03:03:37 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-13 03:03:15 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -54.000 |  |
| 2026-05-13 03:03:13 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-05-13 03:03:13 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -54.000 |  |
| 2026-05-13 03:03:06 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-13 03:02:53 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.062 |  |
| 2026-05-13 03:02:32 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:02:20 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-13 03:02:19 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-05-13 03:02:13 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | -0.173 |  |
| 2026-05-13 03:02:11 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.137 |  |
| 2026-05-13 03:02:02 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-13 03:01:54 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.065 |  |
| 2026-05-13 03:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-05-13 03:00:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:00:51 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.075 |  |
| 2026-05-13 02:56:53 | Magura (Kalu Ganga) | 2.91 | 🟢 Normal | -1.503 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 03:09:11 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-05-13 03:03:37 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-13 03:02:02 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-13 03:08:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.64 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-13 03:05:07 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-13 03:04:42 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-13 03:07:55 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-13 03:11:37 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 03:06:37 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:10:21 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:06:06 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:00:55 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:02:32 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:05:50 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:09:11 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:06:30 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-05-13 03:12:08 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.005 |  |
| 2026-05-13 03:03:13 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-05-13 03:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-05-13 03:09:28 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-05-13 03:03:54 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2026-05-13 03:02:19 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-05-13 03:03:06 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-13 03:02:20 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-13 02:01:31 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.050 |  |
| 2026-05-13 03:10:35 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.057 |  |
| 2026-05-13 03:02:53 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | -0.062 |  |
| 2026-05-13 03:01:54 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.065 |  |
| 2026-05-13 03:00:51 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.075 |  |
| 2026-05-13 03:05:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.088 |  |
| 2026-05-13 03:05:50 | Katharagama (Menik Ganga) | 1.39 | 🟢 Normal | -0.096 |  |
| 2026-05-13 03:06:24 | Kithulgala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.110 |  |
| 2026-05-13 03:02:11 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.137 |  |
| 2026-05-13 03:02:13 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | -0.173 |  |
| 2026-05-13 03:05:16 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -1.503 |  |
| 2026-05-13 03:03:15 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)