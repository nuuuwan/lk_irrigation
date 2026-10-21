# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_10:08:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,892 measurements** from **39** stations.
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
| 2026-10-21 10:08:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-21 10:07:45 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.073 |  |
| 2026-10-21 10:07:29 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.027 |  |
| 2026-10-21 10:06:59 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:32 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:30 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:22 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:06:08 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-10-21 10:06:02 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:00 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-10-21 10:05:36 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-21 10:05:28 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:05:09 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 10:04:47 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.030 |  |
| 2026-10-21 10:04:43 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-21 10:04:43 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:03:51 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 10:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:03:33 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 10:03:29 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 10:03:07 | Moragaswewa (Deduru Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 10:03:05 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:02:53 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:02:50 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 10:02:49 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-10-21 10:02:34 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:02:33 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.011 |  |
| 2026-10-21 10:02:13 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:01:24 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 10:01:16 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 10:00:36 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.606 | 🔺 Rising |
| 2026-10-21 10:00:36 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:00:23 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | -0.023 |  |
| 2026-10-21 09:59:27 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 10:00:36 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.606 | 🔺 Rising |
| 2026-10-21 10:08:00 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-21 10:05:36 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-21 10:02:50 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-21 10:04:43 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-21 10:03:07 | Moragaswewa (Deduru Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 10:03:33 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 10:03:29 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 10:01:16 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 10:01:24 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 10:05:09 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 10:03:51 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 09:12:37 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 10:02:13 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:03:05 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:32 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:06:57 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:02:53 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:59 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:05:28 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:30 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:02 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:05:30 | Thalgahagoda (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:00:36 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-21 10:06:22 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:02:34 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:04:43 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-21 10:02:33 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.011 |  |
| 2026-10-21 10:06:08 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-10-21 10:06:00 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-10-21 09:03:13 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-10-21 10:00:23 | Panadugama (Nilwala Ganga) | 4.03 | 🟢 Normal | -0.023 |  |
| 2026-10-21 09:03:50 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.025 |  |
| 2026-10-21 10:07:29 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.027 |  |
| 2026-10-21 10:04:47 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.030 |  |
| 2026-10-21 10:02:49 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.040 |  |
| 2026-10-21 10:07:45 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)