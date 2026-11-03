# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_18:04:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,920 measurements** from **39** stations.
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
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 18:04:26 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:04:16 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-03 18:04:07 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:04:02 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.039 |  |
| 2026-11-03 18:03:55 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.031 |  |
| 2026-11-03 18:03:47 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 18:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.039 |  |
| 2026-11-03 18:03:38 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 18:03:33 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:03:16 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-03 18:03:13 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.040 |  |
| 2026-11-03 18:02:54 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-03 18:02:37 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.075 |  |
| 2026-11-03 18:02:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-03 18:02:32 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.093 |  |
| 2026-11-03 18:02:17 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-11-03 18:02:14 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:01:39 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.022 |  |
| 2026-11-03 18:01:36 | Moragaswewa (Deduru Oya) | 4.23 | 🟢 Normal | -0.021 |  |
| 2026-11-03 18:01:25 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.090 |  |
| 2026-11-03 18:01:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:01:22 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-03 18:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-11-03 18:01:21 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.023 |  |
| 2026-11-03 18:01:15 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 18:00:48 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.929 |  |
| 2026-11-03 18:00:44 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-03 18:00:17 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 17:03:59 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-03 18:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-11-03 17:02:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-03 18:01:22 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 18:03:16 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-03 18:00:44 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-03 17:06:13 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-03 18:03:38 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 18:03:47 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 18:00:17 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 17:05:59 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 18:02:35 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-03 18:01:15 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 18:01:23 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:04:26 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:03:33 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:02:14 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:05:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 17:01:00 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:04:07 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:02:17 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-11-03 18:04:16 | Giriulla (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-03 17:10:38 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.019 |  |
| 2026-11-03 17:10:09 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-11-03 18:01:36 | Moragaswewa (Deduru Oya) | 4.23 | 🟢 Normal | -0.021 |  |
| 2026-11-03 18:01:39 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.022 |  |
| 2026-11-03 18:01:21 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.023 |  |
| 2026-11-03 17:03:45 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.028 |  |
| 2026-11-03 18:03:55 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.031 |  |
| 2026-11-03 17:01:41 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | -0.031 |  |
| 2026-11-03 18:04:02 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.039 |  |
| 2026-11-03 18:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.039 |  |
| 2026-11-03 18:03:13 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.040 |  |
| 2026-11-03 18:02:54 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-03 18:02:37 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.075 |  |
| 2026-11-03 18:01:25 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.090 |  |
| 2026-11-03 18:02:32 | Hanwella (Kelani Ganga) | 2.51 | 🟢 Normal | -0.093 |  |
| 2026-11-03 18:00:48 | Wellawaya (Kirindi Oya) | 2.05 | 🟢 Normal | -0.929 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)