# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_16:21:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,075 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 16:21:00 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-07-05 16:12:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.053 |  |
| 2026-07-05 16:11:28 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.097 |  |
| 2026-07-05 16:10:50 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:10:49 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:10:49 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:09:19 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-07-05 16:08:30 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:07:35 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-05 16:06:54 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:06:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:06:25 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:06:25 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.068 |  |
| 2026-07-05 16:06:06 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.018 |  |
| 2026-07-05 16:05:33 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 16:04:40 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:04:36 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-07-05 16:04:05 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:03:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:03:35 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-07-05 16:03:33 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:03:25 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.102 |  |
| 2026-07-05 16:02:55 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:02:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-05 16:02:32 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.078 |  |
| 2026-07-05 16:02:24 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-05 16:02:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:54 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:38 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:07 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:53 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:39 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:37 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 16:00:32 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 15:59:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.024 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 16:03:35 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-07-05 16:07:35 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-05 16:02:24 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-05 16:00:37 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 16:05:33 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 16:01:54 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:11 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:04:05 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:06:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:06:54 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 13:09:15 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:10:49 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:06:25 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:08:30 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:04:40 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:02:55 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:03:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:32 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:03:33 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:38 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:02:15 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:53 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:00:53 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:10:50 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:01:07 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-05 16:02:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-05 16:09:19 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-07-05 16:06:06 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | -0.018 |  |
| 2026-07-05 16:21:00 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-07-05 15:59:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.024 |  |
| 2026-07-05 16:04:36 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-07-05 16:12:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.053 |  |
| 2026-07-05 16:06:25 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.068 |  |
| 2026-07-05 16:02:32 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.078 |  |
| 2026-07-05 16:11:28 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.097 |  |
| 2026-07-05 16:03:25 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)