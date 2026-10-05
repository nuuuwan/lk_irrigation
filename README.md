# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_00:18:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 00:18:02 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.033 |  |
| 2026-10-06 00:16:23 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:11:20 | Magura (Kalu Ganga) | 2.95 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-10-06 00:08:52 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-06 00:08:29 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-06 00:08:27 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-06 00:08:20 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-06 00:07:05 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 00:06:56 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.037 |  |
| 2026-10-06 00:06:56 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.186 |  |
| 2026-10-06 00:06:41 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-06 00:06:38 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-10-06 00:06:30 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-06 00:06:17 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-06 00:06:12 | Peradeniya (Mahaweli Ganga) | 3.87 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-06 00:05:17 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:04:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:04:22 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.335 |  |
| 2026-10-06 00:04:02 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-06 00:03:50 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-10-06 00:03:44 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | -0.196 |  |
| 2026-10-06 00:03:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 00:03:18 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-06 00:03:04 | Glencourse (Kelani Ganga) | 13.13 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-06 00:02:52 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:02:41 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-06 00:02:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:02:04 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:01:49 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:00:55 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:00:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 00:11:20 | Magura (Kalu Ganga) | 2.95 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-10-06 00:06:38 | Hanwella (Kelani Ganga) | 4.03 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-10-06 00:08:52 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-10-06 00:02:41 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-06 00:04:02 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-06 00:08:27 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-06 00:06:30 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-06 00:06:12 | Peradeniya (Mahaweli Ganga) | 3.87 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-06 00:03:04 | Glencourse (Kelani Ganga) | 13.13 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-06 00:06:41 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-06 00:03:28 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-06 00:03:18 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-06 00:07:05 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-06 00:00:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-06 00:08:29 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-06 00:02:52 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:01:49 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:00:55 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:02:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:16:23 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:02:04 | Siyambalanduwa (Heda Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:04:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-06 00:05:17 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 23:04:59 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-10-06 00:06:17 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-05 23:06:30 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-06 00:08:20 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-10-06 00:03:50 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-10-06 00:18:02 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.033 |  |
| 2026-10-06 00:06:56 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.037 |  |
| 2026-10-05 22:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.048 |  |
| 2026-10-05 23:00:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.054 |  |
| 2026-10-05 21:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.068 |  |
| 2026-10-06 00:06:56 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.186 |  |
| 2026-10-06 00:03:44 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | -0.196 |  |
| 2026-10-06 00:04:22 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.335 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)