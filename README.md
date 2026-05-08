# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_04:02:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,730 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 04:02:40 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-09 04:02:35 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-09 04:02:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 04:02:09 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-05-09 04:02:07 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.152 |  |
| 2026-05-09 04:01:58 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.182 |  |
| 2026-05-09 04:01:49 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 04:01:44 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-05-09 04:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.146 |  |
| 2026-05-09 04:01:35 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-09 04:01:19 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.063 |  |
| 2026-05-09 04:01:03 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-09 04:01:01 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.076 |  |
| 2026-05-09 03:18:32 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-09 03:16:18 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -5.806 |  |
| 2026-05-09 03:15:47 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -5.806 |  |
| 2026-05-09 03:12:41 | Panadugama (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.109 |  |
| 2026-05-09 03:09:40 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.038 |  |
| 2026-05-09 03:09:29 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.223 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 03:06:39 | Thanamalwila (Kirindi Oya) | 6.13 | 🔴 Major Flood | -0.257 |  |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-09 03:04:31 | Katharagama (Menik Ganga) | 1.29 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-05-09 03:05:26 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-05-09 03:09:29 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-05-09 03:01:25 | Moragaswewa (Deduru Oya) | 2.65 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-05-09 04:02:35 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-09 04:01:03 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-09 03:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-09 03:05:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-09 04:01:35 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-09 03:02:19 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-09 03:02:08 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:04:40 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-09 03:04:54 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-09 04:01:49 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 03:07:14 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 00:03:06 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-09 04:02:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 03:08:44 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-09 04:02:40 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-09 04:01:44 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-05-09 03:04:37 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.018 |  |
| 2026-05-09 03:09:40 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.038 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-09 04:02:09 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-05-09 04:01:19 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.063 |  |
| 2026-05-09 03:02:59 | Moraketiya (Walawe Ganga) | 2.27 | 🟢 Normal | -0.070 |  |
| 2026-05-09 04:01:01 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.076 |  |
| 2026-05-09 03:08:16 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.092 |  |
| 2026-05-09 03:12:41 | Panadugama (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.109 |  |
| 2026-05-09 04:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.146 |  |
| 2026-05-09 04:02:07 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.152 |  |
| 2026-05-09 04:01:58 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | -0.182 |  |
| 2026-05-09 03:04:43 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.298 |  |
| 2026-05-09 03:04:01 | Kuda Oya (Kirindi Oya) | 5.52 | 🟢 Normal | -0.653 |  |
| 2026-05-09 03:16:18 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -5.806 |  |
| 2026-05-09 02:17:02 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -270.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)