# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_15:13:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,605 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 15:13:15 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:10:12 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:07:34 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:07:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-01-03 15:06:52 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:06:42 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:06:36 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.028 |  |
| 2026-01-03 15:06:28 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.056 |  |
| 2026-01-03 15:05:27 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:04:27 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:04:16 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-01-03 15:04:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 15:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:04:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 15:03:52 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.030 |  |
| 2026-01-03 15:03:51 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-01-03 15:03:29 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:03:29 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:03:28 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-01-03 15:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:03:20 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-03 15:03:16 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:03:06 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:02:47 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:02:37 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:02:34 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.014 |  |
| 2026-01-03 15:02:33 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.702 |  |
| 2026-01-03 15:02:20 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.049 |  |
| 2026-01-03 15:02:17 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:02:14 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:02:08 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:01:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:01:28 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:01:18 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-01-03 15:01:17 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 15:00:51 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-01-03 15:00:09 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 14:19:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 15:03:20 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-03 15:04:13 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 15:01:17 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 14:04:14 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 15:04:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 15:13:15 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:03:16 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:02:17 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:02:14 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:02:37 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:05:27 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:00:51 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:06:52 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-03 15:04:06 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:02:08 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:03:29 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:06:42 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:00:09 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:01:28 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:04:27 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:03:29 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-01-03 15:03:51 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2026-01-03 15:04:16 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-01-03 15:02:34 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.014 |  |
| 2026-01-03 15:03:28 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-01-03 15:10:12 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:03:06 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:01:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-01-03 14:00:47 | Galgamuwa (Mee Oya) | 2.58 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:02:47 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-01-03 15:06:36 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.028 |  |
| 2026-01-03 15:07:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-01-03 15:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-01-03 15:03:52 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.030 |  |
| 2026-01-03 15:01:18 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-01-03 15:02:20 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.049 |  |
| 2026-01-03 15:06:28 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.056 |  |
| 2026-01-03 15:02:33 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | -0.702 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)