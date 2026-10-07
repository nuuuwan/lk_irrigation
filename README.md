# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_08:31:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,196 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 08:31:03 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.014 |  |
| 2026-10-07 08:21:31 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-10-07 08:19:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-10-07 08:16:47 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.044 |  |
| 2026-10-07 08:10:55 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 08:09:08 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-07 08:08:42 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:07:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:07:08 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 08:06:50 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-07 08:06:37 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-10-07 08:05:45 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:04:48 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.088 |  |
| 2026-10-07 08:04:46 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:04:41 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-07 08:04:38 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.051 |  |
| 2026-10-07 08:04:25 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | -0.040 |  |
| 2026-10-07 08:04:21 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-10-07 08:04:03 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:03:50 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:03:43 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-07 08:03:41 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:03:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:03:03 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-07 08:02:50 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:02:31 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:02:16 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-07 08:02:08 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:52 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-07 08:01:39 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.317 |  |
| 2026-10-07 08:01:36 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:24 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:18 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-10-07 08:01:17 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:16 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:00:59 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:00:54 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:00:25 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 08:19:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-10-07 08:01:52 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-07 08:02:16 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-07 08:09:08 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-07 08:04:41 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-07 08:03:43 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-07 08:06:50 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-07 08:07:08 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-07 08:10:55 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 08:03:17 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:02:50 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:25 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:00:59 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:07:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:36 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:05:45 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:00:54 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:04:46 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:16 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:01:24 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:02:08 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-07 08:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:08:42 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:04:03 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:02:31 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:03:50 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:03:41 | Hanwella (Kelani Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-07 08:31:03 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.014 |  |
| 2026-10-07 08:04:21 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-10-07 08:03:03 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-07 08:06:37 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-10-07 08:01:18 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-10-07 08:21:31 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-10-07 08:00:25 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.034 |  |
| 2026-10-07 08:04:25 | Thawalama (Gin Ganga) | 2.72 | 🟢 Normal | -0.040 |  |
| 2026-10-07 08:16:47 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.044 |  |
| 2026-10-07 08:04:38 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.051 |  |
| 2026-10-07 08:04:48 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.088 |  |
| 2026-10-07 08:01:39 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.317 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)