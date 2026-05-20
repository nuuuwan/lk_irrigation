# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_01:50:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,428 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 01:50:32 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:38:36 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:35:38 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:18:35 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:15:46 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.042 |  |
| 2026-05-21 01:14:12 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-21 01:13:22 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:13:16 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:12:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-05-21 01:10:08 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-21 01:08:59 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:08:41 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-05-21 01:08:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-05-21 01:08:09 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 01:03:05 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-21 01:01:16 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-21 01:10:08 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-21 00:04:11 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 00:04:58 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-21 01:01:11 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.003 |  |
| 2026-05-20 18:01:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:50:32 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:10:55 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:03:59 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-21 00:02:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:18:35 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:01:47 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:01:01 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:02:37 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:05:45 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:08:59 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:00:34 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:04:30 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:03:53 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:35:38 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:13:22 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:38:36 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:13:16 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-21 01:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.003 |  |
| 2026-05-21 01:12:46 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-05-21 01:06:17 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-21 01:08:09 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-05-21 01:08:41 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-05-20 18:01:19 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-05-21 01:14:12 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-05-21 01:08:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-05-20 18:02:19 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | -0.030 |  |
| 2026-05-21 01:06:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-05-21 00:41:27 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-05-21 01:15:46 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.042 |  |
| 2026-05-21 01:01:31 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.080 |  |
| 2026-05-21 01:03:41 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)