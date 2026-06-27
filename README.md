# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_10:12:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,664 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 10:12:10 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 10:12:04 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:12:02 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:11:15 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:11:01 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-06-27 10:09:59 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-27 10:09:45 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:09:31 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 10:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:06:18 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:06:14 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 10:05:43 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:04:45 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-06-27 10:04:29 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-27 10:04:17 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-27 10:04:05 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:03:53 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:03:47 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:03:47 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-27 10:03:28 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-06-27 10:03:23 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:03:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-27 10:03:01 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:02:54 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | -0.031 |  |
| 2026-06-27 10:02:41 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:34 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:32 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:30 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:02:28 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:02:24 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:02:13 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:08 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:01:46 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 10:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:01:10 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-06-27 10:00:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:00:14 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 10:03:15 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-06-27 10:03:47 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-06-27 10:04:29 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-27 10:01:46 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-27 10:09:59 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-27 10:06:14 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 10:09:31 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 10:12:10 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 10:02:32 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:00:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:13 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:03:53 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:01:10 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:34 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:12:04 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:05:43 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:09:45 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:41 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:00:14 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:06:18 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:03:47 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 09:09:40 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:03:23 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:04:05 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:11:15 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:02:08 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-06-27 10:11:01 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-06-27 09:01:33 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-06-27 10:04:17 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-27 10:04:45 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-06-27 10:02:24 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:03:01 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:02:28 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:02:30 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-06-27 10:03:28 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.030 |  |
| 2026-06-27 10:02:54 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | -0.031 |  |
| 2026-06-27 10:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)