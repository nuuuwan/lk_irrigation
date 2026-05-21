# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_01:32:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 01:32:15 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-22 01:23:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-22 01:17:22 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:17:04 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:17:00 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:16:29 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:13:16 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 01:13:00 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:10:26 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-22 01:10:19 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | 0.439 | 🔺 Rising |
| 2026-05-22 01:09:48 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-22 01:09:03 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:08:28 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.150 |  |
| 2026-05-22 01:08:11 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.066 |  |
| 2026-05-22 01:07:16 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:05:02 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-05-22 01:04:10 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.005 |  |
| 2026-05-22 01:03:53 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-05-22 01:03:35 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-05-22 01:03:31 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:03:21 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 01:03:11 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:02:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:02:11 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-22 01:01:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:52 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 01:01:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-22 01:01:36 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 01:10:19 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | 0.439 | 🔺 Rising |
| 2026-05-22 00:03:17 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-22 01:10:26 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-05-22 01:23:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-22 01:32:15 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-22 01:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-22 01:03:21 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 01:13:16 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-21 18:16:06 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-22 00:07:37 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:36 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:17:22 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 23:00:58 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 18:03:27 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:02:47 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:07:16 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:17:04 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:01:39 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:03:31 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:28:31 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:02:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:13:00 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:09:03 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:03:11 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:02:36 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-22 00:08:40 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:01:52 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-22 01:04:10 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.005 |  |
| 2026-05-22 01:02:11 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-22 01:01:41 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-05-22 01:05:02 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-05-22 01:03:53 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-05-22 01:09:48 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-05-22 01:03:35 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-05-21 18:01:04 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.040 |  |
| 2026-05-22 01:08:11 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.066 |  |
| 2026-05-22 01:08:28 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)