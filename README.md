# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_21:19:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 21:19:08 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-05 21:16:06 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:15:06 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:09:24 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 21:08:40 | Holombuwa (Kelani Ganga) | 2.22 | 🟢 Normal | -0.059 |  |
| 2026-10-05 21:08:00 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-05 21:07:37 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-05 21:07:16 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-05 21:06:40 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-10-05 21:06:20 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-05 21:06:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:06:01 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.357 |  |
| 2026-10-05 21:05:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-05 21:05:28 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-10-05 21:04:59 | Glencourse (Kelani Ganga) | 12.60 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-10-05 21:04:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.053 |  |
| 2026-10-05 21:04:16 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.029 |  |
| 2026-10-05 21:04:02 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-05 21:03:22 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:03:20 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-05 21:03:00 | Thawalama (Gin Ganga) | 2.86 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-05 21:02:54 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.022 |  |
| 2026-10-05 21:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.068 |  |
| 2026-10-05 21:02:34 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-05 21:02:26 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:02:09 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-10-05 21:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.55 | 🟢 Normal | -0.025 |  |
| 2026-10-05 21:01:44 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:01:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-05 21:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:01:34 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-05 21:01:31 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:01:25 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:00:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 21:00:10 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 21:04:59 | Glencourse (Kelani Ganga) | 12.60 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-10-05 20:27:17 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-10-05 21:03:00 | Thawalama (Gin Ganga) | 2.86 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-10-05 21:02:09 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2026-10-05 21:01:34 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-05 21:02:34 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-05 21:07:37 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-05 21:04:02 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-05 21:00:43 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-05 21:06:20 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-05 21:01:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-05 21:08:00 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-05 21:19:08 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-05 21:03:20 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-05 21:09:24 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 21:07:16 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-05 21:02:26 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:16:06 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:15:06 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:01:31 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:00:10 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:06:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:03:22 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:01:25 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-05 20:10:33 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 21:06:40 | Rathnapura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-05 21:05:28 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-10-05 21:02:54 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.022 |  |
| 2026-10-05 21:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.55 | 🟢 Normal | -0.025 |  |
| 2026-10-05 21:04:16 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.029 |  |
| 2026-10-05 21:05:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-05 21:04:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.053 |  |
| 2026-10-05 21:08:40 | Holombuwa (Kelani Ganga) | 2.22 | 🟢 Normal | -0.059 |  |
| 2026-10-05 21:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.068 |  |
| 2026-10-05 21:06:01 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)