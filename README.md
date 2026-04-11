# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_02:19:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,640 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 02:19:08 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:19:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.067 |  |
| 2026-04-12 02:16:33 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.008 |  |
| 2026-04-12 02:16:00 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-12 02:14:20 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:11:21 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:09:41 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:07:26 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-12 02:07:08 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-12 02:05:58 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:05:44 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 02:05:26 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:05:22 | Siyambalanduwa (Heda Oya) | 2.30 | 🟢 Normal | 1.747 | 🔺 Rising |
| 2026-04-12 02:04:39 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-04-12 02:04:29 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:04:25 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-04-12 02:04:18 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -1.565 |  |
| 2026-04-12 02:03:53 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.030 |  |
| 2026-04-12 02:03:32 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -1.565 |  |
| 2026-04-12 02:03:27 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-04-12 02:03:02 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:23 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:16 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:06 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.118 |  |
| 2026-04-12 02:01:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 02:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-12 02:01:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:01:13 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 02:00:41 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:57:36 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:51:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.067 |  |
| 2026-04-12 01:36:45 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 02:05:22 | Siyambalanduwa (Heda Oya) | 2.30 | 🟢 Normal | 1.747 | 🔺 Rising |
| 2026-04-12 02:16:00 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-12 02:07:08 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-12 02:05:44 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 02:01:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 02:01:13 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 00:07:06 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-12 02:04:29 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:05:26 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:23 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:11:00 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 18:03:33 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:11:21 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:14:20 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:16 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:01:46 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:03:02 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:19:08 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 00:03:04 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:01:56 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:05:58 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:00:41 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:36:45 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:13:32 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:04:39 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.005 |  |
| 2026-04-12 02:16:33 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.008 |  |
| 2026-04-12 01:13:59 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-12 02:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-12 02:07:26 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-11 23:06:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.022 |  |
| 2026-04-12 02:03:53 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.030 |  |
| 2026-04-12 02:03:27 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-04-12 02:04:25 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-04-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |
| 2026-04-12 02:19:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.067 |  |
| 2026-04-12 02:02:06 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.118 |  |
| 2026-04-12 02:04:18 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -1.565 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)