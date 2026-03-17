# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_02:20:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 02:20:50 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:17:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:14:02 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:13:22 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.073 |  |
| 2026-03-18 02:09:57 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.303 |  |
| 2026-03-18 02:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-18 02:07:58 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.303 |  |
| 2026-03-18 02:07:57 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.303 |  |
| 2026-03-18 02:07:55 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.303 |  |
| 2026-03-18 02:07:45 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-18 02:07:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-03-18 02:07:04 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-03-18 02:05:11 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:05:09 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.073 |  |
| 2026-03-18 02:04:55 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.029 |  |
| 2026-03-18 02:04:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:04:16 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:04:12 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-03-18 02:04:11 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:04:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:03:58 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 02:03:56 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-18 02:03:56 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 2.667 | 🔺 Rising |
| 2026-03-18 02:03:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:03:29 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 2.667 | 🔺 Rising |
| 2026-03-18 02:03:08 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:02:46 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:02:25 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:02:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:02:09 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-03-18 02:01:39 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:01:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:01:25 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.216 |  |
| 2026-03-18 02:01:24 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:01:16 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 02:01:03 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-18 02:00:56 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:00:49 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 02:03:56 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 2.667 | 🔺 Rising |
| 2026-03-18 02:09:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-18 02:03:58 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-18 02:00:49 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-18 02:07:45 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-18 02:01:16 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-18 02:01:03 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-18 02:01:28 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-18 01:02:29 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:04:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:05:11 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:03:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-17 23:00:39 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:04:05 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:04:16 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:01:39 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:14:02 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:20:50 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:03:08 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:02:46 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:00:56 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:02:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:17:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 18:01:54 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:04:11 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:01:24 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-18 02:02:25 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 01:01:29 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-18 02:02:09 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-03-18 00:03:15 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-18 02:04:12 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-03-18 02:07:04 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-03-18 02:03:56 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-18 02:07:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.028 |  |
| 2026-03-18 02:04:55 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.029 |  |
| 2026-03-17 21:02:27 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.045 |  |
| 2026-03-18 02:13:22 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.073 |  |
| 2026-03-18 02:01:25 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.216 |  |
| 2026-03-18 02:09:57 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.303 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)