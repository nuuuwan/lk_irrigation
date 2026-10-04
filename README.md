# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_08:10:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,503 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 08:10:33 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.047 |  |
| 2026-10-04 08:09:08 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:09:00 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-10-04 08:07:51 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-10-04 08:07:17 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 08:06:48 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-04 08:06:35 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.029 |  |
| 2026-10-04 08:06:14 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:06:04 | Panadugama (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.061 |  |
| 2026-10-04 08:05:18 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-04 08:05:01 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.116 |  |
| 2026-10-04 08:04:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-04 08:04:51 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:04:49 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-04 08:04:30 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:04:25 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.153 |  |
| 2026-10-04 08:03:48 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.056 |  |
| 2026-10-04 08:03:37 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-04 08:03:32 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-04 08:03:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.039 |  |
| 2026-10-04 08:03:05 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:03:01 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:02:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.023 |  |
| 2026-10-04 08:02:38 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 08:02:33 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.150 |  |
| 2026-10-04 08:02:23 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-04 08:02:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:02:01 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-04 08:02:00 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:59 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:58 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:57 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:56 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:50 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.051 |  |
| 2026-10-04 08:01:48 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:39 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-10-04 08:01:22 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:18 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 08:01:10 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:00:54 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-04 08:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-04 08:00:08 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 08:05:18 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-04 08:03:32 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-04 08:01:18 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 08:04:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-04 08:02:01 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-04 08:03:37 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-04 08:07:17 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 08:02:38 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 08:06:48 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-04 08:01:22 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:06:14 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:48 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:03:05 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:04:51 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:09:08 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:02:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:02:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:03:01 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:01:10 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:04:30 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-04 08:09:00 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-10-04 08:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-04 08:02:23 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-04 08:00:54 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-04 08:07:51 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-10-04 08:04:49 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-04 08:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | -0.023 |  |
| 2026-10-04 08:06:35 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.029 |  |
| 2026-10-04 08:03:20 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.039 |  |
| 2026-10-04 08:01:39 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.040 |  |
| 2026-10-04 08:10:33 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.047 |  |
| 2026-10-04 08:01:50 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.051 |  |
| 2026-10-04 08:00:08 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.051 |  |
| 2026-10-04 08:03:48 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.056 |  |
| 2026-10-04 08:06:04 | Panadugama (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.061 |  |
| 2026-10-04 08:05:01 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.116 |  |
| 2026-10-04 08:02:33 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.150 |  |
| 2026-10-04 08:04:25 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)