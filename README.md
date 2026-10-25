# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_14:24:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,619 measurements** from **39** stations.
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
| 2026-10-25 14:24:26 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:15:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:12:05 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 2.250 | 🔺 Rising |
| 2026-10-25 14:11:33 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 2.250 | 🔺 Rising |
| 2026-10-25 14:09:25 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-25 14:08:36 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-10-25 14:08:22 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 14:08:00 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-25 14:07:43 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:07:13 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.045 |  |
| 2026-10-25 14:04:33 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.040 |  |
| 2026-10-25 14:04:22 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 14:04:20 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-25 14:04:09 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 14:04:06 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 14:03:55 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-25 14:03:45 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.024 |  |
| 2026-10-25 14:03:42 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:03:37 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-25 14:03:37 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.099 |  |
| 2026-10-25 14:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-25 14:03:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:03:17 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-25 14:03:08 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:03:05 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-25 14:03:01 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-25 14:02:52 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-10-25 14:02:49 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 14:02:48 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:42 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:35 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:13 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:13 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:08 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-25 14:02:02 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-25 14:01:20 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.150 |  |
| 2026-10-25 14:01:17 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.020 |  |
| 2026-10-25 14:01:06 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 14:01:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:00:31 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-25 14:00:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 14:12:05 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 2.250 | 🔺 Rising |
| 2026-10-25 14:03:55 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-25 14:03:05 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-25 14:02:02 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-25 14:02:52 | Magura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-10-25 14:03:17 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-25 14:09:25 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-25 14:04:20 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-25 14:04:06 | Ellagawa (Kalu Ganga) | 6.76 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-25 14:04:22 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 14:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-25 14:03:37 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-25 14:00:31 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-25 14:01:06 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 14:02:49 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 14:08:22 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 14:04:09 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 14:03:08 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:03:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:15:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:24:26 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:13 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:01:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:07:43 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:03:01 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:03:42 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:48 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:35 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 14:02:08 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-25 14:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-25 14:08:36 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-10-25 14:01:17 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.020 |  |
| 2026-10-25 14:00:30 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.023 |  |
| 2026-10-25 14:03:45 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.024 |  |
| 2026-10-25 14:04:33 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.040 |  |
| 2026-10-25 14:07:13 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.045 |  |
| 2026-10-25 14:08:00 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.050 |  |
| 2026-10-25 14:03:37 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.099 |  |
| 2026-10-25 14:01:20 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)