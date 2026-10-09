# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_10:18:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,071 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 10:18:16 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-10-09 10:16:12 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.016 |  |
| 2026-10-09 10:14:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-10-09 10:14:07 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.070 |  |
| 2026-10-09 10:11:50 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:11:31 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.062 |  |
| 2026-10-09 10:11:27 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-10-09 10:10:04 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.141 |  |
| 2026-10-09 10:08:31 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.039 |  |
| 2026-10-09 10:08:30 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.009 |  |
| 2026-10-09 10:07:46 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | -0.102 |  |
| 2026-10-09 10:07:31 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:07:06 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:07:03 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.239 |  |
| 2026-10-09 10:05:16 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:04:48 | Badalgama (Maha Oya) | 4.57 | 🟢 Normal | -0.140 |  |
| 2026-10-09 10:04:24 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.147 |  |
| 2026-10-09 10:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:03:44 | Giriulla (Maha Oya) | 3.38 | 🟢 Normal | -0.097 |  |
| 2026-10-09 10:03:44 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-09 10:03:38 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:03:38 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.151 |  |
| 2026-10-09 10:03:30 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:03:05 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-09 10:03:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:02:43 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.100 |  |
| 2026-10-09 10:02:35 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:02:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:02:10 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.021 |  |
| 2026-10-09 10:02:04 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-09 10:01:51 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:01:40 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:01:40 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 10:01:11 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.102 |  |
| 2026-10-09 10:01:01 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:00:52 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.023 |  |
| 2026-10-09 10:00:51 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:00:42 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 10:02:04 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-09 10:03:05 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-09 10:01:40 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-09 10:03:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:01:40 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:07:06 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:02:35 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:07:31 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:03:30 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:00:51 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:02:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:11:50 | Thanthirimale (Malwathu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:01:51 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | 0.000 |  |
| 2026-10-09 10:14:23 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-10-09 10:08:30 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | -0.009 |  |
| 2026-10-09 10:11:27 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-10-09 10:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:03:38 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:05:16 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:01:01 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:00:42 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-10-09 10:16:12 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.016 |  |
| 2026-10-09 10:18:16 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-10-09 10:03:44 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-10-09 10:02:10 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.021 |  |
| 2026-10-09 10:00:52 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.023 |  |
| 2026-10-09 10:08:31 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.039 |  |
| 2026-10-09 10:11:31 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.062 |  |
| 2026-10-09 10:14:07 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.070 |  |
| 2026-10-09 10:03:44 | Giriulla (Maha Oya) | 3.38 | 🟢 Normal | -0.097 |  |
| 2026-10-09 10:02:43 | Hanwella (Kelani Ganga) | 3.82 | 🟢 Normal | -0.100 |  |
| 2026-10-09 10:01:11 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.102 |  |
| 2026-10-09 10:07:46 | Moragaswewa (Deduru Oya) | 1.59 | 🟢 Normal | -0.102 |  |
| 2026-10-09 10:04:48 | Badalgama (Maha Oya) | 4.57 | 🟢 Normal | -0.140 |  |
| 2026-10-09 10:10:04 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.141 |  |
| 2026-10-09 10:04:24 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.147 |  |
| 2026-10-09 10:03:38 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.151 |  |
| 2026-10-09 10:07:03 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)