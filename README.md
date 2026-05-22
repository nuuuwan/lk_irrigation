# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_21:19:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 21:19:03 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:17:18 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.030 |  |
| 2026-05-22 21:10:34 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:09:55 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-22 21:08:18 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:08:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:08:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:08:13 | Hanwella (Kelani Ganga) | 8.03 | 🟠 Minor Flood | -0.037 |  |
| 2026-05-22 21:07:48 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:07:40 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-22 21:07:38 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.028 |  |
| 2026-05-22 21:07:28 | Nagalagam Street (Kelani Ganga) | 1.46 | 🟡 Alert | -0.031 |  |
| 2026-05-22 21:05:48 | Magura (Kalu Ganga) | 4.29 | 🟡 Alert | -0.029 |  |
| 2026-05-22 21:05:24 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:05:04 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-05-22 21:04:28 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-22 21:04:08 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-22 21:04:07 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.080 |  |
| 2026-05-22 21:03:51 | Rathnapura (Kalu Ganga) | 7.21 | 🟡 Alert | -0.098 |  |
| 2026-05-22 21:03:48 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:03:46 | Glencourse (Kelani Ganga) | 14.51 | 🟢 Normal | -0.298 |  |
| 2026-05-22 21:03:20 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:03:12 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.060 |  |
| 2026-05-22 21:03:06 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-05-22 21:03:02 | Ellagawa (Kalu Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 21:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-05-22 21:02:42 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:02:36 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.022 |  |
| 2026-05-22 21:02:15 | Dunamale (Aththanagalu Oya) | 5.15 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-22 21:01:55 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-22 21:01:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:01:53 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:01:50 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:01:48 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:01:43 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.033 |  |
| 2026-05-22 21:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-22 21:01:05 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 21:02:15 | Dunamale (Aththanagalu Oya) | 5.15 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-22 21:08:13 | Hanwella (Kelani Ganga) | 8.03 | 🟠 Minor Flood | -0.037 |  |
| 2026-05-22 21:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-05-22 21:05:48 | Magura (Kalu Ganga) | 4.29 | 🟡 Alert | -0.029 |  |
| 2026-05-22 21:07:28 | Nagalagam Street (Kelani Ganga) | 1.46 | 🟡 Alert | -0.031 |  |
| 2026-05-22 21:03:51 | Rathnapura (Kalu Ganga) | 7.21 | 🟡 Alert | -0.098 |  |
| 2026-05-22 21:04:28 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-22 21:07:40 | Thawalama (Gin Ganga) | 2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-22 21:01:05 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 21:09:55 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-22 21:03:02 | Ellagawa (Kalu Ganga) | 9.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 21:08:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:02:42 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:10:34 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:01:48 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:01:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:08:18 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:05:24 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:19:03 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:01:53 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:03:20 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:08:14 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:03:48 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 21:05:04 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-05-22 21:01:55 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-22 21:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-22 20:05:10 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-22 21:04:08 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-05-22 21:03:06 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-05-22 21:02:36 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.022 |  |
| 2026-05-22 21:07:38 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.028 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-22 21:17:18 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.030 |  |
| 2026-05-22 21:01:43 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.033 |  |
| 2026-05-22 21:03:12 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.060 |  |
| 2026-05-22 21:04:07 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.080 |  |
| 2026-05-22 21:03:46 | Glencourse (Kelani Ganga) | 14.51 | 🟢 Normal | -0.298 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)