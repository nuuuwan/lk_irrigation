# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_03:19:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,042 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 03:19:00 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:17:39 | Dunamale (Aththanagalu Oya) | 4.52 | 🟠 Minor Flood | -0.032 |  |
| 2026-05-16 03:17:16 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.026 |  |
| 2026-05-16 03:17:01 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.411 |  |
| 2026-05-16 03:14:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.008 |  |
| 2026-05-16 03:13:14 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.026 |  |
| 2026-05-16 03:11:00 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.018 |  |
| 2026-05-16 03:08:28 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 03:07:37 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:06:59 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.085 |  |
| 2026-05-16 03:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 1.180 | 🔺 Rising |
| 2026-05-16 03:06:07 | Hanwella (Kelani Ganga) | 4.22 | 🟢 Normal | -0.060 |  |
| 2026-05-16 03:06:06 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | -0.018 |  |
| 2026-05-16 03:06:03 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.058 |  |
| 2026-05-16 03:05:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | 1.180 | 🔺 Rising |
| 2026-05-16 03:05:14 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | -0.032 |  |
| 2026-05-16 03:04:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:04:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.068 |  |
| 2026-05-16 03:04:36 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:04:26 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-05-16 03:03:40 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | -0.021 |  |
| 2026-05-16 03:03:15 | Giriulla (Maha Oya) | 2.73 | 🟢 Normal | -0.040 |  |
| 2026-05-16 03:03:13 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:03:09 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:03:07 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:03:07 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:03:01 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:02:47 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.090 |  |
| 2026-05-16 03:02:33 | Moragaswewa (Deduru Oya) | 3.90 | 🟢 Normal | -0.040 |  |
| 2026-05-16 03:02:28 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-05-16 03:02:25 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-05-16 03:02:25 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | -0.411 |  |
| 2026-05-16 03:01:47 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:01:24 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-16 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.185 |  |
| 2026-05-16 03:00:47 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-16 03:00:39 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 03:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | 1.180 | 🔺 Rising |
| 2026-05-16 03:17:39 | Dunamale (Aththanagalu Oya) | 4.52 | 🟠 Minor Flood | -0.032 |  |
| 2026-05-16 03:06:06 | Magura (Kalu Ganga) | 4.00 | 🟡 Alert | -0.018 |  |
| 2026-05-16 03:01:24 | Peradeniya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 03:00:47 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-16 03:00:39 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-16 03:08:28 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:01:47 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:04:57 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 02:02:47 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:19:00 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:14:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.008 |  |
| 2026-05-16 02:08:07 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-05-16 03:03:07 | Ellagawa (Kalu Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:07:37 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:03:09 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:03:13 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:03:07 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:04:36 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-16 03:11:00 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.018 |  |
| 2026-05-16 03:02:28 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-05-16 03:03:40 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | -0.021 |  |
| 2026-05-16 03:04:26 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-05-16 03:13:14 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.026 |  |
| 2026-05-16 03:17:16 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.026 |  |
| 2026-05-16 03:02:25 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-05-16 03:05:14 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | -0.032 |  |
| 2026-05-16 03:02:33 | Moragaswewa (Deduru Oya) | 3.90 | 🟢 Normal | -0.040 |  |
| 2026-05-16 03:03:15 | Giriulla (Maha Oya) | 2.73 | 🟢 Normal | -0.040 |  |
| 2026-05-16 03:06:03 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.058 |  |
| 2026-05-16 03:06:07 | Hanwella (Kelani Ganga) | 4.22 | 🟢 Normal | -0.060 |  |
| 2026-05-16 03:04:44 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.068 |  |
| 2026-05-16 03:06:59 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.085 |  |
| 2026-05-16 03:02:47 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.090 |  |
| 2026-05-16 03:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.185 |  |
| 2026-05-16 03:17:01 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.411 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)