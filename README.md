# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_13:20:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,577 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 13:20:46 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:13:10 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.044 |  |
| 2026-10-25 13:09:42 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 13:08:54 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:08:40 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:08:27 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:08:24 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 13:08:22 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-10-25 13:08:13 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 13:07:44 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.109 |  |
| 2026-10-25 13:07:40 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:07:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-25 13:07:00 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-25 13:06:40 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:06:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:06:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:06:00 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-25 13:05:59 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-10-25 13:05:30 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-25 13:05:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 13:04:49 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-25 13:04:47 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-10-25 13:04:39 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-25 13:04:34 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-25 13:03:56 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:03:53 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 13:03:15 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-25 13:03:07 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.085 |  |
| 2026-10-25 13:03:06 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 13:04:49 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-25 13:04:34 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-25 13:05:30 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-25 13:04:39 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-25 13:07:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-25 13:00:12 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-25 12:05:47 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-25 13:06:00 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-25 13:09:42 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 13:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 13:07:00 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-25 13:02:04 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 13:05:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 13:03:53 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 13:08:13 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 13:08:24 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 13:01:20 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:06:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:08:40 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:03:56 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:20:46 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:06:09 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:03:06 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:00:49 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:06:40 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:08:27 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:08:54 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:07:40 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 13:04:47 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-10-25 13:08:22 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.009 |  |
| 2026-10-25 13:02:35 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-25 13:03:15 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-25 13:02:31 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-10-25 13:05:59 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-10-25 13:01:21 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-10-25 13:13:10 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.044 |  |
| 2026-10-25 13:03:07 | Rathnapura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.085 |  |
| 2026-10-25 13:07:44 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.109 |  |
| 2026-10-25 13:01:17 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)