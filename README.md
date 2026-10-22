# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_16:08:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,022 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 16:08:41 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-22 16:08:22 | Holombuwa (Kelani Ganga) | 1.73 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-10-22 16:08:18 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.038 |  |
| 2026-10-22 16:07:54 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 16:07:32 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-22 16:07:29 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 16:06:28 | Galgamuwa (Mee Oya) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 16:06:18 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 16:06:14 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-22 16:06:08 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 16:06:02 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-10-22 16:05:33 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 16:05:01 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.021 |  |
| 2026-10-22 16:04:43 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 16:04:38 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-22 16:04:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 16:04:17 | Hanwella (Kelani Ganga) | 4.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 16:04:02 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 16:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-22 16:03:11 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-22 16:02:53 | Rathnapura (Kalu Ganga) | 4.14 | 🟢 Normal | -0.030 |  |
| 2026-10-22 16:02:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 16:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 16:02:27 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-22 16:02:10 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-22 16:02:04 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 16:01:40 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-10-22 16:01:26 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 16:01:26 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-10-22 16:01:25 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -72.000 |  |
| 2026-10-22 16:01:24 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -72.000 |  |
| 2026-10-22 16:01:23 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -72.000 |  |
| 2026-10-22 16:01:19 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-10-22 16:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 16:01:02 | Moragaswewa (Deduru Oya) | 4.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-22 16:00:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 16:08:22 | Holombuwa (Kelani Ganga) | 1.73 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-10-22 14:20:02 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-10-22 16:06:14 | Glencourse (Kelani Ganga) | 12.43 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-22 16:02:10 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-22 15:04:41 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-22 16:04:38 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-22 16:04:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-22 16:01:02 | Moragaswewa (Deduru Oya) | 4.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-22 16:07:32 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-22 16:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.61 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-22 16:04:02 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-22 16:07:29 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-22 16:07:54 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 16:02:04 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 16:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 16:04:17 | Hanwella (Kelani Ganga) | 4.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 16:02:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 16:06:28 | Galgamuwa (Mee Oya) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-22 16:01:26 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-22 16:06:18 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 16:04:43 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 16:06:08 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 16:05:33 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-22 16:02:42 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 16:08:41 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-22 15:00:59 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-22 16:03:11 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-22 16:02:27 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-22 16:06:02 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.019 |  |
| 2026-10-22 16:01:19 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-10-22 16:01:26 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-10-22 16:01:40 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-10-22 16:05:01 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.021 |  |
| 2026-10-22 15:01:53 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.029 |  |
| 2026-10-22 16:02:53 | Rathnapura (Kalu Ganga) | 4.14 | 🟢 Normal | -0.030 |  |
| 2026-10-22 16:08:18 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.038 |  |
| 2026-10-22 15:07:06 | Horowpothana (Yan Oya) | 3.06 | 🟢 Normal | -0.051 |  |
| 2026-10-22 16:00:56 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.066 |  |
| 2026-10-22 16:01:25 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)