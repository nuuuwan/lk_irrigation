# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_06:32:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 06:32:43 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.002 |  |
| 2026-08-13 06:10:28 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.006 |  |
| 2026-08-13 06:07:59 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-13 06:07:48 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:07:29 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.027 |  |
| 2026-08-13 06:07:22 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:07:10 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-08-13 06:06:28 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:05:11 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:04:58 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.085 |  |
| 2026-08-13 06:04:49 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:04:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:04:22 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:04:18 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-13 06:03:37 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.037 |  |
| 2026-08-13 06:03:36 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:03:28 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-13 06:03:15 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.012 |  |
| 2026-08-13 06:03:12 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 06:03:12 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:03:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.012 |  |
| 2026-08-13 06:02:54 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-13 06:02:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.079 |  |
| 2026-08-13 06:02:28 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-08-13 06:02:21 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-08-13 06:02:21 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.082 |  |
| 2026-08-13 06:02:10 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 06:02:09 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.006 |  |
| 2026-08-13 06:02:08 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 06:01:57 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:01:38 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:01:34 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:01:33 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-13 06:01:22 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:01:21 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-08-13 06:01:14 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:00:50 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:00:30 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | -1.197 |  |
| 2026-08-13 05:58:51 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-13 05:53:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -1.197 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 06:04:18 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-13 06:03:28 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-13 06:02:10 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 06:01:33 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-13 06:07:59 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-13 06:03:12 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 06:02:08 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 06:32:43 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.002 |  |
| 2026-08-13 06:01:14 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:04:30 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:01:34 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:00:50 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:04:49 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:03:36 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:00:30 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:04:22 | Glencourse (Kelani Ganga) | 10.29 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:01:38 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:03:12 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:02:54 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:06:28 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:07:48 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:07:22 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:01:22 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 06:02:09 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.006 |  |
| 2026-08-13 06:10:28 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.006 |  |
| 2026-08-13 06:02:28 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.010 |  |
| 2026-08-13 06:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-13 06:07:10 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-08-13 06:03:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.012 |  |
| 2026-08-13 06:03:15 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.012 |  |
| 2026-08-13 06:02:21 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-08-13 06:07:29 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.027 |  |
| 2026-08-13 06:01:21 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-08-13 06:03:37 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.037 |  |
| 2026-08-13 06:02:39 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.079 |  |
| 2026-08-13 06:02:21 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.082 |  |
| 2026-08-13 06:04:58 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.085 |  |
| 2026-08-13 06:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | -1.197 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)