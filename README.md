# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_10:11:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,989 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 10:11:31 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-10-20 10:09:46 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.044 |  |
| 2026-10-20 10:09:44 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:08:23 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-20 10:07:22 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:07:21 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-20 10:07:19 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:06:10 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:06:09 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-10-20 10:05:44 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-10-20 10:05:34 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:05:31 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:05:29 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:05:16 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.048 |  |
| 2026-10-20 10:04:53 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-20 10:04:29 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:04:11 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:04:06 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-10-20 10:03:49 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:03:47 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:03:47 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 10:03:46 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-10-20 10:03:34 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.039 |  |
| 2026-10-20 10:03:27 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:03:25 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:03:04 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:03:01 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.040 |  |
| 2026-10-20 10:02:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:02:41 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.040 |  |
| 2026-10-20 10:02:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:02:10 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-10-20 10:02:03 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.063 |  |
| 2026-10-20 10:01:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-20 10:01:43 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | -0.050 |  |
| 2026-10-20 10:01:18 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 10:00:15 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-20 10:00:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:00:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 10:08:23 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-20 10:07:21 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-20 10:00:15 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-20 10:01:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-20 10:01:18 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 10:03:47 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 10:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:03:04 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:06:10 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:00:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:04:29 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:00:09 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:05:29 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:02:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:02:18 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:04:11 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:05:31 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:03:49 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:07:22 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:09:44 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:03:47 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 10:11:31 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-10-20 10:05:44 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-10-20 10:05:34 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:03:27 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:07:19 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:03:25 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.010 |  |
| 2026-10-20 10:06:09 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-10-20 10:03:46 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-10-20 10:02:10 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-10-20 10:04:06 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.021 |  |
| 2026-10-20 10:03:34 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | -0.039 |  |
| 2026-10-20 10:02:41 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.040 |  |
| 2026-10-20 10:03:01 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.040 |  |
| 2026-10-20 10:09:46 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.044 |  |
| 2026-10-20 10:05:16 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | -0.048 |  |
| 2026-10-20 10:01:43 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | -0.050 |  |
| 2026-10-20 10:02:03 | Glencourse (Kelani Ganga) | 10.94 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)