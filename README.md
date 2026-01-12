# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_11:08:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 11:08:35 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.055 |  |
| 2026-01-12 11:08:17 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-12 11:07:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:07:29 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-01-12 11:07:01 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.039 |  |
| 2026-01-12 11:06:41 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | 0.729 | 🔺 Rising |
| 2026-01-12 11:05:40 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-01-12 11:05:17 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:04:52 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:04:51 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:04:29 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:04:22 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-01-12 11:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-01-12 11:04:04 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:03:43 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-12 11:03:37 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-01-12 11:03:35 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-01-12 11:03:34 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:03:22 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:03:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.071 |  |
| 2026-01-12 11:02:54 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 11:02:49 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 11:02:41 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.062 |  |
| 2026-01-12 11:02:33 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-12 11:02:25 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:02:24 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-12 11:02:00 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-01-12 11:01:46 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:01:40 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:01:38 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:01:15 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.243 |  |
| 2026-01-12 11:01:11 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:01:03 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-01-12 11:00:48 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.111 |  |
| 2026-01-12 11:00:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-01-12 10:15:41 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.729 | 🔺 Rising |
| 2026-01-12 10:15:37 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 11:06:41 | Yaka Wewa (Ma Oya) | 1.40 | 🟢 Normal | 0.729 | 🔺 Rising |
| 2026-01-12 11:08:17 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-12 11:02:33 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-12 11:03:43 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-12 11:02:54 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 11:02:49 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 11:01:38 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:04:29 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:01:40 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:03:22 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:04:04 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:01:46 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:09:16 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:07:42 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:02:25 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:04:52 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:05:17 | Manampitiya (Mahaweli Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:15:37 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 10:03:14 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:01:11 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:03:34 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 11:07:29 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.009 |  |
| 2026-01-12 11:03:37 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-01-12 11:05:40 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-01-12 11:04:22 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-01-12 11:01:03 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-01-12 11:04:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-01-12 11:02:24 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-12 11:03:35 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-01-12 11:00:33 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-01-12 11:02:00 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-01-12 11:07:01 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.039 |  |
| 2026-01-12 11:08:35 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.055 |  |
| 2026-01-12 11:02:41 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.062 |  |
| 2026-01-12 11:03:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.071 |  |
| 2026-01-12 11:00:48 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.111 |  |
| 2026-01-12 10:08:43 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.148 |  |
| 2026-01-12 11:01:15 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.243 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)