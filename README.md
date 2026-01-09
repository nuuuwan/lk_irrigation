# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_20:15:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,183 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 20:15:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:15:17 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:12:07 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:12:00 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-01-09 20:10:26 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-09 20:09:21 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.075 |  |
| 2026-01-09 20:07:50 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-01-09 20:07:19 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 20:07:08 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:06:35 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:05:18 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.029 |  |
| 2026-01-09 20:05:02 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:04:59 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:04:53 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 20:04:25 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:04:23 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-01-09 20:03:47 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:36 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:33 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:30 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 20:03:27 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-09 20:03:23 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.059 |  |
| 2026-01-09 20:02:40 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-09 20:02:33 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:02:21 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 20:02:20 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 20:02:04 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.075 |  |
| 2026-01-09 20:01:58 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:01:51 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:01:43 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:00:43 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.015 |  |
| 2026-01-09 20:00:41 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:00:32 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.044 |  |
| 2026-01-09 20:00:15 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 19:35:03 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 19:27:58 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 20:07:50 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-01-09 20:03:27 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-09 20:00:15 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 20:04:53 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 20:03:30 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 20:07:19 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 20:02:21 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 20:02:20 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 19:20:58 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-09 20:01:43 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:01:36 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:06:35 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:15:17 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:36 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:01:58 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:12:07 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:47 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:00:41 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:23 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:05:02 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:04:59 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:01:51 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:03:33 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:04:25 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:15:25 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:02:33 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-09 20:12:00 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | -0.010 |  |
| 2026-01-09 20:10:26 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-09 20:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-01-09 20:00:43 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.015 |  |
| 2026-01-09 20:02:40 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-09 20:05:18 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.029 |  |
| 2026-01-09 20:00:32 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.044 |  |
| 2026-01-09 20:03:11 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.059 |  |
| 2026-01-09 20:02:04 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.075 |  |
| 2026-01-09 20:09:21 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)