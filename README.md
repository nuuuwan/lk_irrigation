# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_16:07:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 16:07:44 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-10-20 16:06:26 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:06:21 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-20 16:05:58 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-10-20 16:05:23 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-10-20 16:05:13 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-20 16:05:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:05:04 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:04:41 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-20 16:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.040 |  |
| 2026-10-20 16:04:28 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:04:19 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:04:17 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:04:15 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-10-20 16:04:06 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.041 |  |
| 2026-10-20 16:04:05 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-10-20 16:03:37 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.040 |  |
| 2026-10-20 16:03:16 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.057 |  |
| 2026-10-20 16:02:55 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:02:52 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.022 |  |
| 2026-10-20 16:02:51 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 16:02:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-20 16:02:20 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 16:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:02:15 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.060 |  |
| 2026-10-20 16:02:07 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:02:07 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.041 |  |
| 2026-10-20 16:02:06 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:01:20 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-20 16:01:07 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 16:00:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 15:05:36 | Thalgahagoda (Nilwala Ganga) | 1.64 | 🟡 Alert | -0.010 |  |
| 2026-10-20 16:04:41 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-20 15:02:34 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-20 16:05:13 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-20 16:01:07 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 16:02:51 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-20 16:02:20 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 16:02:06 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:05:04 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:04:17 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:04:19 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:06:26 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:04:28 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:02:55 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 15:08:00 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:05:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:02:07 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 16:07:44 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-10-20 16:05:58 | Pitabeddara (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-10-20 16:04:15 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-10-20 15:04:03 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-10-20 15:04:58 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-20 16:06:21 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-20 16:02:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-20 16:05:23 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-10-20 16:01:20 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-20 15:02:08 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.020 |  |
| 2026-10-20 16:04:05 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.021 |  |
| 2026-10-20 16:02:52 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.022 |  |
| 2026-10-20 16:00:49 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-10-20 15:02:59 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-10-20 16:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.040 |  |
| 2026-10-20 16:03:37 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.040 |  |
| 2026-10-20 16:04:06 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.041 |  |
| 2026-10-20 16:02:07 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.041 |  |
| 2026-10-20 16:03:16 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.057 |  |
| 2026-10-20 16:02:15 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.060 |  |
| 2026-10-20 15:06:48 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)