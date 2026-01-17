# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_06:09:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,797 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 06:09:19 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-01-17 06:09:00 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:07:44 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-01-17 06:07:24 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-01-17 06:07:11 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:06:53 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:06:47 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-01-17 06:06:30 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-17 06:05:50 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:05:33 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.052 |  |
| 2026-01-17 06:04:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:24 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:23 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:09 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:03:22 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.111 |  |
| 2026-01-17 06:02:47 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-01-17 06:02:43 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-17 06:02:42 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:39 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 06:02:34 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:27 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:22 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:12 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:59 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:55 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:43 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:38 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:37 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:34 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.064 |  |
| 2026-01-17 06:01:27 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.044 |  |
| 2026-01-17 06:01:13 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.161 |  |
| 2026-01-17 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:00:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.052 |  |
| 2026-01-17 05:41:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.111 |  |
| 2026-01-17 05:17:52 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 05:17:24 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 06:06:30 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-17 06:02:43 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-17 06:02:39 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 05:12:50 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-17 06:04:33 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:03:22 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:22 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:24 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:59 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:12 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-16 18:06:10 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:06:53 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:55 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:42 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:07:11 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 05:02:23 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:09:00 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:09 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:38 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:23 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:43 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:27 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:04:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:02:34 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:01:13 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:05:50 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 06:07:24 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-01-17 06:06:47 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-01-17 06:07:44 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.009 |  |
| 2026-01-17 06:02:47 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-01-16 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-01-17 06:09:19 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.038 |  |
| 2026-01-17 06:01:27 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.044 |  |
| 2026-01-17 06:05:33 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.052 |  |
| 2026-01-17 06:00:09 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.052 |  |
| 2026-01-17 06:01:34 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.064 |  |
| 2026-01-17 06:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.111 |  |
| 2026-01-17 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)