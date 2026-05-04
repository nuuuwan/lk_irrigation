# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_11:12:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,596 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 11:12:07 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.042 |  |
| 2026-05-04 11:10:41 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:09:48 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-05-04 11:08:28 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-04 11:08:05 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.084 |  |
| 2026-05-04 11:07:28 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-04 11:06:37 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.017 |  |
| 2026-05-04 11:06:16 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:06:04 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-04 11:05:59 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-05-04 11:05:31 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.041 |  |
| 2026-05-04 11:05:10 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.048 |  |
| 2026-05-04 11:04:39 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-05-04 11:04:27 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:04:19 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:04:08 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:03:55 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-04 11:03:20 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 11:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-05-04 11:03:16 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:03:16 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-05-04 11:03:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:02:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-04 11:02:19 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:02:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-04 11:01:59 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:54 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.051 |  |
| 2026-05-04 11:01:44 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 11:01:32 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:19 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 11:01:16 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:11 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:06 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.011 |  |
| 2026-05-04 11:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:00:13 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:58:54 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:31:02 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 11:03:16 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-05-04 11:02:48 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-04 11:08:28 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-04 11:01:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 11:01:19 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 11:03:20 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 11:00:13 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:11 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:04:27 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:10:41 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:04:08 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:58:54 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:44 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:06:16 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:03:16 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:03:07 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:04:19 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:02:19 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:32 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:16 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:01:59 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-04 11:09:48 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-05-04 11:02:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-04 11:04:39 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-05-04 11:01:06 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.011 |  |
| 2026-05-04 11:06:37 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.017 |  |
| 2026-05-04 11:03:55 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-05-04 11:06:04 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-04 11:07:28 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-04 11:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.030 |  |
| 2026-05-04 11:05:59 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-05-04 11:05:31 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.041 |  |
| 2026-05-04 11:12:07 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.042 |  |
| 2026-05-04 11:05:10 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.048 |  |
| 2026-05-04 11:01:54 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.051 |  |
| 2026-05-04 11:08:05 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)