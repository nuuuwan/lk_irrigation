# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_22:08:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 22:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.091 |  |
| 2026-10-31 22:08:41 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-10-31 22:08:10 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:08:09 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-31 22:07:39 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:07:31 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-31 22:06:18 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:06:08 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 22:05:52 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-31 22:05:37 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:05:26 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:05:25 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.050 |  |
| 2026-10-31 22:04:59 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:04:44 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.020 |  |
| 2026-10-31 22:04:42 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-10-31 22:04:32 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-10-31 22:04:12 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | -0.030 |  |
| 2026-10-31 22:04:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-10-31 22:04:05 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-31 22:04:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:03:36 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:03:32 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:03:23 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.039 |  |
| 2026-10-31 22:03:23 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 22:03:00 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-10-31 22:02:59 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.050 |  |
| 2026-10-31 22:02:55 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 22:02:53 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-10-31 22:02:21 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:02:18 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:01:35 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:26 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:00:49 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 22:00:40 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 22:03:23 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | -0.039 |  |
| 2026-10-31 22:04:32 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-10-31 22:02:55 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-31 22:08:09 | Rathnapura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-31 22:00:49 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-31 21:03:15 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 22:06:08 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-31 22:03:23 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 22:03:36 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:00:40 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:26 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:03:32 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:04:00 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:07:39 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:01:35 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:08:10 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 22:07:31 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-31 22:08:41 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-10-31 22:06:18 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:05:37 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:04:59 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:05:26 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:02:18 | Dunamale (Aththanagalu Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-31 22:02:21 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 22:04:05 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-10-31 22:05:52 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.020 |  |
| 2026-10-31 22:04:42 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-10-31 22:04:44 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-31 22:02:53 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-10-31 22:04:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-10-31 22:04:12 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | -0.030 |  |
| 2026-10-31 22:05:25 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.050 |  |
| 2026-10-31 22:02:59 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.050 |  |
| 2026-10-31 22:03:00 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | -0.051 |  |
| 2026-10-31 22:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)