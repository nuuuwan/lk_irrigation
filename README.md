# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_12:12:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,635 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 12:12:58 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:12:12 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:09:06 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-04 12:07:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:07:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-04 12:06:03 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:05:18 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-05-04 12:05:18 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-04 12:05:08 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.019 |  |
| 2026-05-04 12:05:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-04 12:04:44 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-05-04 12:04:34 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:04:28 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.031 |  |
| 2026-05-04 12:04:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:04:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:04:06 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.069 |  |
| 2026-05-04 12:03:21 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 12:03:21 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:03:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-05-04 12:03:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:03:08 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:02:42 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-04 12:02:35 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:02:34 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.010 |  |
| 2026-05-04 12:02:16 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-05-04 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-05-04 12:02:07 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:57 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:41 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-05-04 12:01:36 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.030 |  |
| 2026-05-04 12:01:33 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.041 |  |
| 2026-05-04 12:01:29 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:00 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:00:53 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:00:44 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-05-04 12:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-04 12:00:37 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.005 |  |
| 2026-05-04 12:00:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 12:09:06 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-05-04 12:07:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-04 12:02:42 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-04 12:03:21 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 12:03:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:02:35 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:07:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:04:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:12:58 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:12:12 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:02:07 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:00 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:03:21 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:04:09 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:03:08 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:04:34 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:00:53 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:29 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:06:03 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:00:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:01:57 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-04 12:00:37 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.005 |  |
| 2026-05-04 12:05:18 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-05-04 12:05:03 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-04 12:02:34 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.010 |  |
| 2026-05-04 12:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-04 12:05:18 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-05-04 12:01:41 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-05-04 12:05:08 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.019 |  |
| 2026-05-04 12:03:18 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-05-04 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-05-04 12:00:44 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-05-04 12:01:36 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.030 |  |
| 2026-05-04 12:04:44 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2026-05-04 12:04:28 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.031 |  |
| 2026-05-04 12:02:16 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2026-05-04 12:01:33 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.041 |  |
| 2026-05-04 12:04:06 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)