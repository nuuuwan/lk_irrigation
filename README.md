# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_02:28:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 02:28:28 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-12 02:20:03 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.241 |  |
| 2025-12-12 02:16:08 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:14:58 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.017 |  |
| 2025-12-12 02:13:58 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2025-12-12 02:13:57 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2025-12-12 02:13:56 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2025-12-12 02:13:55 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2025-12-12 02:12:23 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-12 02:12:05 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:08:22 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-12 02:07:37 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -18.000 |  |
| 2025-12-12 02:07:35 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -18.000 |  |
| 2025-12-12 02:07:25 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 02:07:01 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:06:57 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.037 |  |
| 2025-12-12 02:05:41 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:05:22 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:05:19 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.129 |  |
| 2025-12-12 02:05:04 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.082 |  |
| 2025-12-12 02:04:48 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-12 02:04:41 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | -0.104 |  |
| 2025-12-12 02:03:02 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 02:02:42 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-12 02:02:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 02:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:02:19 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 02:02:15 | Moragaswewa (Deduru Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:02:02 | Horowpothana (Yan Oya) | 4.31 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-12 02:01:40 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:01:31 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:01:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:01:06 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 01:58:47 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 02:13:56 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | 216.000 | 🔺 Rising |
| 2025-12-12 02:13:58 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2025-12-12 00:04:41 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 02:28:28 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-12 02:02:42 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-12 02:08:22 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-12 02:12:23 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-12 02:04:48 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-12 02:02:02 | Horowpothana (Yan Oya) | 4.31 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-12 01:08:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-12 02:02:21 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-12 02:01:06 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 02:07:25 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 02:02:19 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 02:03:02 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 02:01:40 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:02:15 | Moragaswewa (Deduru Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:01:31 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:12:05 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:05:22 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:16:08 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:05:41 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:07:01 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 02:14:58 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.017 |  |
| 2025-12-12 01:58:47 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.021 |  |
| 2025-12-12 01:04:59 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.029 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-12 02:06:57 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.037 |  |
| 2025-12-12 02:05:04 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.082 |  |
| 2025-12-12 02:04:41 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | -0.104 |  |
| 2025-12-12 02:05:19 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.129 |  |
| 2025-12-12 00:01:45 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -0.205 |  |
| 2025-12-12 02:20:03 | Urawa (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.241 |  |
| 2025-12-12 02:07:37 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)