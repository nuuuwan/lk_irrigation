# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_08:22:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,659 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 08:22:42 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:19:17 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.085 |  |
| 2026-01-29 08:15:09 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:11:21 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:10:16 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:09:49 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.027 |  |
| 2026-01-29 08:09:32 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:08:38 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:06:47 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-01-29 08:06:37 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.027 |  |
| 2026-01-29 08:06:21 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:05:42 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:05:40 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-01-29 08:05:15 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-01-29 08:04:31 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-29 08:03:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-01-29 08:03:30 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-29 08:03:17 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:03:07 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 08:03:02 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:03:01 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 08:02:43 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:02:33 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:02:31 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.033 |  |
| 2026-01-29 08:02:17 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:02:02 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 08:01:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.081 |  |
| 2026-01-29 08:01:38 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:01:34 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.067 |  |
| 2026-01-29 08:01:27 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:01:09 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:00:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:00:50 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:00:50 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 08:00:36 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:00:35 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-01-29 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:00:10 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 08:04:31 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-29 08:03:30 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-29 08:00:50 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 08:02:02 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 08:03:07 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 08:03:01 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 08:00:50 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:06:21 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:00:10 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:05:42 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:11:21 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:01:38 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:02:33 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:02:17 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:03:02 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:15:09 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:01:09 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:09:32 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:02:43 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:06:47 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:10:16 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:00:36 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:22:42 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 08:03:17 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:08:38 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:00:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:01:27 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-29 08:05:40 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-01-29 08:06:37 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.027 |  |
| 2026-01-29 08:09:49 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.027 |  |
| 2026-01-29 08:05:15 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-01-29 08:03:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-01-29 08:00:35 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-01-29 08:02:31 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.033 |  |
| 2026-01-29 08:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2026-01-29 08:01:34 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.067 |  |
| 2026-01-29 08:01:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.081 |  |
| 2026-01-29 08:19:17 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)