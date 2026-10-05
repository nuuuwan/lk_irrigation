# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_23:15:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,970 measurements** from **39** stations.
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
| 2026-10-05 23:15:16 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-10-05 23:12:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-10-05 23:12:03 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.267 |  |
| 2026-10-05 23:11:00 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-05 23:10:38 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 23:08:48 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-05 23:07:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:07:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-10-05 23:06:36 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:06:30 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:05:31 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-05 23:04:59 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:04:54 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:04:39 | Glencourse (Kelani Ganga) | 13.09 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-05 23:04:32 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.044 |  |
| 2026-10-05 23:04:22 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-10-05 23:04:19 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-10-05 23:04:05 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 23:04:02 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-05 23:03:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:03:32 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.232 |  |
| 2026-10-05 23:03:26 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 23:02:52 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 23:02:42 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:02:25 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:02:18 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-10-05 23:02:08 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:02:03 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-05 23:01:32 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-05 23:01:27 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:01:03 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:00:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.054 |  |
| 2026-10-05 23:00:45 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-10-05 23:00:15 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 23:15:16 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-10-05 23:02:18 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-10-05 23:05:31 | Thawalama (Gin Ganga) | 3.45 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-05 23:02:03 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-05 23:04:39 | Glencourse (Kelani Ganga) | 13.09 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-05 23:04:02 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-05 23:08:48 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-05 23:01:32 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-05 22:04:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 23:11:00 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-05 23:04:05 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 23:10:38 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-05 23:02:52 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 23:03:26 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 23:02:08 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:01:27 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:03:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:07:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:01:03 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:04:54 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:06:36 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:04:59 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:06:30 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:02:25 | Ellagawa (Kalu Ganga) | 5.49 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:02:42 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:00:45 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-10-05 23:12:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.018 |  |
| 2026-10-05 23:04:19 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.019 |  |
| 2026-10-05 23:07:09 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-10-05 23:04:22 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-10-05 23:04:32 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.044 |  |
| 2026-10-05 22:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.048 |  |
| 2026-10-05 23:00:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.054 |  |
| 2026-10-05 21:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.068 |  |
| 2026-10-05 23:03:32 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.232 |  |
| 2026-10-05 23:12:03 | Holombuwa (Kelani Ganga) | 1.61 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)