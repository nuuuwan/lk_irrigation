# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--22_03:14:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,917 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 03:14:34 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:13:57 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:13:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-22 03:12:36 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.017 |  |
| 2026-06-22 03:08:04 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:07:05 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.029 |  |
| 2026-06-22 03:05:19 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-06-22 03:05:16 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 03:05:14 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:04:12 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 03:04:09 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:04:08 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:04:06 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:03:53 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.182 |  |
| 2026-06-22 03:03:34 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -32.727 |  |
| 2026-06-22 03:03:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:03:06 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:02:48 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:02:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:02:40 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 03:02:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:02:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:02:12 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-22 03:02:06 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.103 |  |
| 2026-06-22 03:02:03 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:57 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:55 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:01:44 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -32.727 |  |
| 2026-06-22 03:01:31 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:29 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:23 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:16 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-22 02:56:15 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.103 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-22 03:13:37 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-22 03:02:12 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-21 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-22 03:02:40 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-22 01:08:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-22 03:05:16 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 03:04:12 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-22 03:13:57 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:31 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:04:08 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:03:12 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:23 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 18:07:51 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:21:31 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:05:14 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:04:16 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:16 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-22 02:00:27 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:57 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:02:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:14:34 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:01:29 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-22 03:04:09 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.010 |  |
| 2026-06-21 21:01:51 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:02:48 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:01:55 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:08:04 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:03:06 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-06-22 03:12:36 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.017 |  |
| 2026-06-22 02:01:56 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-22 02:02:40 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-06-21 18:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-06-22 03:05:19 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.028 |  |
| 2026-06-22 03:07:05 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.029 |  |
| 2026-06-22 00:32:10 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-06-22 03:02:06 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.103 |  |
| 2026-06-22 03:03:53 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.182 |  |
| 2026-06-22 03:03:34 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -32.727 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)