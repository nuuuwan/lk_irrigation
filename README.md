# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_22:14:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 22:14:19 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:12:58 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-21 22:12:13 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:11:37 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:11:03 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:10:04 | Wellawaya (Kirindi Oya) | 3.31 | 🟢 Normal | 1.725 | 🔺 Rising |
| 2026-02-21 22:08:19 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | 1.037 | 🔺 Rising |
| 2026-02-21 22:08:05 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-02-21 22:07:56 | Thaldena (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.070 |  |
| 2026-02-21 22:07:33 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 22:07:33 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.209 |  |
| 2026-02-21 22:06:51 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:06:37 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | -0.070 |  |
| 2026-02-21 22:06:34 | Urawa (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.894 | 🔺 Rising |
| 2026-02-21 22:06:00 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:05:13 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.094 |  |
| 2026-02-21 22:05:05 | Rathnapura (Kalu Ganga) | 5.15 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-02-21 22:05:04 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-02-21 22:05:03 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 22:03:48 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-21 22:03:44 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | 0.489 | 🔺 Rising |
| 2026-02-21 22:03:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:03:41 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-02-21 22:03:36 | Nakkala (Kumbukkan Oya) | 2.91 | 🟢 Normal | -0.682 |  |
| 2026-02-21 22:03:30 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 22:03:15 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.093 |  |
| 2026-02-21 22:03:10 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-02-21 22:03:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:02:48 | Padiyathalawa (Maduru Oya) | 1.41 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-21 22:02:34 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 22:02:28 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 22:02:28 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:02:22 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-21 22:02:18 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 22:01:59 | Peradeniya (Mahaweli Ganga) | 4.28 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 22:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-21 22:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.115 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 22:10:04 | Wellawaya (Kirindi Oya) | 3.31 | 🟢 Normal | 1.725 | 🔺 Rising |
| 2026-02-21 22:08:19 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | 1.037 | 🔺 Rising |
| 2026-02-21 22:06:34 | Urawa (Nilwala Ganga) | 2.27 | 🟢 Normal | 0.894 | 🔺 Rising |
| 2026-02-21 22:05:05 | Rathnapura (Kalu Ganga) | 5.15 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-02-21 22:03:44 | Holombuwa (Kelani Ganga) | 2.18 | 🟢 Normal | 0.489 | 🔺 Rising |
| 2026-02-21 22:08:05 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | 0.403 | 🔺 Rising |
| 2026-02-21 22:03:41 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-02-21 22:03:10 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-02-21 22:05:04 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-02-21 22:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-02-21 22:02:48 | Padiyathalawa (Maduru Oya) | 1.41 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-21 22:12:58 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-21 22:01:59 | Peradeniya (Mahaweli Ganga) | 4.28 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-21 22:03:48 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-21 22:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-21 22:02:22 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-21 22:05:03 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 22:02:18 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 22:03:30 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 22:02:28 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 22:02:34 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 18:05:22 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 22:07:33 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 22:11:37 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:12:13 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:11:03 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:02:28 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:03:01 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:03:43 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 22:14:19 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-21 18:03:01 | Weraganthota (Mahaweli Ganga) | -1.88 | 🟢 Normal | -0.020 |  |
| 2026-02-21 22:06:37 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | -0.070 |  |
| 2026-02-21 22:07:56 | Thaldena (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.070 |  |
| 2026-02-21 22:03:15 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.093 |  |
| 2026-02-21 22:05:13 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.094 |  |
| 2026-02-21 21:04:33 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.110 |  |
| 2026-02-21 22:07:33 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.209 |  |
| 2026-02-21 22:03:36 | Nakkala (Kumbukkan Oya) | 2.91 | 🟢 Normal | -0.682 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)