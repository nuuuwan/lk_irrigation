# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_15:07:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,654 measurements** from **39** stations.
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
| 2026-10-25 15:07:23 | Pitabeddara (Nilwala Ganga) | 1.76 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-25 15:06:58 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 15:06:17 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-25 15:05:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:05:52 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-10-25 15:05:41 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-25 15:05:04 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:04:11 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-25 15:04:05 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-25 15:04:04 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-10-25 15:03:57 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 15:03:56 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:03:49 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-10-25 15:03:42 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 15:03:36 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-25 15:03:34 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 15:03:13 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 15:03:10 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 15:03:02 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:03:01 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:56 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:32 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.054 |  |
| 2026-10-25 15:02:28 | Ellagawa (Kalu Ganga) | 6.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-25 15:02:26 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:26 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-25 15:02:17 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-25 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 15:02:15 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-25 15:02:13 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:09 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:01:30 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.130 |  |
| 2026-10-25 15:01:26 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.042 |  |
| 2026-10-25 15:01:20 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 15:01:14 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-10-25 15:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 14:12:05 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 2.250 | 🔺 Rising |
| 2026-10-25 15:04:04 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-10-25 15:03:49 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-10-25 15:04:05 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-25 15:03:36 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-25 15:02:28 | Ellagawa (Kalu Ganga) | 6.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-25 15:05:41 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-25 15:07:23 | Pitabeddara (Nilwala Ganga) | 1.76 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-25 15:02:17 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-25 15:03:13 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-25 15:04:11 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-25 15:06:58 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 15:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 15:01:20 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 15:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 15:03:42 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 15:03:57 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 15:03:10 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 15:06:17 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-25 15:03:34 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 15:02:13 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:03:02 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:03:56 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:26 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:05:04 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:03:01 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:05:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:56 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:09 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 15:02:15 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-25 15:02:26 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-25 15:05:52 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-10-25 15:01:14 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-10-25 14:00:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.023 |  |
| 2026-10-25 14:04:33 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.040 |  |
| 2026-10-25 15:01:26 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.042 |  |
| 2026-10-25 15:02:32 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.054 |  |
| 2026-10-25 14:03:37 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.099 |  |
| 2026-10-25 15:01:30 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)