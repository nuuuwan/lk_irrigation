# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_12:14:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 12:14:16 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:11:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:10:01 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:09:30 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.045 |  |
| 2026-02-02 12:08:30 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-02-02 12:08:24 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-02 12:08:10 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:08:07 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.053 |  |
| 2026-02-02 12:08:02 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-02-02 12:07:20 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:06:32 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2026-02-02 12:06:12 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:05:46 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-02-02 12:05:14 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-02-02 12:05:08 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-02-02 12:04:56 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-02-02 12:04:55 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:04:43 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 12:03:50 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.014 |  |
| 2026-02-02 12:03:36 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:03:34 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:03:31 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-02-02 12:03:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:03:07 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-02 12:03:05 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.138 |  |
| 2026-02-02 12:02:53 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.029 |  |
| 2026-02-02 12:02:46 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:02:41 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:02:37 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.116 |  |
| 2026-02-02 12:02:35 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:02:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-02 12:02:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:01:52 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:01:43 | Thanthirimale (Malwathu Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-02-02 12:01:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:01:18 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 12:00:56 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.041 |  |
| 2026-02-02 12:00:52 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:00:08 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 11:34:05 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 12:05:46 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-02-02 12:02:30 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-02-02 12:04:43 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 12:01:18 | Yaka Wewa (Ma Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 12:03:31 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:02:46 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:06:12 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:02:41 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:10:01 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 12:01:52 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:01:41 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:00:08 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:08:10 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:03:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:14:16 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:00:52 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:03:34 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:04:55 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:03:36 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:02:35 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:02:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:11:23 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-02 12:08:02 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-02-02 12:08:30 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-02-02 12:03:07 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-02 12:08:24 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-02 12:03:50 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.014 |  |
| 2026-02-02 12:02:53 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.029 |  |
| 2026-02-02 12:05:08 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-02-02 12:01:43 | Thanthirimale (Malwathu Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-02-02 12:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-02-02 12:06:32 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.039 |  |
| 2026-02-02 12:00:56 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.041 |  |
| 2026-02-02 12:09:30 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.045 |  |
| 2026-02-02 12:05:14 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-02-02 12:08:07 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.053 |  |
| 2026-02-02 12:02:37 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.116 |  |
| 2026-02-02 12:03:05 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)