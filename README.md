# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_05:07:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,445 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 05:07:32 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-13 05:06:45 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.076 |  |
| 2026-10-13 05:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.015 |  |
| 2026-10-13 05:05:38 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 05:05:13 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-10-13 05:05:11 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-10-13 05:04:25 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-13 05:03:52 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-10-13 05:03:12 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-13 05:03:04 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 05:02:51 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.065 |  |
| 2026-10-13 05:02:39 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-13 05:02:37 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 05:02:28 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.020 |  |
| 2026-10-13 05:02:21 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -10.080 |  |
| 2026-10-13 05:02:19 | Rathnapura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.037 |  |
| 2026-10-13 05:02:07 | Pitabeddara (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.344 |  |
| 2026-10-13 05:02:07 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.050 |  |
| 2026-10-13 05:01:59 | Ellagawa (Kalu Ganga) | 7.03 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-13 05:01:56 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -10.080 |  |
| 2026-10-13 05:01:47 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.006 |  |
| 2026-10-13 05:01:47 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.036 |  |
| 2026-10-13 05:01:36 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 05:01:22 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-13 05:01:18 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-13 05:01:15 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 05:00:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-10-13 05:00:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.024 |  |
| 2026-10-13 04:44:29 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.065 |  |
| 2026-10-13 04:28:35 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 04:03:23 | Panadugama (Nilwala Ganga) | 6.27 | 🟠 Minor Flood | 0.122 | 🔺 Rising |
| 2026-10-13 05:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.015 |  |
| 2026-10-13 05:05:13 | Putupaula (Kalu Ganga) | 1.87 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-10-13 05:03:12 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-10-12 23:05:57 | Thawalama (Gin Ganga) | 3.39 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-13 05:01:59 | Ellagawa (Kalu Ganga) | 7.03 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-13 05:01:36 | Thalgahagoda (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-13 04:00:52 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-13 05:07:32 | Moraketiya (Walawe Ganga) | 1.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-13 05:05:38 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 05:01:15 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:23:36 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-13 05:03:04 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:02:59 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 04:03:42 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | 0.000 |  |
| 2026-10-13 05:02:37 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-13 05:04:25 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 03:07:45 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.005 |  |
| 2026-10-13 05:01:47 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.006 |  |
| 2026-10-13 05:02:39 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-13 05:01:22 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-13 05:01:18 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-13 05:00:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-10-13 05:02:28 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.020 |  |
| 2026-10-13 05:00:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.024 |  |
| 2026-10-13 05:01:47 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.036 |  |
| 2026-10-13 05:02:19 | Rathnapura (Kalu Ganga) | 3.91 | 🟢 Normal | -0.037 |  |
| 2026-10-13 04:16:49 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.043 |  |
| 2026-10-13 05:02:07 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.050 |  |
| 2026-10-13 04:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.052 |  |
| 2026-10-13 05:02:51 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.065 |  |
| 2026-10-13 05:03:52 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.076 |  |
| 2026-10-13 05:06:45 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.076 |  |
| 2026-10-13 04:08:02 | Urawa (Nilwala Ganga) | 2.37 | 🟢 Normal | -0.137 |  |
| 2026-10-13 05:02:07 | Pitabeddara (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.344 |  |
| 2026-10-13 05:02:21 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -10.080 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)