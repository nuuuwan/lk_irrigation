# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_07:17:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 07:17:29 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-10-05 07:14:13 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.018 |  |
| 2026-10-05 07:09:11 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-05 07:08:48 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.036 |  |
| 2026-10-05 07:07:29 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-10-05 07:06:48 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.055 |  |
| 2026-10-05 07:06:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:06:17 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 07:06:10 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.181 |  |
| 2026-10-05 07:05:35 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:05:24 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.054 |  |
| 2026-10-05 07:04:59 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.073 |  |
| 2026-10-05 07:04:56 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-10-05 07:04:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-05 07:04:20 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.040 |  |
| 2026-10-05 07:04:10 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-05 07:03:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 07:03:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-10-05 07:03:31 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-05 07:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.29 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-05 07:03:06 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:03:05 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:02:42 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 07:02:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:02:36 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.018 |  |
| 2026-10-05 07:02:33 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.049 |  |
| 2026-10-05 07:02:32 | Glencourse (Kelani Ganga) | 11.77 | 🟢 Normal | -0.160 |  |
| 2026-10-05 07:02:12 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-05 07:02:10 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-05 07:01:59 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.057 |  |
| 2026-10-05 07:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.082 |  |
| 2026-10-05 07:01:00 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:00:52 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.030 |  |
| 2026-10-05 07:00:48 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:00:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.034 |  |
| 2026-10-05 06:57:47 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-10-05 06:51:23 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.057 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 07:04:46 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-05 07:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.29 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-05 07:02:10 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-05 07:03:48 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 07:02:12 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-05 07:02:42 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 07:06:17 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 07:09:11 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-05 07:05:35 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:00:48 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:03:05 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:03:06 | Ellagawa (Kalu Ganga) | 6.23 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:06:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:01:00 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:02:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:07:24 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-05 06:01:17 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-05 07:04:10 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-05 07:07:29 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-10-05 07:14:13 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.018 |  |
| 2026-10-05 07:02:36 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.018 |  |
| 2026-10-05 06:57:47 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-10-05 07:00:52 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.030 |  |
| 2026-10-05 07:04:56 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-10-05 07:00:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.034 |  |
| 2026-10-05 07:08:48 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.036 |  |
| 2026-10-05 07:17:29 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-10-05 07:04:20 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.040 |  |
| 2026-10-05 07:03:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-10-05 07:02:33 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.049 |  |
| 2026-10-05 07:03:31 | Giriulla (Maha Oya) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-05 07:05:24 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.054 |  |
| 2026-10-05 07:06:48 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.055 |  |
| 2026-10-05 07:01:59 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.057 |  |
| 2026-10-05 07:04:59 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.073 |  |
| 2026-10-05 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.082 |  |
| 2026-10-05 07:02:32 | Glencourse (Kelani Ganga) | 11.77 | 🟢 Normal | -0.160 |  |
| 2026-10-05 07:06:10 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)