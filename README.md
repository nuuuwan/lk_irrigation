# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_14:12:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 14:12:33 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-05-04 14:10:56 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:08:07 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-04 14:07:37 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:07:34 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-05-04 14:07:06 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 14:06:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-04 14:05:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:05:58 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-05-04 14:05:57 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-05-04 14:05:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:05:37 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-05-04 14:05:01 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-05-04 14:04:52 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:04:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:04:30 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:03:56 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-04 14:03:49 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:03:20 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:03:12 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.079 |  |
| 2026-05-04 14:02:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:02:45 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-04 14:02:36 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:02:36 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:02:23 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-05-04 14:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:02:00 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:01:58 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:44 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-04 14:01:35 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.020 |  |
| 2026-05-04 14:01:33 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:31 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:14 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:00:56 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-05-04 14:00:43 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:00:16 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 14:05:58 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-05-04 14:06:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-05-04 14:02:45 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-05-04 14:01:39 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-04 14:03:56 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-04 14:07:06 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 14:01:14 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:58 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:02:36 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:00:16 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:33 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:10:56 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:31 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:05:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:07:37 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:02:36 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:01:44 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:02:53 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:03:49 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:04:30 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:04:40 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 13:03:49 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:00:43 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:04:52 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:00:56 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 14:05:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:03:20 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:02:00 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-04 14:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-05-04 14:05:01 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-05-04 14:05:57 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-05-04 14:05:37 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-05-04 14:07:34 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-05-04 14:08:07 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-04 14:01:35 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.020 |  |
| 2026-05-04 14:02:23 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-05-04 14:12:33 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-05-04 14:03:12 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)