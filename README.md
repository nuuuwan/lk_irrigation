# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_06:30:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,810 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 06:30:29 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:09:22 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.091 |  |
| 2026-09-10 06:08:26 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-10 06:08:04 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-10 06:06:58 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-10 06:06:16 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -1.003 |  |
| 2026-09-10 06:05:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:05:05 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:05:03 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:04:56 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-10 06:04:31 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:04:29 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:50 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.026 |  |
| 2026-09-10 06:03:45 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2026-09-10 06:03:37 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:27 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.040 |  |
| 2026-09-10 06:03:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-10 06:03:12 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-09-10 06:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-10 06:02:50 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:46 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-10 06:02:33 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:30 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:06 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:00 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-10 06:01:50 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 06:01:48 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:01:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:01:15 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.756 | 🔺 Rising |
| 2026-09-10 06:01:01 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.041 |  |
| 2026-09-10 06:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:48 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:37 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.199 |  |
| 2026-09-10 06:00:37 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:35 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-10 05:53:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | 0.064 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 06:01:15 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.756 | 🔺 Rising |
| 2026-09-10 06:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-10 06:03:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-10 06:08:04 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-09-09 18:02:14 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-10 06:02:46 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-10 06:01:50 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 06:08:26 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-10 06:01:30 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:37 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:50 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:35 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-10 04:01:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:30:29 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:30 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:37 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:05:03 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:04:31 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-09-10 05:01:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:05:05 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:05:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:33 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:00:48 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:04:29 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:04:56 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-10 06:02:00 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-10 06:06:58 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-10 06:03:50 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.026 |  |
| 2026-09-10 06:03:27 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.040 |  |
| 2026-09-10 06:01:01 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.041 |  |
| 2026-09-10 06:03:45 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2026-09-10 06:03:12 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-09-10 06:09:22 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.091 |  |
| 2026-09-10 06:00:37 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.199 |  |
| 2026-09-10 06:06:16 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -1.003 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)