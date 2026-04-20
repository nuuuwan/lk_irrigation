# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_15:15:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,274 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 15:15:02 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 15:14:16 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-04-20 15:11:55 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:09:40 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:09:37 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:07:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 15:06:18 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 15:05:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:05:23 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.050 |  |
| 2026-04-20 15:04:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 15:04:45 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:43 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:35 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:33 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-04-20 15:04:31 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:10 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:03 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:02 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-04-20 15:03:49 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:03:38 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-04-20 15:03:34 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-20 15:03:31 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-20 15:03:30 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:28 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:25 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:24 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.534 | 🔺 Rising |
| 2026-04-20 15:03:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:02:53 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 15:02:34 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.075 |  |
| 2026-04-20 15:02:13 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-20 15:02:00 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.140 |  |
| 2026-04-20 15:01:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:01:51 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:01:36 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:01:33 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:01:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-04-20 15:01:09 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:00:41 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-20 15:00:20 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:55:55 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 14:53:07 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.079 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 15:03:24 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.534 | 🔺 Rising |
| 2026-04-20 15:14:16 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-04-20 15:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-04-20 15:03:34 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-20 15:00:41 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-20 15:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-20 15:03:31 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-20 15:15:02 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 15:02:53 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-20 15:06:18 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 15:07:32 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 15:04:47 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 15:01:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:09:40 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:01:36 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:09:37 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:30 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:01:51 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:11:55 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:31 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:43 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:03:25 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:45 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-20 15:04:33 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-04-20 15:05:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:02:13 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:03:49 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:01:33 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:01:09 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:01:51 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-04-20 15:04:02 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-04-20 15:03:38 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-04-20 15:00:20 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-04-20 14:10:53 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-04-20 15:05:23 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.050 |  |
| 2026-04-20 15:02:34 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.075 |  |
| 2026-04-20 15:02:00 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)