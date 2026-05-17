# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_22:12:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 22:12:17 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:10:37 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:09:37 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:08:00 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 22:06:31 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.040 |  |
| 2026-05-17 22:06:16 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:05:46 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 22:05:40 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.019 |  |
| 2026-05-17 22:05:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:04:52 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.030 |  |
| 2026-05-17 22:04:35 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-05-17 22:04:20 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:04:02 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-17 22:03:42 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.091 |  |
| 2026-05-17 22:03:38 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.061 |  |
| 2026-05-17 22:03:19 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:03:16 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:03:10 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:02:41 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:02:27 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.050 |  |
| 2026-05-17 22:02:20 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.040 |  |
| 2026-05-17 22:02:11 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:02:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:01:54 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:01:48 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:01:43 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:01:36 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:01:28 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-17 22:01:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.202 |  |
| 2026-05-17 22:01:24 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:01:17 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-05-17 22:01:08 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 22:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:31:09 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 21:00:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.48 | 🟡 Alert | -0.064 |  |
| 2026-05-17 22:01:28 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-17 22:05:46 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 22:01:08 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-17 22:08:00 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 22:04:20 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-17 21:02:19 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:03:19 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:03:10 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:02:11 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:05:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:01:48 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:02:10 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:03:16 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:09:37 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:01:54 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:12:17 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-17 22:10:37 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-05-17 21:03:39 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:02:41 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:06:16 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:01:24 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:01:36 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:01:43 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-17 22:05:40 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.019 |  |
| 2026-05-17 22:04:35 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-17 22:01:17 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-17 22:04:02 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-17 22:04:52 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.030 |  |
| 2026-05-17 22:06:31 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.040 |  |
| 2026-05-17 22:02:20 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.040 |  |
| 2026-05-17 22:02:27 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.050 |  |
| 2026-05-17 22:03:38 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.061 |  |
| 2026-05-17 22:03:42 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | -0.091 |  |
| 2026-05-17 22:01:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)