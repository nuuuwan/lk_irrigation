# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_17:06:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 17:06:02 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.131 |  |
| 2026-06-23 17:05:25 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:05:23 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:05:18 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.072 |  |
| 2026-06-23 17:04:34 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:04:27 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.042 |  |
| 2026-06-23 17:04:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:03:58 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.039 |  |
| 2026-06-23 17:03:44 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:03:29 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 17:03:18 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:03:15 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-23 17:03:04 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 17:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-23 17:02:59 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 17:02:43 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-23 17:02:34 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.122 |  |
| 2026-06-23 17:02:33 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.029 |  |
| 2026-06-23 17:02:31 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.042 |  |
| 2026-06-23 17:02:18 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:02:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:02:12 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.051 |  |
| 2026-06-23 17:02:03 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:01:58 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-06-23 17:01:54 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.181 |  |
| 2026-06-23 17:01:50 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:01:16 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:01:03 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.088 |  |
| 2026-06-23 17:00:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:00:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:00:17 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-06-23 16:21:57 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-23 16:15:19 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.072 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 16:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.97 | 🟡 Alert | 0.000 |  |
| 2026-06-23 17:03:58 | Dunamale (Aththanagalu Oya) | 3.96 | 🟡 Alert | -0.039 |  |
| 2026-06-23 17:03:29 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-23 16:01:20 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 17:03:04 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 17:02:59 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 17:01:16 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:01:50 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:04:04 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 16:00:35 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:05:25 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:04:34 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:02:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:00:58 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:03:44 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:02:03 | Putupaula (Kalu Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:00:47 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:03:18 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 16:04:25 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 16:21:57 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:02:18 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 17:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-23 17:01:58 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-06-23 17:03:15 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-23 17:02:43 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-06-23 16:09:40 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.012 |  |
| 2026-06-23 16:12:06 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-06-23 17:00:17 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-06-23 17:02:33 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.029 |  |
| 2026-06-23 16:03:28 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.030 |  |
| 2026-06-23 17:04:27 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.042 |  |
| 2026-06-23 17:02:31 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.042 |  |
| 2026-06-23 17:02:12 | Giriulla (Maha Oya) | 2.20 | 🟢 Normal | -0.051 |  |
| 2026-06-23 17:05:18 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.072 |  |
| 2026-06-23 17:01:03 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.088 |  |
| 2026-06-23 16:08:11 | Rathnapura (Kalu Ganga) | 2.85 | 🟢 Normal | -0.094 |  |
| 2026-06-23 17:02:34 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.122 |  |
| 2026-06-23 17:06:02 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.131 |  |
| 2026-06-23 17:01:54 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)