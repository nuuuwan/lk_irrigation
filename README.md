# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_13:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,773 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 13:17:01 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:15:07 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:13:13 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 13:11:46 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-01-20 13:10:50 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:09:02 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:08:31 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:07:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:06:40 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-01-20 13:06:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-20 13:06:15 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-20 13:06:08 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:05:22 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-20 13:05:03 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.153 |  |
| 2026-01-20 13:04:38 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.093 |  |
| 2026-01-20 13:04:29 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.029 |  |
| 2026-01-20 13:04:21 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:03:38 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.075 |  |
| 2026-01-20 13:03:23 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:03:16 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 13:03:02 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:03:01 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 13:02:47 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.095 |  |
| 2026-01-20 13:02:47 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-20 13:02:33 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:02:28 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:02:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-20 13:02:23 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-20 13:02:18 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-01-20 13:02:08 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.136 |  |
| 2026-01-20 13:01:54 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:37 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:23 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:05 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:04 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 13:00:31 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 13:02:23 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-20 13:06:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-20 13:02:28 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-20 13:03:16 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 13:13:13 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 13:03:01 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 13:00:43 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 13:04:21 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:00:31 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:37 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:54 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:10:50 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:15:07 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:08:31 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:03:23 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:06:08 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:09:02 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:02:28 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:05 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:03:02 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:17:01 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:07:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:02:47 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:04 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:02:33 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:23 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:11:46 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-01-20 13:06:15 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-20 13:05:22 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-20 13:02:18 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-01-20 13:06:40 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-01-20 13:04:29 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.029 |  |
| 2026-01-20 13:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-20 13:03:38 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.075 |  |
| 2026-01-20 13:04:38 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.093 |  |
| 2026-01-20 13:02:47 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.095 |  |
| 2026-01-20 13:02:08 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.136 |  |
| 2026-01-20 13:05:03 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)