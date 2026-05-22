# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_23:17:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 23:17:07 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -6.294 |  |
| 2026-05-22 23:15:08 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:12:31 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.027 |  |
| 2026-05-22 23:09:59 | Rathnapura (Kalu Ganga) | 7.00 | 🟡 Alert | -0.102 |  |
| 2026-05-22 23:07:38 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.040 |  |
| 2026-05-22 23:07:28 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-05-22 23:07:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-05-22 23:06:06 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-05-22 23:06:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:06:06 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | -0.019 |  |
| 2026-05-22 23:06:05 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 23:06:01 | Hanwella (Kelani Ganga) | 7.92 | 🟡 Alert | -0.062 |  |
| 2026-05-22 23:05:53 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.047 |  |
| 2026-05-22 23:05:32 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:05:23 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-22 23:04:25 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:04:21 | Glencourse (Kelani Ganga) | 14.20 | 🟢 Normal | -0.146 |  |
| 2026-05-22 23:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-05-22 23:04:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.003 |  |
| 2026-05-22 23:04:02 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-22 23:03:57 | Ellagawa (Kalu Ganga) | 9.69 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-22 23:03:16 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:03:05 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.042 |  |
| 2026-05-22 23:03:00 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:02:49 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -6.294 |  |
| 2026-05-22 23:02:49 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:02:48 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.096 |  |
| 2026-05-22 23:01:56 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:01:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:01:17 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 23:00:48 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:00:16 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-22 22:35:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-05-22 22:33:34 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 22:29:01 | Dunamale (Aththanagalu Oya) | 5.16 | 🟠 Minor Flood | 0.007 | 🔺 Rising |
| 2026-05-22 23:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-05-22 23:06:06 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | -0.019 |  |
| 2026-05-22 22:07:55 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | -0.030 |  |
| 2026-05-22 23:06:01 | Hanwella (Kelani Ganga) | 7.92 | 🟡 Alert | -0.062 |  |
| 2026-05-22 23:09:59 | Rathnapura (Kalu Ganga) | 7.00 | 🟡 Alert | -0.102 |  |
| 2026-05-22 22:00:54 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 1.017 | 🔺 Rising |
| 2026-05-22 23:03:57 | Ellagawa (Kalu Ganga) | 9.69 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-22 23:05:23 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-22 22:33:34 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-22 23:01:17 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 23:06:05 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 23:04:06 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.003 |  |
| 2026-05-22 23:06:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:00:48 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:15:08 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:01:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:03:16 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:03:00 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:00:16 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:04:25 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:05:32 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:01:56 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 23:07:15 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-05-22 23:04:02 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-22 23:06:06 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-05-22 22:07:48 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-05-22 23:07:28 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-05-22 22:04:45 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-05-22 23:12:31 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.027 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-22 23:07:38 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.040 |  |
| 2026-05-22 23:03:05 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.042 |  |
| 2026-05-22 23:05:53 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | -0.047 |  |
| 2026-05-22 23:02:48 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.096 |  |
| 2026-05-22 23:04:21 | Glencourse (Kelani Ganga) | 14.20 | 🟢 Normal | -0.146 |  |
| 2026-05-22 23:17:07 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -6.294 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)