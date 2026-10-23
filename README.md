# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_23:35:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,178 measurements** from **39** stations.
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
| 2026-10-23 23:35:08 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.028 |  |
| 2026-10-23 23:12:46 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-23 23:11:51 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:11:14 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-23 23:08:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | -0.018 |  |
| 2026-10-23 23:07:41 | Putupaula (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-10-23 23:07:10 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-23 23:06:29 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-10-23 23:06:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-23 23:05:51 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-10-23 23:05:47 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:04:30 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:04:18 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-23 23:03:51 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 23:03:41 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 23:03:30 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-10-23 23:03:11 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-10-23 23:03:03 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.015 |  |
| 2026-10-23 23:02:57 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.040 |  |
| 2026-10-23 23:02:55 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:02:53 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 23:02:13 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-23 23:01:53 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:01:48 | Moragaswewa (Deduru Oya) | 4.03 | 🟢 Normal | -0.084 |  |
| 2026-10-23 23:01:46 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:01:45 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-23 23:01:41 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | -0.040 |  |
| 2026-10-23 23:01:39 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:01:37 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 23:01:34 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-23 23:01:10 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.052 |  |
| 2026-10-23 23:01:02 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.030 |  |
| 2026-10-23 23:00:27 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 23:11:14 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-23 23:06:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-23 23:03:41 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 23:03:51 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 23:02:53 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 23:07:10 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-23 23:01:37 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 23:00:27 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 23:01:46 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:11:51 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:02:55 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:05:47 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:01:34 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:04:30 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:01:53 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-23 23:01:39 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-23 23:03:03 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.015 |  |
| 2026-10-23 23:08:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | -0.018 |  |
| 2026-10-23 23:07:41 | Putupaula (Kalu Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-10-23 22:39:47 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.019 |  |
| 2026-10-23 23:06:29 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-10-23 23:04:18 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-23 23:03:30 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-10-23 23:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-23 23:05:51 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-10-23 23:35:08 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.028 |  |
| 2026-10-23 22:05:54 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-10-23 23:02:13 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-23 23:01:02 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.030 |  |
| 2026-10-23 23:12:46 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-23 23:02:57 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.040 |  |
| 2026-10-23 23:01:41 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | -0.040 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-23 23:03:11 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.049 |  |
| 2026-10-23 23:01:10 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.052 |  |
| 2026-10-23 23:01:48 | Moragaswewa (Deduru Oya) | 4.03 | 🟢 Normal | -0.084 |  |
| 2026-10-23 20:01:32 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | -0.234 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)