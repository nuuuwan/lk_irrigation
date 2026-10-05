# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_16:08:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,710 measurements** from **39** stations.
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
| 2026-10-05 16:08:43 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.018 |  |
| 2026-10-05 16:08:42 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-05 16:08:30 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:07:19 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-10-05 16:07:15 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.089 |  |
| 2026-10-05 16:06:57 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:06:41 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:06:13 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.167 |  |
| 2026-10-05 16:05:05 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.665 | 🔺 Rising |
| 2026-10-05 16:04:45 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 16:04:25 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:04:22 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.071 |  |
| 2026-10-05 16:04:03 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-05 16:03:41 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 16:03:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-10-05 16:03:29 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:03:29 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-05 16:03:24 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.129 |  |
| 2026-10-05 16:03:15 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.049 |  |
| 2026-10-05 16:03:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:03:08 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:02:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:02:35 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-05 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.062 |  |
| 2026-10-05 16:02:16 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-10-05 16:02:10 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-10-05 16:02:04 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-10-05 16:02:03 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:01:50 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:01:43 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:01:42 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-05 16:01:13 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:01:07 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:00:12 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 16:05:05 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.665 | 🔺 Rising |
| 2026-10-05 16:08:42 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-10-05 16:04:03 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-05 16:03:29 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-05 16:04:45 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 15:04:10 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-05 16:03:41 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 16:01:50 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:01:13 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:01:43 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:08:30 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:00:12 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:02:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:06:57 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:01:07 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:04:25 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-05 16:02:03 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 15:06:25 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-05 16:02:04 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-10-05 16:01:42 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-05 16:08:43 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.018 |  |
| 2026-10-05 16:02:10 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-10-05 16:02:35 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-05 16:07:19 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-10-05 16:03:08 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.030 |  |
| 2026-10-05 15:08:28 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:03:29 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:06:41 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:03:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.030 |  |
| 2026-10-05 16:03:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-10-05 15:05:53 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.040 |  |
| 2026-10-05 15:09:22 | Panadugama (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.042 |  |
| 2026-10-05 16:03:15 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.049 |  |
| 2026-10-05 16:02:16 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-10-05 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.062 |  |
| 2026-10-05 16:04:22 | Ellagawa (Kalu Ganga) | 5.84 | 🟢 Normal | -0.071 |  |
| 2026-10-05 16:07:15 | Glencourse (Kelani Ganga) | 10.91 | 🟢 Normal | -0.089 |  |
| 2026-10-05 16:03:24 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.129 |  |
| 2026-10-05 16:06:13 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | -0.167 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)