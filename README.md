# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_18:17:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 18:17:13 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-05-09 18:14:20 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-09 18:12:50 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:10:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.035 |  |
| 2026-05-09 18:09:42 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-05-09 18:09:20 | Katharagama (Menik Ganga) | 1.81 | 🟢 Normal | -0.106 |  |
| 2026-05-09 18:07:55 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:07:39 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:06:41 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-05-09 18:06:24 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.096 |  |
| 2026-05-09 18:06:21 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:06:08 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:06:00 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.090 |  |
| 2026-05-09 18:05:30 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.075 |  |
| 2026-05-09 18:05:06 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.043 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-09 18:04:01 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-05-09 18:03:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:03:41 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:03:33 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.029 |  |
| 2026-05-09 18:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.067 |  |
| 2026-05-09 18:03:19 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-05-09 18:03:08 | Moragaswewa (Deduru Oya) | 3.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 18:02:57 | Thanamalwila (Kirindi Oya) | 2.24 | 🟢 Normal | -0.029 |  |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-09 18:02:37 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:02:26 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.032 |  |
| 2026-05-09 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | -0.085 |  |
| 2026-05-09 18:02:06 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-05-09 18:01:53 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | -0.041 |  |
| 2026-05-09 18:01:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 18:00:47 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.076 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 18:00:16 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 18:00:10 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 18:06:41 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.398 | 🔺 Rising |
| 2026-05-09 18:02:06 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-09 18:14:20 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-09 18:03:08 | Moragaswewa (Deduru Oya) | 3.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 18:00:10 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-09 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 18:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:03:41 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:07:39 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:02:37 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:12:50 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:01:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:03:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:06:21 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:07:55 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 18:17:13 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-05-09 17:04:17 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-05-09 18:00:16 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 18:03:19 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-05-09 16:01:00 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-05-09 18:03:33 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.029 |  |
| 2026-05-09 18:02:57 | Thanamalwila (Kirindi Oya) | 2.24 | 🟢 Normal | -0.029 |  |
| 2026-05-09 18:09:42 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-05-09 18:02:26 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | -0.032 |  |
| 2026-05-09 18:10:26 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.035 |  |
| 2026-05-09 18:01:53 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | -0.041 |  |
| 2026-05-09 18:05:06 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.043 |  |
| 2026-05-09 18:04:01 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-05-09 18:06:08 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-09 18:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.067 |  |
| 2026-05-09 18:05:30 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.075 |  |
| 2026-05-09 18:00:47 | Kuda Oya (Kirindi Oya) | 2.24 | 🟢 Normal | -0.076 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-09 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | -0.085 |  |
| 2026-05-09 18:06:00 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.090 |  |
| 2026-05-09 18:06:24 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.096 |  |
| 2026-05-09 18:09:20 | Katharagama (Menik Ganga) | 1.81 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)