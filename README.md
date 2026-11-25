# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_11:17:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,280 measurements** from **39** stations.
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
| 2026-11-25 11:17:56 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.064 |  |
| 2026-11-25 11:15:43 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:10:35 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:08:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.040 |  |
| 2026-11-25 11:08:00 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:07:48 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.180 |  |
| 2026-11-25 11:07:43 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:06:57 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.129 |  |
| 2026-11-25 11:06:05 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:05:59 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-11-25 11:05:39 | Rathnapura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.157 |  |
| 2026-11-25 11:05:21 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.076 |  |
| 2026-11-25 11:04:31 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-11-25 11:03:57 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:03:45 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:03:38 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 11:03:27 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-25 11:03:17 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.042 |  |
| 2026-11-25 11:03:04 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-25 11:02:58 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-11-25 11:02:53 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:48 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:43 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.081 |  |
| 2026-11-25 11:02:33 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:32 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.139 |  |
| 2026-11-25 11:02:22 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.084 |  |
| 2026-11-25 11:02:14 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.137 |  |
| 2026-11-25 11:02:10 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-25 11:02:03 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-25 11:01:55 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 11:01:48 | Dunamale (Aththanagalu Oya) | 3.13 | 🟢 Normal | -0.106 |  |
| 2026-11-25 11:01:47 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:01:45 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.050 |  |
| 2026-11-25 11:01:28 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:00:31 | Moraketiya (Walawe Ganga) | 2.24 | 🟢 Normal | -0.411 |  |
| 2026-11-25 11:00:23 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 11:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-25 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 11:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-25 11:02:10 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-25 11:03:04 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-25 11:02:03 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-25 11:01:55 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 11:00:23 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 11:03:38 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 11:08:00 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:03:57 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:33 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:48 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:53 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:01:28 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:10:35 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:15:43 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:04:31 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-11-25 11:06:05 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:01:47 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:07:43 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:03:27 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-25 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 11:05:59 | Pitabeddara (Nilwala Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-11-25 11:02:58 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-11-25 11:08:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.040 |  |
| 2026-11-25 11:03:17 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.042 |  |
| 2026-11-25 11:01:45 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.050 |  |
| 2026-11-25 11:17:56 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.064 |  |
| 2026-11-25 11:05:21 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.076 |  |
| 2026-11-25 11:02:43 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.081 |  |
| 2026-11-25 11:02:22 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.084 |  |
| 2026-11-25 11:01:48 | Dunamale (Aththanagalu Oya) | 3.13 | 🟢 Normal | -0.106 |  |
| 2026-11-25 11:06:57 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.129 |  |
| 2026-11-25 11:02:14 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.137 |  |
| 2026-11-25 11:02:32 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.139 |  |
| 2026-11-25 11:05:39 | Rathnapura (Kalu Ganga) | 3.19 | 🟢 Normal | -0.157 |  |
| 2026-11-25 11:07:48 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.180 |  |
| 2026-11-25 11:00:31 | Moraketiya (Walawe Ganga) | 2.24 | 🟢 Normal | -0.411 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)