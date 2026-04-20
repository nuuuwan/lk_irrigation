# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_12:13:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,154 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 12:13:42 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.017 |  |
| 2026-04-20 12:08:41 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-20 12:06:41 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:06:30 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:06:14 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:05:58 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.111 |  |
| 2026-04-20 12:05:04 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:04:52 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-04-20 12:04:46 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-04-20 12:04:43 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 12:04:42 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:04:41 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:04:24 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-20 12:04:10 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:03:54 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-20 12:03:50 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:03:42 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.040 |  |
| 2026-04-20 12:03:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:03:35 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-20 12:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:03:17 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 12:03:03 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-20 12:02:50 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:02:33 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.052 |  |
| 2026-04-20 12:02:22 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.040 |  |
| 2026-04-20 12:02:12 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 12:02:00 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.139 |  |
| 2026-04-20 12:01:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:52 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 12:01:37 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-20 12:01:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:26 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:10 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-04-20 12:01:09 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:00:56 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:00:26 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:00:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-20 11:55:57 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 11:47:57 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 12:00:17 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-20 12:01:37 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-20 12:03:54 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-20 12:04:24 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-20 12:03:17 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 12:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 12:04:43 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 12:02:12 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 12:04:41 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:00:26 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:29 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:04:10 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:02:50 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:03:50 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:26 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:06:30 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:06:14 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:00:56 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:04:42 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:03:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:06:41 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:05:04 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:52 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:01:09 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-04-20 12:04:52 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-04-20 12:03:03 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-20 12:08:41 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-20 12:13:42 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.017 |  |
| 2026-04-20 12:03:35 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-20 12:04:46 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-04-20 12:01:10 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-04-20 12:03:42 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.040 |  |
| 2026-04-20 12:02:22 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.040 |  |
| 2026-04-20 12:02:33 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.052 |  |
| 2026-04-20 12:05:58 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.111 |  |
| 2026-04-20 12:02:00 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)