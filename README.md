# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_01:51:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 01:51:47 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:50:35 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.028 |  |
| 2026-02-23 01:20:52 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:13:02 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 01:11:42 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:11:42 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.131 |  |
| 2026-02-23 01:08:14 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.087 |  |
| 2026-02-23 01:06:35 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-23 01:06:13 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-02-23 01:06:10 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-23 01:06:08 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:05:14 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.065 |  |
| 2026-02-23 01:05:12 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:05:04 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.049 |  |
| 2026-02-23 01:04:37 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:03:57 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.040 |  |
| 2026-02-23 01:03:31 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:03:17 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:02:52 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.115 |  |
| 2026-02-23 01:02:40 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:02:38 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.069 |  |
| 2026-02-23 01:02:32 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:02:29 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-23 01:02:06 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:01:55 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:01:48 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.049 |  |
| 2026-02-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:01:31 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-02-23 01:01:15 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-23 01:01:09 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-02-23 01:00:53 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:00:38 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-02-23 01:00:20 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 01:01:15 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 00:03:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-23 01:13:02 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 01:11:42 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:02:32 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:01:44 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:00:53 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:20:52 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:02:40 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:01:55 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:08:10 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:03:17 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:04:08 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:51:47 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:04:37 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-23 01:05:12 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.005 |  |
| 2026-02-23 01:06:35 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-23 01:02:29 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-02-23 01:00:20 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-02-23 01:06:10 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-02-23 01:00:38 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.028 |  |
| 2026-02-23 01:50:35 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.028 |  |
| 2026-02-23 01:01:31 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-02-23 00:04:35 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-02-23 01:06:13 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.040 |  |
| 2026-02-23 01:03:57 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.040 |  |
| 2026-02-23 01:05:04 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.049 |  |
| 2026-02-23 01:01:48 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.049 |  |
| 2026-02-23 00:04:00 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.053 |  |
| 2026-02-23 01:05:14 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.065 |  |
| 2026-02-23 01:02:38 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.069 |  |
| 2026-02-23 01:01:09 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-02-23 01:08:14 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.087 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-23 01:02:52 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.115 |  |
| 2026-02-23 01:11:42 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)