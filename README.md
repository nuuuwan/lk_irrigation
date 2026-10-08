# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_19:10:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 19:10:42 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-10-08 19:10:05 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.043 |  |
| 2026-10-08 19:09:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 19:09:23 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.037 |  |
| 2026-10-08 19:06:55 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.085 |  |
| 2026-10-08 19:06:45 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.028 |  |
| 2026-10-08 19:06:27 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-08 19:05:52 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-10-08 19:05:21 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.010 |  |
| 2026-10-08 19:05:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:05:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-08 19:05:07 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.071 |  |
| 2026-10-08 19:04:50 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 19:04:43 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-08 19:04:11 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-10-08 19:03:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.030 |  |
| 2026-10-08 19:03:42 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-08 19:03:17 | Holombuwa (Kelani Ganga) | 4.21 | 🟠 Minor Flood | 1.054 | 🔺 Rising |
| 2026-10-08 19:03:09 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-08 19:03:05 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-08 19:02:58 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:02:57 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:02:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:02:44 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.030 |  |
| 2026-10-08 19:02:29 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.049 |  |
| 2026-10-08 19:02:10 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-08 19:02:05 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:01:39 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:01:29 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:01:15 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 19:03:17 | Holombuwa (Kelani Ganga) | 4.21 | 🟠 Minor Flood | 1.054 | 🔺 Rising |
| 2026-10-08 19:10:42 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-10-08 18:02:44 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-10-08 19:05:52 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-10-08 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-08 19:03:05 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-10-08 19:03:42 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-08 19:06:27 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-08 19:04:43 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-08 19:03:09 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-08 18:02:08 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-08 19:05:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-08 19:04:50 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 18:03:40 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 19:09:24 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:02:57 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:02:05 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:01:29 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:02:58 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:05:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:02:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:01:15 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:01:39 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 19:05:21 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.010 |  |
| 2026-10-08 19:02:10 | Siyambalanduwa (Heda Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-08 18:11:32 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-10-08 18:10:30 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.026 |  |
| 2026-10-08 19:06:45 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.028 |  |
| 2026-10-08 19:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.030 |  |
| 2026-10-08 19:02:44 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.030 |  |
| 2026-10-08 19:09:23 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.037 |  |
| 2026-10-08 19:10:05 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.043 |  |
| 2026-10-08 19:02:29 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.049 |  |
| 2026-10-08 19:04:11 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-10-08 19:05:07 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.071 |  |
| 2026-10-08 19:06:55 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)