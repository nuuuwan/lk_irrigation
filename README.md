# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_05:35:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,733 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 05:35:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.052 |  |
| 2026-05-27 05:15:50 | Rathnapura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.067 |  |
| 2026-05-27 05:13:33 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:12:31 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:12:03 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-27 05:10:19 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-05-27 05:10:01 | Glencourse (Kelani Ganga) | 11.59 | 🟢 Normal | -0.018 |  |
| 2026-05-27 05:09:00 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-27 05:08:50 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:07:45 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:07:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:07:05 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.029 |  |
| 2026-05-27 05:06:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-05-27 05:05:53 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:05:29 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-27 05:05:02 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-05-27 05:04:56 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-27 05:04:21 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.016 |  |
| 2026-05-27 05:04:19 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:03:51 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-27 05:03:50 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-27 05:03:27 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:03:03 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:02:41 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.012 |  |
| 2026-05-27 05:02:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-27 05:02:32 | Hanwella (Kelani Ganga) | 4.21 | 🟢 Normal | -0.060 |  |
| 2026-05-27 05:02:28 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:02:27 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-05-27 05:01:51 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-05-27 05:01:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:01:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:00:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:00:42 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-27 04:48:57 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 04:48:54 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 04:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.012 |  |
| 2026-05-27 05:02:36 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-27 05:12:03 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-27 05:04:56 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-27 05:03:50 | Putupaula (Kalu Ganga) | 2.36 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-27 05:00:42 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-26 18:04:02 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-27 04:27:29 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-27 05:05:53 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:03:03 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:01:46 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:00:42 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:04:19 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:13:33 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:03:27 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:02:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:08:50 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:07:45 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:12:31 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:01:37 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:07:22 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:02:28 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 05:05:29 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-27 05:09:00 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-05-27 05:02:41 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.012 |  |
| 2026-05-27 05:04:21 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.016 |  |
| 2026-05-27 05:10:01 | Glencourse (Kelani Ganga) | 11.59 | 🟢 Normal | -0.018 |  |
| 2026-05-27 05:01:51 | Ellagawa (Kalu Ganga) | 8.61 | 🟢 Normal | -0.020 |  |
| 2026-05-27 05:02:27 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-05-27 05:10:19 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-05-26 18:04:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.020 |  |
| 2026-05-27 05:07:05 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.029 |  |
| 2026-05-27 05:05:02 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-05-27 05:03:51 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-27 05:35:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.052 |  |
| 2026-05-27 05:02:32 | Hanwella (Kelani Ganga) | 4.21 | 🟢 Normal | -0.060 |  |
| 2026-05-27 05:06:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-05-27 05:15:50 | Rathnapura (Kalu Ganga) | 3.60 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)