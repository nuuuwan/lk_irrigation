# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_07:21:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,328 measurements** from **39** stations.
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
| 2026-08-11 07:21:13 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | -0.038 |  |
| 2026-08-11 07:18:27 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:17:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-11 07:17:36 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:16:40 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.008 |  |
| 2026-08-11 07:13:26 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-11 07:11:58 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.120 |  |
| 2026-08-11 07:11:17 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.102 |  |
| 2026-08-11 07:09:18 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:08:48 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.027 |  |
| 2026-08-11 07:08:08 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-08-11 07:07:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:06:41 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:05:44 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:05:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:04:21 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.052 |  |
| 2026-08-11 07:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:04:16 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:04:15 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 07:04:08 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:03:44 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.041 |  |
| 2026-08-11 07:03:37 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-11 07:03:31 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:03:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:03:07 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:03:06 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:02:59 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.116 |  |
| 2026-08-11 07:02:55 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.077 |  |
| 2026-08-11 07:02:40 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.027 |  |
| 2026-08-11 07:02:32 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:02:15 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:02:02 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:01:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:01:39 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:01:26 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:01:02 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:00:37 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.026 |  |
| 2026-08-11 06:41:29 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.052 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 07:03:37 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-11 07:04:15 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 07:13:26 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-11 07:17:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-11 07:02:40 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:01:39 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:07:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:03:06 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:09:18 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:01:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 04:02:25 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:02:32 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:05:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:04:16 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:06:41 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:03:07 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:05:44 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:18:27 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:01:02 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-11 07:16:40 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.008 |  |
| 2026-08-11 07:03:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:03:31 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:02:15 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:01:26 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:02:02 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-11 07:04:08 | Peradeniya (Mahaweli Ganga) | 3.40 | 🟢 Normal | -0.010 |  |
| 2026-08-11 06:03:21 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.019 |  |
| 2026-08-11 07:08:08 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.021 |  |
| 2026-08-11 07:00:37 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.026 |  |
| 2026-08-11 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | -0.027 |  |
| 2026-08-11 07:08:48 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.027 |  |
| 2026-08-11 07:21:13 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | -0.038 |  |
| 2026-08-11 07:03:44 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.041 |  |
| 2026-08-11 07:04:21 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.052 |  |
| 2026-08-11 07:02:55 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.077 |  |
| 2026-08-11 07:11:17 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.102 |  |
| 2026-08-11 07:02:59 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.116 |  |
| 2026-08-11 07:11:58 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)