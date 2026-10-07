# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_21:09:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,696 measurements** from **39** stations.
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
| 2026-10-07 21:09:27 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:08:10 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.045 |  |
| 2026-10-07 21:07:54 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:07:47 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.030 |  |
| 2026-10-07 21:07:07 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-10-07 21:06:21 | Holombuwa (Kelani Ganga) | 2.47 | 🟢 Normal | 1.465 | 🔺 Rising |
| 2026-10-07 21:05:59 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:05:45 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.049 |  |
| 2026-10-07 21:05:41 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-07 21:05:15 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:04:56 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-10-07 21:04:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:04:12 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 1.043 | 🔺 Rising |
| 2026-10-07 21:04:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:03:52 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.040 |  |
| 2026-10-07 21:03:50 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:03:36 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:03:30 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:03:29 | Peradeniya (Mahaweli Ganga) | 3.51 | 🟢 Normal | 0.425 | 🔺 Rising |
| 2026-10-07 21:03:26 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:03:23 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-07 21:03:21 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-07 21:03:04 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:02:52 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:02:49 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 21:02:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-07 21:02:19 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:01:37 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:01:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:01:35 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-10-07 21:01:32 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:01:24 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.044 |  |
| 2026-10-07 21:01:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.031 |  |
| 2026-10-07 21:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.030 |  |
| 2026-10-07 21:00:52 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:00:31 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-07 21:00:15 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-10-07 20:36:35 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 1.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 21:06:21 | Holombuwa (Kelani Ganga) | 2.47 | 🟢 Normal | 1.465 | 🔺 Rising |
| 2026-10-07 21:04:12 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 1.043 | 🔺 Rising |
| 2026-10-07 21:03:29 | Peradeniya (Mahaweli Ganga) | 3.51 | 🟢 Normal | 0.425 | 🔺 Rising |
| 2026-10-07 21:04:56 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-10-07 21:02:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-07 21:05:41 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-07 21:03:23 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-07 21:03:21 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 21:02:49 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 21:01:32 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:04:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:01:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:03:50 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:09:27 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:04:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:03:04 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:00:52 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:02:19 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:05:15 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-07 21:07:54 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:05:59 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:03:26 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:01:37 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:03:30 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-10-07 21:01:35 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-10-07 21:00:15 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.016 |  |
| 2026-10-07 21:07:07 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-10-07 21:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.030 |  |
| 2026-10-07 21:07:47 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.030 |  |
| 2026-10-07 21:00:31 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-07 21:01:09 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.031 |  |
| 2026-10-07 21:03:52 | Ellagawa (Kalu Ganga) | 5.43 | 🟢 Normal | -0.040 |  |
| 2026-10-07 21:01:24 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.044 |  |
| 2026-10-07 21:08:10 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.045 |  |
| 2026-10-07 21:05:45 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)