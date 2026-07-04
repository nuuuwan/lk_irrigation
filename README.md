# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--04_23:36:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 23:36:55 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:23:33 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:19:13 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:12:11 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-07-04 23:11:43 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | 37.500 | 🔺 Rising |
| 2026-07-04 23:10:07 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 37.500 | 🔺 Rising |
| 2026-07-04 23:09:49 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:08:27 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:08:20 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:08:00 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:07:42 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 23:07:18 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-04 23:07:16 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-04 23:07:14 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-07-04 23:06:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:05:26 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.048 |  |
| 2026-07-04 23:05:13 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-07-04 23:04:33 | Holombuwa (Kelani Ganga) | 1.52 | 🟢 Normal | -0.042 |  |
| 2026-07-04 23:04:25 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-07-04 23:04:06 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:04:00 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.097 |  |
| 2026-07-04 23:03:39 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:03:02 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:02:16 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-04 23:02:11 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:02:08 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-04 23:01:58 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:41 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 23:01:33 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.063 |  |
| 2026-07-04 23:01:11 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:00:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 23:00:30 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:00:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:00:11 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-04 23:11:43 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | 37.500 | 🔺 Rising |
| 2026-07-04 23:04:25 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-07-04 23:02:08 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-07-04 23:07:16 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-04 23:05:13 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-07-04 23:02:16 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-04 23:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 23:00:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-04 23:07:42 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 22:14:56 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-04 23:08:27 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:00:15 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:06 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:33 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:04:06 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:19:13 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:00:30 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:23:33 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:08:20 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:08:00 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:03:02 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:00:11 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:09:49 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:06:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:58 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:02:11 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:01:11 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:36:55 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-04 23:07:18 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-07-04 23:12:11 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-07-04 23:04:33 | Holombuwa (Kelani Ganga) | 1.52 | 🟢 Normal | -0.042 |  |
| 2026-07-04 23:05:26 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.048 |  |
| 2026-07-04 23:07:14 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.050 |  |
| 2026-07-04 23:01:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.063 |  |
| 2026-07-04 22:12:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.092 |  |
| 2026-07-04 23:04:00 | Deraniyagala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)