# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_20:25:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 20:25:54 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.007 |  |
| 2026-05-01 20:21:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:18:14 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:15:04 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:12:35 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.008 |  |
| 2026-05-01 20:10:39 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-05-01 20:10:03 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-05-01 20:08:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:08:46 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 20:08:01 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:07:11 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:05:54 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:05:50 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:05:46 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:05:35 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-01 20:05:23 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:05:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:04:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:04:44 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 20:03:42 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:03:24 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-01 20:03:22 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.040 |  |
| 2026-05-01 20:03:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:03:12 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-05-01 20:03:12 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:03:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:02:49 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:02:37 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:02:33 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.030 |  |
| 2026-05-01 20:02:23 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:02:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-05-01 20:01:55 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.053 |  |
| 2026-05-01 20:01:31 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:01:20 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:01:15 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:01:02 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:00:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 20:03:12 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-05-01 20:02:08 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-05-01 20:05:35 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-01 20:08:46 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 20:04:44 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 20:03:24 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-01 20:21:11 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:08:01 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:02:49 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:03:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:07:11 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:03:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:08:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:01:02 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:02:37 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:05:46 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:05:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:18:14 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:01:15 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 20:25:54 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | -0.007 |  |
| 2026-05-01 20:12:35 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.008 |  |
| 2026-05-01 20:10:39 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-05-01 20:03:42 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:01:31 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:04:58 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:02:23 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:15:04 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:05:50 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:01:07 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-01 20:10:03 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-05-01 20:02:33 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.030 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-01 20:03:22 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.040 |  |
| 2026-05-01 20:01:55 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.053 |  |
| 2026-05-01 20:00:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)