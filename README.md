# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_22:07:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,968 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 22:07:20 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-05-31 22:07:14 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-31 22:07:07 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:06:58 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:06:39 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-05-31 22:06:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 22:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | -0.028 |  |
| 2026-05-31 22:06:11 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 22:05:22 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:04:55 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:04:44 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:04:36 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.065 |  |
| 2026-05-31 22:04:21 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:03:40 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:03:28 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.034 |  |
| 2026-05-31 22:03:15 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 22:03:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:03:13 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.030 |  |
| 2026-05-31 22:02:59 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-31 22:02:52 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-05-31 22:02:22 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:22 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-05-31 22:02:12 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:11 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:09 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:01:38 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-31 22:01:29 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:01:19 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-31 22:01:14 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:01:08 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 22:02:59 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-31 22:01:19 | Glencourse (Kelani Ganga) | 9.97 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-31 22:01:38 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-31 22:03:15 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 22:06:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 22:02:11 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:01:08 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:01:59 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:06:58 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:03:13 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:04:44 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:01:29 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:07 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:12 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:09 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:01:14 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:04:55 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:06:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:07:07 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:05:22 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:03:40 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:02:22 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:04:21 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:07:20 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-05-31 22:06:39 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-05-31 22:07:14 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-31 22:06:11 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-05-31 22:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | -0.028 |  |
| 2026-05-31 21:05:20 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.030 |  |
| 2026-05-31 22:02:22 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-05-31 22:02:52 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-05-31 20:52:07 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-31 22:03:13 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.030 |  |
| 2026-05-31 22:03:28 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.034 |  |
| 2026-05-31 22:04:36 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)