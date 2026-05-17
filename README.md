# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_13:24:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,316 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 13:24:29 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.015 |  |
| 2026-05-17 13:23:39 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.023 |  |
| 2026-05-17 13:21:51 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-17 13:14:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.018 |  |
| 2026-05-17 13:12:56 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:10:20 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:09:04 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:08:57 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.060 |  |
| 2026-05-17 13:07:06 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-17 13:06:43 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-05-17 13:06:24 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.066 |  |
| 2026-05-17 13:05:58 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 13:05:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-17 13:05:08 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:04:33 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-05-17 13:04:28 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.090 |  |
| 2026-05-17 13:04:17 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:04:05 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.030 |  |
| 2026-05-17 13:04:03 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 13:03:57 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:03:54 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:03:44 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 13:03:26 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:03:15 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-05-17 13:03:12 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:03:02 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:02:49 | Galgamuwa (Mee Oya) | 1.80 | 🟢 Normal | -0.022 |  |
| 2026-05-17 13:02:42 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 13:02:22 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.029 |  |
| 2026-05-17 13:02:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:02:06 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-05-17 13:01:57 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 13:01:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:01:50 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:01:22 | Thanthirimale (Malwathu Oya) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:01:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:01:02 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:00:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.011 |  |
| 2026-05-17 12:44:32 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 13:14:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | -0.018 |  |
| 2026-05-17 13:05:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-17 13:07:06 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-17 13:01:57 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 13:02:42 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 13:21:51 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-17 13:03:44 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 13:04:03 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 13:05:58 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 13:03:12 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:01:02 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:01:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:12:56 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:04:17 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:03:02 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:01:20 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:02:09 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:03:57 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:03:26 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:05:08 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:09:04 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-17 13:01:22 | Thanthirimale (Malwathu Oya) | 3.66 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:10:20 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:03:54 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:01:50 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-05-17 13:00:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.011 |  |
| 2026-05-17 13:24:29 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.015 |  |
| 2026-05-17 13:06:43 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-05-17 13:04:33 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-05-17 13:02:49 | Galgamuwa (Mee Oya) | 1.80 | 🟢 Normal | -0.022 |  |
| 2026-05-17 13:23:39 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.023 |  |
| 2026-05-17 13:02:22 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.029 |  |
| 2026-05-17 13:04:05 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.030 |  |
| 2026-05-17 13:03:15 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-05-17 13:02:06 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-05-17 13:08:57 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.060 |  |
| 2026-05-17 13:06:24 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.066 |  |
| 2026-05-17 13:04:28 | Rathnapura (Kalu Ganga) | 2.99 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)