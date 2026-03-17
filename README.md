# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_00:09:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,231 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 00:09:14 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:08:27 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:08:19 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:07:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:06:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:06:04 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-03-18 00:06:03 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 00:04:59 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:04:43 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:04:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-18 00:03:44 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:03:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:03:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-18 00:03:18 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-18 00:03:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-18 00:03:09 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-18 00:02:54 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:02:49 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-18 00:02:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.088 |  |
| 2026-03-18 00:02:35 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.013 |  |
| 2026-03-18 00:02:35 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 00:02:25 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.020 |  |
| 2026-03-18 00:02:15 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:01:59 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:00:44 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-18 00:00:36 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-03-17 23:59:33 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:56:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 20:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-03-18 00:00:44 | Peradeniya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-18 00:04:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-18 00:03:09 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-18 00:03:18 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-18 00:06:03 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-18 00:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 23:01:31 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 00:08:27 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:09:14 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:03:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:03:14 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:00:39 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:04:05 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 22:05:25 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:04:59 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:02:35 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:15:56 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:04:22 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:59:33 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:02:54 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:06:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:01:59 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:07:34 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:02:15 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:04:43 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:01:54 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:01:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:08:19 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-18 00:02:49 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-18 00:03:19 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-18 00:03:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-18 00:02:35 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.013 |  |
| 2026-03-18 00:06:04 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-03-18 00:02:25 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.020 |  |
| 2026-03-18 00:00:36 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-03-17 23:00:51 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.041 |  |
| 2026-03-17 21:02:27 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.045 |  |
| 2026-03-18 00:02:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)