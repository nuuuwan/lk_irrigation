# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_14:19:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 14:19:37 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-06 14:13:15 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:09:44 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:09:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:08:47 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:07:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-04-06 14:06:58 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:42 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:35 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:01 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:01 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-04-06 14:05:59 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:05:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:05:54 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:05:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:05:51 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-06 14:05:04 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-06 14:04:27 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:04:13 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:04:11 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:04:10 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:03:59 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-06 14:03:15 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-04-06 14:03:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-04-06 14:03:07 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:47 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:41 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:37 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-06 14:02:28 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:12 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:01:50 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:01:40 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-06 14:01:37 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.041 |  |
| 2026-04-06 14:01:36 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:01:34 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.337 |  |
| 2026-04-06 14:00:53 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-06 14:00:37 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:00:13 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 14:07:56 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-04-06 14:03:15 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-04-06 14:05:04 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-04-06 14:02:37 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-06 14:19:37 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-06 14:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-06 14:05:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:01:50 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:00:37 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:05:59 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:03:07 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:12 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:01 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:04:13 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:05:54 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:08:47 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:05:51 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:04:27 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:09:00 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:47 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:58 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:42 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:41 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:06:35 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:04:11 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:28 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:09:44 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:03:59 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:13:15 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:01:36 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-04-06 14:05:51 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-04-06 14:01:40 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-06 14:00:53 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-04-06 14:06:01 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-04-06 14:03:14 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-04-06 14:00:13 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | -0.040 |  |
| 2026-04-06 14:01:37 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | -0.041 |  |
| 2026-04-06 14:01:34 | Weraganthota (Mahaweli Ganga) | -2.58 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)