# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_13:22:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 13:22:02 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:15:18 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-05-18 13:10:15 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.018 |  |
| 2026-05-18 13:09:31 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-05-18 13:09:14 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2026-05-18 13:08:44 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:08:28 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:08:28 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-18 13:07:11 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:06:49 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-05-18 13:06:12 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.028 |  |
| 2026-05-18 13:05:49 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 13:04:39 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:04:32 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-18 13:04:19 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:04:12 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-05-18 13:03:48 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:03:45 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-05-18 13:03:40 | Thanthirimale (Malwathu Oya) | 3.04 | 🟢 Normal | -0.029 |  |
| 2026-05-18 13:03:37 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 13:02:58 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.039 |  |
| 2026-05-18 13:02:45 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:02:43 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | -0.070 |  |
| 2026-05-18 13:02:27 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.060 |  |
| 2026-05-18 13:02:13 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | -0.073 |  |
| 2026-05-18 13:02:11 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:02:02 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:01:54 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:01:47 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:01:47 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-18 13:01:37 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:01:32 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:01:08 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:00:53 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:00:40 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:00:38 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.62 | 🟡 Alert | -0.070 |  |
| 2026-05-18 13:08:28 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-05-18 13:01:47 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-18 13:04:32 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-18 13:05:49 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 13:03:37 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-18 13:00:40 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:01:37 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:02:45 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:01:32 | Galgamuwa (Mee Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:00:53 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:07:11 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:01:08 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-18 09:00:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:08:28 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:02:11 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:01:47 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:03:48 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:04:39 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:22:02 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:08:44 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-18 13:15:18 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-05-18 13:02:43 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:04:19 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:02:02 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:01:54 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-05-18 13:09:31 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-05-18 13:10:15 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.018 |  |
| 2026-05-18 13:03:45 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-05-18 13:06:49 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-05-18 13:06:12 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.028 |  |
| 2026-05-18 13:03:40 | Thanthirimale (Malwathu Oya) | 3.04 | 🟢 Normal | -0.029 |  |
| 2026-05-18 13:09:14 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2026-05-18 13:02:58 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.039 |  |
| 2026-05-18 13:00:38 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.040 |  |
| 2026-05-18 13:04:12 | Hanwella (Kelani Ganga) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-05-18 13:02:27 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.060 |  |
| 2026-05-18 13:02:13 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)