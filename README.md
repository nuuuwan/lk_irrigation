# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_17:07:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,060 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 17:07:57 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 17:06:47 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 17:06:40 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.045 |  |
| 2026-10-22 17:06:35 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.021 |  |
| 2026-10-22 17:06:35 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-22 17:06:29 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-10-22 17:06:08 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 17:05:29 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 17:05:14 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-22 17:04:46 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-22 17:04:43 | Holombuwa (Kelani Ganga) | 2.26 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-10-22 17:04:21 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-22 17:04:10 | Rathnapura (Kalu Ganga) | 4.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 17:04:06 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-22 17:03:50 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.182 |  |
| 2026-10-22 17:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 17:03:28 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-10-22 17:03:25 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-10-22 17:03:17 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 17:03:16 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 17:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-22 17:02:59 | Galgamuwa (Mee Oya) | 2.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 17:02:25 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-22 17:02:19 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 17:02:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 17:02:04 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 17:02:01 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-10-22 17:01:58 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-22 17:01:43 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-10-22 17:01:34 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-22 17:01:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-22 17:01:00 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-10-22 17:00:56 | Moragaswewa (Deduru Oya) | 4.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-22 16:57:15 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.182 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 17:04:43 | Holombuwa (Kelani Ganga) | 2.26 | 🟢 Normal | 0.564 | 🔺 Rising |
| 2026-10-22 17:01:12 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-10-22 17:06:47 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-22 17:01:34 | Pitabeddara (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-22 17:04:21 | Putupaula (Kalu Ganga) | 1.72 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-22 17:04:06 | Hanwella (Kelani Ganga) | 4.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-22 17:06:35 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-22 17:03:16 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 16:04:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 17:00:56 | Moragaswewa (Deduru Oya) | 4.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-22 16:07:32 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-22 17:02:25 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-22 17:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-22 17:03:31 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-22 17:02:59 | Galgamuwa (Mee Oya) | 2.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 16:07:54 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 17:03:17 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 16:02:04 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 17:06:08 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 17:04:10 | Rathnapura (Kalu Ganga) | 4.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 17:02:04 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 17:05:29 | Thanthirimale (Malwathu Oya) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 17:07:57 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 17:02:19 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 17:04:46 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-22 17:02:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 17:05:14 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-10-22 16:08:41 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-22 16:11:35 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | -0.009 |  |
| 2026-10-22 17:01:58 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-22 17:01:00 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-10-22 17:03:28 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2026-10-22 17:03:25 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-10-22 17:01:43 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-10-22 17:06:35 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.021 |  |
| 2026-10-22 17:06:29 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.028 |  |
| 2026-10-22 17:02:01 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-10-22 17:06:40 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.045 |  |
| 2026-10-22 17:03:50 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)